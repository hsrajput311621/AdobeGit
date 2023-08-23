import module1
import module2
import sys
sys.path.append("D:/PYTHON-PROJECTS/Python-Projects/Modules&Packages/pack1")

module1.dislpay()   # method in module1 inside package
module2.show()      # method in mdoule2 inside package

# if the client is outside the package we can not import,
# module1 and module2 both are in other package.



# we need to import the 'sys' in order to use the module1 and module2 coz, the
#client module out of the package and if client need to access the methods, its
#must import the sys module.


# Approach 2 ###

from module1 import *
from module2 import *

dislpay()
show()