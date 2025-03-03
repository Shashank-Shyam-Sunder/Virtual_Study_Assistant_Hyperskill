my_list = []
while True:
    input_number = input()
    if input_number == ".":
        break
    else:
        my_list.append(float(input_number))

print(min(my_list))



