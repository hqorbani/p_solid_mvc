# 3- functions can be passed to other functions (higher-order functions)

def hi(name , family):
    return f"hello {name} {family}..."

# havij = "livan"
# print(hi(havij))

def message(havij , name , f):
    # name = "Hamid"
    # f = "barati"
    return havij(name , f)

print(message(hi , "hamzeh", "Qorbani"))

