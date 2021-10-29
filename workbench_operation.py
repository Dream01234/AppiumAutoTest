import workbench
class workbench_control:

    "选择组织架构"
    def changeorganization(self):
        t = workbench.cloudworkbench()
        t.clickorganization()
        t.clickorganization_launched()
        t.clicktager()

    "选择更多"
    def click_more(self):
        t = workbench.cloudworkbench()
        t.clickmore()


