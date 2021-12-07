import area

"-------区域操作类"
class district_control:

    "输入区域名称查询"
    def selectarea(self,name):
        t = area.district()
        t.findarea(name)

    "选择楼栋(单栋)"
    def selectbudling(self,buildingname):
        t = area.district()
        t.findbuilding(buildingname)

    "选择楼层(末级为层级)"
    def selectfloor(self,floorname):
        t = area.district()
        t.findfloor(floorname)

    "选择本级"
    def selectthis(self,name):
        t = area.district()
        t.findthis_level(name)
