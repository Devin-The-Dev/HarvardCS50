emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(f"{phrase} {emoticon}")


main()