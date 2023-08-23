# Client2 is currently outside of the package

import sys
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package1")
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package1\package2")
import module3
import module4

module3.m2()
module4.m1()

#Approach 2

import sys
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package1")
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package1\package2")

from module3 import *
from module4 import *

m1()
m2()