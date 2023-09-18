# _*_ coding ： utf-8 _*_
# @Time ：2023/9/13 17:15
# @Author ： LI李
# @File ：train2_2
# @Project ：函数的声明

# 函数1
def function_name(name):
    return name


print(function_name("你的名字"))


def printname(str_name):
    print(str_name)
    return


# 函数2
printname("我的名字")


def change_value(a):
    a = 10
    return a


a = 12
print(a)
print(change_value(a))


# 形参传入的顺序

def logistic_change(name, age):
    print("name:", name)
    print("age", age)
    return


logistic_change("张三", "22")
logistic_change("李四", 20)

logistic_change(age="17", name="王五")

# lambda函数

sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值:", sum(10, 20))
print("相加后的值:", sum(40, 60))

# 全局变量和局部变量

total = 0


def sum_and(sum1, sum2):
    total = sum1 + sum2
    print("this is a 局部变量", total)


sum_and(10, 200)
print("this is a 全局变量", total)

