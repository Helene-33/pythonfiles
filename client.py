class client():
    def __init__(self, name, email):
        self.name=name
        self.email=email
    
    def getclientname(self):
        return self.name

    def setclientname(self, name):
        self.name=name

    def getemail(self):
        return self.email

    def setemail(self, email):
        self.email=email
    
    def __str__(self):
        return self.name + ' ' + self.email

