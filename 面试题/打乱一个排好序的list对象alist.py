# @Time    : 2020/7/22 15:12
# @Author  : Libuda
# @FileName: 打乱一个排好序的list对象alist.py
# @Software: PyCharm

list = list(range(1,100))

import random
def shuffle(list):
    # 要注意 不会返回
    random.shuffle(list)
    return list

if __name__ == '__main__':

    res = shuffle(list)
    print(res)
