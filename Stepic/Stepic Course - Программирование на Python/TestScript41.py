import requests
r=requests.get('https://stepic.org/media/attachments/course67/3.6.2/324.txt', verify=False)
a=r.text
print(len(a.splitlines()))
