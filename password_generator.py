import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

# print(s1,s2,s3,s4)

password_len = int(input("Enter Password Length : ")) # Asking for Password Length

s = []
s.extend(list(s1))   # Storing variable's value in an empty list
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# print(s)

random.shuffle(s)   # Shuffling the list 
print("Your Password is : ")

'''Two Methods to print Passwords'''

print("".join(s[0:password_len])) # Join : used to join all given values from the list

# print("".join(random.sample(s,password_len)))

