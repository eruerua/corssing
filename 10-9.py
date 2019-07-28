import re
with open('corssing/paper.txt','r') as f:
    text=f.readlines()
    text=[x.strip() for x in text]
string=re.compile(r'\b\w+\b')
sum=0
for i in text:
    sum+=len(re.findall(string,i))
print('字数总数:%d'%sum)