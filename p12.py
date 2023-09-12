def is_prime(n):
   if n<=2:

    return False
   else:
     for i in range(1,n+1):
        if n%i==0:
            return False
    return True
        