import requests #url을 가져와 문자열 데이터를 얻기 위해 request모듈을 import해 줍니다.

import re #re.sub을 이용하기 위해 re모듈을 import합니다

url='https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day§ionId=100&date=20181121' #2018년. 11월. 21일자의 인기 뉴스. 30개가 정렬된 주소를 가져와 url을 정의해줍니다.

r=requests.get(url) #request로 url의 데이터를 가져옵니다

data=str(r.text) #r의 텍스트를 string으로 하여 data를 정의해줍니다.

begin=data.find('<li class="ranking_item is_num1">') #가지고 온 data에는 뉴스 제목 이외의 포털 사이트 이름 등의 불필요한 부분이 있어 필요한 부분의 시작점을 설정합니다.

end=data.rfind('국회 본회의 의결과 헌법 재 …')+len('국회 본회의 의결과 헌법 재 …') #마찬가지로 끝점 역시 설정해주는데, 이때 끝에서부터 찾기 위해 rfind를 사용했습니다 그리고 설정한 부분이 자료에 포함되게 하기 위해 len으로 그만큼을 더해줍니다

data=data[begin:end] #begin부터 end지점까지의 부분만을 data로 새롭게 정의해줍니다

data=re.sub('<a href.*?>',' ',data)  #re.sub을 통해 단어 추출에 방해되는 태그나 기능어들을 공백으로 대치시킵니다.

data=re.sub('&quot;', ' ', data)

 

line=[] #기사의 제목은 "title= ~" 형태를 취하고 있습니다 따라서 if문을 통해 line에서 시작점과 끝점이 조건에 맞는 것만을 뽑아줍니다.

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

    str1=str1+line[I] #도출된 line[I]을 str1에 더해 조건에 맞는 데이터가 str에 들어가도록 합니다

str1=str1.replace('"','') #문장부호가 붙어 있으면 단어로 추출되지 않기 때문에 공백으로 대치시킵니다

str1=str1.replace(',','')

words=str1.split()

frequency={} #빈 딕셔너리를 만들어줍니다

for w in words:

    if w in frequency:

        if len(w)<=1: #한 글자로 이루어진 '안' 등의 관형어가 추출되는 것을 막기 위해 길이가 한 글자인 경우 빈도를 0으로 해줍니다

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

for key in sorted(frequency, key=keyfunction, reverse=True)[:5]: #상위5위까지의 단어만 보도록 하겠습니다

    print("%s:%i"%(key,frequency[key])) #딕셔너리의 키와 밸류값을 프린트합니다
