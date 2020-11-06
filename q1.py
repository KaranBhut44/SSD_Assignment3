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

emp_list = input().split()
emp_list = emp_list[1:]
flag=0
for i in emp_list:
    if (i == data["L0"][0]["name"]):
        print("Leader not found")
        flag=1
        break
        
if flag==0:
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
    
    for i in emp_list:
        if i not in child_parents:
            print("Leader not found")
            flag=1
            break
    if flag==0:
        child_parents_list=[]
        for i in emp_list:
            child_parents_list.append(child_parents[i])
        min_length=len(child_parents_list[0])
        for i in child_parents_list:
            if len(i)<min_length:
                min_length=len(i)
                
        level=[]
        for i in range(len(emp_list)):
            level.append(0)
        flag,index,parent=0,0,""
        
        while(flag==0 and index<min_length):
            temp=[]
            for i in range(len(emp_list)):
                temp.append(False)
            for i in range(len(emp_list)):
                temp[i]=child_parents_list[i][index]
            res = all(ele == temp[0] for ele in temp) 
            if res:
                parent=child_parents_list[0][index]
                for i in range(len(child_parents_list)):
                    level[i] = len(child_parents_list[i])-index
            else:
                flag=1
            index+=1
        print("common leader: "+parent)
        for i in range(len(level)):
            print("leader "+parent+" is "+str(level[i])+" levels above employee "+emp_list[i])        