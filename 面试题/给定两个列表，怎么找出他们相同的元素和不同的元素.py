# @Time    : 2020/7/22 15:30
# @Author  : Libuda
# @FileName: 给定两个列表，怎么找出他们相同的元素和不同的元素.py
# @Software: PyCharm

list1 = [1,2,3]
list2 = [3,4,5]

# 初步思想是  遍历两次 求出相同和不同

# 答案是python中的& ^ 可以求交集和并集
set1 = set(list1)
set2 = set(list2)

print(set1 & set2)
print(set1 ^ set2)