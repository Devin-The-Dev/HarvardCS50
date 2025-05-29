# Put words into a list
face = input().split()

# Identify and replace emoticons with emojis
def emoticonToEmoji(phrase):
    conversion = []

    for word in phrase:
        if word == ":)":
            conversion.append("\U0001F642")
        elif word == ":(":
            conversion.append("\U0001F641")
        else:
            conversion.append(word)

    # Remove the brackets and single quotes
    print(' '.join(conversion))

emoticonToEmoji(face)