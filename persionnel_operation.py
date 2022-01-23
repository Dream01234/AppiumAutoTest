import persionnel

"----人员操作类"
class member_control:

    "选择人员"
    def selectmember(self,value):
        t = persionnel.member()
        t.findname(value)
        t.clickname(value)