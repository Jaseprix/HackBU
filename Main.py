import random
import time

print("Welcome to the Valentine's Day date generator!")
time.sleep(1)

class User():

  def __init__(self):
    name = input("Please enter your name. ")
    age = int(input("Please enter your age. "))
    while True:
      gender = input("Please enter your gender. (M/F) ").lower()
      if gender == "m" or gender == "f":
        break
      else:
        print("Please select a presented option. ")
        continue
    self.name = name
    self.age = age
    self.gender = gender

  def orientation(self):
    while True:
      global ori
      ori = input("Please select the letter of your sexual orientation: S(straight)/G(gay)/B(bisexual)/A(asexual)/P(pansexual) ").lower()
      if ori == "s":
        orientation = "Straight"
        return "Straight"
      elif ori == "g":
        orientation = "Gay"
        return "Gay"
      elif ori == "b":
        orientation = "bisexual"
        return "Bisexual"
      elif ori == "a":
        orientation = "Asexual"
        return "Asexual"
      elif ori == "p":
        orientation = "Pansexual"
        return "Pansexual"
      else:
        print("ERR: Please input a valid letter. ")
        continue

  def bio(self):
    print(
      f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}\n Orientation: {orientation}"
    )

User1 = User()
User1.orientation()

class Bots():

  def __init__(self):
    names = ["Thomas", "Jaron", "Shawn", "Jayson", "Colin", "Abigail", "Bill", "Max", "George"]
    ages = [18, 19, 20, 21, 22, 23, 24, 25]
    gender = ["Female", "Male"]
    orientation = ["Straight", "Gay", "Bisexual", "Asexual"]
    self.name = random.choice(names)
    self.age = random.choice(ages)
    self.gender = random.choice(gender)
    self.orientation = random.choice(orientation)

  def __repr__(self):
    return f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}\n Orientation: {self.orientation}\n"

Bot1 = Bots()
Bot2 = Bots()
Bot3 = Bots()
Bot4 = Bots()
Bot5 = Bots()
Bot6 = Bots()
Bot7 = Bots()
Bot8 = Bots()
Bot9 = Bots()
Bot10 = Bots()
Bot11 = Bots()
Bot12 = Bots()
Bot13 = Bots()
Bot14 = Bots()
Bot15 = Bots()

botlist = [Bot1, Bot2, Bot3, Bot4, Bot5, Bot6, Bot7, Bot8, Bot9, Bot10, Bot11, Bot12, Bot13, Bot14, Bot15]

time.sleep(1)

if ori == "s" and User1.gender == "m": 
  for x in botlist:
    if x.gender == "Female" and x.orientation != "Gay":
      print(f"There's a match! Your match is:\n{x}")
      break
if ori == "s" and User1.gender == "f":
  for x in botlist:
    if x.gender == "Male" and x.orientation != "Gay":
      print(f"There's a match! Your match is:\n{x}")
      break
if ori == "b" or ori == "a" or ori == "p" and User1.gender == "f":
  for x in botlist:
    if x.gender == "Male" and x.orientation != "Gay":
      print(f"There's a match! Your match is:\n{x}")
      break
elif ori == "b" or ori == "a" or ori == "p" and User1.gender == "m":
  for x in botlist:
    if x.gender == "Male" and x.orientation != "Straight":
      print(f"There's a match! Your match is:\n{x}")
      break
if ori == "g" and User1.gender == "m":
  for x in botlist:
    if x.gender == "Male" and x.orientation != "Straight":
      print(f"There's a match! Your match is:\n{x}")
      break
if ori == "g" and User1.gender == "f":
  for x in botlist:
    if x.gender == "Female" and x.orientation != "Straight":
      print(f"There's a match! Your match is:\n{x}")
      break

input("Would you like to explore potential dates with your match? \nPress Enter to continue. \n")

time.sleep(1)

restaurant = [
    "Five Guys",
    "Olive Garden",
    "Red Lobster",
    "Nirchi's Pizza",
    "Chipotle",
    "Social on State",
    "Little Venice Restaurant",
    "Lost Dog Café & Lounge",
    "Pho Nhu Y Restaurant",
    "Hacienda Mexican Restaurant",
    "Texas Roadhouse",
    "P S Restaurant",
    "The Shop",
    "Tully's"]
  
bar = [
    "Abel's Pub",
    "The Ale House",
    "Coppertop Tavern",
    "Irish Kevins",
    "Sach's Tee House",
    "Johnnie's Tavern",
    "Sliderz Bar & Grill",
    "Beer Tree"]
  
mall = [
    "Binghamton Plaza",
    "Vestal Plaza",
    "Riverside Plaza",
    "Oakdale Mall",
    "Town Square",
    "Northgate Plaza",
    "Campus Plaza",
    "Parkway Plaza",
    "Westover Plaza"]
  
museum = [
    "BU Art Museum",
    "Bundy Museum of History and Art",
    "Roberson Museum and Science Center",
    "Endicott History and Heritage Center",
    "Vestal Museum",
    "Phelps Mansion Museum",
    "TechWorks!",
    "Broome County Historical Society",
    "Rockbottom Dam Firefighter's Memorial",
    "Susquehanna County Historical Society"]
  
movies = [
    "Horror/Thriller",
    "Comedy",
    "Romance",
    "Action",
    "Documentary",
    "Indie",
    "Sci-fi",
    "Drama",
    "Western",
    "Animation",
    "Superhero"]
  
outdoors = [
    "BU Nature Preserve",
    "Lake Liberman",
    "Finch Hollow Nautre Center",
    "King Nautre Preserve",
    "Woodbourne Forest And Wildlife Preserve",
    "Wildwood Nature Resreve",
    "Oakley Corners State Forest",
    "Logan Hill Nature Preserve",
    "The Rail Trail",
    "Owego Riverwalk",
    "Vestal Rail Trail",
    "Finger Lakes Trail",
    "Chenango River Walk",
    "Wittman Dam",
    "abbott Loop",
    "Aqua-Terra Wilderness Area",
    "Eldridge Wilderness Trail",
    "Park"]

class UserLocation():

  def __init__(self):
    resorbar = input("Would you prefer a restaurant or a bar? (Enter r/b). ").lower().strip()
    while True:
      if resorbar == "r":
        print(f"Your date location is: {random.choice(restaurant)}!")
        break
      elif resorbar == "b":
        print(f"Your date location is: {random.choice(bar)})!")
        break
      elif resorbar != "b" or resorbar != "r":
        print("Please input r or b. ")
        continue
    more = input("Would you like to explore other options? (y/n) ")
    if more == "y":
      mallormus = input("Would you prefer a mall or a museum? (Enter mall/mus). ").lower().strip()
      while True:
        if mallormus == "mall":
          print(f"Your date location is: {random.choice(mall)}!")
          break
        elif mallormus == "mus":
          print(f"Your date location is: {random.choice(museum)})!")
          break
        elif mallormus != "mall" or mallormus != "mus":
          print("Please input mall or mus. ")
          continue
      more2 = input("Would you like to explore other options? (y/n) ")
      if more2 == "y":
        moro = input("Would you prefer movies or outdoors? (Enter m/o). ").lower().strip()
        while True:
          if moro == "m":
            print(f"Your date genre is: {random.choice(movies)}!")
            break
          elif moro == "o":
            print(f"Your date location is: {random.choice(outdoors)})!")
            break
          elif moro != "m" or moro != "o":
            print("Please input m or o. ")
            continue
      elif more2 == "n":
        pass
    elif more == "n":
      pass
        

UserL = UserLocation()

print("\nYour date and match are complete! Take your pick of location and enjoy your Valentine's.")

