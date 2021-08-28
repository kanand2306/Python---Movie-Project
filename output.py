from decimal import *

def quer1():
    p=open("movie.txt",'r').readlines()
    c=0
    for i in p:
        p=i.strip("\n").split(",")
        if int(p[2])>=1950 and int(p[2])<=1960:
            c+=1
    return c


def quer2():
    p=open("movie.txt",'r').readlines()
    
    d=0
    for i in p:
        q=i.strip("\n").split(",")
        if q[3]!='':
            a=Decimal(q[3])
        else:
            continue
        b=Decimal(4)
        if a.compare(b)==1:
            d+=1
    return d


def quer3():
    p=open("movie.txt",'r').readlines()
    
    e=0

    for i in p:
        q=i.strip("\n").split(",")
        global a
        if q[3]!='':
            a=Decimal(q[3])
        else:
            continue
        b=Decimal(4)
        c=Decimal(3)
        if a.compare(b)==-1 and a.compare(c)==1:
            print(q)
            e+=1

    return e

def quer4():
    p=open("movie.txt",'r').readlines()
    f=0
    for i in p:
        p=i.strip("\n").split(",")
        if p[4]=='':
            p[4]=0
        if int(p[4])>=7200:
            f+=1
    return f

def quer5():
    p=open('movie.txt','r')
    c=0
    s=[]
    print("\nThe list of years and number of movies released each year = \n")
    for i in p:
        f=i.split(",")
        s.append(f[2])
    q=list(set(s))
    q.sort()
    for i in range(len(q)):
        store=s.count(q[i])
        print(q[i],store)
    p.close()




def quer6():
    n=sum(1 for line in open(r"C:\Users\HP\Desktop\Revature\Project\movie.txt"))
    return n



if __name__=='__main__':
    print("Total number of movies released between 1950 and 1960 = ",quer1())
    print("\nTotal number of movies having rating more than 4 = ",quer2())
    print("\nTotal number of movies whose rating are between 3 and 4 = ",quer3())
    print("\nTotal number of movies whose duration is more than 2 hours (7200 second)= ",quer4())
    quer5()
    print("\nTotal number of movies in dataset = ",quer6())


