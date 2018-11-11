import requests
url = 'https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text '
r = requests.get(url)
r.encoding = 'utf8'
data = str(r.text)

mydict = {}
words = input('data').split()
words = words.replace('"','')
words = words.replace("'", "")
print(words)
for w in words:
    if w in mydict:
        mydict[w] += 1
    else:
        mydict[w] = 1

print(mydict)
for k in reverse_sorted(mydict.keys()):
    print('%s: %s'%(k, mydict[k]))


