#Define the password

password = "ilovecoding"

#Set the max number of attempts

attempts = 5

#A loop for entering the password with the limit of 5 attempts

while attempts > 0:
    entered = input("Type your password: ")

    if entered == password:
        print("Correct! You are logged in.")
        break
    else:
        attempts = attempts - 1
        
        if attempts > 0:
            print("Incorrect password. You still have", attempts, "tries left.")
        else:
            print("No tries left. Login failed.")