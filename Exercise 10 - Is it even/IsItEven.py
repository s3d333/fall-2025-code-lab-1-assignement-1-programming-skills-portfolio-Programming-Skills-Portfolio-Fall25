#A function to see if the number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."
    
#Run a odd/even check

def main():
    num = int(input("Enter number:"))
    result = check_even_odd(num)
    print(result)

#Run the function

if __name__ == "__main__":
    main()