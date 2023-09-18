# _*_ coding ： utf-8 _*_
# @Time ：2023/9/13 11:02
# @Author ： LI李
# @File ：train1_3
# @Project ：字典

#  字典的定义   key：value { }
tinydic = {2: 'x', 'w': 6}
print("9行:", tinydic)

print("11行:", tinydic[2])
print("12行:", tinydic['w'])

# 值可以去任意数据类型，但键必须是不可变的 如字符串 、数字、元组、

# 访问字典里的值

tinydic1 = {5: 'kie', 'ni': 64}
print("19行:", tinydic1)

# 修改字典里面的值
tinydic1[5] = 'wide'
tinydic1['ni'] = '4515'
print("24行:", tinydic1)

# 删除字典里面的值
print("27行:", tinydic)
del tinydic[2]
print("29行:", tinydic)
del tinydic  # 删除整个字典

# 不允许一个字典中有两个相同键
# 不允许字典中的键出现列表

tinydic3 = {(1, 2): '20', 'w': 12}
print("36行:", tinydic3)

# 字典内置函数

# len 计算键的个数
print("41行:", len(tinydic3))

# 打字符串
print("44行:", str(tinydic3))

# 返回变量的类型
print("47行:", type(tinydic3))

# 删除字典内所有元素
tinydic3.clear()
print("51行:", tinydic3)

# 返回一个字典的浅复制
tinydic1_x = tinydic1.copy()
print("55行:", tinydic1_x)

# 返回指定键的值，如果不存在则返回default中的值为None
eg_tinydic = {'1': 100, '李志强': '2021'}
str1 = eg_tinydic.get('1')
print("60行:", str1)
str2 = eg_tinydic.get('wide')
print("62行:", str2)

# 检测key是否在字典中 并返回对应值  没有返回None  并将该值设置到字典中
eg_tinydic1 = {2: 200, '梦想的': '远方'}
print("66行:", eg_tinydic1.setdefault('1', 'x'))

# 返回字典中的所有值
print("69行:", eg_tinydic1.values())

# 返回字典中的所有键
print("72行:", eg_tinydic1.keys())

# 删除字典中的特定的key对应的value值并返回value值
print("75行:", eg_tinydic1.pop(2))  # output：200
print("76行:", eg_tinydic1)  # output：{'梦想的': '远方', '1': 'x'}

# 返回并删除字典中最后一对键和值
print("79行:", eg_tinydic1.popitem())  # output:('1', 'x')

# 增加一个字典值
eg_tinydic1['c'] = "增加的值"
print("83行：增加一个字典键值对：", eg_tinydic1)

# 增加多个字典的值
a_dic = {"a": 1, "b": 2, "c": 3}
print("87行：", a_dic)
b_dic = {"d": 4, "e": 5, "f": 6, "a": 7}  # 当出现相同的键时使用update会将原来的键对应的值给覆盖掉
a_dic.update(b_dic)
print("90行：", a_dic)

# 解包字典创建
a = ['a', 'b', 'c']
b = [1, 2, 3, 4, 5, 6]
c = dict(zip(a, b))
print("96行：", c)

# for 循环返回字典中的键
print("100行:c字典中的键有", end=" ")
for i_key in c.keys():
    print(i_key, end=" ")
print()

# for 循环返回字典中的值
print("107行:c字典中的值有", end=" ")
for i_value in c.values():
    print(i_value, end=" ")
print()

# for 循环返回字典中的 键和值一对
print("111行:c字典中的键和值有", end=" ")
for i_key_value in c.items():
    print(i_key_value, end=" ")
print()

# 创建集合
my_set = set({})
print("118行:一个空集合的创建方式", my_set)

# 列表和集合的相互转换
a_list = [1, 2, 3, 4, 5, 6, 4, 8, 9, 8, 1, 5, 4, 6, 5, 4, 6, 5]
a_set = set(a_list)
print("123行:", a_set)
a_list = list(a_set)
print("125行:", a_list)

# 集合的交&、并|、差- 集
b_set = {1, 3, 5, 9, 11, 12, 6}
c_set = {1, 2, 3, 4, 5, 6, 8, 9}
print("130交集:", b_set & c_set)
print("131并集:", b_set | c_set)
print("132差集:", b_set - c_set)
