#统计错误问题数
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

    for word, count in word_count.items():
        print(f"{word}:{count}")

if __name__ == '__main__':
        word= feilei(result_file)