text = input("Enter String: ")
result = ""
for i in text:
    redult = result + chr(ord(i)+3)
print("Encrypted text: " + result)    