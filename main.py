import waifu
import player
import random

player_name1 = input("Entrez votre nom d'invocateur Joueur 1 : ")
player_name2 = input("Entrez votre nom d'invocateur Joueur 1 : ")

# Initialiser les joueurs
p1 = player.Player(player_name1)
p2 = player.Player(player_name2)

# Demander waifus du joueur 1
for i in range(5):
    waifu_p1 = input(f"Veuillez saisir le nom de vos Waifus, {p1.get_name()} : ")
    waifu_p1 = waifu.Waifu(waifu_p1, random.randint(1, 100))
    p1.add_waifu(waifu_p1)
    waifu_p1.get_waifus_list().append(waifu_p1)

# Demander waifus du joueur 2
for i in range(5):
    waifu_p2 = input(f"Veuillez saisir le nom de vos Waifus, {p2.get_name()} : ")
    waifu_p2 = waifu.Waifu(waifu_p2, random.randint(1, 100))
    p2.add_waifu(waifu_p2)
    waifu_p2.get_waifus_list().append(waifu_p2)

# Debug verifier si waifus snt bien là
print("Waifus P1 :", p1.get_waifus())
print("Waifus P2 :", p2.get_waifus())

# GAME STARTO
while len(p1.get_waifus()) or len(p2.get_waifus()) == 0:
    print("---------WAIFU P1----------\n")
    for i in range(len(p1.get_waifus())):
        print(p1.get_specefic_desk(i).get_name(), "(", p1.get_specefic_desk(i).get_points(), ")", ":", i)
    p1_pick = int(input(f"A toi de jouer, {p1.get_name()}"))
    p1_pick_object = p1.get_specefic_desk(p1_pick)
    print("---------FIN WAIFU P1----------\n")

    # Joueur 2
    print("---------WAIFU P2----------\n")
    for i in range(len(p1.get_waifus())):
        print(p1.get_specefic_desk(i).get_name(), "(", p1.get_specefic_desk(i).get_points(), ")", ":", i)
    print("---------FIN WAIFU P2----------\n")
    
    # Je demande au joueur de rentrer un nombre qui désignera l'element n de la liste de waifus waifus[n]
    p2_pick = int(input(f"A toi de jouer, {p2.get_name()}"))
    # Maintenant que j'ai ça la méthode get_specific... va me retourner la liste waifus[n] à savoir ici waifus[p2_pick] p2_pick étant un chiffre
    p2_pick_object = p2.get_specefic_desk(p2_pick)

    # Si le joueur 1 gagne la manche
    if p1_pick_object.get_points() > p2_pick_object.get_points():
        # instructions
        p1.remove_waifu(p1_pick_object)
        print("Aïe |", p1.get_name(), "a perdu la manche !", p1_pick_object.get_name(), "est hors jeu !")
        print("Waifu restantes de", p1.get_name())
        for i in range(len(p1.get_waifus())):
            print(p1.get_specefic_desk(i).get_name(), "(", p1.get_specefic_desk(i).get_points(), ")", ":", i)
        print("---------FIN WAIFU P1----------\n")
    # Si le joueur 2 gagne la manche
    if p2_pick_object.get_points() > p1_pick_object.get_points():
        # instructions
        p2.remove_waifu(p2_pick_object)
        print("Aïe |", p2.get_name(), "a perdu la manche !", p2_pick_object.get_name(), "est hors jeu !")
        print("Waifu restantes de", p2.get_name())
        for i in range(len(p2.get_waifus())):
            print(p2.get_specefic_desk(i).get_name(), "(", p1.get_specefic_desk(i).get_points(), ")", ":", i)
        print("---------FIN WAIFU P2----------\n")

    if len(p1.get_waifus()) == 0:
        print(p2.get_name(), "a gagné la partie ! GG à tous")
    elif len(p2.get_waifus()) == 0:
        print(p1.get_name(), "a gagné la partie ! GG à tous")







