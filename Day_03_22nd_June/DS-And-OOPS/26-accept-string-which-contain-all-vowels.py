def check(string):
    string=string.lower()
    vowels=("aeiou")
    s=set({})

    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass
    if len(s)==len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")

string = "SEEquoial"
check(string)