import  indicators
"-----指标操作类"

class indicator_control:

    "点击确认"
    def confirm(self):
        t = indicators.indicator()
        t.clickconfirm()

    "选择检查项"
    def selectindicator(self,itemname):
        t = indicators.indicator()
        t.clickitem(itemname)

    "选择末级检查项"
    def selectlastitem(self,itemname):
        t = indicators.indicator()
        t.clicklastitem(itemname)

    "点击重置"
    def reset(self):
        t = indicators.indicator()
        t.clickreset()