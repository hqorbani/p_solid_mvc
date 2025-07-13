def study_plan_generator(grades, target='konkur'):
    
    def evaluate_level(score):
        if score < 50:
            return 'poor'
        elif score < 75:
            return 'average'
        else:
            return 'good'
    
    def suggest_strategy(level):
        def for_final_exam():
            if level == 'poor':
                return 'Comprehensive review + Practice with basic questions'
            elif level == 'average':
                return 'Practice questions + Review of key points'
            else:
                return 'Quick review of important concepts'
        
        def for_konkur():
            if level == 'poor':
                return 'Thorough textbook review + Fundamental practice questions'
            elif level == 'average':
                return 'Focus on frequently asked questions'
            else:
                return 'Review of challenging questions'
        
        if target == 'konkur':
            return for_konkur()
        else:
            return for_final_exam()

    plan = {}
    for subject, score in grades.items():
        level = evaluate_level(score)
        strategy = suggest_strategy(level)
        plan[subject] = f"{level}: {strategy}"

    return plan

target = 'konkur'
grades = {
    'riazi': 78,
    'zist': 45,
    'phizik': 62,
    'shimi': 83
}
plans = study_plan_generator(grades, target)
for grade , plan in plans.items():
    print(grade , plan)
