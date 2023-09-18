# _*_ coding ： utf-8 _*_
# @Time ：2023/9/13 18:27
# @Author ： LI李
# @File ：train4_1
# @Project ：文件流

# open() 打开、创建文件

# f1 = open("test.txt", "r")  # x 表示的是读一个文件，如果没有的话就创建它 ； r 表示读的意思

# content = f1.read()  # 这表示全部读入
# # content1 = f1.read(10)  # 只读10个字符
# # content2 = f1.readline()  # 只读一行
# # 注意这里的话读取时不能同时进行多个文件的读入，必须要关闭 打开后才能再次读入
# print(content)

#
# for line in f1:
#     # print(line)  # 这里读出来会空行的原因是文件道中每次读取的时候会加上换行符
#     print(line.strip())  # 表示的是去掉行两边的换行符

#
# lines = f1.readlines()
# print(lines)  # 读取到的每行的列表
#
# # 关闭文件
# f1.close()


# --------------分割线------------------

# 如何去写一个文件

# f = open("test.txt", 'w')  # 文件的写w  但是会覆盖原本的内容
#
# f.write("hello world python")
# f.close()


# 如何删除一个文件
# import os
# os.remove("test.txt")  # 将这个文件移除掉


# # 文件的追加模式
#
# f = open("test.txt",'a')
#
# f.write("hello world Python!")
#
# f.close()
