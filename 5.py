def prime_find_2019_1_60_051(n):
    for i in range(2, n + 1, 1):
        if(n%i)==0:
            return False
            break
        else:
          return True
n = int (input("Enter number:"))
if(prime_find_2019_1_60_051(n)==False):
    print(n," is not a prime number")
else:
    print(n," is a prime number.")