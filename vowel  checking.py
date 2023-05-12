#string method

'''letter=input("enter the letter : ")
if letter in('a','e','i','o','u'):
    print("the entered letter is a vowel",letter)
else:
    print("the entered letter is not a vowel",letter)'''


# using ascii

#letter=int(input("enter the letter :"))


#checking alphabet is a vowel,consenent or not using for loop
char=input("enter a charecter :")
vowel=('a','e','i','o','u')
for i in vowel:
    if char in vowel:
        print("vowel")
        break
    else:
        print("consonent")
        break