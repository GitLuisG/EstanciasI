import requests


url='https://www.google.com.mx/'
response = requests.get(url)

#print(response.status_code)

content=response.content
#print(response.content)
file = open('google.html','wb')
file.write(content)
file.close()
