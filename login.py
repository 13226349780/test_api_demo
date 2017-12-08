import requests


class login_fun(object):
    def login(cookies):
        url = 'http://dcdh.cqmsyy.com/app/main/login'
        token = '862dc26eff856f42e24037ae8ac6558d'
        request = requests.post(url=url, \
                                data=({'token': token, 'mobile': '13226349780',
                                       'password': '123456'}))
        cookies = request.cookies
        return cookies
