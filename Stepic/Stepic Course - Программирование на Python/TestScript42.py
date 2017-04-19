import requests
r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt", verify=False)
s = "https://stepic.org/media/attachments/course67/3.6.3/";
f = (requests.get(s+r.text, verify=False)).text
while True:
    print(s+f)
    f = requests.get(s+f, verify=False).text
    if f[:2] == 'We':
        print(f)
        break
print(requests.get(s+f,verify=False).text)
