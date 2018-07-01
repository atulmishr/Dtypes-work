#python strings
Atul="Welcome into the world of Bollywood"
print(Atul)

print(Atul*2)
print(Atul[1:10])
print(Atul[9:])
print(Atul + "Atul Mishra with Sanjay Kapoor")

#python Lists
Heros = ['Aamir','Salman','Ranveer','Shahid','Akshay']
print(Heros)
print(Heros[1:2])
print(Heros[2:])

Heroiens= ['Dyna','Katreena','Karishma','kareena','kirti']
print(Heros + Heroiens)
#list operations
Heros.append('Rajkumar Rao')
print(Heros)
Heroiens.insert(3,'Aalia')
print(Heroiens)
Heros.extend('Sonu sood')
print(Heros)

#deleting
players=['Ronaldo,Messi','Dhoni','jadeja','Raina']
print(players)
del players([1:3])
print(players)
