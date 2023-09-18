# _*_ coding ： utf-8 _*_
# @Time ：2023/9/13 10:39
# @Author ： LI李
# @File ：train1_2
# @Project ：元组

# 创建空元组
tup1 = ()

# 只有一个元素要加,
tup2 = (1,)

# 访问元素
tup3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tup3[4])

# 切片
print(tup3[6::-3])
# 如果我想切 7 4 2 呢？ 该怎么切？

# 元组不能随意的修改元素

# tup3[1] = 100  # 非法

# 删除元组  注意：元组中的元素不能被删除  只能将整个元组删除

del tup1
# print(tup1) 显示未定义

# 任意无符号的对象，以逗号隔开，默认为元组
tuple4 = 1, 5, 9, 7, 3, 8, 6
print(tuple4)
# len计算个数 + 连接 *倍数
print(len(tuple4))
print(tuple4 + (12, 10, 20))
print(tuple4 * 2)

# 迭代 遍历
for x in tup3:
    print(x, end=" ")

# min max
print()
print(max(tup3))
print(min(tup3))

# 列表转换为元组 tuple
list4 = [1, 5, 6, 7, 2, 0]
print(tuple(list4))

# 元组不可改变是指它的地址时不可改变的
a_tuple = (1, 2, 3, [4, 5, 6], 7, 8)
print(id(a_tuple[3]))  # id是拿地址的
a_tuple[3][1] = 10
print(a_tuple)
print(id(a_tuple))
