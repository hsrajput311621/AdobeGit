class STU:
    def __init__(self, sid,sname,grade):
        self.sid=sid
        self.sname = sname
        self.grade = grade

    def display(self):
        print(self.sid, end=" ")
        print(self.sname, end=" ")
        print(self.grade)
