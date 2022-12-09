# Lab-10: Primality Test using Fermat method
# func to calculate Power 
def power(b,n):
    if n ==0:
        return 1
    x = power(b,n//2) 
    if n%2==0:
        return x*x
    if n%2 ==1:
        return b*x*x 
# func to check is_prime
def test_prime(n):
    m = n-1
    for b in range(2,n-1):
        e =power(b,m)
    if e % n!= 1:
        return False
                 
    return True             
print(test_prime(3007))
print(power(5,5))    