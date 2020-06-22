"""x = 1
while x < 50 :
  print('Facile ! '+ str(x))
  x+=1"""

"""x=1
while x<25:
  print('*',end='')
  x+=1"""

"""for x in range(21,146):
  print(x)"""

"""for x in range(1,41):
  print('le carre de '+str(x)+' est '+str(x**2))"""

"""y=0
for x in range(21,146):
  y+= x
  print(y)"""

"""nbr = 35
fact = 1
for i in range(1, nbr+1):
  fact = fact * i
print (nbr,'! = ',fact)"""

"""nb =1
for x in range(15):
  for y in range(nb):
    print('*',end='')
  print('')
  nb+=1"""

dico = {}
rep = 'o'
while rep == 'o':
    print("Saisir un mot anglais.")
    ang = input('> ')
    print("Saisir la traduction française.")
    fr = input('> ')
    dico[ang] = fr
    print("Voulez-vous saisir une nouvelle entrée ?")
    rep = input('> ')
else:
    for k, v in dico.items():
        print(k, v)

        
