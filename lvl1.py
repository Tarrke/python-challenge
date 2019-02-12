

# Build our dictionnary based on the first clue : k => m
def build_dict(char_from, char_to):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    spec  = "' ()."
    index_fr = alpha.index(char_from)
    index_to = alpha.index(char_to)
    return dict(zip(alpha[index_fr:]+alpha[:index_fr]+spec, alpha[index_to:]+alpha[:index_to]+spec))

def tr(char):

    return m[char]

#print(tr('a'))

#print(''.join(map(tr, 'aaa')))

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
d = build_dict('k', 'm')
r = ''.join(list(map(lambda x: d[x], s)))
print(r)

# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
url = "map"
r = ''.join(list(map(lambda x: d[x], url)))
print(r)