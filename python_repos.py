import requests

#make an api call and store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#store api response in a variable
responseDict = r.json()

#process results
print(responseDict.keys())