# a sample of using * in func parameters
# def average_score(*score):
#     return sum(score) / len(score)

# print(average_score(80,90,45,21))

# a sample of using ** in func parameters
def student_info(**std_info):
    for key , value in std_info.items():
        print(key , value)

student_info(name='hamzeh' , age = 40)
