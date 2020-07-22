# @Time    : 2020/7/22 15:09
# @Author  : Libuda
# @FileName: 判断日期.py
# @Software: PyCharm

#输入日期， 判断这一天是这一年的第几天？

import datetime
def judge(year,month,day):
    start_date = datetime.date(year=year,month=1,day=1)
    end_date = datetime.date(year,month,day)
    print((end_date-start_date).days+1)

if __name__ == '__main__':

    judge(2020,1,2)