class Material:

    def __init__(self, name='', quantity='', date=''):
        self.name = name
        self.quantity = quantity
        self.date_out = date
        self.date_in = None

    def setData(self, name=None, quantity=None, date_out=None, date_in=None):
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if date_out is not None:
            self.date_out = date_out
        if date_in is not None:
            self.date_in = date_in

    def getData(self):
        return self.name, self.quantity, self.date_out, self.date_in

    # def updateQuantity(self, quantity):
    #     self.quantity = quantity
