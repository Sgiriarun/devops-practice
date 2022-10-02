import wikipedia


def ask_arun(name="my_god", length=1):
    """this about wikipedia, with help of ask_arun method"""
    wiki = wikipedia.summary(name, length)
    return wiki
def list_arun(name):
    """this to list the search item, select appropriate to ask_arun"""
    result= wikipedia.search(name)
    return result