# 5- functions can capture local state (lexical closure):
def person(name , age):

    def adult():
        return f'{name} is adult...'
    
    def kid():
        return f'{name} is bache...'
    if age > 12:
        return adult
    else:
        return kid

result = person('Hamzeh' , 26 )()
print(result)
