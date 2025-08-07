import requests
import json


url = "https://dummyjson.com/products"
params = {"limit": 1000, "skip": 0}

response = requests.get(url, params=params)

response_json = response.json()
products = response_json["products"]

# print(products)


# dict to string
base_dict = {'age': 12, 'address': 'Рибниця', 'married': False, 'more': None, 'money': 123.55}
string_from_dict = json.dumps(base_dict)
string_from_dict = json.dumps(base_dict, indent=4)
string_from_dict = json.dumps(base_dict, indent=4, ensure_ascii=False)
string_from_dict = json.dumps(base_dict, ensure_ascii=False, separators=(',', ':'), sort_keys=True)
print(string_from_dict)
print("\u0420")

# json string to dict
dict_from_string = json.loads(string_from_dict, parse_int=float)
print(dict_from_string)


# dict to file

# with open('products.json', mode='w', encoding='utf-8') as file:
#     json.dump(products, file, ensure_ascii=False, indent=4)

with open('products.json') as file:
    pr = json.load(file)
    print(pr[0])