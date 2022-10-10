import random
import sys
from tkinter import W
class Spieler:
    runde = 1
    def __init__(self,name):
        self.name = name
    
    def get_key(val,fragerunde):
        for key, value in fragerunde.items():
            if val == value:
                return key
    def Gewonnen(count):
        if count == 8:
            print("Glückwunsch Sie haben 1 Million Euro gewonnen!")
            sys.exit()

    
    def Aussteigen(fragerunde,count):
        if fragerunde.get(count) < 4000:
            print("Wenn Sie jetzt aussteigen würden Sie 0 Euro gewinnen.")
        elif fragerunde.get(count) >= 4000 and fragerunde.get(count) < 64000:
            print("Wenn Sie jetzt aussteigen würden Sie 4000 Euro gewinnen.")
        else:
            print("Wenn Sie jetzt aussteigen würden Sie 64000 Euro gewinnen.")
        print("Möchten Sie jetzt aussteigen?")
        
        is_answer_valid = False
        while not is_answer_valid:
            antwort = input("")
            if antwort == "Ja":
                if fragerunde.get(count) < 4000:
                    print("Glückwunsch Sie haben 0 Euro gewonnen!")
                    sys.exit()
                elif fragerunde.get(count) >= 4000 and fragerunde.get(count) < 64000:
                    print("Glückwunsch Sie haben 4000 Euro gewonnen!")
                    sys.exit()
                else:
                    print("Glückwunsch Sie haben 64000 Euro gewonnen!")
                    sys.exit()
                is_answer_valid = True
                return True
                break
            elif antwort == "Nein":
                is_answer_valid = True
                return False
            else:
                print("Fehler. Bitte probieren Sie es nochmal")
        
            
    
    def Joker(answers,lösung,count):
        print("Wollen Sie einen Joker benutzen?")
        antwort_joker = input("")
        final = []
        is_running = False
        while is_running == False:
            if antwort_joker == "Ja":
                print("Welchen Joker wollen Sie verwenden?")
                print("1: 50/50 2: Publikum 3: Anruf")
                num = input("")
                num = int(num)
                if num == 1:
                    for rang in range(0,count):
                        for k, v in answers.items():
                            final = list(v.values()) 
                            print(final)
                    #Es werden 2 random Nummern generiert, welche dann aus der Liste der Antwortmöglichkeiten gestrichen werden
                    randnum1 = random.randint(1,4)
                    randnum2 = random.randint(1,3)
                    final.pop(randnum1)
                    final.pop(randnum2)
                    print("Ihre Antwortmöglichkeiten sind: A:", final[0],"oder B:",final[1])
                    is_running = True
                
                elif num == 2:
                    # 4 Nummern die Prozentzahlen darstellen und zusammen 100 ergeben
                    rnum1 = random.randint(1,100)
                    diff = 100 - rnum1
                    rnum2 = random.randint(1,diff)
                    diff2 = diff - rnum2
                    rnum3 = random.randint(1,diff2)
                    diff3 = diff2 - rnum3
                    if diff3 > 0:
                        rnum4 = random.randint(1,diff3)
                    else:
                        rnum4 = 0
                    percentages = [rnum1,rnum2,rnum3,rnum4]
                    final = {}
                    percentages.sort()
                    chance = random.randint(1,100)
                    #count repräsentiert die Rundennummer
                    if count <= 4:
                        #je früher im Spiel desto höher die Chance, dass das Publikum die Antwort kennt
                        if chance > 10:
                            if lösung == "A":
                                final.update({"A":percentages[3]})
                                final.update({"B":percentages[1]})
                                final.update({"C":percentages[0]})
                                final.update({"D":percentages[2]})
                            elif lösung == "B":
                                final.update({"A":percentages[2]})
                                final.update({"B":percentages[3]})
                                final.update({"C":percentages[0]})
                                final.update({"D":percentages[1]})
                            elif lösung == "C":
                                final.update({"A":percentages[1]})
                                final.update({"B":percentages[2]})
                                final.update({"C":percentages[3]})
                                final.update({"D":percentages[0]})
                            elif lösung == "D":
                                final.update({"A":percentages[2]})
                                final.update({"B":percentages[0]})
                                final.update({"C":percentages[1]})
                                final.update({"D":percentages[3]})
                        else:
                            final.update({"A":percentages[2]})
                            final.update({"B":percentages[1]})
                            final.update({"C":percentages[0]})
                            final.update({"D":percentages[3]})
                    elif count <= 6:
                        if chance > 30:
                            if lösung == "A":
                                final.update({"A":percentages[3]})
                                final.update({"B":percentages[2]})
                                final.update({"C":percentages[1]})
                                final.update({"D":percentages[0]})
                            elif lösung == "B":
                                final.update({"A":percentages[1]})
                                final.update({"B":percentages[3]})
                                final.update({"C":percentages[0]})
                                final.update({"D":percentages[2]})
                            elif lösung == "C":
                                final.update({"A":percentages[1]})
                                final.update({"B":percentages[0]})
                                final.update({"C":percentages[3]})
                                final.update({"D":percentages[2]})
                            elif lösung == "D":
                                final.update({"A":percentages[0]})
                                final.update({"B":percentages[1]})
                                final.update({"C":percentages[2]})
                                final.update({"D":percentages[3]})
                        else:
                            final.update({"A":percentages[2]})
                            final.update({"B":percentages[1]})
                            final.update({"C":percentages[0]})
                            final.update({"D":percentages[3]})
                    else:
                        if chance > 50:
                            if lösung == "A":
                                final.update({"A":percentages[3]})
                                final.update({"B":percentages[0]})
                                final.update({"C":percentages[1]})
                                final.update({"D":percentages[2]})
                            elif lösung == "B":
                                final.update({"A":percentages[2]})
                                final.update({"B":percentages[3]})
                                final.update({"C":percentages[1]})
                                final.update({"D":percentages[0]})
                            elif lösung == "C":
                                final.update({"A":percentages[2]})
                                final.update({"B":percentages[1]})
                                final.update({"C":percentages[3]})
                                final.update({"D":percentages[0]})
                            elif lösung == "D":
                                final.update({"A":percentages[2]})
                                final.update({"B":percentages[1]})
                                final.update({"C":percentages[0]})
                                final.update({"D":percentages[3]})
                        else:
                            final.update({"A":percentages[0]})
                            final.update({"B":percentages[2]})
                            final.update({"C":percentages[1]})
                            final.update({"D":percentages[3]})
                    print("So hat sich das Publikum entschieden:")
                    print(final.items())
                    is_running = True
                elif num == 3:
                    print("Welchen Experten wählen Sie?")
                    print("A: Ihren Freund")
                    print("B: Ihren Professor")
                    print("C: Ihren Vater")
                    antwort_experte = input("")
                    is_true = False
                    while is_true == False:
                        if antwort_experte == "A":
                            is_true = True
                            freund = random.randint(1,100)
                            #freund hier der dümmste, weshalb die Wahrscheinlichkeit, dass seine Antwort richtig ist geringer ist
                            if freund > 50:
                                print("Ich glaube es ist Antwortmöglichkeit:",lösung)
                                is_running = True
                            else:
                                char = random.randint(1,4)
                                if char == 1:
                                    print("Ich glaube es ist Antwortmöglichkeit: A")
                                elif char == 2:
                                    print("Ich glaube es ist Antwortmöglichkeit: B")
                                elif char == 3:
                                    print("Ich glaube es ist Antwortmöglichkeit: C")
                                else: 
                                    print("Ich glaube es ist Antwortmöglichkeit: D")
                                is_running = True
                        elif antwort_experte == "B":
                            is_true = True
                            prof = random.randint(1,100)
                            if prof > 10:
                                print("Ich glaube es ist Antwortmöglichkeit:",lösung)
                                is_running = True
                            else:
                                char = random.randint(1,4)
                                if char == 1:
                                    print("Ich glaube es ist Antwortmöglichkeit: A")
                                elif char == 2:
                                    print("Ich glaube es ist Antwortmöglichkeit: B")
                                elif char == 3:
                                    print("Ich glaube es ist Antwortmöglichkeit: C")
                                else: 
                                    print("Ich glaube es ist Antwortmöglichkeit: D")
                                is_running = True
                        elif antwort_experte == "C":
                            is_true = True
                            vater = random.randint(1,100)
                            if vater > 30:
                                print("Ich glaube es ist Antwortmöglichkeit:",lösung)
                                is_running = True
                            else:
                                char = random.randint(1,4)
                                if char == 1:
                                    print("Ich glaube es ist Antwortmöglichkeit: A")
                                elif char == 2:
                                    print("Ich glaube es ist Antwortmöglichkeit: B")
                                elif char == 3:
                                    print("Ich glaube es ist Antwortmöglichkeit: C")
                                else: 
                                    print("Ich glaube es ist Antwortmöglichkeit: D")
                                is_running = True
            else:
                is_running = True
                
        #return final
   