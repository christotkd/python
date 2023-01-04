def datevalide(date):

  if len(date) != 8:
    print("La date n'est pas au bon format")
    return False

  jour = int(date[:2])
  mois = int(date[2:4])
  annee = int(date[4:])


  if jour < 1 or jour > 31:
    print("Le jour est incorrect")
    return False


  if mois < 1 or mois > 12:
    print("Le mois est incorrect")
    return False

  if annee < 1900:
    print("L'année est incorrecte")
    return False

  return True

date = input("Entrée une date : ")
if datevalide(date):
  print(date, "est une date valide")
else:
  print(date, "n'est pas une date valide")


