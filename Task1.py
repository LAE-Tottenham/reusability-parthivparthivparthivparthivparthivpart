# Help! My code is too messy :( Please help me organise it and extract out the duplications.
import math
def get_float(prompt):
    while True:
        try:
            answer = float(input(prompt))
            break
        except ValueError:
            print('Please enter a decimal/number value.')
    return answer
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

def weird_calculation():
    # get the length and width of the first triangle from the user
    opp1 = get_float(("Enter your triangle's opposite side length: "))
    adj1 = get_float(("Enter your triangle's adjacent side length: "))
    return ((opp1**2+adj1**2)**(1/2))
weird_answer = weird_calculation()
print(weird_answer)
weird_answe2 = weird_calculation()
print(weird_answer, 'other triangle')
print((weird_answer**2+weird_answe2**2)**(1/2), 'new triangle')

# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
#User can not input a letter
# 2. Validate the user's input based on your preconditions.
#
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
#the code looks really small , and I can re use the function that checks if the input is a float to never break the code
# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
