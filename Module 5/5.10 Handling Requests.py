# Request handling module

# Request ---> (API)url ----> Response Cycle # api er through te ei dhoroner request korte pari,
# Ostad er website e account create kori  - POST 
# Course details dekhar request kori      - GET 
# Ami nijer porofile update korete pari   - PUT/PATCH/UPDATE
# Ostad kono course delete korte pare     - DELETE
 

#jekono system ei 4 ta requst diye chole
#python has inbuild request module that can use to maintian avobe this request
import requests

# GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts") # post dekhlam, like read korlam
print(response)
#output:
# <Response [200]>  # 200 means (OK) Standard response for successful HTTP requests.
print(response.status_code)
#200 #a request was successful
print(response.json())



# POST request (like account create korbo)

data = {'userId': 1, 'id': 1, 'title': 'for test'}
response =  requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)
#201  #means Created 
print(response.json())


# UPDATE request
data = {'userId': 1, 'id': 1, 'title': 'for test(updated)'}
response =  requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)
print(response.status_code)
#200   #a request was successful
print(response.json())
# {'userId': 1, 'id': 1, 'title': 'for test(updated)'} #updated


# DELETE request
#data = {'userId': 1, 'id': 1, 'title': 'for test'} # data lagbe na , cz id1 k dlt korbo
response =  requests.delete("https://jsonplaceholder.typicode.com/posts/1", json=data)
print(response.status_code)
print(response.json())