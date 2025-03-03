cafe_names, cafe_cats = [], []
while True:
    cafe_data = input().split()
    if cafe_data[0] == "MEOW":
        break
    else:
        cafe_names.append(cafe_data[0])
        cafe_cats.append(int(cafe_data[1]))

print(cafe_names[cafe_cats.index(max(cafe_cats))])



