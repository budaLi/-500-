# @Time    : 2020/7/22 14:55
# @Author  : Libuda
# @FileName: 文件操作.py
# @Software: PyCharm

# 正常读取文件   当文件过大时会存在Io性能瓶颈
def read_file(path):
    with open(path) as f:
        datas = f.readlines()
    return datas

# 现在要处理一个大小为10G的文件，但是内存只有4G，应该如何实现？需要考虑的问题都有那些？
def read_file_two(path,number):
    with open(path) as f:
        datas = f.readlines(number)
    return datas



if __name__ == '__main__':

    path = "text.txt"
    for line in read_file_two(path,30):
        print(line.strip())

