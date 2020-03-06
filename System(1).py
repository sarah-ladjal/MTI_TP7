import sys
import platform
#Classe Widget.
class Widget:
  def paint(self):
    pass
  pass
#Classe Boutton hérite la Classe Widget.
class Button(Widget):
  def paint(self):
    pass
  pass
#Classe Edit hérite la Classe Widget.
class Edit(Widget):
  def paint(self):
    pass
  pass
#Classe WinButton hérite la Classe Button.
class WinButton(Button):
  def paint(self):
    print("Vous avais Choisir GUI pour un bouton Windows.")
    pass
  pass
#Classe LinuxButton hérite la Classe Button.
class LinuxButton(Button):
  def paint(self):
    print("Vous avais Choisir GUI pour un bouton Linux.")
    pass
  pass
#Classe WinEdit hérite la Classe Edit.
class WinEdit(Edit):
  def paint(self):
    print("Vous avais Choisir GUI pour un Edit Windows.")
    pass
  pass
#Classe LinuxEdit hérite la classe Edit.
class LinuxEdit(Edit):
  print("Vous avais Choisir GUI pour un Edit Linux.")
  def paint(self):
    pass
  pass
#Classe GuiFactory.
class GuiFactory:
  def createGui(Gui):
    pass
  pass
#Classe WinGuiFactory hérite la classe GuiFactory.
class WinGuiFactory:
  def createGui(Gui):
    if Gui=="Windows Button GUI":
      return WinButton()
    elif Gui=="Windows Edit GUI":
      return WinEdit()
    else :
      print("Bad Creation GUI",Gui)
    pass
  pass
#Classe LinuxGuiFactory hérite la classe GuiFactory.
class LinuxGuiFactory:
  def createGui(Gui):
    if Gui=="Linux Button GUI":
      return LinuxButton()
    elif Gui=="Linux Edit GUI":
      return LinuxButton()
    else :
      print("Bad Creation GUI",Gui)
    pass
  pass
if __name__=="__main__":
  print("\t******** Programme de GUI d'un système d'exploitation ************")
  print("Chosier parmi les GUI Suivant :")
  print("1)- pour le GUI de Button Windows.")
  print("2)- pour le GUI de Edit Windows.")
  print("3)- pour le GUI de Button Linux.")
  print("4)- pour le GUI de Edit Linux.")
  nombre = int(input("Entrer Votre Choix : "))
  if nombre==1:
    system_exploi = WinGuiFactory.createGui("Windows Button GUI")
    system_exploi.paint()
    pass
  elif nombre==2:
    system_exploi = WinGuiFactory.createGui("Windows Edit GUI")
    system_exploi.paint()
    pass
  elif nombre==3:
    system_exploi = WinGuiFactory.createGui("Linux Button GUI")
    system_exploi.paint()
    pass
  elif nombre==4:
    system_exploi = WinGuiFactory.createGui("Linux Edit GUI")
    system_exploi.paint()
    pass
  else:
    print()
  

