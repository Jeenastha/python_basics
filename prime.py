num = 9
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag == True: 
        print(f"{num} not prime number")
    else:
        print(num, "prime number")    
             
