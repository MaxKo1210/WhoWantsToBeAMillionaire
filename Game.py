from Player import Spieler

class Game:
    #print("Hello whats your name?")
    #name = input(" ")
    #print("Nice to meet you " + name)
    #print("Lets get started!")
    runde_counter = 1
    print("Question Number", runde_counter,":")
    fragerunde = {1: 100, 2:500, 3:1000, 4:4000, 5: 16000, 6:64000, 7:500000, 8:1000000}
    questions = {1:["Zu welcher Erkenntnis gelangt man, hat man sich an der Supermarktkasse da angestellt, wo es am langsamsten vorangeht?"],2: ["Wer ein alkoholisches Getränk zu sich nimmt, kippt sich einen ...?"], 3: ["Wer von Deutschland aus immer genau in Richtung Osten fliegt, überquert irgendwann ...?"], 4: ["Von wem ist überliefert, dass er sich zur Tarnung einen Bart und die üppige Haartracht eines Ritters wachsen ließ?"], 5: ["""Was machte man in der ehemaligen DDR mit einem 'Stereomat'?
"""],6: ["Wieviel Stunden betrug die durchschnittliche Wochenarbeitszeit einer vollzeiterwerbstätigen Person in Deutschland 2021?"], 7: ["Kam es zu einer Infestation, so hat man womöglich ...?"], 8: ["Welcher Verein wurde 2021 mit 30 Siegen in 30 Spielen Deutscher Meister im Frauenhandball?"]}
    answers = {1: {"A" : "Sturer Bock", "B": "falsche Schlange", "C": "krummer Hund", "D": "böser Wolf"}, 2: {"A": "über die Windel", "B": "in den Tampon", "C": "hinter der Binde", "D": "auf die Slipeinlage"}, 3: {"A": "den Äquator", "B": "die Datumsgrenze", "C": "den indischen Ozean", "D": "das Taka-Tuka-Land"}, 4: {"A": "Julius Caesar", "B": "Martin Luther", "C": "Napoleon Bonaparte", "D": "Erich Honecker"}, 5: {"A": "Musik hören", "B": "Bilder malen", "C": "Dias anschauen", "D": "Filme aufnehmen"}, 6: {"A": 36.8, "B": 38.7, "C": 40.6, "D":42.6}, 7: {"A": "Läuse im Haar", "B": "den Beichtstuhl aufgesucht", "C": "viel Geld verspekuliert", "D": "Kost und Logis in der JVA"}, 8:{"A": "Werder Bremen", "B": "Eintracht Frankfurt", "C": "RB Leipzig", "D": "Borussia Dortmund"}}
    lösung = {1:"B", 2:"C", 3:"B", 4:"B", 5:"C", 6:"C",7:"A", 8:"D"}
    count = 1

    
    for answer in answers:
        lösungen = lösung.get(count)
        print("In dieser Frage geht es um",fragerunde.get(count),"Euro")
        if fragerunde.get(count) == 4 or fragerunde.get(count) == 6:
            print("Glückwunsch Sie haben eine neue Sicherheitsstufe erreicht")
        if fragerunde.get(count) > 100:
            Spieler.Aussteigen(fragerunde,count) 
            #erst nach der ersten Runde sinnvoll zu fragen ob ausgestiegen werden möchte
        print(questions.get(count))
        print(answers.get(answer))
        Spieler.Joker(answers,lösungen,count)
        print("Dann nennen Sie mir jetzt Ihre Antwort")
        antwort = input("")
        if antwort == lösungen:
            print("Glückwunsch das war die richtige Antwort")
        else: 
            print("Die richtige Antwort wäre gewesen:",lösungen)
            print("Sie haben", fragerunde.get(count),"Euro gewonnen!")
            break
        Spieler.Gewonnen(count)
        count += 1
           

        
        
        
    