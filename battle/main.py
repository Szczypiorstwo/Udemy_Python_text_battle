from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

#Create black magic spells
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 125, "black")
blizzard= Spell("Blizzard", 10, 100, "black")
meteor= Spell("Meteor", 20, 200, "black")
quake= Spell("Quake", 14, 140, "black")

#Create white magic spells
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")
curaga = Spell("Curaga", 60, 3000, "white")

#Create some Items

potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Superpotion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixier", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixier", "elixer", "Fully restores party's HP/MP ", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

#Instatiate People

player_magic =[fire, thunder, blizzard, meteor, cure, cura]
enemy_magic = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]

player1 = Person("Valos:", 1450, 165, 160, 45, player_magic, player_items)
player2 = Person("Nick :", 3450, 105, 165, 45, player_magic, player_items)
player3 = Person("Robot:", 2550, 122, 150, 45, player_magic, player_items)

enemy1 = Person("Imp   ",1200, 105, 145, 25, enemy_magic, [])
enemy2 = Person("Magus ",11200, 165, 145, 25, enemy_magic, [])# empty list on magic index means no magic available []
enemy3 = Person("Imp   ",1200, 105, 145, 25, enemy_magic, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS !" + bcolors.ENDC)

while running:
    print("===================")
    print("\n\n")
    print("NAME                     HP                                                          MP")
    for player in players:
        player.get_stats()
    print("\n")

    for enemy in enemies:
        if enemy.get_hp() != 0:
            enemy.enemy_get_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action by number: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You've attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage. Enemy HP:", enemies[enemy].get_hp())

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic spell by number: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            # cost = spell.cost
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\n You don't have enough magic to do that!" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == 'black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg) + " points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item by number: ")) -1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left ..." + bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1


            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for " + str(item.prop) + bcolors.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixier":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp - i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print("\n" + bcolors.OKGREEN + item.name + "Fully restores HP/MP." + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print("\n" + bcolors.FAIL + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]


# Check if battle is over:
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

# Check if we won:
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You've won!" + bcolors.ENDC)
        running = False

# Check if Enemy won:
    elif defeated_players == 2:
        print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
        running = False

# Enemy attack phase:
    print("\n")
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            #choose attack:
            enemy_dmg = enemy.generate_damage()
            target = random.randrange(0, 3)
            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for " + str(enemy_dmg) + " points of damage.")

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(magic_dmg)

            if spell.type == 'white':
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name.replace(" ", "") + " for ", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == 'black':
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg) # player target
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg) + " points of damage to " + players[target].name.replace(":", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]

#github/nickgermaine