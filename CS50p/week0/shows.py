SHOWS = [
    " avatar: the last airbender",
    "Ben 10",
    "Arthur",
    "Jimmy Neutron  ",
    "The Proud family",
    "Spongebob squarepants ",
    "   kim possible",
    "phineas and ferb"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))


main()