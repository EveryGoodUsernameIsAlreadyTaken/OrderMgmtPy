from Customer import Cust
from MyUtils import Message
from pysql import pySQL

class CustomerMgmt:
    def __init__(self):
        self.curCust = Cust
        self.sql = pySQL()
        pass

    def _LogIn(self):
        Message._Message('Log In Page', 2)

        szCustNo = input('Please input your customer number: ')
        self.curCust = self.sql.LogIn(szCustNo)
        if bool(self.curCust):
            Message._Message('Logged In Successfully', 2)
            return szCustNo
        else:
            return 0

    def _LogOut(self):
        Message._Message('Logging Out', 2)

        self.curCust = None

    def _Disconnect(self):
        self.sql._Disconnection()

    def _AppendCustomerInfo(self):
        Message._Message('Register Page', 2)

        self.curCust = self.sql._AppendNewCustInfo()
        Message._Message('Registered Successfully', 2)
        return self.curCust.CustNo

    def _ModifyCustomerInfo(self):
        Message._Message('Modification Page', 2)
    
        FName = input('Please input your first name ({0}): '.format(self.curCust.FName))
        if bool(FName):
            self.curCust.FName = FName;

        LName = input('Please input your last name ({0}): '.format(self.curCust.LName))
        if bool(LName):
            self.curCust.LName = LName;

        City = input('Please input your city ({0}): '.format(self.curCust.City))
        if bool(City):
            self.curCust.City = City;
            
        Addr = input('Please input your address ({0}): '.format(self.curCust.Addr))
        if bool(Addr):
            self.curCust.Addr = Addr;
            
        PhoneNo = input('Please input your phone number ({0}): '.format(self.curCust.PhoneNo))
        if bool(PhoneNo):
            self.curCust.PhoneNo = PhoneNo;

        self.sql.ModifyCustomerInfo(self.curCust)
        Message._Message("Successfully Modified Customer Info", 2)

    def _DeleteCustomerInfo(self):
        Message._Message('Deletion Page', 2)

        print('Are you sure you want to delete?\nPress (Y/y) to delete or anything else to cancel')
        ichoice = input('Choice: ')
        if not (ichoice == 'Y' or ichoice == 'y'):
            print('Canceling...\n')
            return

        self.sql._DeleteCustomerInfo(self.curCust.CustNo)
        self.curCust = None
        Message._Message('Successfully Deleted', 2)
        self._LogOut()

    def _ViewCustomerInfo(self):
        Message._Message('View Info Page', 2)
        
        print('CID'.ljust(10, ' ') + 'First Name'.ljust(30, ' ') + 'Last Name'.ljust(30, ' ') + 'City'.ljust(30, ' ') + 'Address'.ljust(30, ' ') + 'PhoneNo'.ljust(12, ' '))
        print('---'.ljust(10, ' ') + '----------'.ljust(30, ' ') + '---------'.ljust(30, ' ') + '----'.ljust(30, ' ') + '-------'.ljust(30, ' ') + '-------'.ljust(12, ' '))
        print(str(self.curCust.CustNo).ljust(10, ' ') + self.curCust.FName.ljust(30, ' ') + self.curCust.LName.ljust(30, ' ') + self.curCust.City.ljust(30, ' ') + self.curCust.Addr.ljust(30, ' ') + self.curCust.PhoneNo.ljust(12, ' '))
        print()

    def _ViewCustomerList(self):
        Message._Message('View Customer List Page', 2)
        self.sql.ViewCustomerList()