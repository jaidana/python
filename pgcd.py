def pgcd(a,b):
#pgcd has no reminders
    print(a, b)
    if a%b == 0:
        return b
    else:
#methode elucidien
        return (pgcd(b, a%b))
print (pgcd(11,66))
