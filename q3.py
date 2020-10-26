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
                l.append((a,b))
    return l
         
def find_required_slot(l,s):
    for i in l:
        if i[1]-i[0] >= float(s):
            return convert_24hr_to_12hr([(str(i[0])+"-"+str(i[0]+float(s)))])
    return "no slot available"
    
with open("Employee1.txt","r") as file:
    e1=file.read()
file.close()
with open("Employee2.txt","r") as file:
    e2=file.read()
file.close()

E1 = ast.literal_eval(e1)
E2 = ast.literal_eval(e2)

emp_name1 = list(E1.keys())[0]
emp_name2 = list(E2.keys())[0]

date1 = list(E1[emp_name1].keys())[0]
date2 = list(E2[emp_name2].keys())[0]

list1 = list(E1[emp_name1].values())[0]
list2 = list(E2[emp_name2].values())[0]

if date1!=date2:
    dummy_var = input()
    file_op = open("output.txt","w")
    file_op.write("no slot available")
    file_op.close()
else:
    updated_list1 , updated_list2 = [] , []
    for i in list1:
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
        updated_list1.append((start,end))
    
    for i in list2:
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
        updated_list2.append((start,end))
    
    l1=find_complement(updated_list1)
    show_l1=convert_24hr_to_12hr(l1)
    l2=find_complement(updated_list2)
    show_l2=convert_24hr_to_12hr(l2)
    slot=input()
    
    available_slots = find_intersaction(l1,l2)
    a=find_required_slot(available_slots,slot)
    line1 = emp_name1+": "+str(show_l1)
    line2 = emp_name2+": "+str(show_l2)
    sample=[]
    if type(a) == type(sample):
        d=dict()
        d[date1] = a
        line3 = d
        file_op = open("output.txt","w")
        file_op.write("Available slot\n"+line1+"\n"+line2+"\n\nSlot Duration: "+slot+" hour\n"+str(line3))
        file_op.close()
    else:
        file_op = open("output.txt","w")
        file_op.write(a)
        file_op.close()
