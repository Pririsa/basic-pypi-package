
class Profile:
    def __init__(self, name):
        self.name = name
        self.company = ''
        self.hobby = []
        self.art = '''           
                    ____
                    /    \
            ._.     /___/\ \
            :(_):    |6.6| \|
            \\     '.-.'  O
            \\____.-"-.____
            '----|     |--.\
                    |==[]=|  _\\_
                    \___/    /|\
                    // \\
                    //   \\
                    \\    \\  Max
                    _\\    \\__
                (___|    \__)'''

    def show_email(self):
        print(f'{self.name}@{self.company if self.company != "" else "@gmail"}.com')

    def show_myart(self):
        print( self.art)

    def show_hobby(self):
        if len(self.hobby) != 0:
            print('------my hobby-----')
            for i, h in enumerate(self.hobby, start=1):
                print(i, h)
            print('-----------')
        else:
            print('-No Hobby')

if __name__ == '__main__':
    my = Profile()
    my.company = 'company'
    my.hobby = ['youtube', 'facebook']
    print(my.name)
    my.show_email()
    my.show_myart()
    my.show_hobby()
