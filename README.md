# KI-Fallstudie-2
Gruppenarbeit Programmieren
Teilnehmer: Luke, Sohrab, Lukasz, Malik, Max

Developer-Präsident: Luke
Dokumentations-Don: Max
Testverantwortlicher: Sohrab
Präsentationsverantwortlicher: Lukasz 
KI-Prüfer: Malik

Unser Projekt ist eine einfache Konsolenversion des Spiels „Hangman“. Das Programm wählt zu Beginn ein zufälliges Wort aus einer Wortliste aus. Anschließend versucht der Spieler, dieses Wort durch das Eingeben einzelner Buchstaben zu erraten. Für jeden falschen Versuch wird ein weiterer Teil der Hangman-Grafik angezeigt. Das Spiel endet, sobald entweder das Wort vollständig erraten wurde oder die maximale Anzahl an Fehlversuchen erreicht ist.

Die Umsetzung besteht aus mehreren Python-Dateien, die miteinander arbeiten. Die Hauptlogik befindet sich in der Datei, die das Spiel ausführt. Zusätzlich werden zwei externe Dateien für die Wortliste und die Darstellung des Galgens verwendet.

Das Projekt besteht aus vier Dateien. In main.py befindet sich die komplette Spiellogik. Die Datei Words_Hangman.py enthält die Wortliste, aus der das Spiel zufällig ein Wort auswählt. In Galgen_Hangman.py liegen die ASCII-Grafiken für den Galgen sowie die Funktion zur Anzeige der jeweiligen Stufen. Die README.md dient als Dokumentation des gesamten Projekts.

Words_Hangman.py ist die Wortliste bei der wir uns für ein Tupel entschieden haben. Ein Tupel eignet sich für die Wortliste des Hangman-Spiels besser, weil seine Elemente unveränderlich sind und dadurch nicht versehentlich verändert oder gelöscht werden können. Außerdem ist ein Tupel etwas ressourcenschonender als eine Liste, was bei einer festen Sammlung von Wörtern von Vorteil ist.

Die Datei Galgen_Hangman.py enthält alle ASCII-Grafiken, die die einzelnen Stadien des Galgens darstellen. Zusätzlich befindet sich darin die Funktion, die abhängig von der Anzahl der Fehlversuche die passende Grafik ausgibt und so den aktuellen Fortschritt des Spiels visualisiert.

Funktionsweise:
Zu Beginn des Spiels wählt das Programm ein zufälliges Wort aus der vorgegebenen Wortliste aus und zeigt es dem Spieler zunächst nur als Unterstriche an, sodass die Länge des Wortes erkennbar ist. Der Spieler gibt daraufhin einzelne Buchstaben ein, die überprüft werden, ob sie im Wort enthalten sind. Wird ein Buchstabe richtig geraten, wird er an allen entsprechenden Stellen im Wort angezeigt. Beispielsweise zeigt die Funktion display_hint(hint) das aktuelle Wort an.

Wird ein Buchstabe falsch geraten, erhöht sich die Anzahl der Fehlversuche, und die Funktion display_man(wrong_guesses) zeigt den entsprechenden Stand des Galgens an. Dabei entspricht wrong_guesses = 2 dem dritten Galgen-Stadium in der ASCII-Darstellung.

Die Überprüfung und Aktualisierung des Wortes erfolgt über eine Schleife, die jeden Buchstaben des Antwortwortes prüft: wenn der Spieler z. B. den Buchstaben "A" rät, werden alle passenden Positionen im Hinweis aktualisiert.

Das Spiel läuft so lange, bis der Spieler entweder alle Buchstaben erraten hat oder die maximale Anzahl an Fehlversuchen erreicht ist. Bereits geratene Buchstaben werden angezeigt, um doppeltes Raten zu vermeiden. Durch diese Kombination aus Eingabe, Überprüfung, Anzeige des Wortes und Darstellung des Galgens wird der Spielablauf klar strukturiert und für den Spieler nachvollziehbar.

Bedienung:
Das Spiel wird über die Konsole gestartet, indem die Datei main.py ausgeführt wird. Sobald das Spiel läuft, fordert das Programm den Spieler auf, einzelne Buchstaben einzugeben. Die Eingabe erfolgt über die Funktion input(), zum Beispiel guess = input("Gib einen Buchstaben ein: ").upper(). Dabei wird die Eingabe automatisch in Großbuchstaben umgewandelt, um die Überprüfung zu vereinfachen.

Zusammenfassung:
Dieses Hangman-Spiel zeigt auf einfache Weise, wie ein klassisches Konsolenspiel in Python umgesetzt werden kann. Es verwendet eine feste Wortliste, aus der das Programm zufällig ein Wort auswählt, und ASCII-Grafiken, um den Fortschritt des Spiels visuell darzustellen. Die Hauptlogik befindet sich in der Funktion run_game(), die Eingaben verarbeitet, das Wort überprüft und den aktuellen Spielstand aktualisiert.
