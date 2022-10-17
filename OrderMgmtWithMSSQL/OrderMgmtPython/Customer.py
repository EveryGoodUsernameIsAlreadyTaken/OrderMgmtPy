class Cust:
    CustNo = 0
    FName = ''
    LName = ''
    City = ''
    Addr = ''
    PhoneNo = ''

    def __init__(self):
        pass

    def _FullName(self):
        return self.fname + " " + self.lname


