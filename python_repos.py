import requests

#make an api call and store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#store api response in a variable
responseDict = r.json()
print(f"Total repositories: {responseDict['total_count']}")

#explore information about the repositories
repoDicts = responseDict["items"]
print(f"Repositories returned: {len(repoDicts)}")

#examine the first repository
repoDict1 = repoDicts[0]
print("\nKeys: ", len(repoDict1))
for key in repoDict1.keys():
    print(key)

