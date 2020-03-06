import sys
#Classe Pizza.
class Pizza:
  def getPrice(Price):
    return Price
  pass
#Classe TunaPizza hérite la classe Pizza.
class TunaPizza(Pizza):
  def getPrice(Price):
    Price = 150 # Dinar
    return Price
  pass
#Classe SimplePizza hérite la classe Pizza.
class SimplePizza(Pizza):
  def getPrice(Price):
    Price = 120 # Dinar
    return Price
  pass
#Classe MargaritaPizza hérite la classe Pizza.
class MargaritaPizza(Pizza):
  def getPrice(Price):
    Price = 250 # Dinar
    return Price
  pass
#Classe PizzaFactory.
class PizzaFactory:
  def createPizza(typePizza):
    pass
  pass
#Classe PizzeriaHoma hérite la classe PizzaFactory.
class PizzeriaHoma(PizzaFactory):
  def createPizza(typePizza):
    if typePizza =="Tuna Pizza" :
      return TunaPizza()
    elif typePizza=="Simple Pizza":
      return SimplePizza()
    else :
      print("Bad Pizza Creation ",typePizza)
      sys.exit()
    pass
  pass

#Classe PizzeriaLux hérite la classe PizzaFactory.
class PizzeriaLux(PizzaFactory):
  def createPizza(typePizza):
    if typePizza =="Margarita Pizza" :
      return MargaritaPizza()
    elif typePizza=="Simple Pizza":
      return SimplePizza()
    else :
      print("Bad Pizza Creation ",typePizza)
      sys.exit()
    pass
  pass
#Lanceur de programme.
if __name__=="__main__":
  print("\t\t\t******** Programme de prix des Pizzeria ************")
  print("Chosier parmi les Pizzeria Suivant :")
  print("1)- pour le Pizzeria Homa.")
  print("2)- pour le Pizzeria Lux.")
  nombre = int(input("Entrer Votre Choix : "))
  if nombre==1:
    for typePizza in ("Tuna Pizza","Simple Pizza"):
      pizza = PizzeriaHoma.createPizza(typePizza)
      price =  pizza.getPrice()
      print("le",typePizza,":",price,"Da")
  elif nombre==2:
      for typePizza in ("Margarita Pizza","Simple Pizza"):
        pizza = PizzeriaLux.createPizza(typePizza)
        price =  pizza.getPrice()
        print("le",typePizza,":",price,"Da")
