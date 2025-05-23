"""
What is a JSON File?
-A JSON (JavaScript Object Notation) file is a lightweight 
 data format used to store and exchange structured data. 
 It is easy for both humans and machines to read and write.

 -kind of kay vale pair

Key Features of JSON:
✅ Lightweight – Simple, text-based, and easy to use.
✅ Readable – Uses key-value pairs (like a dictionary in Python).
✅ Language-Independent – Works with Python, Java, JavaScript, etc.
✅ Widely Used – API responses, configuration files, data storage, etc



Example: Why JSON is Used & How It Works
Scenario:
You are building a weather app that fetches live temperature data from a server. 
The server sends the data in JSON format, and your app processes it.

"""

"""
JSON to Python (data type):

JSON   --      Python
...........................

object         dict
array          list
string         str
number(int)    int
number(real)   float
true           True
false          False
null           None
"""


# json.load() vs json.loads()

# json.load(): 
# Used to read a JSON file and convert it into a Python dictionary.
# Takes a file object as input.

# json.loads():
# Used to parse a JSON string and convert it into a Python dictionary.
# Takes a JSON-formatted string as input.

# Example Use Cases:
# json.load() → When reading JSON data from a file.
# json.loads() → When parsing a JSON string received from an API or other sources.
