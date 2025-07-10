# 4- functions can be nested (inner and outer functions):
def person(age):

    def adult(name):
        return f'{name} is adult...'
    
    def kid(name):
        return f'{name} is kid...'
    if age > 12:
        return adult
    else:
        return kid

p = person(4)

print(p('Hamzeh'))
