word=input("enter a word:")
start=word[0]
end=word[-1]
swap=end+word[1:-1]+start
print("swapped word=",swap)