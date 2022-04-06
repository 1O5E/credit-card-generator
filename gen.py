import random, datetime

def front():
    first = random.randint(1000, 10000)
    second = random.randint(1000, 10000)
    third = random.randint(1000, 10000) # generate the 16 digit code on the front, 16 ** 9 gives us 68719476736 possible outcomes
    fourth = random.randint(1000, 10000)
    front_number = f'{first} {second} {third} {fourth}'
    with open('names.txt', 'r') as names:
        name = names.readlines()
        first_name = random.choice(name) # get first and second names
    with open('second_names.txt', 'r') as second_names:
        xyz = second_names.readlines()
        second_name = random.choice(xyz)
    expiry_months = []
    expiry_years = []
    now = datetime.datetime.now().year
    for i in range(0, 5):
        expiry_years.append(int(str(now)[2:]) + i) # just so the years for the expiry date are not out of date
    now = datetime.datetime.now().month
    current_month = int(str(now))
    length = 12 - current_month
    for i in range(0, length+1): # same as the expiry year gen thingy
        current_month = int(str(now)) + i
        expiry_months.append(current_month)
    expiry_one = random.choice(expiry_months)
    expiry_two = random.choice(expiry_years)
    expiry = f'{expiry_one}/{expiry_two}' # format it
    cvc = random.randint(100, 999) # just the cvc
    return first_name, second_name, front_number, expiry, cvc # send it all back


print(f"""
First name: {front()[0].lower()}
Second name: {front()[1].lower()}
Card: {front()[2]}
Expiry: {front()[3]}
CVC: {front()[4]}""")
            
