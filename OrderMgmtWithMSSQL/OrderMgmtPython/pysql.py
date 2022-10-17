from Customer import Cust
from OrderHistory import Order
from datetime import date
from MyUtils import Message
import pyodbc

class pySQL:
    def __init__(self):
        self.cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=noesys; DATABASE=CPPDB; UID=cpptest; PWD=cpptest;')
        self.cursor = self.cnxn.cursor()

    def _Disconnection(self):
        self.cursor.close() #DISCONNECTION
        
    def LogIn(self, custNo):
        self.cursor.execute("{CALL PQ_GET_CUSTOMER(?)}", custNo)
        rset = self.cursor.fetchone()
        if rset is None:
            print('No such customer number\n')
            return None
        else:
            newCust = Cust()
            newCust.CustNo = rset[0]
            newCust.FName = rset[1]
            newCust.LName = rset[2]
            newCust.City = rset[3]
            newCust.Addr = rset[4]
            newCust.PhoneNo = rset[5]

            return newCust #LOGIN

    def _AppendNewCustInfo(self) -> Cust:
        szNewCust = Cust

        self.cursor.execute("{CALL PQ_NEW_CUSTNO}")
        rset = self.cursor.fetchone()
        szNewCust.CustNo = rset[0]

        while True:
            szNewCust.FName = input('Please input your first name: ')
            if bool(szNewCust.FName):
                break
            print('First name cannot be empty!\n')

        while True:
            szNewCust.LName = input('Please input your last name: ')
            if bool(szNewCust.LName):
                break
            print('Last name cannot be empty!\n')

        while True:
            szNewCust.City = input('Please input your city: ')
            if bool(szNewCust.City):
                break
            print('City cannot be empty!\n')

        while True:
            szNewCust.Addr = input('Please input your address: ')
            if bool(szNewCust.Addr):
                break
            print('Address cannot be empty!\n')

        while True:
            szNewCust.PhoneNo = input('Please input your phone number: ')
            if bool(szNewCust.PhoneNo):
                break
            print('Phone number cannot be empty!\n')

        args = (szNewCust.CustNo, szNewCust.FName, szNewCust.LName, szNewCust.City, szNewCust.Addr, szNewCust.PhoneNo)
        self.cursor.execute("{CALL PQ_INSERT_CUSTOMER(?,?,?,?,?,?)}", args)
        self.cnxn.commit()

        return szNewCust #APPENDNEWCUST
    
    def ModifyCustomerInfo(self, cust):
        args = (cust.CustNo, cust.FName, cust.LName, cust.City, cust.Addr, cust.PhoneNo)
        self.cursor.execute("{CALL PQ_UPDATE_CUSTOMER(?,?,?,?,?,?)}", args) 
        self.cnxn.commit() #MODIFYCUSTOMER

    def _DeleteCustomerInfo(self, custNo):
        self.cursor.execute("{CALL PQ_DELETE_CUSTOMER(?)}", custNo)
        self.cnxn.commit() #DELETECUSTOMER

    def ViewCustomerList(self):
        self.cursor.execute("SELECT * FROM CUSTOMERS")
        rows = self.cursor.fetchall()
        
        print('CID'.ljust(10, ' ') + 'First Name'.ljust(30, ' ') + 'Last Name'.ljust(30, ' ') + 'City'.ljust(30, ' ') + 'Address'.ljust(30, ' ') + 'PhoneNo'.ljust(12, ' '))
        print('---'.ljust(10, ' ') + '----------'.ljust(30, ' ') + '---------'.ljust(30, ' ') + '----'.ljust(30, ' ') + '-------'.ljust(30, ' ') + '-------'.ljust(12, ' '))
        for row in rows:
            print(str(row[0]).ljust(10, ' ') + row[1].ljust(30, ' ') + row[2].ljust(30, ' ') + row[3].ljust(30, ' ') + row[4].ljust(30, ' ') + row[5].ljust(12, ' '))
        print() #VIEWCUSTOMERLIST
        
    def _AppendNewOrderInfo(self, custNo) -> Order:
        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        szNewOrder = Order

        self.cursor.execute("{CALL PQ_GET_NEW_ORDERID}")
        rset = self.cursor.fetchone()
        szNewOrder.OrderID = rset[0]
        szNewOrder.CustNo = custNo
        szNewOrder.Date = date.today().strftime("%d/%m/%Y")
    
        while True:
            szNewOrder.Product = input('Product: ')
            if bool(szNewOrder.Product):
                break
            print('Product cannot be empty!\n')
    
        while True:
            price = input('Price: ')
            if bool(price) & isfloat(price):
                szNewOrder.Price = float(price)
                break
            print('Price cannot be empty!\n')
    
        while True:
            quantity = input('Quantity: ')
            if bool(quantity) & quantity.isnumeric():
                szNewOrder.Quantity = int(quantity)
                break
            print('Product cannot be empty!\n')

        args = (szNewOrder.OrderID, szNewOrder.CustNo, szNewOrder.Date, szNewOrder.Product, szNewOrder.Price, szNewOrder.Quantity)
        self.cursor.execute("{CALL PQ_INSERT_ORDER(?,?,?,?,?,?)}", args)
        self.cnxn.commit()

        return szNewOrder #APPENDNEWORDER

    def _ModifyOrderInfo(self, Order):
        args = (Order.OrderId, Order.Product, Order.Price, Order.Quantity)
        self.cursor.execute("{CALL PQ_UPDATE_ORDER(?,?,?,?,?,?)}", args) 
        self.cnxn.commit() #MODIFYORDER

    def _DeleteOrder(self, orderId):
        self.cursor.execute("{CALL PQ_DELETE_CUSTOMER(?)}", orderId) #DELETEORDER

    def _ViewOrderList(self):
        self.cursor.execute("SELECT * FROM ORDERHISTORY")
        rows = self.cursor.fetchall()
        
        print('OrderId'.ljust(10, ' ') + 'Cust Id'.ljust(10, ' ') + 'Date'.ljust(30, ' ') + 'Product'.ljust(20, ' ') + 'Price'.ljust(10, ' ') + 'Quantity'.ljust(10, ' '), 'Total'.ljust(10, ' '))
        print('-------'.ljust(10, ' ') + '-------'.ljust(10, ' ') + '----'.ljust(30, ' ') + '-------'.ljust(20, ' ') + '-----'.ljust(10, ' ') + '--------'.ljust(10, ' '), '-----'.ljust(10, ' '))
        for row in rows:
            tot = row[4] * row[5]
            print(str(row[0]).ljust(10, ' ') +  str(row[1]).ljust(10, ' ') +  row[2].ljust(30, ' ') +  row[3].ljust(20, ' ') + "{:.2f}".format(row[4]).ljust(10, ' ') + str(row[5]).ljust(12, ' ') + "{:.2f}".format(tot).ljust(10, ' '))
        print() #VIEWORDERLIST
        
    def _FindOrder(self, orderId, custNo):
        args = (orderId, custNo)
        self.cursor.execute("{CALL PQ_GET_ORDER(?, ?)}", args)
        rset = self.cursor.fetchone()
        if rset is None:
            print('No such order id\n')
            return None
        else:
            Message._Message('Successfully found order', 2)
            newOrder = Order()
            newOrder.OrderID = rset[0]
            newOrder.CustNo = rset[1]
            newOrder.Date = rset[2]
            newOrder.Product = rset[3]
            newOrder.Price = rset[4]
            newOrder.Quantity = rset[5]

            return newOrder #FINDORDER