#################################################
##Semantic quantifier calculator               ##
##by Andrés Lou, 2015                          ##
##Creative Commons Attribution License (cc-by) ##
#################################################

###EXAMPLE OF USE###

#M = <{l, m, n, o, p}, i> , where i has the following graph:
#John ----->    n
#Coco ----->    l
#monkeys -->    {l,m,p}
#teachers ->    {n,o}
#laughed -->    {n,o}

#“Most monkeys”

#>>> for i in Qmost("lmp","lmnop"): print(i)

##['n', 'm', 'p']
##['l', 'm', 'n', 'o', 'p']
##['l', 'm', 'n', 'o']
##['l', 'm', 'n']
##['l', 'o', 'p']
##['l', 'n', 'p']
##['l', 'm', 'o', 'p']
##['m', 'p']
##['l', 'm', 'n', 'p']
##['l', 'p']
##['m', 'o', 'p']
##['l', 'n', 'o', 'p']
##['n', 'm', 'o', 'p']
##['l', 'm']
##['l', 'm', 'o']
##['l', 'm', 'p']

#“No monkeys”

#>>> for i in Qno("lmp","lmnop"): print(i)

##['n']
##['n', 'o']
##['o']

##“Most monkeys”

##>>> for i in Qmost("lmp","lmnop"): print(i)

##['n', 'm', 'p']
##['l', 'm', 'n', 'o', 'p']
##['l', 'm', 'n', 'o']
##['l', 'm', 'n']
##['l', 'o', 'p']
##['l', 'n', 'p']
##['l', 'm', 'o', 'p']
##['m', 'p']
##['l', 'm', 'n', 'p']
##['l', 'p']
##['m', 'o', 'p']
##['l', 'n', 'o', 'p']
##['n', 'm', 'o', 'p']
##['l', 'm']
##['l', 'm', 'o']
##['l', 'm', 'p']

#“Every teacher”

# >>> for i in Qevery("no","lmnop"): print(i)
# 
# ['o', 'n', 'm', 'l']
# ['o', 'n', 'm', 'p']
# ['o', 'n', 'l', 'p']
# ['o', 'n', 'm', 'l', 'p']
# ['o', 'n']
# ['o', 'n', 'p']
# ['o', 'n', 'l']
# ['o', 'n', 'm']

from itertools import chain, combinations

##powerset takes a string converts it into a iterator
##that defines a powerset utilising each character as
##an element. Only used internally.
def powerset(iterable):
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

##convertToPowerSets takes two strings, A and B, and
##returns A as a frozenset object and B as a set
##object. B is meant to represent the universe of discourse
##and A the quantified noun.
def convertToPowerSets(Astr,Bstr):
    Bprime = list(powerset(Bstr))
    A = set(Astr)
    B = set()
    Blist = []
    for i in Bprime:
        if i != ():
            Blist.append(frozenset(i))
    B = set(Blist)

    return A,B

##All Q methods take two parameters, the set A which is
##the subset of the elements being quantified, and the 
##set B, which is all the elements in the universe of
##discourse
def Qmost(Astr,Bstr):
    A,B = convertToPowerSets(Astr,Bstr)
    listOfSets = []
    for subset in B:
        if len(A.intersection(subset)) > len(A.difference(subset)):
            listOfSets.append(list(subset))

    return listOfSets

def QfewerThan3(Astr,Bstr):
    A,B = convertToPowerSets(Astr,Bstr)
    listOfSets = []
    for subset in B:
        if len(A.intersection(subset)) < 3:
            listOfSets.append(list(subset))

    return listOfSets

def Qevery(Astr,Bstr):
    A,B = convertToPowerSets(Astr,Bstr)
    listOfSets = []
    for subset in B:
        if A.issubset(subset):
            listOfSets.append(list(subset))

    return listOfSets

def Qsome(Astr,Bstr):
    A,B = convertToPowerSets(Astr,Bstr)
    listOfSets = []
    for subset in B:
        if A.intersection(subset) != set():
            listOfSets.append(list(subset))
    return listOfSets

def Qno(Astr,Bstr):
    A,B = convertToPowerSets(Astr,Bstr)
    listOfSets = []
    for subset in B:
        if A.intersection(subset) == set():
            listOfSets.append(list(subset))
    return listOfSets

def Qtwo(Astr, Bstr):
    A,B = convertToPowerSets(Astr, Bstr)
    listOfSets = []
    for subset in B:
        if len(A.intersection(subset)) == 2:
            listOfSets.append(list(subset))
    return listOfSets

def Qshmewer(Astr,Bstr):
    A,B = convertToPowerSets(Astr,Bstr)
    listOfSets = []
    for subset in B:
        if len(A) < len(subset):
            listOfSets.append(list(subset))
    return listOfSets

