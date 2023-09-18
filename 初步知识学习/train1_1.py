# _*_ coding ： utf-8 _*_
# @Time ：2023/9/13 9:36
# @Author ： LI李
# @File ：train1_1
# @Project ：列表

#  列表
list1 = ['String', 'int', 1, 2, 3]

list1.append('来之前')
list1.append('来之后')
print("12行:", list1)  # output：['String', 'int', 1, 2, 3, '来之前', '来之后']

del list1[2]
print("15行:", list1)  # output:['String', 'int', 2, 3, '来之前', '来之后']

# 长度 len()
list1_n = len(list1)
print("19行:", list1_n)

# 组合+
list1_1 = ['This', 'is', 'my', 'name']
list1_zh = list1 + list1_1
print("24行:", list1_zh)  # ['String', 'int', 2, 3, '来之前', '来之后', 'This', 'is', 'my', 'name']

# 重复 *n
print("27行:", list1_zh * 2)

# 判断元素是否存在列表中
judge_list1 = 2 in list1
print("31行:", judge_list1)  # True

# 迭代遍历
for x in list1:
    #    print(x)  # 自动换行
    print("36行:", x, end=" ")  # 不换行

# -------------------------分隔线-----------------------------

# 截取
list2 = [1, 2, 3]
print("42行:", list2[-1])
print("43行:", list2[1:])

# 列表函数和方法
list2_max = max(list2)
print("47行:", list2_max)  # 不能出现字符类型
list2_min = min(list2)
print("49行:", list2_min)

# 元组转化为列表
tuple1 = ('1', 2, 'lz')
print("53行:", tuple1)
list3 = list(tuple1)
print("55行:", list3)

# 总结  append 末尾添加元素
list_end = [520, 12, 20, 82]
list_end.append('ps')
print("60行:", list_end)

# count 统计某个元素在列表中出现的次数
print("63行:", list_end.count(12))

# index 找出列表中某个值第一个匹配的索引
print("66行:", list_end.index(520))

# insert将对象插入列表
print("69行:", list_end)
list_end.insert(-7, 'an')
print("71行:", list_end)

# extend 末尾一次性追加另一个序列中的多个值
list_end.extend([1, 6, 7])
print("75行:", list_end)

# pop 移出列表中的一个元素 默认最后一个
list_end.pop(4)  # 这里的4是指下标中的。
print("79行:", list_end)

# remove移除列表中的某个值的第一个匹配项
list_end.remove(1)  # 删除列表中的  第一次出现 值 1
print("83行:", list_end)

# reverse反向列表中的元素
list_end.reverse()
print("87行:", list_end)

# sort对原列表进行排序
list_end1 = [3, 5, 8, 4, 6, 1, 92]
list_end1.sort(reverse=False)  # False升序
print("92行:", list_end1)
list_end1.sort(reverse=True)  # True降序
print("94行:", list_end1)
