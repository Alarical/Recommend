# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:50:47 2019

@author: alaric
"""
import pandas as pd
import numpy as np
import math

def UserSimilarity(train , IIF = False):
    # IIF 是否对 过于热门即 购买人数过于多的物品 在计算用户相似度的时候进行惩罚
    # 因为很多用户对之间并没有对相同的物品产生过行为，只计算对相同物品产生过行为的用户之间的相似度。
    # 采用余弦相似度
    # 建立倒排表，对每个物品保存只对其产生过行为的用户列表。
    item_users = dict() # 物品-用户 倒排表
    for u, items in train.items():
        for i in items:
            # 这里将 item_users.keys() 改为 item_users , 文中例子 应该用set 或 list存，而不是dict:
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)
            
    # 建立如图2-7所示的倒排矩阵
    C = dict() # key 用户对 value 购买同一物品的次数
    N = dict() # N(u) 表示用户购买的 商品数 {'A': 3, 'B': 2, 'C': 2, 'D': 3}
    for i,users in item_users.items():
        for u in users:
            if u not in N.keys():
                N[u] = 0
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                if (u,v) not in C.keys():
                    C[u,v] = 0
                if IIF:
                    # len(users) 表示购买此物品的用户数，越热门，购买用户越多,C[u,v] 就越小
                    # 相当于之前的分子是相交个数，现在是
                    C[u,v] += 1 / math.log(1 + len(users))
                else:
                    C[u,v] += 1
    W = dict()
    for co_user, cuv in C.items():
        W[co_user] = cuv / math.sqrt(N[co_user[0]]*N[co_user[1]])
    
    return W

# UserCF 推荐算法
def UserCFRecommend(user,train,W,k):
    # rvi 代表用户v对物品i的权重
    rvi = 1 
    rank = dict()
    interacted_items = train[user]
    related_user=[]
    # 和 A 有相似度的用户 ，B,C,D
    for co_user,sim in W.items():
        if co_user[0] == user:S
            related_user.append((co_user[1],sim))
    # v : 有相似度的用户 , wuv : 用户间相似度 
    for v , wuv in sorted(related_user , key = lambda a:a[1], reverse = True)[0:k]:
        for item in train[v]:
            if item in interacted_items:
                continue
            else:
                # 还是得初始化，才可以赋值
                if item not in rank.keys():
                    rank[item] = 0 
                rank[item] += wuv*rvi
    return rank
        

if __name__=='__main__':
    train = {'A':('a','b','d'),'B':('a','c'),'C':('b','e'),'D':('c','d','e')}
    W = UserSimilarity (train , IIF = False)
    rank = UserCFRecommend('A', train, W , k = 3)
    print (rank)










