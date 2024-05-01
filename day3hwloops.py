# Question 1 

feelings = ["Excited", "Calm", "Happy", "Nervous", "Sad", "Anxious", "Witty"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(len(feelings)):
    import random
    feeling = random.choice(feelings)
    day = random.choice(days)
    
    print(f"On {day} you were feeling {feeling}")


# Question 2 

feelings = ["Excited", "Calm", "Happy", "Nervous", "Sad", "Anxious", "Witty"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time = ["morning", "afternoon", "night"]

for day in days:
    for tod in time:
        import random
        feeling = random.choice(feelings)
        print(f"On {day} {tod} you were {feeling}")




    