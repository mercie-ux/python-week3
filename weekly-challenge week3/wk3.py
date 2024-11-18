# coding challenge for basic control flows and functions
#1. Large Power
 def is_power_greater_than_5000(base, exponent): # function to accept two input parameter called base and exponent
    #calculate the result of base to the power of exponent
    result = base ** exponent

    #conditional statement to check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False
    # output of the result
    print(is_power_greater_than_5000(50, 30))
    print(is_power_greater_than_5000(5, 4))
    
    def divisible_by_ten(num):
        # check if the number is divisible by 10
        if num % 10 == 0:
            return True
        else: 
            return False
    # output
    print(divisible_by_ten(60)) # output true
    print(divisible_by_ten(11)) # output false
    