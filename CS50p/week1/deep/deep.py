answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Lowercase to reduce number of conditions
# Have it all as one word
# Delete hyphens
# Delete whitespace at either ends of string
newA = answer.lower().replace(" ", "").replace("-", "").strip()

# If it's not 42 or "fortytwo" say no
if (newA == "42" or newA == "fortytwo"):
    print("Yes")

else:
    print("No")