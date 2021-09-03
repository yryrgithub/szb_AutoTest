import csv

from email.mime.image import MIMEImage
import pymysql

# from functools import reduce
#
#
# def fun_test():
#     # while True:
#     #     n = int(input("请输入整数："))
#     #     for i in range(n):
#     #         print(fun3(i), end=" ")
#     #     print("")
#     # bubble_sort()
#     fun5()
#
#
# def fun1(n):
#     for i in range(n):
#         for j in range(0, n - i):
#             print(end=" ")
#         for k in range(n - 1 - i, n):
#             print("*", end=" ")
#         print("")
#
#
# def fun2(n):
#     for i in range(n):
#         for j in range(n - i, n):
#             print(end=" ")
#         for k in range(0, n - i):
#             print("*", end=" ")
#         print("")
#
#
# def fun3(n):
#     if n <= 1:
#         return n
#     else:
#         return fun3(n - 1) + fun3(n - 2)
#
#
# def fun4():
#     list = [1, 3, 5, 2, 22, 4, 25, 6, 17, 33]
#     length = len(list)
#     for i in range(length):
#         for j in range(length - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     print(list)
#
#
# def fun5():
#     l = [1, 2, 3, 'a', 'b', 'c', 1, 2, 'a', 'b', 3, 'c', 'd', 'a', 'b', 1]
#     set1 = set(l)
#     print(set1)
#     result = [(item, l.count(item)) for item in set1]
#     result.sort(key=lambda x: x[1], reverse=True)
#     print(result)
#
#
# def fun6(num):
#     list = []
#     for n in range(num):
#         row = [1]
#         list.append(row)
#         if n == 0:
#             print(row)
#             continue
#         for m in range(1, n):
#             row.append(list[n - 1][m - 1] + list[n - 1][m])
#         row.append(1)
#
#         print(row)
#
#
# def bubble_sort():
#     list = [2, 4, 1, 24, 7, 9, 0, 32, 14, 6]
#     l = len(list)
#     for i in range(l - 1):
#         for j in range(l - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#
#     print(list)
#
#
# def fun7():
#     list = []
#     list.insert(0, "1")
#     list.insert(0, "2")
#     list.insert(0, "3")
#     for i in range(len(list)):
#         print(list.pop(0))
#     # list.pop()
#     # list.pop()
#     # list.pop()
#     # print(list)
#
#
# def fun8():
#     for i in range(10):
#         for j in range(10 - i, 10):
#             print(end=' ')
#         for k in range(0, 10 - i):
#             print("#", end=' ')
#         print('')
#
#
# def fun9():
#     for i in range(10):
#         for j in range(0, 10 - i):
#             print(end=' ')
#         for k in range(10 - i - 1, 10):
#             print('*', end=' ')
#         print('')
#
#
# def fun10():
#     for i in range(10):
#         for j in range(10 - i, 10):
#             print(end=' ')
#         for k in range(10 - i):
#             print('*', end=' ')
#         print('')
#
#
# def fun11(n):
#     if n <= 1:
#         return n
#     else:
#         return fun11(n - 1) + fun11(n - 2)
#
#
# def fun12(n):
#     list = []
#     for i in range(n):
#         row = [1]
#         list.append(row)
#         if i == 0:
#             print(row)
#             continue
#         for j in range(1, i):
#             row.append(list[i - 1][j - 1] + list[i - 1][j])
#         row.append(1)
#         print(row)
#
#
# s2 = (85 - 72) / 85 * 100
# print('%.2f%%' % s2)
#
#
# def fun20():
#     height = 1.75
#     weight = 80.5
#     bmi = weight / (height * height)
#     if bmi < 18.5:
#         print('过轻')
#     elif bmi >= 18.5 and bmi < 25:
#         print('正常')
#     elif bmi >= 25 and bmi < 28:
#         print('过重')
#     elif bmi >= 28 and bmi < 32:
#         print('肥胖')
#     else:
#         print('严重肥胖')
#
#     L = ['Bart', 'Lisa', 'Adam']
#     for name in L:
#         print("hell %s!" % name)
#
#     print(hex(1000))
#
#
# def my_abs(n):
#     if n > 0:
#         return n
#     else:
#         return -n
#
#
# myabs_n = my_abs(123)
#
#
# def add_end1(l=[]):
#     l.append('END')
#     return l
#
#
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
#
# # add_end()
# # add_end()
# print(add_end(None))
#
# # print(abs_n)
# print(myabs_n)
#
#
# def cacl(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = cacl(*l)
# print(result)
#
#
# def str_lower():
#     l = ['Hello', 'World', 18, 'APple', None]
#     for s in l:
#         if isinstance(s, str):
#             print(s.lower())
#
#
# # str_lower()
#
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b, end=' ')
#         a, b = b, a + b
#         n = n + 1
#
#
# def triangles(num):
#     l = []
#     for i in range(num):
#         row = [1]
#         l.append(row)
#         print(end='')
#         if i == 0:
#             # 将prin换成yield，该函数变成generator
#             yield row
#             continue
#         for j in range(1, i):
#             row.append(l[i - 1][j - 1] + l[i - 1][j])
#         row.append(1)
#         yield row
#
#
# for t in triangles(10):
#     print(t)
#
#
# def fun(x, y):
#     return x * 10 + y
#
#
# def strint(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}[s]
#
#
# # a=strint('3')
# # print(a)
# ll = reduce(fun, map(strint, '2403'))
# print(ll)
#
#
# def normalize(name):
#     return name.capitalize()
#
#
# L1 = ['adam', 'LISA', 'barT']
# l2 = list(map(normalize, L1))
# print(l2)
#
#
# def prod(L):
#     def mul(x, y):
#         return x * y
#
#     l2 = reduce(mul, L)
#     return l2
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, -7, -9]))
#
#
# def str2float(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def charnum(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#     return reduce(fn, map(charnum, s.replace('.','')))
#
#
# s = '123.456'
# if s.find(".") != -1:
#     print('str2float(\'%s\') =' %s, str2float(s) / pow(10,len(s) - s.find(".") - 1))
# else:
#     print('str2float(\'%s\') =' %s, str2float(s))


# fun20()
# fun10()
# fun9()
# fun1(10)
# fun2(10)
# print(fun11(10))
# print(fun3(10))
# for i in range(11):
#     print(fun3(i),end=' ')
# print('')
# # fun6(10)
# fun12(10)
# # fun_test()
# import datetime
#
# import math
# from openpyxl import load_workbook
#
#
# def analyse():
#     filename = 'F:\\DS_WZF301_result-10-200.jtl'
#     file = csv.reader(open(filename))
#     data = []
#     for row in file:
#         data.append(row)
#     data.pop(0)
#     elapseds = []
#     errorCount = 0
#     for item in data:
#         elapseds.append(int(item[1]))
#         if (str(item[7]) != 'true'):
#             errorCount = errorCount + 1
#     elapseds.sort()
#     print(elapseds)
#
#     times = len(data)
#     elapsedMs = int(data[-1][0]) - int(data[0][0])
#     keys = []
#     keys.append(str('吞吐量TPS：'))
#     keys.append(str('最小响应时长ms：'))
#     keys.append(str('最大响应时长ms：'))
#     keys.append(str('平均响应时长ms：'))
#     keys.append(str('错误率：'))
#     keys.append(str('90%时长ms：'))
#     keys.append(str('95%时长ms：'))
#     keys.append(str('95%时长ms：'))
#
#     values = []
#     values.append(float(times) / elapsedMs * 1000)
#     values.append(str(elapseds[0]))
#     values.append(str(elapseds[-1]))
#     # values.append(str(float(sum(elapseds))/times))
#     values.append(str(float(sum(elapseds)) / times))
#     values.append(str(float(errorCount) / times))
#     values.append(str(elapseds[int(times * 0.9)]))
#     values.append(str(elapseds[int(times * 0.95)]))
#     values.append(str(elapseds[int(times * 0.99)]))
#
#     print(values)
#     return keys, values
#
#
# def print_file(rest, file):
#     for key in rest[0]:
#         print(key, end='\t', file=file)
#     print(file=file)
#     for value in rest[1]:
#         print(value, end='\t', file=file)
#     print(end='\r\n', file=file)
#
#
# def write_file():
#     result_name = 'F:\\'
#     current_time = datetime.datetime.now().strftime('_%Y%m%d%H%M%S')
#     dest = open(result_name + 'anlyse' + current_time + '.txt', 'a')
#     d = analyse()
#     print_file(d, dest)
#
#
# write_file()


import datetime, time
import threading
# def do_thing(name):
#  """线程运行的方法"""
#  print('start doing thing:' + str(name), datetime.datetime.now())
#  time.sleep(5)
#  print('end doing thing:' + str(name), datetime.datetime.now())
# names = ["第一条线程", "第二条线程", "第三条线程"]
# for name in names:
#  # 创建线程
#  t = threading.Thread(target=do_thing, args=(name,))
#  # 启动线程
#  t.start()
#  time.sleep(1)


class MyThreading(threading.Thread):
    def __init__(self, arg):
        super(MyThreading, self).__init__()

        self.arg = arg

    def run(self):
        """重写 run()方法运行"""

        print('start doing thing:' + str(name), datetime.datetime.now())
        time.sleep(5)
        print('end doing thing:' + str(name), datetime.datetime.now())


names = ["第一条线程", "第二条线程", "第三条线程"]
for name in names:
    t = MyThreading(arg=(name,))
    t.start()
    time.sleep(1)