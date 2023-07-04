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
## 3.1 发起评论，触发webhook
![image](https://github.com/kernelry/webhookToEmail/assets/19744542/e559ea2b-3099-44fb-ae37-ed5e4461f0cf)
## 3.2 接收webhook
![image](https://github.com/kernelry/webhookToEmail/assets/19744542/6c16c901-4365-43b4-9130-69cc496186af)
## 3.3 接收邮件通知
![image](https://github.com/kernelry/webhookToEmail/assets/19744542/50deb02b-b4d2-4e6e-bb02-8ca07abdb309)



