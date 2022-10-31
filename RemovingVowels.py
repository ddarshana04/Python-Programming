text = "The food is very tasty"
vowels = ['a','e','i','o','u']
for i in text.lower():
    if i in vowels:
        text = text.replace(i,"")
print("After removing vowels: ")
print(text)        
