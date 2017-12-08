import unittest
from time import sleep

import nose
import requests
import unittest

from nose import run

import login


class test_userinfo(unittest.TestCase):
    def test1_userinfo(self):
        login.login()
        url = 'http://dcdh.cqmsyy.com/app/login_in/userinfo'
        r = requests.get(url)
        rs = r.json()
        print(rs)


    def test2_suerinfo(self):
        request = requests.post(url='http://dcdh.cqmsyy.com/app/main/login', \
                                data=({'token': '862dc26eff856f42e24037ae8ac6558d', 'mobile': '13226349780',
                                        'password': '123456'}))
        userinfo = request.json()
        userinfo_state = userinfo['code']
        print(userinfo_state)
        assert userinfo_state == 0, '登录成功'
        sleep(5)


if __name__ == '__main__':
    unittest.main()
















