class Footballer:

    def __init__(self, name):
        self.name = name

    def right_foot(self):
        self.right_foot = True

    def left_foot(self):
        self.right_foot = False

    def get_info(self):
        return self.name

class Barcelona(Footballer):

    def __init__(self, name, age):
        super().__init__(name=name)
        self.age = age

    def get_info(self):
        return f'Имя: {self.name}, возраст: {self.age}'

class Bayern_Munich(Footballer):

    def __init__(self, name='Kingsley Coman'):
        super().__init__(name=name)

    def weekfoot_strong(self):
        self.five_star_weekfoot = True

    def weekfoot_low(self):
        self.five_star_weekfoot = False

if __name__ == '__main__':
    player1 = Footballer('Jordan Henderson')
    player2 = Barcelona('Gavi', 18)
    player3 = Bayern_Munich()

    players = [player1,  player2, player3]

    for player in players:
        print(player.name)

    print(player1.get_info())
    print(player2.get_info())
    player3.weekfoot_strong()
    print(player3.five_star_weekfoot)


