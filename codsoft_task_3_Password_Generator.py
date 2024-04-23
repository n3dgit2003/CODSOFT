import random

print("PASSWORD GENERATOR\n")
#Get the required length of the password
nr_char=int(input("Enter the number of characters required : "))

#Create a list of characters
list_of_char=list("1 2 3 4 5 6 7 8 9 0 @ # ! $ % ^ & * ( ) - _ + = / \ | . ; : < > a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split())

passwordlist=[]

for i in range(nr_char):
    passwordlist.append(random.choice(list_of_char))

password=""
for char in passwordlist:
    password=password+char

print(f"The recommended password is : {password}")
