from datetime import date


class Data:

    def __init__(self):
        self.data = date.today*()

    def formatada(self):

        self.data = '{}/{}/{}' .format(self.data.day, self.data.month, self.data.year)
        print(self.data)


d = Data() 
d.formadata()

