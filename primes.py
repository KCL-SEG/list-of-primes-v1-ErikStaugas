"""List of prime numbers generator."""

def primes(number_of_primes):
    list = []
    
    number = 0
    while len(list) < number_of_primes: 
        number += 1
        divisor = 2 

        if(number == 2):
            list.append(number)
        
        if(number % 2 != 0):   
            is_prime = False         
            for divisor in range(2, number): 
                print(divisor)
                if(number % divisor == 0):
                    is_prime = False
                    break
                else:
                    is_prime = True
            
            if(is_prime):
                list.append(number)
    return list

print(primes(10))