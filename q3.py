import ast
def find_complement(l):
    l1=[]
    if float(l[0][0]) > 9:
        l1.append("9-"+l[0][0])
    for i in range(1,len(l)):
        if l[i][0]!=l[i-1][1]:
            l1.append(l[i-1][1]+"-"+l[i][0])
    
    if float(l[-1][1]) < 17:
        l1.append(l[-1][1] + "-" + "17")
    return l1

def convert_12hr_to_24hr(l):
    updated_list=[]
    for i in l:
        start , end = i.split("-")
        start , end = start.strip() , end.strip()
        a , b = start.split(":")
        if len(a)==1 and b[-2] == 'P':
            a= int(a) + 12
            start = str(a) + ":" + b
        a , b = end.split(":")
        if len(a)==1 and b[-2] == 'P':
            a= int(a) + 12
            end = str(a) + ":" + b
        start , end = start[:-2] , end[:-2]
        a , b = start.split(":")
        if b != "00":
            a = str( int(a) + 0.5 )
        start = a
        a , b = end.split(":")
        if b != "00":
            a = str( int(a) + 0.5 )
        end = a
        updated_list.append((start,end))    
    return updated_list
    
def convert_24hr_to_12hr(l):
    l1=[]
    for slot in l:
        start , end = slot.split("-")
        if float(start) >= 12:
            postfix = "PM"
        else:
            postfix = "AM"
        min30 = 0
        if float(start) != int(float(start)):
            min30 = 1
        if postfix == "PM":
             if start[:2] == "12":
                pass
             else:
                start = str(float(start) - 12)
        if min30 == 1:
            start = str(int(float(start))) + ":" + "30"
        else:
            start = str(int(float(start))) + ":" + "00"
        
        start = start + postfix
        
        if float(end) >= 12:
            postfix = "PM"
        else:
            postfix = "AM"
        min30 = 0
    
        if float(end) != int(float(end)):
            min30 = 1
        if postfix == "PM":
            if end[:2] == "12":
                pass
            else:
                end = str(float(end) - 12)
        if min30 == 1:
            end = str(int(float(end))) + ":" + "30"
        else:
            end = str(int(float(end))) + ":" + "00"
        
        end = end + postfix
        l1.append(start+" - "+end)
    return l1
        
def find_intersaction(l1,l2):
    l3,l4=[],[]
    for i in l1:
        a,b=i.split("-")
        a,b=float(a),float(b)
        l3.append((a,b))
    for i in l2:
        a,b=i.split("-")
        a,b=float(a),float(b)
        l4.append((a,b))
    l=[]
    for i in l3:
        for j in l4:
            if i[0]<j[1] and i[1]>j[0]:
                a= max(i[0],j[0])
                b= min(i[1],j[1])
                l.append(""+str(a)+"-"+str(b))
    return l
         
def find_required_slot(l,s):
    for i in l:
        if i[1]-i[0] >= float(s):
            return convert_24hr_to_12hr([(str(i[0])+"-"+str(i[0]+float(s)))])
    return "no slot available"

import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
file_list=[]
for i in files:
    if i.endswith(".txt") and i.startswith("Employee"):
        file_list.append(i)
if "output.txt" in file_list:
    file_list.remove("output.txt")
                 
e_list=[]
for i in range(len(file_list)):
    with open(file_list[i],"r") as file:
        e_list.append(file.read())
    file.close()

E_list=[]
for i in e_list:
    E_list.append(ast.literal_eval(i))

emp_name_list=[]
for i in E_list:
    emp_name_list.append(list(i.keys())[0])

date_list=[]
for i in range(len(emp_name_list)):
    date_list.append(list(E_list[i][emp_name_list[i]].keys())[0])

list_list=[]
for i in range(len(emp_name_list)):
    list_list.append(list(E_list[i][emp_name_list[i]].values())[0])   

res = all(ele == date_list[0] for ele in date_list) 
if not(res):
    dummy_var = input()
    file_op = open("output.txt","w")
    file_op.write("no slot available")
    file_op.close()
else:
    updated_list=[]
    for i in list_list:
        updated_list.append(convert_12hr_to_24hr(i))
    l_list=[]
    for i in updated_list:
        l_list.append(find_complement(i))
    
    show_list=[]
    for i in l_list:
        show_list.append(convert_24hr_to_12hr(i))

    slot=input()
    temp=l_list[0]
    for i in l_list:
        temp=find_intersaction(temp,i)
    available_slots=temp
    new_list=[]
    for i in available_slots:
        a,b=i.split("-")
        a,b=float(a),float(b)
        new_list.append((a,b))
    
    a=find_required_slot(new_list,slot)
    line=""
    for i in range(len(emp_name_list)):
        line+=emp_name_list[i]+": "+str(show_list[i])+"\n"

    sample=[]
    if type(a) == type(sample):
        d=dict()
        d[date_list[0]] = a
        line3 = d
        file_op = open("output.txt","w")
        file_op.write("Available slot\n"+line+"\n\nSlot Duration: "+slot+" hour\n"+str(line3))
        file_op.close()
    else:
        file_op = open("output.txt","w")
        file_op.write(a)
        file_op.close()