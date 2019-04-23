import re

def find_char(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

def musique(musique):
    if (musique == '-'):
        return 5.72 / 11.0
    if (musique == 'Inédit'):
        return 5.72 / 11.0

    musique = re.sub("[\(\[].*?[\)\]]", "", musique)
    locs = list(find_char(musique, 'p'))

    pos = []
    for loc in locs:
        if (musique[loc - 1] == "T" or musique[loc - 1] == "A"):
            pos.append(0)
        elif (musique[loc - 1] == "D" or musique[loc - 1] == "R"):
            pos.append(6)
        else:
            pos.append(int(musique[loc - 1]))

    if (len(pos) > 0):
        score = 0
        for p in pos:
            if (p == 0):
                score += 11
            else:
                score += p
        return (score / len(pos)) / 11.0
    else:
        return 5.72 / 11.0
