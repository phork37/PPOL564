import copy

friends = ["Benny","Juice","Hewy","Samantha"]
friends.append("Ralph")
friends.remove("Juice")
friends.sort()
print(friends)

grades = {"John": [90,88,95,86],"Susan":[87,91,92,89],"Chad":[56,None,72,77]}
keys = list(grades.keys())
print(keys)
transfer_file = grades.pop("Chad")
print(transfer_file)
print(grades)

new = copy.deepcopy(grades)
new["John"][1] = 90
print(grades["John"])
print(new["John"])
