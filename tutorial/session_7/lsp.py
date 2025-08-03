class Drink:
    def get_temperature(self):
        return 'cold'
class Tea(Drink):
    def get_temperature(self):
        return 'hot'
class Juice(Drink):
    def get_temperature(self):
        return 'very cold'
    
dj = Juice()
print(dj.get_temperature())