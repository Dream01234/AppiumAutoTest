import details
import persionnel_operation
import date_operation

"-----爆点详情操作类"
class boompoint_control:

    "选择整改负责人"
    def selectrepairer(self,name):
        t = details.boompoint()
        m = persionnel_operation.member_control()
        t.clickrepairer()
        m.selectmember(name)

    "选择整改期限"
    def selectdate(self,date):
        t = details.boompoint()
        d = date_operation.dates_control()
        t.clickdate()
        d.selectdate(date)

    "保存问题"
    def save(self):
        t = details.boompoint()
        t.clicksave()