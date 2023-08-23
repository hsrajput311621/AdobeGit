import sys
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package_emp")
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package_stu")

import emp
e_obj = emp.EMP(101, "Hitesh", 10000)
e_obj.display()

import stu
s_obj = stu.STU(110030, "Rahul", "A")
s_obj.display()

##Approach 2
import sys
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package_emp")
sys.path.append("D:\PYTHON-PROJECTS\Python-Projects\Modules&Packages\pack1\package_stu")

from emp import EMP
e = EMP(105, "Archana", 20000)
e.display()

from stu import STU
s = STU(110, "Papa", "A+")
s.display()

