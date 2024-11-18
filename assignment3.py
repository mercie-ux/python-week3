# question 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20: # check if the discount is 20% or higher
        discount_price = price * (1 - discount_percent / 100)
        return discount_price
    else:
        # return the original price if discount is less than 20%
        return price
    

# output
print(calculate_discount(80, 35))
print(calculate_discount(30, 20))

# question 2
def calculate_discount(price, discount_percent):
    #check if the discount is 20% or higher
    if discount_percent >= 20:
        #calculate the discounted price
        discounted_price = price * (1 - discount_percent / 100)
        return discount_price
    else:
        # return the original price if discount is less than 20%
        return price
    
# output
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# calculate the final price
last_price = calculate_discount(original_price, discount_percent)

# output
if last_price < original_price:
    print(f"The last price after applying the discount is: ${last_price:.2f}")
else:
    print(f"No discount was applied. The original price is ${original_price:.2f}") 
    
