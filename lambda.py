def prime_check(n):
    if n<2:
        return False
    else:
        for i in range(2,n-1):
            if n%i==0:
                return False
        return True
    
print_prime=list(filter(prime_check,range(1,50)))  
print(print_prime)


