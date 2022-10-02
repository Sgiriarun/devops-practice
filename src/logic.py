import wikipedia


def ask_arun(name="my_god", length=1):
    """this about wikipedia, with help of ask_arun method"""
    wiki = wikipedia.summary(name, length)
    return wiki
