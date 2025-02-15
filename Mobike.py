class mobike:
    def input(self,Bike_number,phone_number,Customer_name,day):
        self.b=Bike_number
        self.p=phone_number
        self.cn=Customer_name
        self.d=day

    def charges(self):
        if self.d <= 5:
            self.your_payment=self.d * 500

        elif self.d > 5 and self.d <= 10:
            self.your_payment = 2500+ (self.d - 5 )* 400

        elif self.d > 10: 
            self.your_payment = 4500+(self.d - 10 ) * 200

        
        
    def display(self):
        print('Bike Number',self.b , 'Phone Number',self.p , 'Name', self.cn , ' day of rent', self.d, 'Your Final Payment is ', self.your_payment)


ob= mobike()

bike_number= input('Enter The bike Number: ')
phone_number=int(input('Enter The Phone NUmber: '))
Customer_name=  input('Enter The Name: ')
day=int(input('Enter The Bike Rent Day: '))

ob.input(bike_number,phone_number, Customer_name, day)
ob.charges()
ob.display()
