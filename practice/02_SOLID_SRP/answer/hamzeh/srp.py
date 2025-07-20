class LevelEvaluator:
    def evaluate(self, score):
        if score < 50:
            return 'poor'
        elif score < 75:
            return 'average'
        else:
            return 'good'

class StrategySuggester:
    def __init__(self, target):
        self.target = target

    def suggest(self, level):
        if self.target == 'konkur':
            strategies = {
                'poor': 'Thorough textbook review + Fundamental practice questions',
                'average': 'Focus on frequently asked questions',
                'good': 'Review of challenging questions'
            }
        else:
            strategies = {
                'poor': 'Comprehensive review + Practice with basic questions',
                'average': 'Practice questions + Review of key points',
                'good': 'Quick review of important concepts'
            }
        return strategies[level]

class StudyAdvisor:
    def __init__(self, target):
        self.evaluator = LevelEvaluator()
        self.suggester = StrategySuggester(target)

    def __call__(self, grades: dict):
        plan = {}
        for subject, score in grades.items():
            level = self.evaluator.evaluate(score)
            strategy = self.suggester.suggest(level)
            plan[subject] = f'{level}: {strategy}'
        return plan

advisor = StudyAdvisor('konkur')
grades = {
    'math': 70,
    'chemistry': 68,
    'physics': 85
}

study_plan = advisor(grades)
for subject, suggestion in study_plan.items():
    print(f'{subject}: {suggestion}')