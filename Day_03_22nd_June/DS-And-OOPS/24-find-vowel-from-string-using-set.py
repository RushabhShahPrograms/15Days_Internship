str = "PythonDjango"
count=0
vowel=set("aeiouAEIOU")

for alphabet in str:
    if alphabet in vowel:
        count = count+1
    
print("Number of vowels:",count)