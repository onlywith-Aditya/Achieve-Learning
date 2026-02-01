# # How to sort a dictionary by values.

# # 1. Itemgetter.
# from operator import itemgetter
# data_list= [{"name": "Nandini", "age": 20},
#             {"name": "Manjeet", "age": 21},
#             {"name": "Nikhil", "age": 19}]
# print("\n The list printed sorting by age:")
# print(sorted(data_list, key=itemgetter('age')))
# print("\r")

# # Sorting age and name:
# print("\n The list printed sorting by age and name :")
# print(sorted(data_list, key=itemgetter('age', 'name')))
# print("\r")

# # Descending Order:
# print("\n The list printed sorting by age in descending order: ")
# print(sorted(data_list, key=itemgetter('age'), reverse= True))


# 2. Lambda Function
# list = [{"name": "Nandini", "age": 20},
#     {"name": "Manjeet", "age": 20},
#     {"name": "Nikhil", "age": 19}]

# print("The list printed sorting by age: ")
# print(sorted(list, key=lambda i:i['age']))

# print("\nThe list printed sorting by age and name: ")
# print(sorted(list, key=lambda i:(i['age'], i['name'])))

# print("\nThe list printed sorting by age in descending order: ")
# print(sorted(list, key=lambda i:i['age'], reverse= True))