import random
import sys
    
is_running = False
print("Willkommen zu: Wer wird Millionär!")

fragerunde = {1: 100, 2: 500, 3: 1000, 4: 4000,
              5: 16000, 6: 64000, 7: 500000, 8: 1000000}

questions = {1: ["Zu welcher Erkenntnis gelangt man, hat man sich an der Supermarktkasse da angestellt, wo es am langsamsten vorangeht?"],
             2: ["Wer ein alkoholisches Getränk zu sich nimmt, kippt sich einen ...?"],
             3: ["Wer von Deutschland aus immer genau in Richtung Osten fliegt, überquert irgendwann ...?"],
             4: ["Von wem ist überliefert, dass er sich zur Tarnung einen Bart und die üppige Haartracht eines Ritters wachsen ließ?"],
             5: ["Was machte man in der ehemaligen DDR mit einem 'Stereomat'?"],
             6: ["Wieviel Stunden betrug die durchschnittliche Wochenarbeitszeit einer vollzeiterwerbstätigen Person in Deutschland 2021?"],
             7: ["Kam es zu einer Infestation, so hat man womöglich ...?"],
             8: ["Welcher Verein wurde 2021 mit 30 Siegen in 30 Spielen Deutscher Meister im Frauenhandball?"]}

answers = {1: {"A": "Sturer Bock", "B": "falsche Schlange", "C": "krummer Hund", "D": "böser Wolf"},
           2: {"A": "über die Windel", "B": "in den Tampon", "C": "hinter der Binde", "D": "auf die Slipeinlage"},
           3: {"A": "den Äquator", "B": "die Datumsgrenze", "C": "den indischen Ozean", "D": "das Taka-Tuka-Land"},
           4: {"A": "Julius Caesar", "B": "Martin Luther", "C": "Napoleon Bonaparte", "D": "Erich Honecker"},
           5: {"A": "Musik hören", "B": "Bilder malen", "C": "Dias anschauen", "D": "Filme aufnehmen"},
           6: {"A": 36.8, "B": 38.7, "C": 40.6, "D": 42.6},
           7: {"A": "Läuse im Haar", "B": "den Beichtstuhl aufgesucht", "C": "viel Geld verspekuliert", "D": "Kost und Logis in der JVA"},
           8: {"A": "Werder Bremen", "B": "Eintracht Frankfurt", "C": "RB Leipzig", "D": "Borussia Dortmund"}}

lösung = {1: "B", 2: "C", 3: "B", 4: "B", 5: "C", 6: "C", 7: "A", 8: "D"}
count = 1

def gewonnen(count):
    if count == 8:
        print("Sie haben 1 Million Euro gewonnen!")
        sys.exit()  

def aussteigen(fragerunde, count):
    print("Möchten Sie jetzt aussteigen j oder n?")

    if fragerunde.get(count) >= 4000 and fragerunde.get(count) < 500000:
        print("Sie hätten dann 4000 Euro gewonnen.")
    else:
        print("Sie hätten dann 64000 Euro gewonnen")
    
    is_answer_valid = False
    while not is_answer_valid:
        antwort = input("")

        if str.lower(antwort) == "j":
            if fragerunde.get(count) >= 4000 and fragerunde.get(count) < 500000:
                print("Glückwunsch Sie haben 4000 Euro gewonnen!")
            else:
                print("Glückwunsch Sie haben 64000 Euro gewonnen!")
            sys.exit()
            is_answer_valid = True
            return True
            break

        elif str.lower(antwort) == "n":
            is_answer_valid = True
            return False

        else:
            print("Fehler. Bitte probieren Sie es nochmal")

def fifty_fifty(count, answers, lösung):
    # takes correct answer out of possible options
    correct_answer = lösung[count]
    options = list(answers[count].keys())
    options.remove(correct_answer)
      # removes two random options out of wrong answers
    rest = random.sample(options, 2)
    for num in rest:
        del answers[count][num]

    return(answers[count])

def publikum(answers, lösung, count):

    correct_answer = lösung[count]
    options = list(answers[count].keys())
    percentages = []
    diff = 100
        
    #vier random nummern die insgesamt 100 ergeben
    for i in range(4):
        rnum = random.randint(1, max(diff, 1))
        if diff > 0:
            percentages.append(rnum)
        else:
            percentages.append(0)    
        diff -= rnum
        
    if diff > 0:
        percentages.append(percentages[3]+diff)
    
    final = {}
    percentages.sort()
    chance = random.randint(1,100)

    #count ist rundenzahl
    #je höher count desto höher muss chance sein um richtige antwort zu bekommen
    if count <= 4:
        if chance > 10:
            final.update({correct_answer:percentages[3]})
            options.remove(correct_answer)
            for i in range(3):
                final.update({options[i]:percentages[i]})
        else:
            for i in range(4):
                final.update({options[i]:percentages[i]})       
    elif count <= 6:
        if chance > 30:
            final.update({correct_answer:percentages[3]})
            options.remove(correct_answer)
            for i in range(3):
                final.update({options[i]:percentages[i]})            
        else:
            for i in range(4):
                final.update({options[i]:percentages[i]}) 
    else:
        if chance > 60:
            final.update({correct_answer:percentages[3]})
            options.remove(correct_answer)
            for i in range(3):
                final.update({options[i]:percentages[i]})            
        else:
            for i in range(4):
                final.update({options[i]:percentages[i]})             
    final = {key: val for key, val in sorted(final.items(), key = lambda ele: ele[0])}
    for key, value in final.items():
        print(key, ":", value)                 
    
def anruf(answers,lösung,count):
    
    print("Welchen Experten wählen Sie?")
    print("A: Einen Freund\nB: Vater\nC: Lehrer")
    antwort_experte = input("")
    random_number = random.randint(1, 100)

    if str.upper(antwort_experte) == "A":
        if random_number > 50:
            print("Ich glaube es ist Antwortmöglichkeit:", lösung[count])
        else:
            letter = chr(random.randint(ord('A'), ord('D')))
            print("Ich glaube es ist Antwortmöglichkeit:", letter)

    if str.upper(antwort_experte) == "B":
        if random_number > 40:
            print("Ich glaube es ist Antwortmöglichkeit:", lösung[count])
        else:
            letter = chr(random.randint(ord('A'), ord('D')))
            print("Ich glaube es ist Antwortmöglichkeit:", letter)
    if str.upper(antwort_experte) == "C":
        if random_number > 10:
            print("Ich glaube es ist Antwortmöglichkeit:", lösung[count])
        else:
            letter = chr(random.randint(ord('A'), ord('D')))
            print("Ich glaube es ist Antwortmöglichkeit:", letter) 

for answer in answers:
    lösungen = lösung.get(count)

    if fragerunde.get(count) == 16000 or fragerunde.get(count) == 500000:
        print("Glückwunsch Sie haben eine neue Sicherheitsstufe erreicht!\n")

    # ab der ersten Sicherheitsstufe Frage,ob Ausstieg
    if fragerunde.get(count) > 4000:
        aussteigen(fragerunde, count)

    print("Frage", count,"(" + str(fragerunde[count]) + " Euro): " + questions[count][0])
    for letter, answer in answers[count].items():
        print("  ", str(letter) + ") " + str(answer))   
    
    # Frage ob Spieler einen Joker verwenden möchte
    joker = {1: "50/50", 2: "Publikum", 3: "Anruf"}
    print("Wollen Sie einen Joker benutzen j oder n?")
    antwort_joker = input("")
    
    if antwort_joker == "j":
        print("Welchen Joker wollen Sie verwenden?")
        
        for key, value in joker.items():
            print(str(key) + ": " + value)
        num = input("")
        num = int(num)
        joker.pop(num)
        
        # 50/50
        if num == 1:
            options = fifty_fifty(count, answers, lösung)
            for key, value in options.items():
                print(key + ": " + value)
        
        # publikum
        elif num == 2:
            publikum(answers, lösung, count)
        
        # anruf
        elif num == 3:
            anruf(answers, lösung, count)

    print("Nennen Sie mir jetzt Ihre Antwort")
    antwort = input("")

    if str.upper(antwort) == lösungen:
        print("Glückwunsch das war die richtige Antwort\n")
    else:
        print("Die richtige Antwort wäre gewesen:", lösungen)
        print("Sie haben", fragerunde.get(count), "Euro gewonnen!")
        break
    gewonnen(count)
    count += 1

        
        
        
    

        
        
    
