month_number={"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12}
month_days = [31,28,31,30,31,30,31,31,30,31,30,31] 

def make_list(a):
    """arg is 1 date seperated by . or / or -
    returns list of date,month,year"""
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
    """arg is list of both dates
    internally called by fun(a,b) function
    returns no of days"""
    date1,date2=l
    d1,m1,y1=date1
    d2,m2,y2=date2
    total_days_b4_date1 = y1*365 + d1 + sum(month_days[:m1-1]) + leap(m1,y1)
    total_days_b4_date2 = y2*365 + d2 + sum(month_days[:m2-1]) + leap(m2,y2)
    return abs(total_days_b4_date2 - total_days_b4_date1)
    
def fun(a,b):
    '''arg is 2 dates in any format
    returns no. of days'''
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

file_ip = open("date_calculator.txt","r")
l=file_ip.readlines()
file_ip.close()

file_op = open("output.txt","w")
file_op.write(str(fun(l[0],l[1])))
file_op.close()
