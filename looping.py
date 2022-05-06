# basic while loop
s = "Hello World!"

i = 0
c = 0
while i < len(s):
    if s[i].lower() in "aeiou":
        c += 1
    i += 1
    
print(f"Number of vowels in {s} is {c}")
     