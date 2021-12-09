try:
  yer = open("mailbox.txt")
except:
  print('ERROR 404')
  exit()

lines=yer.readlines()
nur=open('output.txt', 'w')
for line in lines:
    if 'Cyrus' in line:
      nachalo=line.find('(')
      konec=line.find(')')
      tekst=line[nachalo+7:konec]
      print(tekst)
      nur.write(tekst)
      nur.write('\n')
yer.close()
