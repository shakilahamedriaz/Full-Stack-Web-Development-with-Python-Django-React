#convert dictonary to json & json to dictonary

import json

data = {
    'name' : "Rahim",
    'age'  : 30,
    'is_logget_int' : True,   
}


# serialization: python --> Json
# convert this(data) to json string format
json_string = json.dumps(data, indent=4) # to convert data into json format, indent 4 means: maintain 4 spaces
print(json_string)

"""
#output:
{
    "name": "Rahim",
    "age": 30,
    "is_logget_int": true
}
"""

print(type(json_string))
#<class 'str'>




# Deserialization : Json ---> Python
# convert json string to python (dict)

json_string = '{"name": "Rahim", "age": 30, "is_logget_int": true}'
#key name should be in (double quotes("key" : value))
python_dict = json.loads(json_string)
print(python_dict)



