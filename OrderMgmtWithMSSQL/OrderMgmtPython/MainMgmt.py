from tarfile import USTAR_FORMAT
from CustomerMgmt import CustomerMgmt
from OrderHistoryMgmt import OrderHistory
from MyUtils import Message

class MainMgmt:
    def __init__(self):
        self.custMgmt = CustomerMgmt()
        self.orderMgmt = OrderHistory()
        self._logged = False
        pass


    def _MainMenu(self):
        choice = ''
        if not self._logged:
            choice = input('press (1)Login\npress (2)Register\npress (0)Exit\nChoice: ')
            if choice.isnumeric():
                ichoice = int(choice)
                if ichoice >= 0 & ichoice <= 2:
                    return ichoice
        else:
            choice = input('press (3)Modify Customer\npress (4)Delete Customer\npress (5)View Customer Info\npress (6)View All Customer List\npress (7)New Order\npress (8)Modify Order\npress (9)Delete Order\npress (10)View Order\npress (11)View All Order List\npress (12)Find Order\npress (13)Main Menu\nChoice: ')
            if choice.isnumeric():
                ichoice = int(choice)
                if ichoice >= 3 & ichoice <= 13:
                    return ichoice
        
        print('That is not a choice\n')
        return -1

    def _MyChoice(self, ichoice):
        if not self._logged:
            if ichoice == 0:
                self.custMgmt._Disconnect()
                self.orderMgmt._Disconnect()
                return False
            elif ichoice == 1:
                self.custNo = self.custMgmt._LogIn()
                if bool(self.custNo):
                    self._logged = True
            elif ichoice == 2:
                self.custNo = self.custMgmt._AppendCustomerInfo()
                if bool(self.custNo):
                    self._logged = True
            else:
                Message._Message('Please input a real choice', 2)
        else:
            if ichoice == 3:
                self.custMgmt._ModifyCustomerInfo()
            elif ichoice == 4:
                self.custMgmt._DeleteCustomerInfo()
                self._logged = False
            elif ichoice == 5:
                self.custMgmt._ViewCustomerInfo()
            elif ichoice == 6:
                self.custMgmt._ViewCustomerList()
            elif ichoice == 7:
                self.orderMgmt._AppendNewOrder(self.custNo)
            elif ichoice == 8:
                self.orderMgmt._ModifyOrder()
            elif ichoice == 9:
                self.orderMgmt._DeleteOrder()
            elif ichoice == 10:
                self.orderMgmt._ViewOrder()
            elif ichoice == 11:
                self.orderMgmt._ViewOrderList(self.custNo)
            elif ichoice == 12:
                self.orderMgmt._FindOrder(self.custNo)
            elif ichoice == 13:
                print('Logging out')
                self.custMgmt._LogOut()
                self._logged = False
            else:
                Message._Message('Please input a real choice', 2)
        return True

