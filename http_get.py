#This Python3 scrirpt makes a GET request with various parameters then prints the response.

#Required libraries
import requests

#This is the target URL
target = 'http://target-url-to-test.com'

#This is the header information, comment out what is not needed.
payload1 = {
    'Accept': '*/*',
    'Accept-Charset': 'utf-8',
    'Accept-Language': 'en-US',
    'Content-Type': 'application/xml',
    'Connection': 'keep-alive',
    #'Keep Alive': 'timeout=5, max=100',
    #'X-HTTP-Method-Override': 'content',
    #'X-Forwarded-For': '1.2.3.4',
    #'X-Forwarded-Host': 'domain.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/74.0'
}

#Note: Not all of the remaining items will be necessary. Comment out what is not needed.

#This is any necssary parameter information (as part of the URL), ex: target-url.com?parameter=value
payload2 = {'parameter':'value'}

#This is the cookie information
payload3 = dict(parameter='value')

#This is the authentication information
payload4 = ('username', 'admin')

#This is the actual HTTP GET request
x = requests.get(target, headers=payload1, params=payload2, cookies=payload3, auth=payload4)

#Optional - Print the HTTP status code
print('HTTP status code: ' + str(x.status_code))

#Optional - Print the created URL for testing
print(x.url + '\n')

#Print the HTTP response
print(x.content)