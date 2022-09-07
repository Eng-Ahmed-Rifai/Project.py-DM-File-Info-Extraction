"""
AI
Task scraping extract files infos using re
1- Sort names ends with a dot extracted into new file.
2- Sort numbers by their companies keys number extracted into new file.
3- Sort and collect emails extracted into new file.
4- Counter on everything.
5- Don't worry current working directory handled.
by.Eng AhmedRifai
"""
import random
import re
import os
# Generating a random phone number.
if False :    
    VphoneNums = "012"
    for i in range(8):
        VphoneNums+=str(random.randint(0,9)) 
    print(VphoneNums)

# Changing the current working directory to the directory of this file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

Sfile = open("Test_file.txt" , "r")
data_file = Sfile.read()
print(data_file)
Sfile.close()
# separator
print("-" * 50)
# Finding all the words that have a space between them and end with a dot using regular expression.
pattern = re.compile(r"\w+\s\w+\s\w+\.")
matches = pattern.finditer(data_file)
names=[]
# Iterating through the matches and appending them to the list.
for match in matches:
    # Appending the names to the list and then sorting them.
    names.append(data_file[match.span()[0]:match.span()[1]])
    names.sort()
print(names)

# separator
print("-" * 50)
# Extra
# extract the names to a file.
Names_file = open("Names_file.txt","w")
Names_file.write(f"Sorted Names :\n")
Counter_names = 0
for name in names:
    Counter_names+=1
    Names_file.writelines(f"{Counter_names}- {name}\n")
Names_file.close()
# separator
print("-" * 50)

# The below code is doing the following:
# 1- Open the file "data.txt" and read it.
# 2- Find all the numbers in the file using regular expression.
# 3- Write the numbers in a new file "Numbers_files.txt"
# 4- Write the numbers in the new file according to companies key numbers.
pattern = re.compile(r"01\d{9}")
matches = pattern.finditer(data_file)
numbers = [] 
for match in matches:
    numbers.append(data_file[match.span()[0]:match.span()[1]])
print(numbers)
my_numbers = open("Numbers_files.txt","w")

# Sorting the numbers according to their companies keys numbers.
Enums ,Vnums ,Onums ,Tnums = [],[],[],[]
for num in numbers:
    if num.startswith("011"):
        Enums.append(num)
    elif num.startswith("010"):
        Vnums.append(num)
    elif num.startswith("012"):
        Onums.append(num)
    elif num.startswith("015"):
        Tnums.append(num)
print(Enums,Tnums,Vnums,Onums)
my_numbers.writelines(f"Etisalat numbers is:\n")
Counter1 =0
for Etisalat in Enums:
    Counter1+=1
    my_numbers.writelines(f"{Counter1}- {Etisalat}\n")
my_numbers.writelines(f"\nVodafone numbers is:\n")
Counter2=0
for Vodafone in Vnums:
    Counter2+=1
    my_numbers.writelines(f"{Counter2}- {Vodafone}\n")
my_numbers.writelines(f"\nOrange numbers is:\n")
Counter3=0
for Orange in Onums:
    Counter3+=1    
    my_numbers.writelines(f"{Counter3}- {Orange}\n")
my_numbers.writelines(f"\nTelecom numbers is:\n")
Counter4=0
for Telecom in Tnums:
    Counter4+=1    
    my_numbers.writelines(f"{Counter4}- {Telecom}\n")
my_numbers.close()

# separator
print("-" * 50)

# The below code is searching for emails in the data_file 
# then sorting them and writing them in a new file + Counting them.
pattern = re.compile(r"(\w+\.?\w+?\d?)(\@\w+)(\.\w+\.?\w+)")
matches = pattern.finditer(data_file)
Emails = [] 
for match in matches:
    Emails.append(data_file[match.span()[0]:match.span()[1]])
    Emails.sort()
print(Emails)

my_Email = open("Email_file.txt","w")
my_Email.write(f"All Emails sorted and ready :\n")
Counter_mails = 0
for email in Emails:
    Counter_mails+=1
    my_Email.writelines(f"{Counter_mails}- {email}\n")
my_Email.close()

# separator
print("-" * 50)