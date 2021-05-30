import sys
month_number={"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12}
month_days = [31,28,31,30,31,30,31,31,30,31,30,31] 

def make_list(a):
    l1=[]
    flag1=0
    if '-' in a:
        c='-'
    elif '/' in a:
        c='/'
    elif '.' in a:
        c='.'
    else:
        flag1=1
    if flag1==0:
        p=0
        temp=""
        for i in range(len(a)):
            if a[i]!=c:
                temp+=a[i]
            else:
                l1.append(int(temp))
                temp=""
                p=i
        l1.append(int(a[p+1:]))
    return l1

def make_list_string(a):
    datemonth,year=a.split(',')
    year=int(year)
    date,month=datemonth.split(' ')
    month=month.lower()
    if len(month)>3:
        month=month[:3]
    month=month_number[month]
    temp=""
    for i in date:
        if i.isdigit():
            temp+=i
        else:
            break
    date=int(temp)
    return [date,month,year]
    
def leap(m,y):
    if m<=2:
        y-=1
    count=0
    count+=y//4
    count-=y//100
    count+=y//400
    return count
    
def count(l):
    date1,date2=l
    d1,m1,y1=date1
    d2,m2,y2=date2
    total_days_b4_date1 = y1*365 + d1 + sum(month_days[:m1-1]) + leap(m1,y1)
    total_days_b4_date2 = y2*365 + d2 + sum(month_days[:m2-1]) + leap(m2,y2)
    return abs(total_days_b4_date2 - total_days_b4_date1)
    
def fun(a,b):
    inp_list1,inp_list2=[],[]
    if any([ '.' in a , '/' in a , '-' in a]):
        inp_list1 = make_list(a)
    else:
        inp_list1 = make_list_string(a)
    if any([ '.' in b , '/' in b , '-' in b]):
        inp_list2 = make_list(b)
    else:
        inp_list2 = make_list_string(b)
    return count([inp_list1,inp_list2])

def change_mmddyyyy_to_ddmmyyyy(l):
    p_list=[]
    for i in range(len(l)):
        if '.' in l[i]:
            p_list=l[i].split('.')
        elif '-' in l[i]:
            p_list=l[i].split('-')
        elif '/' in l[i]:
            p_list=l[i].split('/')
        l[i]=p_list[1]+"."+p_list[0]+"."+p_list[2]
    return l
def writer(l):
    file_op = open("output.txt","w")
    result=fun(l[0],l[1])
    if result==0 or result==1:
        file_op.write("Date Difference: "+str(result)+" Day")
    else:
        file_op.write("Date Difference: "+str(result)+" Days")
    file_op.close()
def reader():
    file_ip = open("date_calculator.txt","r")
    l=file_ip.readlines()
    l[0] , l[1] = (l[0].split(':'))[1].lstrip() , (l[1].split(':'))[1].lstrip()
    file_ip.close()
    return l

l=reader()
if (len(sys.argv) == 2) and (sys.argv[1][0]=='m'):
    l=change_mmddyyyy_to_ddmmyyyy(l)
writer(l)

