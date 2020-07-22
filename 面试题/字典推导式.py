# @Time    : 2020/7/22 15:17
# @Author  : Libuda
# @FileName: 字典推导式.py
# @Software: PyCharm

def gen_dict():
    dict = {key:value for key,value in enumerate(range(100))}

    return dict


res = gen_dict()
print(res)