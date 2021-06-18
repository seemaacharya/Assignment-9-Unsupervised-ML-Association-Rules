# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:44:36 2021

@author: Soumya PC
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules

As the data is already in binary format, we will read as
book = pd.read_csv("book.csv")

frequent_itemsets = apriori(book, min_support=0.005, max_len=3,use_colnames= True)
frequent_itemsets.shape
frequent_itemsets.sort_values('support',ascending =False,inplace = True)
import matplotlib.pyplot as plt
plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgybkmc')
plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item_sets');plt.ylabel('support')

#Generating rules-

rules = association_rules(frequent_itemsets, metric='lift',min_threshold=1)
rules.shape
rules.head(5)
rules.sort_values('lift',ascending = False,inplace= True)
rules.sort_values

#By using support=0.005, we have got frequent_itemsets= 224, rules= 1054 (ItalArt,RefBks and ItalAtlas found to be highly associated) 
#so we will now use support=10% i.e support= 0.001


frequent_itemsets = apriori(book, min_support=0.001,max_len=3,use_colnames= True)
frequent_itemsets.shape
frequent_itemsets.sort_values('support',ascending = False,inplace= True)
#plotting the bar plot b/w frequent_itemsets on x-axis and support on y-axis
plt.bar(x = list(range(0,5)),height = frequent_itemsets.support[0:5],color='rgybkmc')
plt.xticks(list(range(0,5)),frequent_itemsets.itemsets[0:5])
plt.xlabel('item_sets');plt.ylabel('support')

Generating rules-

rules =association_rules(frequent_itemsets, metric ='lift',min_threshold=1)
rules.shape
rules.head(5)
rules.sort_values('lift',ascending = False,inplace= True)
rules.sort_values

#By using support=0.001, we have got frequent_itemsets= 231, rules= 1096 (ItalArt,RefBks and ItalAtlas found to be highly associated)


#To eliminate the redundancy in Rules
def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list)+rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)


unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]
index_rules = []
for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
#getting rules without any redundancy
rules_no_redundancy = rules.iloc[index_rules,:]   
#Sorting them with respect to list and getting top 10 rules
rules_no_redundancy.sort_values('lift',ascending=False).head(10)











