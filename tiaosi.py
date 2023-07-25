#调试python调用jemter用
import datetime
import os
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
                save(linelist[2],linelist[4])
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

#存储结果
def save(name,check_result):
    #判断文件存在否，不存在则新建并写入数据
    file_path = "D:\\1.txt"
    if os.path.exists(file_path):
        with open(file_path,'a',encoding='utf-8') as f:
                now = datetime.datetime.now()
                f.writelines([format(now),'----',name,'---',check_result])
                f.writelines("\n")
    else:
        with open(file_path,'w',encoding='utf-8')as f:
            now = datetime.datetime.now()
            f.writelines([format(now),'----',name, '---', check_result])
            f.writelines("\n")

if __name__ == '__main__':
        result_msg,result = get_result(result_file)
        print(result_msg)