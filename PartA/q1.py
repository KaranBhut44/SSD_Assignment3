l=[]
l1=[]
def find_parents(k):
    l.append(d[k])
    if d[k] in d.keys():
        find_parents(d[k])
    else:
        l.reverse()
        l1.append(l)
    
import json
f = open('org.json',)
data = json.load(f)
f.close()

emp1,emp2=input().split()

if (emp1 == data["L0"][0]["name"]) or (emp2 == data["L0"][0]["name"]):
    print("Leader not found")
else:
    d=dict()
    for i in data.keys():
        if i != "L0":
            for p in data[i]:
                d[p["name"]]=p["parent"]
    
    c1=[]
    for k in d:
        l=[]
        c1.append(k)
        find_parents(k)

    child_parents=dict(zip(c1,l1))
    
    if (emp1 not in child_parents) or (emp2 not in child_parents):
        print("Leader not found")
    else:
        l1=child_parents[emp1]
        l2=child_parents[emp2]
        flag,index,parent,level1,level2=0,0,0,0,0
        while(flag==0 and index<len(l1) and index<len(l2)):
            if l1[index]!=l2[index]:
                flag=1
            else:
                parent=l1[index]
                level1=len(l1)-index
                level2=len(l2)-index
            index+=1
        print(parent)
        print(parent+" is "+str(level1)+" levels above "+emp1)
        print(parent+" is "+str(level2)+" levels above "+emp2)