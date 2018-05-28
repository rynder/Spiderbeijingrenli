from pyquery import PyQuery as pq
import requests

url = 'http://www.bjrbj.gov.cn/xxgk/gsgg/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/65.0.3325.162 Safari/537.36'
}
html = requests.get(url, headers=headers)
html.encoding = 'GBK'
htmll = html.text

doc = pq(htmll)
print(doc.find('.conright'))

items = doc('.conright').items()

#print(doc)
for item in items:
    title = item.find('.con').text()
   # date = item.find('.span').text()
    print(1)
    file = open('spider.txt', 'a', encoding='utf-8')
    file.write('\n'.join([title]))
    file.write('\n'+'='*50+'\n')
    file.close()
