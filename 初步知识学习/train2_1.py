# _*_ coding ： utf-8 _*_
# @Time ：2023/9/13 17:01
# @Author ： LI李
# @File ：train2_1
# @Project ：时间和日期

# time 函数模块

import calendar
import time

# 获取时间戳
ticks1 = time.time()
print("当前时间戳为:", ticks1)

# 获取当前时间 localtime
ticks1_1 = time.localtime(ticks1)
print(ticks1_1)

# 格式化时间  其中ticks1_是当前时间
ticks1_2 = time.asctime(ticks1_1)
print(ticks1_2)

# 获取某月日历
cal_9 = calendar.month(2023, 9)
print(cal_9)