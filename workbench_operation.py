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


    "查询模块并选择模块"
    def findmodule(self,module_name):
        t = workbench.cloudworkbench()
        t.clickfind()
        t.sendkey(module_name)
        t.clickmodule(module_name)

