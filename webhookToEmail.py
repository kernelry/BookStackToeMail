#webhookToEmail

import smtplib,ssl,json,time,argparse #smtplib和ssl用于发送邮件，json用于解析和格式化webhook的json数据，time用于文章标题的日期和格式化，argparse用于传入参数
from concurrent.futures import ThreadPoolExecutor #实现异步发送邮件，接收webhook之后，不需要等待发送邮件成功，即返回给知识库系统
from flask import Flask, request #用于快速搭建webhook信息接收
from email.message import EmailMessage
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart # 导入MIMEMultipart类
from email.mime.text import MIMEText # 导入MIMEText类


app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=1)

def send_email(data, smtpserver, smtpport, sender, password):
    with open('./recMail.env', 'r') as f:
        receiver_emails = f.read().splitlines()
    # 创建一个MIMEMultipart对象，用于组合HTML和纯文本版本的邮件正文
    msg = MIMEMultipart('alternative')
    pname = data["related_item"]["name"]
    pname2 = data["related_item"]["owned_by"]["name"]
    text = data["text"]
    url = data["url"]
    utc_time = datetime.strptime(data["triggered_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    time_diff = timedelta(hours=8) #转换时间为东
    cst_time = utc_time + time_diff
    local_time = time.localtime()
    date_str = time.strftime("%Y-%m-%d", local_time)
    msg['Subject'] = "{} 知识库动态".format(date_str)
    msg['From'] = "知识库小助手"
    # 创建一个HTML版本的邮件正文，可以使用HTML标签来美化内容
    html_output = """\
<html>
  <head></head>
  <body>
    <p><b>动态详情：{text}</b></p>
    <p>文章作者：{pname2}</p>
    <p>文章名称：<a href="{url}">{pname}</a></p>
    <p>动态时间：{cst_time}</p>
  </body>
</html>
""".format(text=text, url=url, pname=pname, cst_time=cst_time,pname2=pname2)
    msgpart = MIMEText(html_output, 'html')
    msg.attach(msgpart)
    context = ssl.create_default_context()
    try: # 使用try执行处理异常
        with smtplib.SMTP_SSL(smtpserver, smtpport, context=context) as server:
            server.login(sender, password)
            server.send_message(msg, sender, receiver_emails)    
    except Exception as e:
        print("Error occurred while sending email:", e)
  
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print("Data received from Webhook is: ", data)
        executor.submit(send_email, data, args.smtpserver, args.smtpport, args.sender, args.password) #异步执行send_email函数
        return "Webhook received!"
    
parser = argparse.ArgumentParser(description="A script for sending emails based on webhook data")
parser.add_argument("-listen", type=int, default="8000", help="webhook listener port")
parser.add_argument("-smtpserver", help="The SMTP server address,example:smtp.exmail.qq.com")
parser.add_argument("-smtpport", type=int, default=465, help="The SMTP server port")
parser.add_argument("-sender",  help="The sender email address,example:zhangsan@qq.com")
parser.add_argument("-password", help="The sender email password")
args = parser.parse_args()

app.run(host='0.0.0.0', port=args.listen)
