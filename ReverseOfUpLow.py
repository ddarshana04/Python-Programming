text = "hElLo WoRlD"
str= ""
for i in range (len(text)):
    if text[i].isupper():
        str += text[i].lower()
    elif text[i].islower():
        str += text[i].upper()
    else:
        str +=text[i]
print("String: " + text)
print("Updated String: " +str)

