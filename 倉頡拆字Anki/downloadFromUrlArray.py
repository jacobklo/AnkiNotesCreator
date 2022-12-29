import requests
import time

urls = [
"https://www.hkcards.com/img/cj/嗷.png",
"https://www.hkcards.com/img/cj/嗽.png",
"https://www.hkcards.com/img/cj/嘀.png",
"https://www.hkcards.com/img/cj/嘂.png",
]

for i in range(len(urls)):
  u = urls[i]
  r = requests.get(u, allow_redirects=True)
  name = u.split('/')[-1]
  open('images/'+name, 'wb').write(r.content)
  print('done ', i+1010, name)
  r.close()
  time.sleep(1)
