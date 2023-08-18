#统计错误问题数
import os
import xlwt
import xlrd
from xlutils.copy import copy
import datetime
result_file = 'D:\\apache-jmeter-5.3\\result_jtl\\20201119_120128\\D__1.txt'

#统计报错总数
def stats(file_path):
    with open(file_path) as f:
        line_count = 0
        for line in f:
            line_count += 1
    return  line_count

#读取txt文档特定列，并分类统计
def feilei(result_file):
    with open(result_file, 'r', encoding='utf-8') as filehandle:
        # next(filehandle)
        filesource = filehandle.readlines()          #逐行读取
        word_count = {}       #定义一个空字典用于存放内容
        list1= []      #定义一个空列表，用于存放指定内容
        for line in filesource:
            linelist = line.split(",")    #用,进行分割
            x = linelist[1]    #取第二列的数
            list1.append(x)    #将第二列的数存放在列表list1

        #将list1列表里面的内容进行统计
        for word in list1:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    #统计并输出
    for word, count in word_count.items():
        print(f"{word}:{count}")


#保存数据到excel文件
def save(name,pro):
    #判断文件存在否，不存在则新建并尾行写入数据
    file_path = 'D:\\diyige.xlsx'
    if os.path.exists(file_path):
        wb = xlrd.open_workbook(file_path,formatting_info=True)   #打开xlsx文件
        sheet1 = wb.sheet_by_index(0)   #获取第一个工作薄
        nrows = sheet1.nrows  #获取非空行数
        newbook = copy(wb)  #复制原来数据
        newsheet = newbook.get_sheet(0)  #获取第一个工作薄
        time = datetime.datetime.now()
        newsheet.write(nrows, 0, time)   #写入数据
        newsheet.write(nrows, 1, name)
        newsheet.write(nrows, 2, pro)
        newbook.save(file_path)   #保存文件内容
    else:
        wb = xlwt.Workbook()  #创建对象
        sh = wb.add_sheet('错误记录')  #创建一个sheet叫 第一个
        sh.write(0, 0,'时间')
        sh.write(0, 1, '表单名')
        sh.write(0, 2, '响应结果')
        wb.save(file_path)



if __name__ == '__main__':
        save()