class Heart:
    def __init__(self,name,beat):
        self.name=name
        self.beat=beat

    def evaluate(self):
        if self.beat>=68 and self.beat<=74:
            print(f'{self.name} is healthy...')

        else:
            print(f'{self.name} is not healthy...')

    
