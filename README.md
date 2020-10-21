# Projekt Aufgaben 
In diesem Projekt "Team Chooser" lernen wir, wie man ein Programm erstellt, um eine Liste von Spielern in zwei zufällige Teams aufzuteilen. Dieses Projekt zeigt die Verwendung von Dateien und Listen.


# Schritte 1 Program benutzen 
Zunächst verwenden wir "thrinket" von Thonny, um Python zu schreiben. Einige von uns haben auch Pycharm und Visual Studio Code benutz.  


# Schritte 2 Spielerliste erstellen
Wir listen den Spielnamen in eckigen Klammern [] mit einem Komma zwischen den einzelnen Elementen in der Liste auf.Print dann Player-Variable. 


# Schritte 3 Random, apend und remove Funktion hinzufügen
Um einen zufälligen Spieler aus Spielerliste zu erhalten, müssen wir zuerst den ausgewählten Teil des "random" moduls importieren.

Um einen zufälligen Spieler zu erhalten, können wir die "choice" verwenden.

Wir können auch zufällig ausgewählten Spieler zum Team hinzufügen. Dazu können wir team xxx “.append“ verwenden.

Wir können auch zufällig ausgewählten Spieler zum Team entfernen. Dazu können wir players “.remove“ verwenden.


# Schritte 3 Mehr Spieler wählen und neue Datei öffnen
Erstellen wir neue Dateien in txt.format als "player.txt" -Datei mit dem schreibgeschützten 'r'.  

file = open("players.txt", "r")

Lesen wir die Liste aus der Datei und fügen wir die Spielerliste hinzu. (Der Splitlines-Code bedeutet, dass jede Zeile in der Datei ein neues Element in der Spielerliste ist.) 

players = file.read().splitlines()

Wenn wir der Datei player.txt einen anderen Namen hinzufügen, sodass wir eine ungerade Anzahl von Spielern haben. Wenn wir Code testen, wird eine Fehlermeldung angezeigt. Der Fehler liegt darin, dass unser Programm weiterhin zufällige Spieler für das Team auswählt A und dann Team B. Wenn es jedoch eine ungerade Anzahl von Spielern gibt, stehen nach Auswahl eines Spielers für Team A keine Spieler mehr zur Auswahl für Team B. Um diesen Fehler zu beheben, können wir das Programm anweisen, aus unserer while-Schleife auszubrechen, wenn die Spielerliste leer ist.

 if players == []:
        
        break

