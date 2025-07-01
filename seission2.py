pupil1 = {"name": "mohamed", "grades": [80, 90, 100]}
pupil2 = {"name": "ahmed", "grades": [75, 88, 92]}
pupil3 = {"name": "ayman", "grades": [60, 70 ,55]}

for student in (pupil1, pupil2, pupil3):
    average = sum(student["grades"]) /len (student["grades"])
    print(student["name"], "average grade:", average)