vowels="aeiou"
element=input("enter a string: ")
pos=[s for s in element.lower() if s in vowels]
print("vowels are",pos)
