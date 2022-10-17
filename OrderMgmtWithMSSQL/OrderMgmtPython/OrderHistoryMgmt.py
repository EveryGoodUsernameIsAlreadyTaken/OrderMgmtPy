from OrderHistory import Order
from MyUtils import Message
from pysql import pySQL

class OrderHistory:
    def __init__(self):
        self.sql = pySQL()
        self.curOrder = Order()
        pass
    
    def _Disconnect(self):
        self.sql._Disconnection()

    def _AppendNewOrder(self, custNo):
        Message._Message('Order Page', 2)

        self.curOrder = self.sql._AppendNewOrderInfo(custNo)
        Message._Message('Successfully made new order', 2)

    def _ModifyOrder(self):
        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        if not bool(self.curOrder.OrderID):
            print('Please make an order first\n')
            return
        Message._Message('Modify Page', 2)

        product = input('Product ({0}):'.format(self.curOrder.Product))
        if bool(product):
            self.curOrder.Product = product; 
            
        price = input('Price ({0}):'.format(self.curOrder.Price))
        if bool(price) & isfloat(price):
            self.curOrder.Price = float(price)
    
        quantity = input('Quantity ({0}):'.format(self.curOrder.Quantity))
        if bool(quantity) & quantity.isnumeric():
            self.curOrder.Quantity = int(quantity)

        self.sql._ModifyOrderInfo(self.curOrder)
        Message._Message('Successfully modified order', 2)

        
    def _DeleteOrder(self):
        if not bool(self.curOrder.OrderID):
            print('Please make an order first\n')
            return
        
        Message._Message('Delete Page', 2)

        print('Are you sure you want to delete?\nPress (Y/y) to delete or anything else to cancel')
        ichoice = input('Choice: ')
        if not (ichoice == 'Y' or ichoice == 'y'):
            print('Canceling...\n')
            return


        self.sql._DeleteOrderInfo(self.curOrder.OrderID)
        self.curOrder = None
        Message._Message('Successfully deleted order', 2)
        
    def _ViewOrder(self):
        if not bool(self.curOrder.OrderID):
            print('Please make an order first\n')
            return

        Message._Message('View Order Info Page', 2)
        
        print('OrderId'.ljust(10, ' ') + 'Cust Id'.ljust(10, ' ') + 'Date'.ljust(30, ' ') + 'Product'.ljust(20, ' ') + 'Price'.ljust(10, ' ') + 'Quantity'.ljust(10, ' '), 'Total'.ljust(10, ' '))
        print('-------'.ljust(10, ' ') + '-------'.ljust(10, ' ') + '----'.ljust(30, ' ') + '-------'.ljust(20, ' ') + '-----'.ljust(10, ' ') + '--------'.ljust(10, ' '), '-----'.ljust(10, ' '))
        tot = self.curOrder.Price * self.curOrder.Quantity
        print(str(self.curOrder.OrderID).ljust(10, ' ') +  str(self.curOrder.CustNo).ljust(10, ' ') +  self.curOrder.Date.ljust(30, ' ') +  self.curOrder.Product.ljust(20, ' ') + "{:.2f}".format(self.curOrder.Price).ljust(10, ' ') + str(self.curOrder.Quantity).ljust(12, ' ') + "{:.2f}".format(tot).ljust(10, ' '))
        print()
        
    def _ViewOrderList(self, custNo):
        Message._Message('View Order List Page', 2)
        
        self.sql._ViewOrderList()

    def _FindOrder(self, custNo):
        Message._Message('Find Order Page', 2)
        
        szOrderId = input('Order Id: ')

        if szOrderId.isnumeric():
            temp = self.sql._FindOrder(int(szOrderId), custNo)
            if bool(temp):
                self.curOrder = temp