class carparking:
    def input(self,vichal_number,hours,):
        self.vn=vichal_number
        self.h=hours
    def parkingcharge(self):
        if self.h <=1:
            self.pay=self.h+3

        elif self.h >1:
            self.paybill=3+(self.h - 1) * 1.5

    def display(self):
        print('Vichal Number: ', self.vn,'hours: ',self.h,'Final Bill: ',self.paybill)
    


ob = carparking()
vichal_number=input('Enter The Vichal number: ')
hours=int(input('Enter The Housr: '))

ob.input(vichal_number,hours)
ob.parkingcharge()
ob.display()