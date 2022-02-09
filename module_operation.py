import module
"-----模块操作类"
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

    "点击全部同步"
    def selectall(self):
        t = module.cloudmodule()
        t.clicksynchronous()
        t.wait_loading()
        t.is_toast_exist("任务同步成功")



