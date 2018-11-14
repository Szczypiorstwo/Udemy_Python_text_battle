import random


class Enemy:
    # atkl = 60
    # atkh = 80

    hp = 200

#initialisation function
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("The attack is", self.atkl)

    def getHp(self):
        print("The Hp is", self.hp)



# enemy1 = Enemy()
#with usage of initialization function
enemy1 = Enemy(40, 67)
enemy1.getAtk()
enemy1.getHp()
# enemy2 = Enemy()
enemy2 = Enemy(65, 80)
enemy2.getAtk()
enemy2.getHp()

'''
playerhp = 250
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("The enemy strikes for", dmg, "damage points. Current player health points is:", playerhp)

### breaking the while loop when we have 30 in this way:
    # if playerhp == 30:
    #
    #     print("You have low health. You've been teleported to the nearest inn.")
    #     break
###or the other way:

    if playerhp > 30:
         continue

    print("You have low health. You've been teleported to the nearest inn.")
    break

'''