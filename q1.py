def isPrimeNumber(n):

    if n < 2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True

def getPrimeNumbers(n):

    for i in range (2, n + 1):
        if isPrimeNumber(i):
            print(i)

getPrimeNumbers(10)
