## differenct between two time
def diff(t2,t1):
    h=m=s=""
    #seconds
    f1 = f2 = False
    if t1[2]>=t2[2]:
        s = str(t1[2]-t2[2])
    else:
        s = str((t1[2]+60)-t2[2])
        f1 = True
    #minute
    if t1[1]>=t2[1]:
        m = str(t1[1]-t2[1])
    else:
        m = str(t1[1]-t2[1]+60)
        f2 = True
    #hours
    if t1[0]>=t2[0]:
        h = str(t1[0]-t2[0])
    else:
        h = str(t1[0]-t2[0]+24)
    
    if f1:
        m = str(int(m)-1)
    if f2:
        h = str(int(h)-1)
    
    if len(s)==1:
        s = "0"+s
    if len(m)==1:
        m = "0"+m
    if len(h)==1:
        h = "0"+h
    
    print(h+":"+m+":"+s)



time1 = list(map(int,input().split(":")))
time2 = list(map(int,input().split(":")))
diff(time1,time2)
