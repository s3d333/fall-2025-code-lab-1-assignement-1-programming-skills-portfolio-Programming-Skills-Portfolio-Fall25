#List the names down

names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]

#Require user input for name

search = input("Enter name:")

#Make a code to search through the names

found = False
for n in names:
    if n == search:
        found = True
        break



#Print the output depending on result

if found:
    print(f"{search} found.")
else:
    print(f"{search} not found.")