#Store all the days of the months in a dictionary
months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

#Gather user input
month_name = (input("Enter a month name:"))

#Make it so capitalization doesnt matter
month_name = month_name.lower()


#We then run a check to make sure the month name is valid and if it is it prints the number of days
if month_name in months:
    print(f"{month_name} has {months[month_name]} days.")


#If the input is not in the list it prints invalid
else:
    print("Month name invalid")