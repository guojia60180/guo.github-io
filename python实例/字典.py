#Author guo
#找出年龄最大的人，并输出

person={'li':18,"wang":20,'zhang':19,"sun":17}
m='zhang'

for key in person.keys():
    if person[m]<person[key]:
        m=key

print('%s,%d'%(m,person[m]))

