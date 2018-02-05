string = input("Enter String to check vowel letters: ")
count = 0
for i in string:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        print(i)
        count += 1
print("Total number of vowel letters in enterd string are: ", count)
