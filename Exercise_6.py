from math import sqrt
#6.1
def is_year_leap(year):
    """Checks if year is leap, and returns result"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

#6.2
def triangle_existance(a,b,c):
    """Checks if the sum of any two arguments is bigger then the third one.
    If yes returns True? if no - False."""
    if a < b + c and b < c + a and c < b + a:
        return True
    else:
        return False

#6.3
def spaceless():
    """Asks to enter the word without spaces, spaces in the beginning and the end are allowed.
    Function works until conditions are met and returns entered word."""
    while True:
        message = input("Enter message: ").strip()
        if " " not in message:
            return(message)

#6.4
def number_request():
    """Asks to enter the number until its done. Returns entered number."""
    while True:
        num = input("Enter number: ")
        try:
            num = float(num)
            return num
        except ValueError:
            pass
        except Exception as e:
            print(e, file=console_log.txt)


#6.5
def triangle_type(a,b,c):
    """Checks arguments correlation with triangle sides:
    If the sum of any two arguments is bigger then the third one returns "Isosceles triangle",
    If less - returns "Not a triangle"
    If all arguments are equal returns "Equilateral triangle\""""
    if a == b == c:
        return "Equilateral triangle"
    elif a < b + c and b < c + a and c < b + a:
        return "Isosceles triangle"
    else:
        return "Not a triangle"

#6.6
#First way
def distance(x1,y1,x2,y2):
    d1 = ((x2-x1)**2 + (y2 - y1)**2)**0.5
    return d1




#Second way using math module
def distance_math(x1,y1,x2,y2):
    d2 = sqrt((x2-x1)**2 + (y2 - y1)**2)
    return d2





