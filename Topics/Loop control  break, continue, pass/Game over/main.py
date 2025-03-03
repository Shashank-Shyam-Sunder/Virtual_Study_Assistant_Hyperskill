scores = input().split()
num_no = 0
num_yes = 0

for ans in scores:
    if ans == "C":
        num_yes += 1
    elif ans == "I":
        num_no += 1
    if num_no == 3:
        print("Game over")
        break
if num_no != 3:
    print("You won")
print(num_yes)
