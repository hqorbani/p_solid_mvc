# open close principle
class LevelEvaluator:
    def evaluate(self, score):
        if score < 50:
            return 'poor'
        elif score < 75:
            return 'average'
        else:
            return 'good'

class StrategyProvider:
    def get_strategy(self, level):
        raise NotImplementedError

class KonkurStrategy(StrategyProvider):
    def get_strategy(self, level):
        strategies = {
            'poor': 'Thorough textbook review + Fundamental practice questions',
            'average': 'Focus on frequently asked questions',
            'good': 'Review of challenging questions'
        }
        return strategies[level]

class FinalExamStrategy(StrategyProvider):
    def get_strategy(self, level):
        strategies = {
            'poor': 'Comprehensive review + Practice with basic questions',
            'average': 'Practice questions + Review of key points',
            'good': 'Quick review of important concepts'
        }
        return strategies[level]

class BeforeNightExamStrategy(StrategyProvider):
    def get_strategy(self, level):
        strategies = {
            'poor': '2a + test',
            'average': '2a',
            'good': '2a + sleep'
        }
        return strategies[level]

class StudyAdvisor:
    def __init__(self, evaluator: LevelEvaluator, strategy_provider: StrategyProvider):
        self.evaluator = evaluator
        self.strategy_provider = strategy_provider

    def __call__(self, grades: dict):
        plan = {}
        for subject, score in grades.items():
            level = self.evaluator.evaluate(score)
            strategy = self.strategy_provider.get_strategy(level)
            plan[subject] = f'{level}: {strategy}'
        return plan

grades = {
    "math": 65,
    "physics": 48,
    "chemistry": 80
}

evaluator = LevelEvaluator()
target = 'konkur'
if target == 'konkur':
# حالت اول: آمادگی برای کنکور
    strategy = KonkurStrategy()
elif target == 'general_exam':
    strategy = FinalExamStrategy()
advisor = StudyAdvisor(evaluator, strategy)
konkur_plan = advisor(grades)
print("Konkur Study Plan:")
for subject, advice in konkur_plan.items():
    print(f"{subject}: {advice}")