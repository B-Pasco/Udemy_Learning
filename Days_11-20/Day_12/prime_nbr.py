# Checking if the nbr is prime number or not.

def is_prime(num):
    if num == 2:
        return True
    elif num == 1:
        return False
        
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True
