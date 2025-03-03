num_list = []
while True:
    num = input()
    if num == ".":
        break
    else:
        num_list.append(int(num))

print(sum(num_list)/len(num_list))



