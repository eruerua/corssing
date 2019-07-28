import re
file=[]
with open('corssing/from.txt',encoding='utf8') as f:
    file=f.readlines()
s=''
for i in file:
    s+=i
print(s)
string=re.compile(r'[A-z]+')
result=re.findall(string,s)
sorted_result=sorted(result)
print(sorted_result)
with open('corssing/to.txt','w',encoding='utf8')  as f:
    for i in sorted_result:
        f.write(i)
        f.write('\n')