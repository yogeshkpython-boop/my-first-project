
#return value practice 

# ek function jo 3 value ka sum return kare

def sum_of_three(a, b, c):
    return a + b + c

print(sum_of_three(10, 20, 30))

# function jo kisi string ki length return kare

def string_length(s):
    return len(s)

print(string_length("Hello"))

# function jo largest of 2 numbers return kare
 
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 20))

# function jo smallest of 3 numbers return kare

def smallest(a, b, c):
    return min(a, b, c)

print(smallest(10, 5, 8))

# CONDITION BASED QUESTION

#function jo age le aur bole adult ho yaan minor 

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(16))

# function jo marks le aur pass/fail btaye 

def check_result(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

print(check_result(45))

# function jo tempreature le or hot/cold btaye 

def check_temperature(temp):
    if temp >= 25:
        return "Hot"
    else:
        return "Cold"

print(check_temperature(30))

#function jo password check karega ki (12345) sahi hai yaan nahi

def check_password(password):
    if password == "12345":
        return "Correct Password"
    else:
        return "Wrong Password"

print(check_password("12345"))

#LOOP + FUNCTION

# function jo 1 se 10 tk print karega

def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()

# function jo table print kare kisi bhi number ka

def print_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

print_table(5)

# function jo list k saare eliments print karega 

def print_list(lst):
    for item in lst:
        print(item)

print_list([1, 2, 3, 4, 5])

# function jo numbers ka total sum nikale list me se  

def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))

# MEDIUM QUESTIONS

# function jo pelindrome check kare 

def is_palindrome(s):
    s = str(s)
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(is_palindrome("madam"))

# function jo prime nmber check kare 

def check_prime(num):
    if num <= 1:
        return "Not Prime"
    
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    
    return "Prime"

number = int(input("Enter number: "))
print(check_prime(number))

# function jo factorial nikle

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(5))

# function jo vovel count kare string me

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    
    for ch in s:
        if ch in vowels:
            count += 1
            
    return count

print(count_vowels("Hello World"))

