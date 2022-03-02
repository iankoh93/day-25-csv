import csv
import pandas
import math

# temperature = []
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     next(data)
#     for row in data:
#         print(row)
#         temperature.append(int(row[1]))
#     print(temperature)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# temp_max = data["temp"].max()
# # print(temp_max)
#
# monday = data[data.day == "Monday"]
# f_temp = monday.temp * (9 / 5) + 32
# print(f_temp)

data_dict = {
    "students": ["Ian", "Jasmine", "Angela"],
    "scores": [90, 76, 99],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
