#调试python调用jemter用
import datetime
import os
import xlwt
import xlrd
from xlutils.copy import copy
result_file = 'D:\\apache-jmeter-5.3\\result_jtl\\20201119_120128\\result.jtl'

def get_result(result_file):
    failcount = 0
    successcount = 0
    result = 0
    count = 0
    first_fail = ''
    second_fail = ''
    third_fail = ''
    with open(result_file, 'r', encoding='utf-8') as filehandle:
        # next(filehandle)
        filesource = filehandle.readlines()[1:]  # 跳过首行
        for line in filesource:
            linelist = line.split(',')
            if linelist[7] == 'false':
                failcount = failcount + 1
                save_excel(linelist[2],linelist[4],linelist[8])
                #save_txt(linelist[2],linelist[4])
                # last_fail = linelist[2]+linelist[13]
            if linelist[7] == 'true':
                successcount = successcount + 1

        for line in filesource:
            linelist = line.split(',')
            if linelist[7] == 'false':
                count = count + 1
                if count == 1:
                    first_fail = "  首个失败请求:" + linelist[2] + linelist[13] + '\n' + linelist[4]
                if count == 2:
                    second_fail = "  第二个失败请求:" + linelist[2] + linelist[13] + '\n' + linelist[4]
                if count == 3:
                    third_fail = "  第三个失败请求:" + linelist[2] + linelist[13] + '\n' + linelist[4]
                    break

    if failcount > 0:
        result_msg = '测试结果失败，错误数:' + str(failcount) + first_fail + '\n' + second_fail + '\n' + third_fail
        result = 1
    else:
        result_msg = '测试结果通过,成功请求数：' + str(successcount)
        result = 2


    return result_msg, result

#存储结果到txt
def save_txt(name,check_result):
    #判断文件存在否，不存在则新建并写入数据
    file_path = "D:\\1.txt"
    if os.path.exists(file_path):
        with open(file_path,'a',encoding='utf-8') as f:
                now = datetime.datetime.now()
                formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
                f.writelines([formatted_date,',',name,',',check_result])
                f.writelines("\n")
    else:
        with open(file_path,'w',encoding='utf-8')as f:
            now = datetime.datetime.now()
            f.writelines([format(now),',',name, ',', check_result])
            f.writelines("\n")

#保存数据到excel文件
def save_excel(name,pro,result):
    #判断文件存在否，不存在则新建并尾行写入数据
    file_path = 'D:\\diyige.xlsx'
    if os.path.exists(file_path):
        wb = xlrd.open_workbook(file_path,formatting_info=True)   #打开xlsx文件
        sheet1 = wb.sheet_by_index(0)   #获取第一个工作薄
        nrows = sheet1.nrows  #获取非空行数
        newbook = copy(wb)  #复制原来数据
        newsheet = newbook.get_sheet(0)  #获取第一个工作薄
        style = xlwt.XFStyle()
        style.num_format_str = 'YY/M/D h:mm'
        time = datetime.datetime.now()   #写入数据时间
        newsheet.write(nrows, 0, time, style)   #写入数据
        newsheet.write(nrows, 1, name)
        newsheet.write(nrows, 2, pro)
        newsheet.write(nrows, 3, result)
        newbook.save(file_path)   #保存文件内容
    else:
        wb = xlwt.Workbook()  #创建对象
        sh = wb.add_sheet('错误记录')  #创建一个sheet叫 第一个
        sh.write(0, 0,'时间')
        sh.write(0, 1, '表单名')
        sh.write(0, 2, '响应结果')
        sh.write(0, 3, '断言失败原因')
        style = xlwt.XFStyle()
        style.num_format_str = 'YY/M/D h:mm'
        time = datetime.datetime.now()  # 写入数据时间
        sh.write(1, 0, time, style)  # 写入数据
        sh.write(1, 1, name)
        sh.write(1, 2, pro)
        sh.write(1, 3, result)
        wb.save(file_path)  # 保存文件内容

if __name__ == '__main__':
        result_msg,result= get_result(result_file)
        print(result_msg)