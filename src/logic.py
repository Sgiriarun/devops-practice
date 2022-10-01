import wikipedia


def ask_arun(name="vikram", length=1):
    wiki = wikipedia.summary(name, length)
    return wiki
