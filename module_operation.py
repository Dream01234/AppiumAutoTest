import module
class task_control:


    "切换项目"
    def changeproject(self,project_name):
        t = module.cloudmodule()
        t.clickunfold()
        t.clickproject(project_name)

    "同步任务"
    def Synchronization_task(self,first,second):
        t = module.cloudmodule()
        t.clicktask(first,second)

    "点击任务"
    def selecttask(self,name):
        t = module.cloudmodule()
        t.clicktask_name(name)




