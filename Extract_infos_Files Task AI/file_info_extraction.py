"""
AI
Task: Scraping and extracting file information using regular expressions.
1- Sort names that end with a dot and extract them into a new file.
2- Sort numbers by their company key numbers and extract them into a new file.
3- Sort and collect emails and extract them into a new file.
4- Count occurrences of various elements.
5- The current working directory is automatically handled.

by Eng Ahmed Rifai
"""

import random
import re
import os

# Generating a random phone number.
if False:
    VphoneNums = "012"
    for i in range(8):
        VphoneNums += str(random.randint(0, 9))
    print(VphoneNums)

# Changing the current working directory to the directory of this file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

# Opening and reading the "Test_file.txt" file.
Sfile = open("Test_file.txt", "r")
data_file = Sfile.read()
print(data_file)
Sfile.close()

# Separator
print("-" * 50)

# Finding all the words that have a space between them and end with a dot using regular expressions.
pattern = re.compile(r"\w+\s\w+\s\w+\.")
matches = pattern.finditer(data_file)
names = []

# Iterating through the matches and appending them to the list.
for match in matches:
    # Appending the names to the list and then sorting them.
    names.append(data_file[match.span()[0]:match.span()[1]])
    names.sort()
print(names)

# Separator
print("-" * 50)

# Extra
# Extract the names to a file.
Names_file = open("Names_file.txt", "w")
Names_file.write(f"Sorted Names:\n")
Counter_names = 0
for name in names:
    Counter_names += 1
    Names_file.writelines(f"{Counter_names}- {name}\n")
Names_file.close()

# Separator
print("-" * 50)

# The following code does the following:
# 1- Open the "data.txt" file and read its content.
# 2- Find all the numbers in the file using regular expressions.
# 3- Write the numbers in a new file called "Numbers_files.txt".
# 4- Write the numbers in the new file according to their company key numbers.
pattern = re.compile(r"01\d{9}")
matches = pattern.finditer(data_file)
numbers = []

for match in matches:
    numbers.append(data_file[match.span()[0]:match.span()[1]])
print(numbers)
my_numbers = open("Numbers_files.txt", "w")

# Sorting the numbers according to their company key numbers.
Enums, Vnums, Onums, Tnums = [], [], [], []
for num in numbers:
    if num.startswith("011"):
        Enums.append(num)
    elif num.startswith("010"):
        Vnums.append(num)
    elif num.startswith("012"):
        Onums.append(num)
    elif num.startswith("015"):
        Tnums.append(num)
print(Enums, Tnums, Vnums, Onums)
my_numbers.writelines(f"Etisalat numbers:\n")
Counter1 = 0
for Etisalat in Enums:
    Counter1 += 1
    my_numbers.writelines(f"{Counter1}- {Etisalat}\n")
my_numbers.writelines(f"\nVodafone numbers:\n")
Counter2 = 0
for Vodafone in Vnums:
    Counter2 += 1
    my_numbers.writelines(f"{Counter2}- {Vodafone}\n")
my_numbers.writelines(f"\nOrange numbers:\n")
Counter3 = 0
for Orange in Onums:
    Counter3 += 1
    my_numbers.writelines(f"{Counter3}- {Orange}\n")
my_numbers.writelines(f"\nTelecom numbers:\n")
Counter4 = 0
for Telecom in Tnums:
    Counter4 += 1
    my_numbers.writelines(f"{Counter4}- {Telecom}\n")
my_numbers.close()

# Separator
print("-" * 50)

# The following code searches for emails in the data_file,
# sorts them, and writes them into a new file.
# It also counts the number of emails.
pattern = re.compile(r"(\w+\.?\w+?\d?)(\@\w+)(\.\w+\.?\w+)")
matches = pattern.finditer(data_file)
emails = []

for match in matches:
    emails.append(data_file[match.span()[0]:match.span()[1]])
    emails.sort()
print(emails)

my_emails = open("Email_file.txt", "w")
my_emails.write(f"All Emails sorted and ready:\n")
counter_emails = 0
for email in emails:
    counter_emails += 1
    my_emails.writelines(f"{counter_emails}- {email}\n")
my_emails.close()

# Separator
print("-" * 50)
