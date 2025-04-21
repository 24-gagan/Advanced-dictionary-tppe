import json

# Python dict to JSON
data = {
    "name": "Rahul",
    "age": 25
}
json_data = json.dumps(data)  # Convert dict to JSON string
print(json_data)

# JSON to Python dict
json_str = '{"name": "Rahul", "age": 25}'
data_dict = json.loads(json_str)
print(data_dict)
