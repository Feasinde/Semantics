from itertools import chain, combinations

def powerset(iterable):
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

def convertToPowerSets(Astr,Bstr):
    Aprime = list(powerset(Astr))
    B = set(Bstr)
    A = set()
    Alist = []
    for i in Aprime:
        if i != ():
            Alist.append(frozenset(i))
    A = set(Alist)

    return A,B

def Qmost(A,B):
    listOfSets = []
    for subset in A:
        if len(subset.intersection(B)) > len(subset.difference(B)):
            listOfSets.append(list(subset))

    return listOfSets

def QfewerThan3(A,B):
    listOfSets = []
    for subset in A:
        if len(subset.intersection(B)) < 3:
            listOfSets.append(list(subset))

    return listOfSets

def Qevery(A,B):
    listOfSets = []
    for subset in A:
        if subset.issubset(B):
            listOfSets.append(list(subset))

    return listOfSets

def Qsome(A,B):
    listOfSets = []
    for subset in A:
        if subset.intersection(B) != set():
            listOfSets.append(list(subset))
    return listOfSets

def Qno(A,B):
    listOfSets = []
    for subset in A:
        if subset.intersection(B) == set():
            listOfSets.append(list(subset))
    return listOfSets
