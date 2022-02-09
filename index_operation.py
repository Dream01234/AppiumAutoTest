import index
"---首页操作类"
class index_control:

    "同意声明"
    def agree(self):
        t = index.cloudIndex()
        t.click_agree()

    "暂时不使用"
    def refuse(self):
        t = index.cloudIndex()
        t.click_no()

    "允许访问"
    def allow(self):
        t = index.cloudIndex()
        for i in range(2) :
            t.click_allow()

    "同意授权并点击马上登录"
    def click_loginNow(self):
        t = index.cloudIndex()
        t.click_agree()
        for i in range(2) :
            t.click_allow()
        t.click_btngotologin()

    "同意授权并点击免费注册"
    def click_freeregister(self):
        t = index.cloudIndex()
        t.click_agree()
        for i in range(2):
            t.click_allow()
        t.click_btnregister()