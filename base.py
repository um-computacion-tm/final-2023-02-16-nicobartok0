class Base:

    def __init__(self, data={}):
        self.data = data

    def __repr__(self):
        return f'{self.data}'
