import wikipedia


def ask_arun(name="my_god", length=1):
    wiki = wikipedia.summary(name, length)
    return wiki
