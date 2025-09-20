# Count Characters in String 
text = input("Enter text: ")
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
print("Character Frequency:", count)
