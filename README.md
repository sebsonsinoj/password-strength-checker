# password strength checker

a simple python program that checks how strong a password is and gives suggestions for improving it.

## features

* checks password length
* checks for lowercase letters
* checks for uppercase letters
* checks for numbers
* checks for symbols
* checks against a list of commonly used passwords
* gives the password a strength rating
* gives suggestions to improve weak passwords

## how it works

the program gives the password a score out of 6 based on different security requirements.

it checks:

* password length
* lowercase letters
* uppercase letters
* numbers
* symbols
* whether the password is commonly used

the final score is then used to give the password a rating of weak, medium, strong or very strong.

## technologies used

* python
* string library

## what i learned

this project helped me practise using python functions, selection, iteration, lists and string manipulation.

i also learned about basic password security concepts and how different password characteristics can be used to create a simple strength-rating system.

## how to run

1. download or clone this repository
2. open `password_strength_checker.py`
3. run the program using python
4. enter a password when prompted
5. the program will display the strength, score and any suggestions

## example

```text
enter a password to check: password123

password strength: medium
score: 3 / 6

suggestions to make your password stronger:
- add some uppercase letters.
- add a symbol such as !, @, # or $.
```

## disclaimer

this is an educational project designed to demonstrate basic password-security concepts. it is not intended to replace professional password-security tools.
