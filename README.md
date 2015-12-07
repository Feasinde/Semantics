#semQuantifiers

##Requirements:

* Python 3 or later (https://www.python.org/downloads/)

##Usage:

On the shell, simply import the script and its functions by typing:

``from semQuantifiers import *``

Each quantifier function returns a list of lists that contain all the pertinent subsets. For a more reader-friendly way of displaying the subsets, use a for loop to display the contents.

###Example of use

M = <{l, m, n, o, p}, i> , where i has the following graph:

monkeys -->    {l,m,p}  
teachers ->    {n,o}

“Most monkeys”

 ``for i in Qmost("lmp","lmnop"): print(i)``

``['n', 'm', 'p']``     
``['l', 'm', 'n', 'o', 'p']  ``  
``['l', 'm', 'n', 'o']  ``  
``['l', 'm', 'n']  ``  
``['l', 'o', 'p']  ``  
``['l', 'n', 'p']  ``  
``['l', 'm', 'o', 'p']  ``  
``['m', 'p']``  
``['l', 'm', 'n', 'p']  ``  
``['l', 'p']  ``  
``['m', 'o', 'p']  ``  
``['l', 'n', 'o', 'p']  ``  
``['n', 'm', 'o', 'p']  ``  
``['l', 'm']  ``  
``['l', 'm', 'o']``    
``['l', 'm', 'p']``

“Every teacher”

``for i in Qevery("no","lmnop"): print(i)``

``['o', 'n', 'm', 'l']``  
``['o', 'n', 'm', 'p']``  
``['o', 'n', 'l', 'p']``  
``['o', 'n', 'm', 'l', 'p']``  
``['o', 'n']``  
``['o', 'n', 'p']``  
``['o', 'n', 'l']``  
``['o', 'n', 'm']``
