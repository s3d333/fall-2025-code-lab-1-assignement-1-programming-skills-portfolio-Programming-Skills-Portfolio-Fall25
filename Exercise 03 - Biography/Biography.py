#Collect users input
name= input("Enter your name:")

hometown= input("Enter your hometowns name:")


#For age we make a while loop to make sure the user inputs a valid number
while True:
    age_input = input("Enter age:")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Age invalid")

    
#Store all the information 
info = {
    "Name": name,
    
    "Hometown": hometown,

    "Age": age,
}
    
#Print all the information
print("User Biography:")

print(info["Name"])

print(info["Hometown"])

print(info["Age"])