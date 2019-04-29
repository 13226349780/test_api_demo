# encoding: utf-8

import os
from time import sleep

import requests
import json
from datetime import datetime as dt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from functools import partial
from nose.tools import *


def send_mail():
    # 读取测试报告内容
    with open(report_file, 'r',encoding='UTF-8') as f:
        content = f.read()

    msg = MIMEMultipart('mixed')
    # 添加邮件内容
    msg_html = MIMEText(content, 'html', 'utf-8')
    msg.attach(msg_html)

    # 添加附件
    msg_attachment = MIMEText(content, 'html', 'utf-8')
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(report_file)
    msg.attach(msg_attachment)

    msg['Subject'] = mail_subjet
    msg['From'] = mail_user
    msg['To'] = ';'.join(mail_to)
    try:
        # 连接邮件服务器
        s = smtplib.SMTP_SSL(mail_host, 465)
        # 登陆
        s.login(mail_user, mail_pwd)
        # 发送邮件
        s.sendmail(mail_user, mail_to, msg.as_string())
        # 退出
        s.quit()
    except Exception as e:
        print ("Exceptioin ", e)


class test_user():


    def test_info(self):
        request = requests.post(url='http://dcdh.cqmsyy.com/app/main/login', \
                                data=({'token': '862dc26eff856f42e24037ae8ac6558d', 'mobile': '13226349780',
                                        'password': '123456'}))
        userinfo = request.json()
        userinfo_state = userinfo['code']
        print(userinfo_state)
        assert userinfo_state == 0, '登录成功'
        sleep(5)


    def test_login(self):
        #cookies = login.login()
        url = 'http://dcdh.cqmsyy.com/app/login_in/userinfo'
        r = requests.get(url)
        rs = r.json()
        code = rs['code']
        assert rs == 0 ,'登录成功'
    def test_qq(self):
        pass
    def test_weixin(self):
        pass
    def test_pt(self):
        pass
    def test_we(self):
        pass


if __name__ == '__main__':
    # 邮件服务器
    mail_host = 'smtp.qq.com'
    # 发件人地址
    mail_user = '755682146@qq.com'
    # 发件人密码
    mail_pwd = '*******'
    # 邮件标题
    mail_subjet = u'NoseTests_测试报告_{0}'.format(dt.now().strftime('%Y%m%d'))
    # 收件人地址list
    mail_to = ['746832476@qq.com']
    # 测试报告名称
    report_file = 'TestReport.html'

    # 运行nosetests进行自动化测试并生成测试报告
    print ('Run Nosetests Now...')
    os.system('nosetests -v test_userinfo.py:test_user --with-html --html-file={0}'.format(report_file))

    # 发送测试报告邮件
    print ('Send Test Report Mail Now...')
    send_mail()
