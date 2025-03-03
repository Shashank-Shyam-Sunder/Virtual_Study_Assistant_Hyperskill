# put your python code here
sum_nums = 0
sum_nums_sqr = 0

while True:
    num = int(input())
    sum_nums += num
    sum_nums_sqr += num ** 2
    if sum_nums == 0:
        print(sum_nums_sqr)
        break
