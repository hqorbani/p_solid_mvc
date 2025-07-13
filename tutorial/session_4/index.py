from advisor import StudyAdvisor
target = 'final_exam'
grades = {
    'riazi': 78,
    'zist': 45,
    'phizik': 62,
    'shimi': 83
}


advisor = StudyAdvisor(target)
reslut = advisor(grades)
print("target:",target)
for subject , message in reslut.items():
    print(f"{subject}: {message}")