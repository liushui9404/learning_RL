#coding:utf-8
'''
用于迭代计算V_star
案例是吴恩达的视频提供的数据
这里是值迭代,异步迭代
学习使用git
学写类
'''
import numpy as np
vs=[[0,0,0],[0,0,0],[0,0,0],[0,-1,1]]#初始化所有的v(s),vs[2][4] vs[3][4]接下来不更新,vs[2][2]也不更新（可以理解为柱子）

vs1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]#注意，是按照列排列的
print vs1[3][0]


RS=-0.02


GAMMA=0.99

def max_cal_sum_pv(j,k):
    '''
    value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j+1][k]
    value_S = 0.8*vs[j][k]+0.1*vs[j][k]+0.1*vs[j+1][k]
    value_W = 0.8*vs[j][k]+0.1*vs[j][k+1]+0.1*vs[j][k]
    value_E = 0.8*vs[j+1][k]+0.1*vs[j][k+1]+0.1*vs[j][k]
    '''
    value = 0
    if j+1==1 and k+1==1:
        value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j+1][k]#
        value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
        value = max(value_N,value_E)
    if j+1==1 and k+1==2:
        value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j][k]
        value_S = 0.8*vs[j][k]+0.1*vs[j][k]+0.1*vs[j][k]
        value = max(value_N,value_S)
    if j+1==1 and k+1==3:
        value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k-1]
        value_S = 0.8*vs[j][k-1]+0.1*vs[j][k]+0.1*vs[j+1][k]
        value = max(value_E,value_S)
    if j+1==2 and k+1==1:
        value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k]
        value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k]
        value = max(value_W,value_E)
    if j+1==2 and k+1==3:
        value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k]
        value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k]
        value = max(value_W,value_E)  
    if j+1==3 and k+1==1:
        value_N = 0.8*vs[j][k+1]+0.1*vs[j-1][k]+0.1*vs[j+1][k]
        value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
        value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
        value = max(value_W,value_E)
        value = max(value,value_N)
    if j+1==3 and k+1==2:
        value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j+1][k]
        value_S = 0.8*vs[j][k-1]+0.1*vs[j][k]+0.1*vs[j+1][k]
        value_E = 0.8*vs[j+1][k]+0.1*vs[j][k+1]+0.1*vs[j][k-1]
        value = max(value_S,value_E)
        value = max(value,value_N)
    if j+1==3 and k+1==3:
        value_S = 0.8*vs[j][k-1]+0.1*vs[j-1][k]+0.1*vs[j+1][k]
        value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k-1]
        value_E = 0.8*vs[j+1][k]+0.1*vs[j][k]+0.1*vs[j][k-1]
        value = max(value_S,value_E)
        value = max(value,value_W)
    if j+1==4 and k+1==1:
        value_N = 0.8*vs[j][k+1]+0.1*vs[j][k]+0.1*vs[j-1][k]
        value_W = 0.8*vs[j-1][k]+0.1*vs[j][k]+0.1*vs[j][k+1]
        value = max(value_N,value_W)


    return value


#迭代1000次,i=0--999
for i in range(10000):
    for j in range(4):
        # print "j=",j
        for k in range(3):
            # print "k=",k
            if not ((j+1==2 and k+1==2)or(j+1==4 and k+1==2)or(j+1==4 and k+1==3)):
                # print j,"   ",k
                vs[j][k] =  RS +GAMMA*max_cal_sum_pv(j,k)
                # print vs[3][2]

print vs
