# @Time    : 2020/7/22 15:05
# @Author  : Libuda
# @FileName: 显示文件.py
# @Software: PyCharm
import os
def print_file(path):
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        if os.path.isdir(file_path):
            print_file(file_path)
        else:
            print(file_path)


if __name__ == '__main__':
    print_file("D:\\")