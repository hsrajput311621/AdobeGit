class EMP:
    def __init__(self, eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.sal = esal

    def display(self):
        print(self.eid, end=" ")
        print(self.ename, end=" ")
        print(self.sal)


