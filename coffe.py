print ('wecome to fast coffe')
name = input ("what is your name? ")
if name == "ben" or name == "max":
    evil = input("are you evel? ")
    deeds = input ("how meny deeds did you do? ")
    if evil == "yes" and int(deeds) > 5:
        print ("you come on in " + name)
    elif evil == "no":
        print ("good that you are not one of thos good " + name + "s")
    else:
        print ("you did do enofe good deeds")
        exit ("you are at the end of the code ")
else:
    print ("niec to meet you " + name)
print ("want do you want. 1.coffe 2.exerseso 3.black coffe 4.water")
oerder = input()
if oerder == "1" or oerder == "one" or oerder == "coffe":
 print ("ok your coffe will be here soon and your bill is 5$")
elif oerder == "2" or oerder == "to" or oerder == "exerseso":
    print ("ok your exerseso will be here soon and your bill is 10$ ")
elif oerder == "3" or oerder == "there" or oerder == "black coffe":
    print ("ok your black coffe will be here soon and you bill is 13$")
elif oerder == "4" or oerder == "for" or oerder == "water":
    print ("ok your wanter will be here soon and your bill is 3$")

