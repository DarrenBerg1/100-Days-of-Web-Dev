### Optimal Change
# P: we will take in two parameters one being "item_cost" and the other "amount_paid"
# R: the return statement should return the difference (amount_paid - item_cost) within a string. 
# E: an example of the return statement is :
# "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
# P: to get started, create a dictionary to hold the denomiation/value of each currency. (ex. key = "Nickel" value = .05)
# You will then need to create a variable to hold the change_due. (ex. amount_paid - item_cost) = change_due.
# With change_due, we can use its value to loop through the dictionary and decrementing it until it reaches 0 (this is similar to the ROMAN NUMERAL(REFERENCE THIS) process and how we decremented/ stacked the numerals together).
# Once we have the change broken down, we will need to push the values into a list (possibly?) -> this will allow us to access them using (variable[0,1,2,etc...]) and concatonating them into our final string.
# we will also need to create a way that we can change the "s" in bills/quarters/dimes/etc.. (this is similar to what we did in 99 bottles(REFERENCE THIS))
## Maybe instead of creating the key as the name of the bill 
# (ie: querter), we should make the key the value and the value = to a count. So that we can track the number of coins/ bills we need. My only other idea is that we push all of them into a list, loop over the list into a new dict to get a count (similar to the character count assignment(REFERENCE THIS))

#from math import ceil
  
def optimal_change(item_cost, amount_paid):

    # dollar_values is a dictionary i am using to iterate through and get the # of each dollar_value i will need to return.    

    dollar_values = {
        100:0,
        50:0,
        20:0,
        10:0,
        5:0,
        1:0,
        0.25:0,
        0.10:0,
        0.05:0,
        0.01:0 }
   
    new_keys = ['$100 bill', '$50 bill', '$20 bill', '$10 bill', '$5 bill', '$1 bill', 'quarter', 'dime', 'nickel', 'penny']
    
    # An if statement to stop the function if the amout_paid == total_cost (exact change) and the elif statement to stop the function if the item_cost is larger than amount_paid (amount we give).

    if amount_paid == item_cost:
        return "Awesome! You have exact change, here is your reciept."
    elif amount_paid < item_cost:
        return "I am sorry, you do not have enough to purchase this item."
    
    # elif statement to filter through the dictionary decrementing the "due" into dollar_values and incrementing the "value" by one for each dollar_value needed to return.
        
    elif amount_paid > item_cost:
        due = round(amount_paid - item_cost,2)
        for change in sorted(dollar_values,reverse = True):
            amt = max(0,due//change)
            due -= amt * change
            dollar_values[change] = round(amt)
            if due > 0.005:
              dollar_values[0.01] += 1

        #print(dollar_values)
    # this new dict, will rename the numerical keys to strings. 
    
    new_dict = {new_keys[i]: value for i, (key, value) in enumerate(dollar_values.items())}
    #print(new_dict)
    
    # we are then placing the keys/ values of new_dict into a list as tuples as (value,key) if the value is >= 1. This allows us to only access the pairs that we want within our final print statement.

    result = [(value, key) for key, value in new_dict.items() if value >= 1]
    #print(result)        
    # we are using this for loop to iterate through the tuples within our new dictionary. This allows us to use the if/ elif statement to change the plural denomination for each tuple that has a value > 1.

    for i, elem in enumerate(result):
        if elem[1] == "penny" and elem[0] > 1:
            new_tuple = (elem[0], 'pennies')
            result[i] = new_tuple
        elif elem[0] > 1:
            new_tuple = (elem[0], elem[1] + 's')
            result[i] = new_tuple 
    
    # removing the commas between elem[0] and elem[1] -> 2, dimes will turn into 2 dimes. This also formats the final part of the sentence to include "and" between the last two tuples.

    if len(result) == 1:
        change_statement = str(result[0][0]) + ' ' + result[0][1]
    else:
        change_statement = ', '.join([str(x) + ' ' + y for x, y in result[:-1]]) + ', and ' + str(result[-1][0]) + ' ' + result[-1][1]
    
    #formatting the beggining part of the statement

    change_template = 'The optimal change for an item that costs ${} with an amount paid of ${} is'.format(item_cost,amount_paid)
    
    #returning the the full statement

    return change_template + " " + change_statement + "."
    

#print(optimal_change(31.51, 50))



