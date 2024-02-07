steps_daily = int(input('Enter no.of steps daily: '))
distance_walked = int(input('Enter distance walked in kms: '))
calories_burnt = distance_walked * 60
steps_week = steps_daily * 7
distance_month = distance_walked * 30
print('Calories burnt',calories_burnt)
print('Steps per week',steps_week)
print('Distance covered in month',distance_month)