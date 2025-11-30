# KI-Fallstudie-2
Gruppenarbeit Programmieren
Teilnehmer: Luke, Sohrab, Lukasz, Malik, Max






Unser Projekt ist eine einfache Konsolenversion des Spiels „Hangman“. Das Programm wählt zu Beginn ein zufälliges Wort aus einer Wortliste aus. Anschließend versucht der Spieler, dieses Wort durch das Eingeben einzelner Buchstaben zu erraten. Für jeden falschen Versuch wird ein weiterer Teil der Hangman-Grafik angezeigt. Das Spiel endet, sobald entweder das Wort vollständig erraten wurde oder die maximale Anzahl an Fehlversuchen erreicht ist.

Die Umsetzung besteht aus mehreren Python-Dateien, die miteinander arbeiten. Die Hauptlogik befindet sich in der Datei, die das Spiel ausführt. Zusätzlich werden zwei externe Dateien für die Wortliste und die Darstellung des Galgens verwendet.

Das Projekt besteht aus vier Dateien. In main.py befindet sich die komplette Spiellogik. Die Datei Words_Hangman.py enthält die Wortliste, aus der das Spiel zufällig ein Wort auswählt. In Galgen_Hangman.py liegen die ASCII-Grafiken für den Galgen sowie die Funktion zur Anzeige der jeweiligen Stufen. Die README.md dient als Dokumentation des gesamten Projekts.

Words_Hangman.py ist die Wortliste bei der wir uns für ein Tupel entschieden haben. Ein Tupel eignet sich für die Wortliste des Hangman-Spiels besser, weil seine Elemente unveränderlich sind und dadurch nicht versehentlich verändert oder gelöscht werden können. Außerdem ist ein Tupel etwas ressourcenschonender als eine Liste, was bei einer festen Sammlung von Wörtern von Vorteil ist.

Die Datei Galgen_Hangman.py enthält alle ASCII-Grafiken, die die einzelnen Stadien des Galgens darstellen. Zusätzlich befindet sich darin die Funktion, die abhängig von der Anzahl der Fehlversuche die passende Grafik ausgibt und so den aktuellen Fortschritt des Spiels visualisiert.
