#6.1
def is_year_leap(year):
    """Checks if year is leap, and returns result"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

#6.2
def triangle_existance(a,b,c):
    if a < b + c and b < c + a and c < b + a:
        return True
    else:
        return False

#6.3
def spaceless():
    while True:
        message = input("Enter message: ").strip()
        if " " not in message:
            return(message)
            break

#6.4
def number_request():
    while True:
        num = input("Enter number: ")
        try:
            num = float(num)
            return num
            break
        except:
            pass

