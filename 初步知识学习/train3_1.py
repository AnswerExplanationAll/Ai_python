# _*_ coding ： utf-8 _*_
# @Time ：2023/9/13 17:45
# @Author ： LI李
# @File ：train3_1
# @Project ：import 模块

# 解释：Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

# 模块能定义函数，类和变量，模块里也能包含可执行的代码。

# 导入自定义的模块support
import support

# 导入自定义模块中的部分语句
from modname import mul


# 把一个模块的所有内容全都导入到当前的命名空间
from train2_2 import *

# ------------------分割线------------------


# 调用自定义模块中的函数
support.print_func("Aime")

# 特殊说明：一个模块只能够被导入执行一次

# 执行自定义模块的部分函数
mul(10, 15)

sum_and(20,13)

