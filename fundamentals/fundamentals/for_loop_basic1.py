#Basic
for i in range(0,150):
  print(i)

#Multiples of Five
for a in range(5,1000,5):
  print(a)

#Counting, the Dojo Way
for dojo in range(1,100):
  if dojo % 10 == 0:
    print('Coding Dojo')
    continue
  elif dojo % 5 == 0:
    print('Coding')
  else:
    print(dojo)

#Whoa. That Sucker's Huge
oddNumberSum = 0
for i in range(0,500000):
  if i%2 != 0:
    oddNumberSum += i
print(oddNumberSum)

#countdown by fours
for i in range(2018,0,-4):
  print(i)

#Flexible Counter
lowNum = 5
highNum = 500
mult = 4
for i in range(lowNum, highNum):
  if i % mult == 0:
    print(i)
