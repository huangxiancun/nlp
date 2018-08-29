# -*- coding: utf-8 -*-
import copy
with open('test.conll_pre1','r') as f:
    txt=f.read().strip()
    s=txt.split('\n')
    s=[i.strip().split('\t') for i in s]
# s_c=copy.deepcopy(s)
all=[]
p=[]
rt=''
while len(s):
    sp=s.pop(0)
    if sp!=[''] and len(s)!=0:
        p.append(sp)
    else:
        rt += '\n'
        print ' '
        for i in p:
            if int(float(i[4]))==0:
                rt+= '0_root\n'
                print '0_root'
            else:
                headi_num=int(float(i[4]))
                ind1=int(float(i[0]))-1
                ind2=headi_num-1
                if ind1>ind2:
                    ind1,ind2=ind2,ind1
                dep2head=p[ind1:ind2+1]
                cix=p[headi_num-1][2]
                nn=[ii[2] for ii in dep2head].count(cix)
                if i[2]==cix:nn-=1
                if float(i[0])<float(i[4]):
                    tag='+'
                else:
                    tag='-'
                rt+= tag+str(nn)+'_'+cix+'\n'
                print tag+str(nn)+'_'+cix

            if len(s)==0:
                break
        p = []


with open('tmp_test.txt','w') as f:
    f.write(rt)



