#################################################
##Semantic quantifier calculator                #
##by Andrés Lou, 2015                          #
##Creative Commons Attribution License (cc-by)  #
#################################################


from itertools import chain, combinations

##powerset takes a string converts it into a iterator
##that defines a powerset utilising each character as
##an element. Only used internally.
def powerset(iterable):
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

##convertToPowerSets takes two strings, A and B, and
##returns A as a powerset set object and B as a frozenset
##object. A is meant to represent the universe of discourse
##and B the quantified noun.
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

##All Q methods take to parameters, a powerset A
##of the universe of discourse, A, and the set of
##the interpretation of the quantified noun, B
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

def Qshmewer(A,B):
    listOfSets = []
    for subset in A:
        if len(subset) < len(B):
            listOfSets.append(list(subset))
    return listOfSets

###EXAMPLE OF USE###

#M = <{l, m, n, o, p}, i> , where i has the following graph:
#John ----->    n
#Coco ----->    l
#monkeys -->    {l,m,p}
#teachers ->    {n,o}
#laughed -->    {n,o}

#>>> A,B = convertToPowerSets("lmnop", "lmp")

#“Most monkeys”

#>>> mostAB = Qmost(A,B)

#“No monkeys”

#>>> noAB = Qno(A,B)

##>>> for i in mostAB: i
##
##['p', 'm']
##['p', 'l', 'm']
##['p', 'n', 'l', 'm']
##['o', 'p', 'l']
##['n', 'l', 'm']
##['m']
##['l', 'm']
##['o', 'p', 'l', 'm']
##['o', 'n', 'l', 'm', 'p']
##['o', 'l', 'm']
##['p', 'n', 'l']
##['p', 'l']
##['o', 'p', 'm']
##['p', 'n', 'm']
##['l']
##['p']

##>>> for i in noAB: i
##
##['o', 'n']
##['o']
##['n']
