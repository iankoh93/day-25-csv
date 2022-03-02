import pandas

gray = 0
cinnamon = 0
black = 0

data = pandas.read_csv("raw_squirrel_data.csv")

# print(data["Primary Fur Color"])

for fur_color in data["Primary Fur Color"]:
    if fur_color == "Gray":
        gray += 1
    elif fur_color == "Cinnamon":
        cinnamon += 1
    elif fur_color == "Black":
        black += 1

# print(f"Gray: {gray}, Cinnamon: {cinnamon}, Black: {black}")

new_csv_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}

# print(new_csv_dict)

new_csv = pandas.DataFrame(new_csv_dict)
new_csv.to_csv("squirrel_count.csv")
