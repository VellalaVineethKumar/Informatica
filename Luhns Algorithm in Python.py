print("Enter Card Number to Check")

cardno=int(input())

if(len(str(cardno))<10):
    print("Enter Vaild Card number")
    exit(0)
print("You Entered",cardno)

lisno= list(map(int, str(cardno)))


sumodd=0 
sumeven=0
ret=0




def getsum(num):
    singsum=0 
    while(num/10>0):
        singsum+=num%10
        num=num//10
    return singsum
        

for i in range(len(lisno)):
    if(i%2!=0):
        sumodd+=lisno[i]
    else:
        
        ret=getsum(lisno[i]*2)
        sumeven+=ret
        
        
print("ODD",sumodd,"Even",sumeven)



totsum=sumeven+sumodd

if(totsum%10==0):
    print("Valid Credit Card")
else:
    print("Invalid Credit card")
        
