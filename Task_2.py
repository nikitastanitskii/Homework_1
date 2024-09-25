import json

my_dict = json.loads(input())
min_key = min(my_dict,key = my_dict.get)

print(min_key)