import requests
from pyfiglet import Figlet
import os, time
import re
from ukpostcodeutils import validation
# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.
def guess_gender(name):
    resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    return [resp["gender"], resp["probability"] * 100]

def display_greeting():
    print(Figlet(font="slant").renderText("HEY!"))
    print("Welcome to the weird weather bot :)\n" + "-" * 30)

def get_name_and_gender():
    name = input("May I take your first name please? ")
    gender, prob_percent = guess_gender(name)
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    return gender

def confirm_gender(gender):
    if input("Am I right? :) (Y/n) ").lower() in ["", "yes", "y", "ye"]:
        print("Woooooooh! Computer 1, Human 0.")
    else:
        print(f"Ahhhh, sorry! I thought you were {gender}.")

def simulate_weather_check():
    print("\nLet me just check the weather there today...\n")
    time.sleep(3)
    print("...")

    
def fetch_cat_fact():
    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    
    joke = requests.get("https://catfact.ninja/fact").json()['fact']
    print(f"\n{'#' * 30}\nCAT FACT:\n{joke}\n{'#' * 30}")
# Define your reusable functions here:
def wait():
    for i in range(3):
        time.sleep(1)
        print("...")
def validatepost(input):
    postcode_pattern = r"^[A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2}$"
    if re.fullmatch(postcode_pattern, input.upper()):
        return True
    else:
        return False
def get_valid_postcode():
    while True:
        postcode_raw = input("Enter a valid postcode: ")
        if validatepost(postcode_raw):
            postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()['result']
            area = postcode_resp['admin_ward']
            print(f"Nice! So you live in {area}.")
            return area  # Return the valid postcode and exit the loop
        else:
            print("Invalid postcode, please try again.")
# Make sure each function only does ONE thing!!!!!!!!!!!
def weird_weather_bot():
    display_greeting()
    gender = get_name_and_gender()
    confirm_gender(gender)
    postcode_raw = input("\nSo, what's your postcode? ")
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    print(f"Nice! so you live in {area}.\n")
    simulate_weather_check()
    fetch_cat_fact()
    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")
    wait()
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    # print(weather_resp)
    weather_kelvin = weather_resp["main"]["temp"]
    # convert to degrees
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")
weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# the functions need to be defined
#I had to copy every bit of code on to the functions I made to not miss out anything
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
#It is useful as you do not need to repeat the long lines of code and you can make the code shorter.
# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
