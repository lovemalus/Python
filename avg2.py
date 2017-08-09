def avg_com(numlist):
    
    num_sum=0
    for i in range(0,len(numlist)):
        num_sum=num_sum+numlist[i]
    avg=num_sum/len(numlist)
    return

#################################
a=[10,15,20,35]
print avg_com(a)
