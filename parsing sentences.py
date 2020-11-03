

#variable for user input
x = input("enter a sentence: ")

#create a blank array
splits = []

#have a variable for spaces(the space character in the sentence)
spaces = ''

#creating a for loop for every letter in the user sentence
for c in x:
    if c == ' ':
        splits.append(spaces)
        spaces = ''
        
    else:
        spaces += c
        
if spaces:
    splits.append(spaces)

#printing the array which is the sentence parsed 
print(splits)
