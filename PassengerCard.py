class Vale:

    def __init__(self, numberCard, credit=0):
        self._numberCard = numberCard
        self._credit = credit
    
    def numCard(self):
        return self._numberCard
    
    def addCredit(self):
        if self._credit >= 0:
            add = int(input('Credit: '))
            self._credit += add
    
    def verify(self):
        return f'Your Passenger Card: {self._numberCard}\nYour Credit: ${self._credit}'

class Student(Vale):

    def __init__(self, numberCard, credit):
        Vale.__init__(self, numberCard, credit)

    def payPass(self):
        if self._credit >= 0:
            #Normal Pass = $3.20
            Pass = 1.60 #Student Pass
            self._credit -= Pass
        return f'You Paid ${Pass}\nCurrent Credit: ${self._credit}'
    
class Commom(Vale):
    def __init__(self, numberCard, credit=0):
        Vale.__init__(self, numberCard, credit)
    
    def payPass(self):
        if self._credit >= 0:
            Pass = 3.20 #Normal Pass
            self._credit -= Pass
        return f'You paid ${Pass}\nCurrent Credit: ${self._credit}'

def main():
    print()
    print('Welcome to the Passenger System\nChoose Your Option\n1-Add Credit\n2-Exit')
    opt = input('Choose: ')
    if opt == '2':
        print('Turn Off!')
        exit()
    if opt not in ('1','2'):
        print('Invalid Answer.')
        exit()
    NumberCard = int(input('Number Card: '))
    Credit = int(input('Add Credit: '))
    if opt == '1':
        print()
        print('Choose Your Pass-Type\n1-Student\n2-Worker')
        print()
        op = input('Answer: ')
        if op == '1':
            Client = Vale(NumberCard, Credit)
            cStudent = Student(NumberCard, Credit)
            print(cStudent.verify())
            print()
            print('Now that you have loaded your credits, do you want to pay for your travel ticket? Y or N')
            Pay = input('Answer: ').upper()
            if Pay == 'Y':
                print(cStudent.payPass())
                print()
                print(cStudent.verify())
                print('Thank You and always come back. Remove Your Card.')
                exit()
            elif Pay == 'N':
                print('Thank you and always come back. Remove Your Card.')
                exit()
            else:
                print('Invalid Answer. Remove Your Card.')
                exit()

        elif op == '2':
            Client = Vale(NumberCard, Credit)
            Citizen = Commom(NumberCard, Credit)
            print(Citizen.verify())
            print()
            print('Now that you have loaded your credits, do you want to pay for your travel ticket? Y or N')
            Pay = input('Answer: ').upper()
            if Pay == 'Y':
                print(Citizen.payPass())
                print()
                print(Citizen.verify())
                print('Thank You and always come back. Remove Your Card.')
                exit()
            elif Pay == 'N':
                print('Thank You and always come back.')
                exit()
            else:
                print('Invalid Answer. Remove Your Card')
                exit()
    else:
        print('Invalid Answer. Remove the card.')
        exit()

main()

