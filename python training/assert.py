#lex_auth_01269442760027340879

def find_smallest_number(num):
    #start writing your code here
    count=1
    n=1
    while(True):
        count=1
        for i in range(1,(n//2)+1):
            if(n%i==0):
                count+=1
        if(count==num):
            break
        n+=1
    return n

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
