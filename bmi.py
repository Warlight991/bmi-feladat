import math


def beker(x, y):
    y= y/100
    tti = x / (y*y)
    return(round(tti,1))


def kategoria():
    if beker(suly,magassag) < 18.5:
        print("Alultáplált")
    elif beker(suly,magassag) < 24.9:
        print("Normal")
    elif beker(suly,magassag) < 29.9:
        print("Túlsúlyos")
    else: print("Elhízott")

if __name__== "__main__":
    suly = float(input("Kérem a testsúlyod (kg):"))
    magassag =float(input("Kérem a mgasságod (cm):"))
    print(beker(suly,magassag))
    kategoria()
    
    