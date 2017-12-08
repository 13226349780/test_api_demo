import unittest
from time import sleep

import nose
import requests
import unittest
import login


class test_userinfo(unittest.TestCase):
    def userinfo(self):
        print(343641654654)
        cookies = login.login_fun.login()
        params = cookies
        url = 'http://dcdh.cqmsyy.com/app/login_in/userinfo'
        r = requests.get(url)
        rs = r.json()

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
    suite = unittest.TestSuite()
    suite.addTest(test_userinfo('userinfo'))
    suite.addTest(test_userinfo('test2_suerinfo'))

















