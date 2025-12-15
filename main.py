# 1.
import logging

def my_generator(gen):
    for i in gen:
        yield i

x = "Code"

for ch in x:
    print(ch)
my_generator(x)

# 2.
arr = [1, 2, 3,4,5,6,7,8,9]

inp = int(input("დაწერეთ ნებისმიერი რიცხვი 1-დან 9-მდე: "))

try:
    print("თქვენი რიცხვია:", arr[inp])
except:
    print("გთხოვთ შეიყვანოთ ციფრი 1-დან 9-მდე!")

# 3.
import logging
from sys import exc_info

logging.basicConfig(filename='game.log', level=logging.INFO)

print("მე დაგისვამ 5 მათემატიკურ შეკითხვას, თითო სწორ პასუხზე მიიღებ 10 ქულას.")

score = 0

inp1 = input("რამდენია 5 * 2? ")
inp1 = int(inp1)
if inp1 == 10:
    print("შენ მიიღე 10 ქულა")
    score += 10
    logging.info(msg='10 ქულა', exc_info=True)
else:
    print("არასწორია")
    logging.info(msg='0 ქულა', exc_info=True)

inp2 = input("რამდენია 10 * 3? ")
inp2 = int(inp2)

if inp2 == 30:
    print("შენ მიიღე 10 ქულა")
    score += 10
    logging.info(msg='10 ქულა', exc_info=True)
else:
    print("არასწორია")
    logging.info(msg='10 ქულა', exc_info=True)

inp3 = input("რამდენია 9 + 15? ")
inp3 = int(inp3)

if inp3 == 24:
    print("შენ მიიღე 10 ქულა")
    score += 10
    logging.info(msg='10 ქულა', exc_info=True)
else:
    print("არასწორია")
    logging.info(msg='0 ქულა', exc_info=True)
inp4 = input("რამდენია 23 - 14? ")
inp4 = int(inp4)

if inp4 == 9:
    print("შენ მიიღე 10 ქულა")
    score += 10
    logging.info(msg='10 ქულა', exc_info=True)
else:
    print("არასწორია")
    logging.info(msg='0 ქულა', exc_info=True)

inp5 = input("რამდენია 11 + 21? ")
inp5 = int(inp5)

if inp5 == 32:
    print("შენ მიიღე 10 ქულა")
    score += 10
    logging.info(msg='10 ქულა', exc_info=True)
else:
    print("არასწორია")
    logging.info(msg='0 ქულა', exc_info=True)

logging.info(score)
print(f"შენი საბოლოო ქულა არის: {score}")

# 4.

logging.basicConfig(filename='quiz.log',level=logging.INFO)

inp1 = input("რა არის მონღოლეთის დედაქალაქი?")
logging.info(inp1)

inp2 = input("რა არის ავსტრალიის დედაქალაქი?")
logging.info(inp2)

inp3 = input("რა არის ჩეხეთის დედაქალაქი?")
logging.info(inp3)

inp4 = input("რა არის საქართველოს დედაქალაქი?")
logging.info(inp4)

inp5 = input("რა არის ისლანდიის დედაქალაქი?")
logging.info(inp5)

# 5.

import random

options = ['მაკრატელი', 'ქვა', 'ბადე']
com = 0
user = 0

print("თამაში არის სამამდე.")

while user < 3 and com < 3:
    inp1 = input('აირჩიეთ ქვა, მაკრატელი ან ბადე: ')

    if inp1 not in options:
        print("გთხოვთ აირჩიოთ ქვა, მაკრატელი ან ბადე!")
        continue

    com_choice = random.choice(options)
    print(f"კომპიუტერმა აირჩია {com_choice}")

    # მომხმარებლის მოგება
    if inp1 == com_choice:
        print("ფრეა")

    elif inp1 == 'ბადე' and com_choice == 'ქვა' or inp1 == 'ქვა' and com_choice == 'მაკრატელი' or \
        inp1 == 'მაკრატელი' and com_choice == 'ბადე':
        print("თქვენ მოიგეთ!")
        user += 1
        print(f"ანგარიში არის {user} : {com}")

    # კომპიუტერის მოგება
    else:
        print("ეს რაუნდი მოიგო კომპიუტერმა")
        com += 1
        print(f"ანგარიში არის {com} : {user}")


    if user == 3:
        print("გილოცავ თქვენ მოიგეთ თამაში")
    elif com == 3:
        print("სამწუხაროდ, თქვენ დამარცხდით")

# 6.


while True:

    gamer1 = random.randint(1, 6)
    gamer2 = random.randint(1, 6)

    print(f"Gamer 1-მა გააგორა: {gamer1}")
    print(f"Gamer 2-მა გააგორა: {gamer2}")

    if gamer1 == gamer2:
        print('ფრეა')
        continue
    elif gamer1 > gamer2:
        print("გაიმარჯვა Gamer 1-მა")
    else:
        print("გაიმარჯვა Gamer 2-მა")
    break
