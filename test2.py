from requests import get
response = get("https://api.github.com/repos/JOJO-men/Horizon/releases/latest")
f = open('example.txt', 'w+')
print(response.json()["published_at"])
f.write(response.json()["published_at"])