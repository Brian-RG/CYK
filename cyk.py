from itertools import repeat,permutations
#A01633401 - Brian Reyes Gálvez
grammar={"S":["AB","BC"],"A":["AB","a"],"B":["CC","b"],"C":["AB","a"]}
def CreateTable(word):
    table=[]
    b=len(word)
    for i in range(b):
        table.append([None]*(b))
    return table
def printtable(cyk):
    for r in cyk:
        for e in r:
            print(e,end=" | ")
        print()
def first(cyk,word):
    i=j=0
    for c in word:
        cyk[i][j]=checklet(c)
        i+=1
        j+=1
    return cyk
def docyk(table,word):
    step=1 
    for i in range(len(word)-1):
        for j in range(len(word)-step):
            flag=False
            k=j+step
            counter=0
            while(k-counter>j):
                a=table[j][k-counter-1]
                b=table[k-counter][k]
                if(len(a)<len(b)):
                    l=[(list(zip(r, p))) for (r, p) in zip(repeat(a), permutations(b))]
                else:
                    l=[(list(zip(p, r))) for (r, p) in zip(repeat(b), permutations(a))]
                aux=[]
                for e in l:
                    for i in e:
                        aux.append(("").join(i))
                for z in aux:
                    s=checklet(z)
                    if(s==None):
                        if(not flag):
                            table[j][k]=set("ø")
                    else:
                        x=table[j][k]
                        if(x==None or x==set("ø")):    
                            table[j][k]=s
                        else:
                            table[j][k]=table[j][k]|s
                        flag=True
                counter+=1                
        step+=1
    return table

def checklet(c):
    aux=set()
    for e in grammar.keys():
        if c in grammar[e]:
            aux.add(e)
    if(len(aux)):
        return aux
    else:
        return None
    
print("The alphabet is : {a,b}")
print("The grammar is: ")
print("S->AB|BC")
print("A->AB|a")
print("B->CC|b")
print("C->AB|a")
word=input("Insert a word for CYK: ")
CYK= CreateTable(word)
first(CYK,word)
CYK=docyk(CYK,word)
print("---------------"*len(word))
printtable(CYK)
