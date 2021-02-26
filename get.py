import requests
import re
import time

url = 'https://video.coral.qq.com/varticle/5963120294/comment/v2'

x = 1614258172153
cursor = 6770547687009275332
for j in range(0,1300):
    time.sleep(1)
    param = {
        'callback': '_varticle5963120294commentv2',
        'orinum': '10',
        'oriorder': 'o',
        'pageflag': '1',
        'cursor': cursor,
        'scorecursor': '0',
        'orirepnum': '2',
        'reporder': 'o',
        'reppageflag': '1',
        'source': '132',
        '_': x,
        }
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
  
    response = requests.get(url = url, params = param ,headers = header)
    page_text = response.text
    content = re.findall('.*?"content":"(.*?)",',page_text,re.S)
    cursor = re.findall('.*?"last":"(.*?)","hasnext"',page_text,re.S)
    x += 1

    with open('tengxun_together.txt','a',encoding = 'utf-8') as fp:
        fp.write(str(content))
#fp = open('tenxun.txt','w',encoding = 'utf-8')
#json.dump(dic_obj, fp = fp, ensure_ascii = False)
#fp.close()
print('over')