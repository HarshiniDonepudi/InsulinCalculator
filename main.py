import math
from datetime import date

today = date.today()

print('Hello, today is ' + str(today))

bs = int(input('Blood Sugar: '))
bst = int(input('Blood Sugar Target: '))
list = []
n = int(input('Enter how many times you take insulin in a day: '))

for i in range(0,n):
  dosage = float(input('Enter insulin dosage: '))
  list.append(dosage)

ttd = sum(list)
print("Total insulin dosage per day:",ttd)

insulintype = str(input('Name of Bolus Insulin being used: '))

I1 = ['Humolog','Novolog','Apidra']

if insulintype in I1:
  crcf=1500/ttd
  print("correction factor is:",crcf)
else:
  crcf=1800/ttd
  print("correction factor is:",crcf)

insamt = float((bs - bst) / (crcf))
carbs = int(input('Carbohydrates: '))
carb_ratio = int(input('Insulin to carbohydrate ratio is 1: '))
carb_crct = float((carbs / carb_ratio))

i = round((insamt + carb_crct),2)
j=math.floor(i)
if(j<= i < j+0.3):
  insulin= j
elif(j+0.3 <= i < j+0.7):
  insulin = j+0.5
elif(j+0.7 <= i <j+1):
  insulin= j+1
print('Delivering ' + str(insulin) + ' units.')

