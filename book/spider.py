import urllib.request
import urllib3

response=urllib.request.urlopen('https://www.baidu.com/')
html=response.read()
print(html)

http=urllib3.PoolManager()
response2=http.request('GET','https://www.baidu.com/')
print(response2.data)