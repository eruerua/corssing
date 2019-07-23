#读取文件，并删掉回车符
with open('report.txt',encoding='utf8') as f:
    report=f.readlines()
    grades=[x.strip().split() for x in report]
#计算总分，平均分并排序
score_list=[]
for grade in grades[1:]:
    score=[]
    score.append(grade[0])
    l=[int(x) for x in grade[1:]]#str转换为int，便于计算
    score+=l
    ave=sum(l)/len(grade[1:])
    score.append(sum(l))
    score.append(round(ave,1))
    score_list.append(score)
sorted_score_list=sorted(score_list,key=lambda a:a[-2],reverse=True)#排序
#插入汇总行
sum_score=[]
for i in range(1,len(score_list[0])):
    avg=sum([x[i] for x in score_list])/len(score_list)
    sum_score.append(round(avg,1))
sum_score.insert(0,'平均')
sorted_score_list.insert(0,sum_score)
#插入名次
[sorted_score_list[i].insert(0,i) for i in range(len(sorted_score_list))]
#替换不合格
for i in sorted_score_list[1:]:
    for n in range(2,len(i)-2):
        if i[n]<60:
            i[n]='不及格'
#插入第一行
title=grades[0]
title.insert(0,'名次')
title.append('总分')
title.append('平均分')
sorted_score_list.insert(0,title)
with open('out.txt','w') as f:
    for lines in sorted_score_list:
        for line in lines:
            f.write(str(line)+' ')
        f.write('\n')