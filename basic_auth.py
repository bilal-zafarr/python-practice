# import requests
# url = "https://postman-echo.com/basic-auth"
# username = "postman"
# password = "password"
# response = requests.get(url, auth=(username, password))
# print(response.status_code)
# print(response.json())


import requests
url = "https://postman-echo.com/basic-auth"
header = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
response = requests.get(url, headers=header)
print(response.status_code)
print(response.json())