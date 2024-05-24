#if else condition
n =int(input("enter a num"))
if n>0:
    print("the number is poistive")
else:
    print("the number is neative")


#elif condition
m =int(input("enter a marks: "))
if m<=25:
    print("Grade is F")
elif 25< m <=50:
    print("Grade is E")
elif 50 < m <= 60:
    print("Grade is D")
elif 60 < m <= 70:
    print("Grade is C")
elif 70 < m <= 80:
    print("Grade is B")
elif m > 80:
    print("Grade is A")


#nested if
yr=int(input("enter a year: "))
if yr%4 ==0:
    if yr%100 ==0:
        if yr %400 ==0:
            print("This is year is leap year")
        else:
            print("This is year is not a leap year")
    else:
            print("This is year is a leap year")
else:
            print("This is year is not a leap year")