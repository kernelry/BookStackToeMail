# 1 简介
将Bookstack知识库软件的webhook消息转发给指定邮箱
# 2 选项
```shell
[root@testkb dist]# ./webhookToEmail  -h
usage: webhookToEmail [-h] [-listen LISTEN] [-smtpserver SMTPSERVER] [-smtpport SMTPPORT] [-sender SENDER] [-password PASSWORD] [-file FILE]

A script for sending emails based on webhook data

options:
  -h, --help            show this help message and exit
  -listen LISTEN        webhook listener port
  -smtpserver SMTPSERVER
                        The SMTP server address,example:smtp.exmail.qq.com
  -smtpport SMTPPORT    The SMTP server port
  -sender SENDER        The sender email address,example:zhangsan@qq.com
  -password PASSWORD    The sender email password
  -file FILE            The reciver email file
```
# 3 使用例子
## 3.1 准备邮件接收列表
```shell
[root@testkb dist]# cat .\recMail.ini
test1@qq.com
test2@qq.com
test3@qq.com
```
## 3.2 启动程序
```shell
[root@testkb dist]# ./webhookToEmail -listen 8000 -smtpserver smtp.exmail.qq.com -smtpport 465 -sender xxxx@qq.com -password xxxx -file ./recMail.ini 
 * Serving Flask app 'webhookToEmail'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.1.121:8000
Press CTRL+C to quit
Data received from Webhook is:  {'event': 'commented_on', 'text': '管理员 评论 "堡垒机创建登录用户"', 'triggered_at': '2023-07-04T03:51:17.000000Z', 'triggered_by': {'id': 1, 'name': '管理员', 'slug': '41f1f'}, 'triggered_by_profile_url': 'http://192.168.1.121/user/41f1f', 'webhook_id': 1, 'webhook_name': 'testpython', 'url': 'http://192.168.1.121/books/c9f0f/page/6da90', 'related_item': {'id': 6, 'book_id': 1, 'chapter_id': 0, 'name': '堡垒机创建登录用户', 'slug': '6da90', 'priority': 7, 'created_at': '2023-05-05T01:12:41.000000Z', 'updated_at': '2023-07-03T05:37:20.000000Z', 'created_by': {'id': 1, 'name': '管理员', 'slug': '41f1f'}, 'updated_by': {'id': 1, 'name': '管理员', 'slug': '41f1f'}, 'draft': False, 'revision_count': 2, 'template': False, 'owned_by': {'id': 1, 'name': '管理员', 'slug': '41f1f'}, 'editor': 'wysiwyg'}}
192.168.1.121 - - [04/Jul/2023 11:51:17] "POST /webhook HTTP/1.1" 200 -
send email OK!
```
## 3.3 发起评论，触发webhook
![image](https://github.com/kernelry/webhookToEmail/assets/19744542/e559ea2b-3099-44fb-ae37-ed5e4461f0cf)
## 3.4 接收webhook
![image](https://github.com/kernelry/webhookToEmail/assets/19744542/6c16c901-4365-43b4-9130-69cc496186af)
## 3.5 接收邮件通知
![image](https://github.com/kernelry/webhookToEmail/assets/19744542/50deb02b-b4d2-4e6e-bb02-8ca07abdb309)



