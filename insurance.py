# A drive is insured if he is married
# male and above 30 years agents
# fermale and above 25 years age

married = input("Enter marrital status[m/u]:")

if married == 'm':
    print("Insured")
    
else:
    gender = input("Enter gender [m/f]:")
    age = int(input("Enter age:"))
    if (gender == 'm' and age > 30) or (gender == 'f' and age > 25):
        print("Insured")
    else:
        print("Not Inusured")
