import random
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_chosen = random.randint(0, 4)

print(f"The name {names[number_chosen]} was chosen to pay!!")