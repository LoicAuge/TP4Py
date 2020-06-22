"""annee =	['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
annee.remove(10)
annee.remove(11)
annee.remove(12)
print(annee)
annee.append("Octobre")
annee.append("Novembre")
annee.append("Decembre")
print(annee)"""

"""annee =	['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
annee[9] = "Octobre"
annee[10] = "Novembre"
annee[11] = "Decembre"
print(annee)"""

"""moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
print(moisDeLannee[3])
print("mars" in moisDeLannee)"""

"""age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23}
age["David"] = 22
age["Veronique"] = 21
age["Sylvie"] = 30
age["Damien"] = 37
print(age)
print(age["Sylvie"])
if 'jean' in age:
  print("Jean présent")
else:
  print("Jean absent")"""

"""club = {}
club['pierre durand']=(1986,1.72,70)
club['victor dupont']=(1987,1.89,57)
club['paul dupuis']=(1989,1.60,92)
club['jean rieux']=(1985,1.88,77)
print(club)
dateNaissSportif = club['paul dupuis'][0]
TailleSportif = club['paul dupuis'][1]
poidsSportif = club['paul dupuis'][2]
formatDonnees = 'Le sportif nommé Paul Dupuis est né en %s, sa taille est de %s m et son poids est de %s kg.'
print(formatDonnees %(dateNaissSportif,TailleSportif,poidsSportif))"""

club = {'pierre durand': (1986, 1.72, 70), 'victor dupont': (1987, 1.89, 57), 'paul dupuis': (1989, 1.6, 92), 'jean rieux': (1985, 1.88, 77)}
formatDonnees = 'Le sportif nommé %s est né en %s, sa taille est de %s m et son poids est de %s kg.'
name = input("> ")
if name in club:
  dateNaissSportif = club[name][0]
  TailleSportif = club[name][1]
  poidsSportif = club[name][2]
  print(formatDonnees %(name,dateNaissSportif,TailleSportif,poidsSportif))
else:
  print(name+" inexistant")