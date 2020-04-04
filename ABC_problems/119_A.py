inp=input()
date=inp.split('/')
#print(date[0])
if int(date[0]) <= 2019 and int(date[1]) <= 4 and int(date[2]) <= 30:
  print('Heisei')
else:
  print('TBD')