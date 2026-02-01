# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 


# 1. Loop

# tes_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

# print("The Original List is: " + str(tes_list))

# res = []
# for sub in tes_list:
#     if res and res[-1][0] == sub[0]:
#         res[-1].extend(sub[1:])
#     else:
#         res.append([ele for ele in sub])
# res=list(map(tuple,res))
# print("The Extracted Element: " + str(res))


# 2. Loop
tes_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The Original List: " + str(tes_list))

res = []
x = []
for i in tes_list:
    if i[0] not in x:
        x.append(i[0])
for i in x:
    p=[]
    p.append(i)
    for j in tes_list:
        if i==j[0]:
            p.append(j[1])
    res.append(p)

print("The extracted elements : " + str(res))