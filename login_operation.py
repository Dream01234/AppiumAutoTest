import login
import index_operation

"---登录操作类"
class loginpage_control:

    "登录智建云(不带企业编码)"
    def logincloud1(self,username,pwd):
        a = index_operation.index_control()
        t = login.Loginel()
        a.click_loginNow()
        t.sendUsename(username)
        t.sendPwd(pwd)
        t.checkAgree()
        t.clickLoginButoon()

    "登录智建云（带企业编码）"
    def logincloud2(self,username,pwd,code):
        a = index_operation.index_control()
        t = login.Loginel()
        a.click_loginNow()
        t.sendUsename(username)
        t.sendPwd(pwd)
        t.sendBusinesscode(code)
        t.checkAgree()
        t.clickLoginButoon()

