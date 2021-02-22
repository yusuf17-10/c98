introString = input("enter A Sentence : ")
characterCount = 0
wordCount = 1

for i in introString:
    characterCount=characterCount+1
    if(i == " "):
        wordCount=wordCount+1

print("number of characters in a string")
print(characterCount)
print("number of words in a string")
print(wordCount)