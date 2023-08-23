## Approach1: import module Name
#3 Approach2: from module name import functions,classes
# Packages : Collections of Modules, modules contain function and classes

#Approach 1:

import A
import B
obj1 = A.Animal()
obj1.display()

obj2 = B.Birds()
obj2.display()


#Approach 2

from A import Animal
from B import Birds

obj1 = Animal()
obj1.display()

obj2 = Birds()
obj2.display()


