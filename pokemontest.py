#Create a test that checks how many of the original 151 pokemon a user can guess
import time
POKEMON = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
correct = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

def checkList(entry):
    temp = -99
    if entry in POKEMON:
       temp = POKEMON.index(entry)
       correct[temp] = True

def getInput():
    entry = str(input("Guess: "))
    if entry == "-99": #user can enter -99 to quit game
        quit()
    import os
    os.system('cls')
    if entry == "Mr. Mime" or entry == "mr. mime" or entry == "Mr. mime": #because of the .capatalize() method, and Mr. Mime's space within his name, an exception has to be made for the user to input Mr. Mime
        pass
    elif entry == "Nidoran" or entry == "nidoran":
        correct[28] = True
        correct[31] = True
    else: 
        entry = entry.capitalize()
    print("Most recent guess:", entry)
    checkList(entry)
    output() 

def setup():
    print("Welcome to the 151 Original Pokemon Quiz!")
    while 1:
        diffInMin = int(input("Select your difficulty in minutes- 10, 15, or 20: "))
        if diffInMin == 10 or diffInMin == 15 or diffInMin == 20:
            break
        else:  
            print("Error, please retry")
    return diffInMin
    #will add to setup function in future versions
    #perhaps add functionality for different generations

def output():
    dexNum = 1
    for i in POKEMON:
        endSpace = ""
        for j in range(10 - len(i)):
            endSpace = endSpace + " "
        if correct[dexNum - 1] == True:
            if (dexNum) % 5 == 0: 
                print(str('{0:03}'.format(dexNum)) + ":", i)
            else:
                print(str('{0:03}'.format(dexNum)) + ":", i, end = " " + endSpace)
        else:
            if (dexNum) % 5 == 0:
                print(str('{0:03}'.format(dexNum)) + ":", "          ")
            else:
                print(str('{0:03}'.format(dexNum)) + ":", "          ", end = " ")
        dexNum += 1

#POKEMON = "BulbasaurIvysaurVenusaurCharmanderCharmeleonCharizardSquirtleWartortleBlastoiseCaterpieMetapodButterfreeWeedleKakunaBeedrillPidgeyPidgeottoPidgeotRattataRaticateSpearowFearowEkansArbokPikachuRaichuSandshrewSandslashNidoran♀NidorinaNidoqueenNidoran♂NidorinoNidokingClefairyClefableVulpixNinetalesJigglypuffWigglytuffZubatGolbatOddishGloomVileplumeParasParasectVenonatVenomothDiglettDugtrioMeowthPersianPsyduckGolduckMankeyPrimeapeGrowlitheArcaninePoliwagPoliwhirlPoliwrathAbraKadabraAlakazamMachopMachokeMachampBellsproutWeepinbellVictreebelTentacoolTentacruelGeodudeGravelerGolemPonytaRapidashSlowpokeSlowbroMagnemiteMagnetonFarfetchdDoduoDodrioSeelDewgongGrimerMukShellderCloysterGastlyHaunterGengarOnixDrowzeeHypnoKrabbyKinglerVoltorbElectrodeExeggcuteExeggutorCuboneMarowakHitmonleeHitmonchanLickitungKoffingWeezingRhyhornRhydonChanseyTangelaKangaskhanHorseaSeadraGoldeenSeakingStaryuStarmieMr. MimeScytherJynxElectabuzzMagmarPinsirTaurosMagikarpGyaradosLaprasDittoEeveeVaporeonJolteonFlareonPorygonOmanyteOmastarKabutoKabutopsAerodactylSnorlaxArticunoZapdosMoltresDratiniDragonairDragoniteMewtwoMew"
#POKEMON = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetchd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. ", "Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
def main():
    gameWon = False
    gameLost = False
    diffInMin = setup()
    start = time.time()
    while(time.time() - start < diffInMin * 60 and gameWon == False and gameLost == False):
        getInput()
        tempMin = int(((diffInMin * 60 - (time.time() - start)) / 60))
        if diffInMin <= 0:
            gameLost == True
            break
        if float(tempMin) < tempMin:
            print("Time remaining:", tempMin - 1, "minutes", '{:.0f}'.format((diffInMin * 60 - (time.time() - start) - (tempMin * 60)) ), "seconds")
        else: #                                                                   60 +  (   total time remaining            ) - seconds accounted for by min * 60
           print("Time remaining:", tempMin, "minutes", '{:.0f}'.format((diffInMin * 60 - (time.time() - start) - (tempMin * 60)) ), "seconds")
    endTime = (tempMin, "minutes", '{:.0f}'.format((diffInMin * 60 - (time.time() - start) - (tempMin * 60)) ), "seconds")
    points = 0
    for i in correct:
        if i == True:
            points += 1
    if gameLost == True:
        print("Thanks for playing! You ran out of time, but guessed", points, "pokemon correctly!")
    else:
        print("Thanks for playing! You earned a perfect score of 151 out of 151, with", endTime, "left!")
main()