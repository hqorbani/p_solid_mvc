#create the main function 
def study_plan_generator(grades, target='konkur'):
    
    #create a function that checks the level of grades
    def get_level(score):
        if score <= 50 :
            return 'Poor'
        elif score <= 75:
            return 'Medium'
        else:
            return 'Good' 
        
    #create a function that provides a program based on the konkur  
    def Konkur(level):
        if level == 'Poor' :
            return 'full review + test'
        elif level == 'Medium' :
            return 'review important point + test'
        else:
            return 'no need to practice'

    #create a function that provides a program based on the finel_exam 
    def finel_exam(level):
        if level == 'Poor' :
            return 'full review '
        elif level == 'Medium' :
            return 'review important point '
        else:
            return 'no need to practice'
        
    #create a dict for output display
    Plan = {}
    #craete a loop to check the input dict(grades)
    for key , value in grades.items() :
        level = get_level(value)
        if target == 'konkur':
            Plan[key] = Konkur(level)
        elif target == 'final_exam':
            Plan[key] = finel_exam(level)
        else:
            Plan[key] = 'uncertain'
    return Plan
    
#input dict    
grades = {
    'riazi' : 78,
    'zist ' : 45,
    'shimi' : 30
}

#calling the main function
Plan = study_plan_generator(grades, 'final_exam')

#print the output dict(Plan)
for key, value in Plan.items():
    print(f"{key}: {value}")




    
    
    

    