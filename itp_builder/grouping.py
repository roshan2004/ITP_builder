def regroup(lst):
    '''
    Takes a list of the beads, and breaks them in such a way that 3 beads is followed by 2, and 2 followed by 3 and so on.
    '''
    threes = [lst[i:i+3] for i in range(0, len(lst), 3)]
    final = []
    for l,r in zip(threes, threes[1:]):
        final.append(l)
        final.append([l[-1], r[0]])
    if len(threes[-1]) > 1:
        final.append(threes[-1])
    return final