import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def dice(dside):
    d6 = random.randint(1, dside)
    return d6
