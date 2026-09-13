import string


def check_password(password):
    score = 0
    feedback = []

    #check length of the pass enterd
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        #giving feedback to increase strength
        feedback.append("use at least 12 characters.")

    #check if there r lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        #giving feedback to increase strength
        feedback.append("add some lowercase letters.")

    #check if there are any uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        #giving feedback to increase strength
        feedback.append("add some uppercase letters.")

    #same thing we did for previous we do for nums
    if any(char.isdigit() for char in password):
        score += 1
    else:
        #giving feedback to increase strength
        feedback.append("add some numbers.")

    #same thing we did for previous we do for symbols
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        #giving feedback to increase strength
        feedback.append("add a symbol such as !, @, # or $.")

    #check for common weak PWs
    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "password123",
        "admin",
        "letmein"
    ]

    #automatically rate the password a 0 if its in common_passwords
    if password.lower() in common_passwords:
        score = 0
        feedback.append("this is a commonly used password.")

    #giving final rating based on paarmeters
    if score <= 2:
        strength = "weak"
    elif score <= 4:
        strength = "medium"
    elif score <= 5:
        strength = "strong"
    else:
        strength = "very strong"

    return strength, score, feedback


#main program which is shown to the user
password = input("enter a password to check: ")

strength, score, feedback = check_password(password)

print("\npassword strength:", strength)
print("score:", score, "/ 6")

if feedback:
    print("\nsuggestions to make your password stronger:")

    #getting all the sugegstions in feedback[] to show the user
    for suggestion in feedback:
        print("-", suggestion)

else:
    #if all feedback paarmeters are okay then this message is displayed
    print("\nno improvements needed")
