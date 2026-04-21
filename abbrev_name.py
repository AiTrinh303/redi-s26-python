def abbrev_name(name):
    first, last = name.split()
    return first[0].upper() + "." + last[0].upper()

abbrev_name = lambda name: ".".join([word[0].upper() for word in name.split()])

def abbrev_name1(name):
    names = name.split()
    return f"{names[0][0]}.{names[1][0]}".upper()

def abbrev_name2(name):
    return ".".join([n[0].upper() for n in name.split()])


