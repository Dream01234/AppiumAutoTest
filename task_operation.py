import task

"---任务操作类"
class picture_control:

    "选择区域"
    def selectarea(self,area):
        t = task.picture
        t.clickarea(area)

    "切换测量"
    def selectmeasure(self,measure):
        t = task.picture
        t.clickmeasure(measure)

    "切换爆点"
    def selectboom(self,boom):
        t = task.picture
        t.clickmeasure(boom)

    "选择指标"
    def selecttarget(self,indicators):
        t = task.picture
        t.clickindicators(indicators)

    "点击图纸"
    def selcetpront(self,x,y):
        t = task.picture
        t.clickpir(x,y)

    "点击空白处新增测量点"
    def open(self):
        t = task.picture
        t.click_null_point()

