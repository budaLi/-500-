# @Time    : 2020/7/22 15:14
# @Author  : Libuda
# @FileName: 字典按value排序.py
# @Software: PyCharm


d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
def sort(dict):
    # 会将字典变为元祖的形式
    print(dict.items())
    # revers代表是否逆序
    dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)

    return dict

if __name__ == '__main__':

    s = sort(d)
    print(s)