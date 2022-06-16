from operator import le
import os


def mao(ls):
    
    for j in range(len(ls)):
        for i in range(len(ls)-j-1):
            if ls[i]>ls[i+1]:
                t = ls[i] 
                ls[i] = ls[i+1]
                ls[i+1] = t
                
            
    print(ls)
        
    
def select_sort(ls):
    for i in range(len(ls)):
        min_index = i
        for j in range(i+1,len(ls)):
            if  ls[j] < ls[min_index]:
                min_index = j
                ls[i],ls[min_index] = ls[min_index],ls[i]
    print(ls)
    
def insert_sort(ls):
    lisa=[]
    for i in range(len(ls)):
        for j in range(i):
            if ls[i]<=ls[j]:
                
                ls.insert(j,ls[i])
                del ls[i+1]
                
 
       
    print(ls)
if __name__ == '__main__':
    ls = [12,25,9,18,56,2,55,45]
    select_sort(ls)
    insert_sort(ls)

    