import requests

import re

url='https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day§ionId=100&date=20181121'

r=requests.get(url)

data=str(r.text)

begin=data.find('<li class="ranking_item is_num1">')

end=data.rfind('국회 본회의 의결과 헌법 재 …')+len('국회 본회의 의결과 헌법 재 …')

data=data[begin:end]

data=re.sub('<a href.*?>',' ',data)

data=re.sub('&quot;', ' ', data)

 

line=[]

while 1 :

    if data.find("title=")!=-1:

        start=data.find("title=")+len('title=')

        end=len(data[:start])+data[start+len('title="'):].find('"')+len('title="')+2

        line.append(data[start:end])

        data=data[end:]

    else:

        break

str1=""

for i in range(len(line)):

    str1=str1+line[i]

str1=str1.replace('"','')

str1=str1.replace(',','')

words=str1.split()

frequency={}

for w in words:

    if w in frequency:

        if len(w)<=1:

            frequency[w]=0

        else:

            frequency[w]+=1

    else:

        if len(w)<=1:

            frequency[w]=0

        else:

            frequency[w]=1

        

def keyfunction(k):

    return frequency[k]

for key in sorted(frequency, key=keyfunction, reverse=True)[:5]:

    print("%s:%i"%(key,frequency[key]))

