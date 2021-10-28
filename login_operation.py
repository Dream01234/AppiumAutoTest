import login
class loginpage_control:

    "登录智建云(不带企业编码)"
    def logincloud1(self,username,pwd):
        t = login.Loginel()
        t.sendUsename(username)
        t.sendPwd(pwd)
        t.checkAgree()
        t.clickLoginButoon()

    "登录智建云（带企业编码）"
    def logincloud2(self,username,pwd,code):
        t = login.Loginel()
        t.sendUsename(username)
        t.sendPwd(pwd)
        t.sendBusinesscode(code)
        t.checkAgree()
        t.clickLoginButoon()

