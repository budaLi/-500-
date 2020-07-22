# @Time    : 2020/7/22 15:19
# @Author  : Libuda
# @FileName: 将字符串处理成字典.py
# @Software: PyCharm

s = "k:1 |k1:2|k2:3|k3:4"


dic = dict()
for item in s.split("|"):
    one = item.strip().split(":")
    dic[one[0]] = one[1]


print(dic)
