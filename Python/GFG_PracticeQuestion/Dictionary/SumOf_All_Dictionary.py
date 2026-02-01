# We have to find the sum of all items in a dictionary.
# Ex-> 'a':100, 'b':200 = 100+200=300.

#1. Using sum()
# d= {'a':100,'b':200,'c':300}
# res= sum(d.values())
# print(res)

#2. List Comprehension
# d= {'a':100,'b':200,'c':300}
# res= sum([d[key] for key in d])
# print(res)

#3. Loop
# d= {'a':100,'b':200,'c':300}
# res= 0
# for i in d.values():
#     res+= i
# print(res)

#4. Map or Lambda
# d= {'a':100,'b':200,'c':300}
# res= sum(map(lambda key: d[key],d))
# print(res)