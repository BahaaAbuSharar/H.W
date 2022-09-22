# Ex2:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
for i in list(sample_dict):
    for item in range(len(keys)):
        if keys[item] == i:
            sample_dict.pop(keys[item])
print(sample_dict)