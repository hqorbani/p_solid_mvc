# 2- functions can be stored in data structures:
# names = ["hamze" , "ali" , "fatemeh" , 154 , ]
# print(names[2])
def hi(name):
    return f"hello {name}..."

def intro(name):
    return f"Dear {name} , I'm your bot "

methods = [hi , intro]
# print(methods[0]("Mina"))
for method in methods:
    print(method("Arefeh"))


    