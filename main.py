# Class -> 40pts
class Monster:
    def __init__(self, hp=100, points=0):
        self.hp = hp
        self.points = points

    def get_hp(self):
        return self.hp

    def lose_hp(self):
        if self.hp > 0:
            self.hp -= 25

    def get_points(self):
        return self.points


def main():
    # Assignment Statements = 3pts
    hp = 100
    score = 0
    lives = 1
    items = []
    turn = False

    caterpillar = Monster(100, 5)
    flowers = Monster(125, 10)
    hatter = Monster(150, 15)
    jabberwocky = Monster(175, 20)
    red_queen = Monster(200, 25)

    # Print Statement = 2pts
    print("Cheshire Cat: “To get through Wonderland you will have to answer riddles and defeat bosses.\nYou will have 3"
          " chances to answer each riddle. Answering riddles and defeating bosses before they defeat you gives you "
          "Cheshire Smiles.\nCollect 100 of these smiles and a key from the Red Queen to return home.“")

    user_input = input("Would you like to continue? Y/N?")

    # If statement = 5pts
    if user_input == "N":
        print("Thank you for your time, you are now stuck here forever ( ͡☉ ͜ʖ ͡☉)")
    else:
        # While loop = 15pts
        while lives != 0 or "key" not in items:
            player_move = input("Cheshire Cat: “Alice? ALiceeeE? Hello? ALICE? Oh there we go! Hello Alice "
                                "you had quite the fall didn’t you?“ "
                                "I’ll let you rest a moment, come find me when you are ready.\nWelcome to Wonderland! "
                                "It seems that dreaded Cat has disappeared and left you alone in an unfamiliar, "
                                "unremarkable, unhelpful clearing.\nThere is a single path ahead of you behind you and "
                                "around the clearing is a menacing darkness-flooded forest.\nTo your left, in a small "
                                "patch of butter-cups, there is a silver can. Maybe you should check it out (^_−)☆.“ "
                                "\nEnter E to explore and to move to the next area.").upper()
            # Nested while loop = 20pts
            while player_move is not "E" or "F":
                if player_move == "E":
                    print("You picked up bug spray! If only there were some bugs around...(☭ ͜ʖ ☭)\n")
                    items.append("bug spray")
                    break
                else:
                    print("Please put in a valid move.")
                    continue

            print(
                "Cheshire Cat: “There you are Alice, come come there is no time  to waste! You want to get home don’t "
                "you?\nWell I am sorry to say but no one really wants you to leave, especially  not a certain raging red"
                " royal.\nThe only way you are getting home is through the door in her castle and guess who has to key"
                " (；・∀・)? "
                "\nOn top of that word on the wood is that there is a bounty out for your HEAD. \nOh but fret not dear"
                " Alice, I am here to help!\nThe best and only path to the castle is up ahead, there might be dangers "
                "ahead so keep your wits about you…\n"
                "\n…"
                "\n…"
                "\n…"
                "\n\n(=ↀωↀ=)\n"
                "\nHmm? Where are your wits? Do you have none child!? How unfortunate! \nTell you what we are going to"
                " find some for you: solve this riddle and your wits should be right up and running!”")

            riddle_answer = input("Riddle: The alphabet goes from A-Z. What goes from Z-A?").lower()

            # Nested if statement = 10pts
            if riddle_answer == "zebra":
                player_input = input(
                    "“Well done Alice! Seeing your wits back really puts a smile on this old cats face!"
                    " Oh no a few smiles have fallen right off my face, \nmind picking those up, they might "
                    "come in handy later. \nPress P to pick up smiles.\n”")
                if player_input == "P":
                    print("You pick up the smiles and tuck them into your apron and the jubilant cat leads "
                          "you down the path.\n""Suddenly, your vision begins to dim. Fog? No it is more like smoke"
                          " –cough- cough- oh no it seems that silly cat has run off!"
                          "\nA voice cuts through the smoke…\n")
                score += 5

            print("Caterpillar: Whooooooo are youuuuuuuuu?\n")
            print("A creeping callous caterpillar crawls through the caustic cloud, oh no Alice this doesn’t look good."
                  " You must have SOMETHING to help you!\n")
            while caterpillar.get_hp() > 0:
                player_input = input("Press 1 to use bug spray ")
                if player_input == "1" and turn is False:
                    caterpillar.lose_hp()
                    print("Caterpillar HP: ", caterpillar.get_hp())
                    print("Alice HP: ", hp)
                    turn = not turn
                if turn is True:
                    print("Caterpillar attacks and does -10 damage.")
                    hp -= 10
                    turn = not turn
            if caterpillar.get_hp() == 0:
                hp += 30
                score += caterpillar.get_points()
                player_input = input(
                    "Caterpillar: “-cough- -cough- youuuu winnnn thiss rounddd ( ͠° ͟ʖ ͡°) \n\nDefeated, the caterpillar"
                    " retreats off the path and into the dark forest, he left something behind. His pipe and something "
                    "else…are those smiles?"
                    "\nWell, now that the pipe isn’t in use you have a better view of your surroundings. "
                    "The path ahead is a slightly more narrow and a hair more winding;\nit is hard to see what is "
                    "past the bend. "
                    "A trash bin with eyes is standing next to a tree; it is staring at your empty bug spray.\n"
                    "You have no use for it anymore so you drop it in; satisfied the trash bin hops away. There is soft"
                    "singing in the distance, but maybe you should \nEXPLORE a bit first."
                    "\nPress E to explore.").upper()
                items.remove("bug spray")
                if player_input == "E":
                    # List = 15pts
                    items.append("pipe")
                    player_input = input("You found the caterpillar's pipe! "
                                         "As you pick up the pipe you feel a weight on your head…"
                                         "\n\nCheshire Cat: “OH ALICE! I was so WORRIED, did that mean caterpillar hurt you? Here let me "
                                         "restore your hit points! Your HP is now 100!”"
                                         "\nYou seem shaken up Alice! Hey where did your wits go!? It is okay I have "
                                         "another riddle that will wits you right up!:\n"
                                         "\n“This is something black and white "
                                         "\n But it’s not an old TV"
                                         "\n It’s a type of animal"
                                         "\n That starts with the letter Z"
                                         "\n What am I?”").lower()
                    if player_input == "zebra":
                        score += 5
                        print("“Wow you are so smart, here have some smiles and let’s go!”"
                              "\n\nCat on your head, you continue down the winding road, the singing gets louder until "
                              "suddenly it is deafening."
                              "\nThe weight disappears from your head as that cowardly cat splits once again. "
                              "The noise is coming from a patch of flowers that cover the path;"
                              "\non the other side the path starts again."
                              " Normally you are not one to step on flowers but it is the only way."
                              "\nFaintly, your foot falls onto the flabbering flowers. The sound abruptly stops and is "
                              "replaced by a union of hundreds of tiny voices."
                              "\n\nFlowers: “HOW RUDE, We will show you WEED!”"
                              "\n\nVines begin to crawl up your legs. If only you had SOMETHING to keep them at bay!")
                        while flowers.get_hp() > 0:
                            player_input = input("Press 1 to use pipe. ")
                            if player_input == "1" and turn is False:
                                flowers.lose_hp()
                                print("Flowers HP: ", flowers.get_hp())
                                print("Alice HP: ", hp)
                                turn = not turn
                            if turn is True:
                                print("Flowers attack and do -10 damage.")
                                # -= = 3pts
                                hp -= 10
                                turn = not turn
                        # Function = 10pts
                        if flowers.get_hp() == 0:
                            hp += 50
                            score += flowers.get_points()
                            player_input = input("Flowers: “RETREAT!”"
                                                 "\n\nThe vines around your legs dissipate and the flowers clear the "
                                                 "path. "
                                                 "Where the flowers once stood a vial of liquid labeled “Drink Me”"
                                                 "\nlies in a pile of Cheshire Smiles. "
                                                 "The path is now clear for you to walk and now free from "
                                                 "distraction the smell of "
                                                 "sweets surrounds your senses. \nWhat could that be? "
                                                 "That trash bin is back and is "
                                                 "staring at the pipe. It is all out of juice "
                                                 "anyways so you throw it into the bin and the bin takes off. "
                                                 "\nMaybe you should explore a bit (͠≖ ͜ʖ͠≖)?\nPress E to explore.\n").upper()
                            items.remove("pipe")
                            if player_input == "E":
                                print("You have picked up a potion! Drink wisely :)")
                                items.append("potion")
                                player_input = input(
                                                "Cheshire Cat: "
                                                "“Alice Alice Alice (⁎˃ᆺ˂)! Thank you so much for clearing "
                                                "the path for us! "
                                                "I will refill that HP for you”"
                                                "\n\n-HP = 100-\n\n"
                                                "Cheshire Cat: “Hey how about another riddle? Ya’know to lighten "
                                                "the mood a bit?”"
                                                "\n\n“I am a type of animal"
                                                "\n You might see on a safari"
                                                "\n I’m covered in black and white stripes"
                                                "\n I’m part of the horse family"
                                                "\n What am I?”").lower()
                                if player_input == "zebra":
                                    score += 5
                                    print(
                                        "Cheshire Cat: “Congrats! Here are some more smiles! Anyways what is that "
                                        "WONDER - ful smell? Let’s keep"
                                        " going!”\n\n"
                                        "You and the Cheshire Cat follow the smell until you reach a colorful "
                                        "clearing with a tremendous tower "
                                        "of toppling tea cups set on a table."
                                        "\nAt the head of the table sits three figures, a mouse, a hare, "
                                        "and a man with a very large Hat. You can sense the Cheshire Cat freezing up,"
                                        "\nnext thing you know that "
                                        "crazed cat is chasing the miniscule mouse into the forest. "
                                        "The Hare follows suit to protect their friend, "
                                        "\nit is now just you and the Hatter.\n\n"
                                        "Hatter: “HAHHAHHAHHA Alice the choice to come through here was not very wise. "
                                        "I am afraid it is time for you to meet your "
                                        "DEMISE ( ͡⚆ ͜ʖ ͡⚆)”"
                                        "\n\nDo something Alice, the Hatter approaches, "
                                        "if only you had something to squish them like roaches! "
                                        "Oh wait no don’t drink too much! ALICE!")
                                    while hatter.get_hp() > 0:
                                        player_input = input("Press 1 to use potion. ")
                                        if player_input == "1" and turn is False:
                                            hatter.lose_hp()
                                            print("Hatter HP: ", hatter.get_hp())
                                            print("Alice HP: ", hp)
                                            turn = not turn
                                        if turn is True:
                                            print("Hatter attacks and does -10 damage.")
                                            hp -= 10
                                            turn = not turn
                                    if hatter.get_hp() == 0:
                                        score += hatter.get_points()
                                        hp += 60
                                        items.remove("potion")
                                        player_input = input(
                                            "Hatter: “My My Alice it seems I am through, but I will live another day, "
                                            "don’t be so blue!”"
                                            "\n\nWith the tip of his hat the Hatter disappears into the forest. "
                                            "It is now just a tea party of one..."
                                            "very large little girl."
                                            "\nThe bottle of potion is so small in your giant hands. Somehow that trash bin "
                                            "has flown up and you know the drill and give it the bottle."
                                            "\nIn the scuffle, most of the  cups and sweets "
                                            "were tossed about onto the ground clearing the table."
                                            "\nYou hear a roar in the distance and you are so "
                                            "high up it is hard to see the path...but you do see the castle in the distance… "
                                            "\nby the looks of things "
                                            "it is about one boss fight away. "
                                            "Upon further inspection the table was actually one giant sword...\n"
                                            "covered in Cheshire Smiles. Since you're now... "
                                            "so large I bet that sword would just... "
                                            "fit in your pocket... if you just exploredddd a bit( ͜。 ͡ʖ ͜。)✧."
                                            "\nPress E to explore.").upper()
                                        if player_input == "E":
                                            print("You have picked up the vorpal sword!")
                                            items.append("sword")
                                            player_input = input(
                                                "Cheshire Cat: “（；^ω^） woooo sorry about that Alice, "
                                                "don’t know what came ove- WHOA (°o°:)..."
                                                "Alice why are you so huge?"
                                                "\nHere here, I will restore your size AND HP this time.”"
                                                "\n\nYour HP is now 100 and you are back to normal size"
                                                "\n\nCheshire Cat: “MMMmmm I feel that your wits have been "
                                                "compromised with all of this size shifting…"
                                                " TIME FOR RIDDLES!”\n"
                                                "\n“This thing has black and white stripes"
                                                "\n But it’s not a barcode"
                                                "\n It is something with four legs"
                                                "\n But it’s not a slimy toad”")
                                            if player_input == "zebra":
                                                score += 5
                                                print(
                                                    "Cheshire: “You are getting good at this Alice, hurry take these "
                                                    "smiles. We must make haste, we are so "
                                                    "close but I hear something sinister up ahead.”"
                                                    "\n\nNow back at your normal size, you and the Cheshire Cat "
                                                    "forge ahead. The castle is in view you are almost"
                                                    " there Alice!\nSuddenly you feel hot breath on your neck, "
                                                    "a drop of drool dangles a distance from your "
                                                    "dress. \nYou turn around just as that cagey cat camouflages "
                                                    "himself and you are alone, face-to-face with the "
                                                    "Jabberwocky."
                                                    "\n\nJabberwocky: “(º﹃º )”"
                                                    "\n\nOkay Alice, think! What could you possibly have to defeat this beast!?"
                                                    "\n\nJabberwocky: “┌( ಠ_ಠ)┘”")
                                                while jabberwocky.get_hp() > 0:
                                                    player_input = input("Press 1 to use sword. ")
                                                    if player_input == "1" and turn is False:
                                                        jabberwocky.lose_hp()
                                                        print("Jabberwocky HP: ", jabberwocky.get_hp())
                                                        print("Alice HP: ", hp)
                                                        turn = not turn
                                                    if turn is True:
                                                        print("Jabberwocky attacks and does -10 damage.")
                                                        hp -= 10
                                                        turn = not turn
                                                if jabberwocky.get_hp() == 0:
                                                    score += jabberwocky.get_points()
                                                    items.remove("sword")
                                                    player_input = input(
                                                        "\nYou embed the Vorpal Sword in the Jabberwocky’s side and "
                                                        "it slumps back into the dark forest, \n"
                                                        "leaving a trail of Cheshire Smiles and a single sparkling scale"
                                                        " in its wake. You have made it to the gate "
                                                        "of HER castle,\nall of this work and riddles and black and "
                                                        "white horses have lead up the this very moment. "
                                                        "You hear a sinister shrieking echoing off the structure of "
                                                        "the castle. \nAre you ready? Maybe you should "
                                                        "explore a bit first, for old times sake."
                                                        "\nPress E to explore.").upper()
                                                    if player_input == "E":
                                                        print("You have found a Jabberwocky scale!")
                                                        items.append("scale")
                                                        hp += 70
                                                        player_input = input(
                                                            "Cheshire Cat: “^ↀᴥↀ^ is it safe to come out? "
                                                            "ALICE wow that was amazing! I assume you need your HP "
                                                            "refilled after that, I got you!”"
                                                            "\n\nYour HP is now 100\n\n"
                                                            "Cheshire Cat: “Okay this is the main event Alice! "
                                                            "We need to make sure those wits are EXTRA sharp. I "
                                                            "made this last riddle extremely difficult,"
                                                            "\nso don’t worry if it takes you a few tries!”\n\n"""
                                                            "“I’m black and white but I’m not a newspaper"
                                                            "\n I have stripes but I’m not a prisoner uniform"
                                                            "\n I have a unique pattern but I’m not a barcode"
                                                            "\n I have four legs but I’m not a skunk"
                                                            "\n I’m part of the horse family but I’m not a donkey"
                                                            "\n What am I?”").lower()
                                                        if player_input == "zebra":
                                                            score += 5
                                                            print(
                                                                "Cheshire Cat: “╥﹏╥ Alice! That was all the riddles I "
                                                                "had and you solved them ALL! Here take the rest of "
                                                                "my smiles! Now go into that castle dear Alice”\n\n"
                                                                "Up the stairs and through the gate you go, past "
                                                                "squawking birds and past trembling card guards. "
                                                                "\nThe cackling of the crowned chick crescendos as you "
                                                                "make your way to the throne room. There she stands, "
                                                                "The Red Queen. \nShe wears a sinister smirk a if she "
                                                                "was expecting you. Your blood runs cold as that cruel "
                                                                "Cat disappears from your side and reappears next to "
                                                                "the Queen, \nyou have been bamboozled Alice! "
                                                                "\n\nQueen: “HOHOHO Did you really think, that my "
                                                                "kingly kitty would really show kindness to you, "
                                                                "you brat! HOHOHOHO OFF WITH YOUR HEAD!”"
                                                                "\n\nCheshire Cat: “... ( ͡◉ ͜ʖ ͡◉)”\n\n")
                                                            print("Alice...do not give up! You have something to defeat"
                                                                  " the queen, don't lose your head!\n\n")
                                                            while red_queen.get_hp() > 0:
                                                                player_input = input("Press 1 to use scale. ")
                                                                if player_input == "1" and turn is False:
                                                                    red_queen.lose_hp()
                                                                    print("Red Queen HP: ", red_queen.get_hp())
                                                                    print("Alice HP: ", hp)
                                                                    turn = not turn
                                                                if turn is True:
                                                                    print("Red Queen attacks and does -10 damage.")
                                                                    hp -= 10
                                                                    turn = not turn
                                                            if red_queen.get_hp() == 0:
                                                                score += red_queen.get_points()
                                                                items.remove("scale")
                                                                print(
                                                                    "Queen: “ Σ(T□T) How could you defeat ME! "
                                                                    "THE QUEEN??” "
                                                                    "\n\nThe Queen adjusts her crown as a deck of card "
                                                                    "guards rise up and lift her to safety. "
                                                                    "It is just you and that conspirator cat now"
                                                                    "\nHe says nothing, gives a small wink and with a "
                                                                    "twitch of his tail...disappears. In his place, a "
                                                                    "single golden key appears in a pile of "
                                                                    "Cheshire smiles.\n"
                                                                    "You look forward and there is a large red door. "
                                                                    "Alice, while it has been fun, I believe it now "
                                                                    "your time to run. You take the key and "
                                                                    "open the door…"
                                                                    "\n… "
                                                                    "\n…"
                                                                    "\nNext thing you know, you are back at home, "
                                                                    "as if you never left. All that is left of "
                                                                    "your journey is a "
                                                                    "pocket full of Cheshire Cat smiles and a zebra"
                                                                    " standing next to you on a leash.")
                                                                items.append("key")
                                                                print("You won! Final Score :", score)
                                                                lives -= 1

        if score == 100 and items[0] == "key":
            print("Congratulations you have successfully escaped Wonderland! Thank you for playing!")

        if lives == 0 and score != 100:
            print("Sorry, you lose. You'll never see your home, family, or friends again.")


main()
