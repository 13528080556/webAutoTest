# @Time    : 2019/12/11 19:17
# @Author  : Hugh
# @email   : 609799548@qq.com

import os
import json
import time
import smtplib
import unittest
from common.Log import Log
from common.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

basePath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class ReadConfig:

    __instance = None
    configPath = os.path.join(basePath, 'config.json')

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        with open(self.configPath, encoding='utf-8') as f:
            self.data = json.load(f)

    def get_database(self):
        return self.data.get('DATABASE')

    def get_http(self):
        return self.data.get('HTTP')

    def get_email(self):
        return self.data.get('EMAIL')


class ExcelUtil:
    pass


class Main:

    project_path = basePath

    def __init__(self, cases_dir='testCases', report_dir='report', logs_dir='logs'):
        """
        :param cases_dir:  测试用例目录名称
        :param report_dir: 测试报告目录名称
        :param logs_dir: 日志目录名称
        """
        self.cases_dir_path = os.path.join(self.project_path, cases_dir)
        self.report_dir_path = os.path.join(self.project_path, report_dir)
        self.logs_dir_path = os.path.join(self.project_path, logs_dir)

    def add_all_cases(self, rule='test*.py'):
        """加载所有测试用例"""
        return unittest.defaultTestLoader.discover(self.cases_dir_path, pattern=rule, top_level_dir=None)

    def run_case(self):
        """执行所有测试用例，并把结果写入HTML测试报告"""
        report_file_path = os.path.join(self.report_dir_path, time.strftime('%Y%m%d') + 'XX测试报告.html')
        with open(report_file_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f, title='XX平台自动化测试报告', description='描述内容')
            runner.run(self.add_all_cases())

    def get_report(self):
        """获取最新测试报告"""
        lists = os.listdir(self.report_dir_path)
        lists.sort(key=lambda fn: os.path.getatime(os.path.join(self.report_dir_path, fn)))
        return os.path.join(self.report_dir_path, lists[-1])

    def send_email(self, sender, psw, receiver, smtp_server='stmp.163.com', port=25):
        """发送邮件"""
        msg = MIMEMultipart()
        email_body = '本次测试结果请下载附件查看'
        body = MIMEText(email_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = 'XX自动化测试结果'  # 邮件标题
        msg['from'] = sender
        msg['to'] = ''.join(receiver)
        msg.attach(body)
        with open(self.get_report(), 'rb') as f:
            att = MIMEText(f.read(), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename= %s' % os.path.basename(self.get_report())
        msg.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server, port)
        smtp.login(sender, psw)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

    def start(self):
        log = Log()
        self.add_all_cases()
        log.info('加载所有测试用例:---> done')
        self.run_case()
        log.info('执行所有测试用例:---> done')


if __name__ == '__main__':
    pass

