class StudyAdvisor:
    def __init__(self , target):
        self.target = target
    
    def __call__(self, grades:dict):
        plan = {}
        for subject , score in grades.items():
            level = self.evaluate_level(score)
            strategy = self.suggest_strategy(level)
            plan[subject] = f'{level}: {strategy}'
        return plan
    
    def evaluate_level(self , score):
        if score < 50:
            return 'poor'
        elif score < 75:
            return 'average'
        else:
            return 'good'
    
    def suggest_strategy(self , level):
        if self.target == 'konkur':
           strategies = {
               'poor' : 'Thorough textbook review + Fundamental practice questions',
               'average' : 'Focus on frequently asked questions',
               'good' : 'Review of challenging questions'
           } 
        else:
            strategies = {
                'poor' : 'Comprehensive review + Practice with basic questions',
                'average' : 'Practice questions + Review of key points',
                'good' : 'Quick review of important concepts'
            }
        return strategies[level]


