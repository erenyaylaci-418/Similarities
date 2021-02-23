from nltk.tokenize import sent_tokenize




def lines(a, b):
    """Return lines in both a and b"""
    satira = a.splitlines()
    satirb = b.splitlines()
    thislist = set()
    for i in range(len(satira)):
        if satira[i] in satirb:
            thislist.add(satira[i])
    return list(thislist)

    # bitti



def sentences(a, b):
    """Return sentences in both a and b"""
    lista = sent_tokenize(a)
    listb = sent_tokenize(b)
    thislist =set()
    for i in range(len(lista)):
        if lista[i] in listb:
            thislist.add(lista[i])


    #biiti
    return list(thislist)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    def subStrs(string, length):
        strings = set()
        end = True
        stringLength = len(string)
        start = 0

        while end:
            stop = start + length
            if stop > stringLength:
                end = False
                continue
            strings.add(string[start: stop])
            start = start + 1
        return list(strings)


    astr = subStrs(a, n)
    bstr = subStrs(b, n)
    thislist = set()

    for i in range(len(astr)):
        if astr[i] in bstr:
            thislist.add(astr[i])

    return list(thislist)

