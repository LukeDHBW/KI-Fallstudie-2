# KI-Fallstudie
Gruppenarbeit Programmieren
Teilnehmer: Luke, Sohrab, Lukasz, Malik, Max

Developer-Präsident: Luke
Dokumentations-Don: Max
Testverantwortlicher: Sohrab
Präsentationsverantwortlicher: Lukasz 
KI-Prüfer: Malik


Organisatorischer Ablauf:
Wir haben uns am 13. November, nachdem die Gruppen eingeteilt wurden, dazu entschieden, eine WhatsApp-Gruppe zu erstellen. In dieser WhatsApp-Gruppe standen wir dann im ständigen Kontakt, haben außerdem direkt das GitHub-Repository erstellt und überlegt, welches Projekt wir umsetzen wollen. Nachdem wir uns darauf geeinigt hatten, dass Hangman das richtige Projekt für uns ist, haben wir die Rollenverteilung festgelegt. Diese wurde zunächst frei nach individuellem Interesse verteilt, sodass jeder sich die Aufgaben aussuchen konnte, die ihm am meisten liegen. Die Rollenverteilung, wie oben bereits beschrieben, bedeutet dabei nicht, dass eine Person alles alleine erledigt hat, sondern wir haben uns gegenseitig immer unterstützt und geholfen. Außerdem haben wir während dieser ersten Session Ideen, Fragen und Anreize gesammelt. Diese erste Sitzung dauerte etwa zwei bis drei Stunden. Nach einer kleinen Pause haben wir uns am 26.11 nach unseren Vorlesungen in einem Gruppenraum getroffen, da wir der Meinung sind, dass persönliche Treffen vor Ort einfach besser geeignet sind, um als Team effektiv zusammenzuarbeiten. In dieser Sitzung haben wir die Feinschliffe am Projekt vorgenommen, die Dokumentation weiter ausgeführt und offene Punkte besprochen.

Projektbeschreibung:
Hangman ist ein klassisches Wortspiel, das hier als Konsolenanwendung in Python umgesetzt wurde. Ziel des Projekts ist es, ein interaktives Spiel zu entwickeln, bei dem der Spieler durch das Raten einzelner Buchstaben ein zufällig gewähltes Wort erraten muss. Das Programm zeigt den aktuellen Fortschritt im Wort, bereits geratene Buchstaben und Fehlversuche über ASCII-Grafiken des Galgens an. Kernfunktionen sind die zufällige Auswahl eines Wortes, die Überprüfung der Buchstabeneingaben, die Verwaltung bereits geratener Buchstaben sowie die Ermittlung von Sieg oder Niederlage.

Bedienungsanleitung:
Die Bedienung des Spiels erfolgt über die Konsole, indem die Datei main.py gestartet wird. Anschließend gibt der Spieler in jeder Runde einen einzelnen Buchstaben ein. Das Programm überprüft jede Eingabe und akzeptiert nur gültige Buchstaben; Zahlen oder mehrere Zeichen werden zurückgewiesen. Bereits geratene Buchstaben werden angezeigt, um Doppelraten zu vermeiden. Richtige Buchstaben werden an allen entsprechenden Stellen im Wort sichtbar gemacht, während falsch geratene Buchstaben die Anzahl der Fehlversuche erhöhen und den Galgen schrittweise vervollständigen. Das Spiel endet, sobald alle Buchstaben des Wortes erraten wurden, was als Gewinn angezeigt wird, oder sobald die maximale Anzahl an Fehlversuchen erreicht ist, was eine Verlustmeldung auslöst.

Beispiel Eingaben und Augaben:

Beispiel 1:
Eingabe: A
Anzeige: _ _ A _ _
Fehlversuche: 0
Der Buchstabe A ist im Wort enthalten, daher wird er an allen passenden Positionen angezeigt.
Beispiel 2:
Eingabe: Z
Anzeige: _ _ A _ _
Fehlversuche: 1
Da Z nicht im Wort vorkommt, wird die Anzahl der Fehlversuche erhöht und die ASCII-Grafik des Galgens zeigt nun das erste zusätzliche Segment.
Beispiel 3:
Eingabe: N
Anzeige: _ _ A N _
Fehlversuche: 1
Der Buchstabe N ist korrekt und wird an den entsprechenden Stellen angezeigt. Die Fehlversuche bleiben unverändert.
Beispiel 4:
Eingabe: S
Anzeige: _ _ A N _
Fehlversuche: 2
S ist nicht im Wort enthalten, daher steigt die Anzahl der Fehlversuche erneut, und die Galgen-Grafik wird um ein weiteres Segment ergänzt.
Beispiel 5 (Gewinn):
Eingabe: P
Anzeige: P _ A N _
Fehlversuche: 2
Mit weiteren richtigen Buchstaben wird das Wort vollständig angezeigt. Sobald alle Buchstaben erraten sind, endet das Spiel mit der Meldung „Gewonnen!“.
Beispiel 6 (Verlust):
Eingabe: X
Anzeige: P _ A N _
Fehlversuche: 6 (maximal)
Das Wort wurde nicht rechtzeitig erraten, die maximale Anzahl an Fehlversuchen ist erreicht und das Spiel endet mit der Meldung „Verloren!“.

Erläuterung:

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


Zusammenfassung:
Dieses Hangman-Spiel zeigt auf einfache Weise, wie ein klassisches Konsolenspiel in Python umgesetzt werden kann. Es verwendet eine feste Wortliste, aus der das Programm zufällig ein Wort auswählt, und ASCII-Grafiken, um den Fortschritt des Spiels visuell darzustellen. Die Hauptlogik befindet sich in der Funktion run_game(), die Eingaben verarbeitet, das Wort überprüft und den aktuellen Spielstand aktualisiert.




# KI-Fallstudie-2: Abgabe bis 29.5.2026

**Rollenverteilung:**  
Lead Developer & GUI Verantwortlicher: Malik  
Testverantwortlicher: Max  
KI-Reflexionsbeauftragter: Luke  
Assistant Developer & Dokumentationsbeauftragter: Sohrab  
Präsentationsbeauftragter: Lukasz  

**Organisatorischer Ablauf**  
Nach Bekanntgabe der Aufgabenstellung im Sommersemester 2026 haben wir uns am 14. Mai 2026 als Gruppe zusammengefunden, um die Aufgabenverteilung für das neue Semester zu besprechen. Die Kommunikation lief wie im Wintersemester über die bestehende WhatsApp-Gruppe, ergänzt durch persönliche Treffen nach den Vorlesungen. Die Rollen wurden neu verhandelt, orientierten sich aber an den Stärken aus dem ersten Semester. Wie zuvor beschreiben die Rollen Hauptverantwortlichkeiten – gegenseitige Unterstützung war selbstverständlich.

**Projektbeschreibung – GUI-Version**  
Im zweiten Semester wurde das bestehende Hangman-Konsolenspiel um eine grafische Benutzeroberfläche erweitert. Die Spiellogik aus Game_Hangman.py sowie alle unterstützenden Dateien aus Semester 1 blieben dabei vollständig unverändert erhalten. Die GUI wurde als neue, eigenständige Schicht über die bestehenden Komponenten gelegt und in einer separaten Datei gui.py implementiert. Das Spiel ist nun vollständig über ein Fenster bedienbar – eine Konsole wird nicht mehr benötigt.
Umgesetzt wurde die Oberfläche mit der Python-Standardbibliothek tkinter, die ohne zusätzliche Installation verfügbar ist.  
![Spielstart – leerer Galgen und verdecktes Wort](screenshots/01_spielstart.png)

**Projektstruktur**  
hangman/  
    src/  
        main.py               # Einstiegspunkt: startet die GUI über gui.main()  
        gui.py                # GUI-Klasse HangmanGUI mit tkinter  
        Game_Hangman.py       # ursprüngliche CLI-Spiellogik (Semester 1, unverändert)  
        Galgen_Hangman.py     # ASCII-Grafiken (HANGMAN_ART-Dictionary + display_man())  
        Words_Hangman.py      # Wortliste als Tupel (unverändert)  
    docs/  
        README.md  

Hinweis zur Struktur: Game_Hangman.py bleibt als erhaltene CLI-Version vollständig im Projekt. Die GUI greift nicht auf diese Datei zurück, sondern implementiert die Spiellogik eigenständig innerhalb der HangmanGUI-Klasse. Gemeinsam genutzt werden weiterhin Words_Hangman.py (Wortauswahl) und Galgen_Hangman.py (ASCII-Darstellung des Galgens über das HANGMAN_ART-Dictionary).  

**Technische Umsetzung:**  
Die gesamte GUI ist in der Klasse HangmanGUI in gui.py umgesetzt. Das Fenster hat eine feste Größe von 600×700 Pixeln und einen einheitlichen Hintergrund. Alle Widgets werden in der Methode create_widgets() erstellt, der Spielzustand wird über Instanzvariablen (answer, hint, wrong_guesses, guessed_letters, game_over) verwaltet.
Verwendete Widget-Typen:

tk.Label – Titel, Wortanzeige, Fehlerstand, geratene Buchstaben, Beschriftungen
tk.Text – Anzeige der ASCII-Galgen-Grafik (schreibgeschützt, Courier-Schrift)
tk.Entry – Eingabefeld für den Buchstaben (Breite 3, zentriert)
tk.Button – „Raten"-Button (grün), „Neues Spiel" (blau), „Beenden" (grau)
tk.Frame – Gruppierung von Eingabe- und Button-Bereich
messagebox (aus tkinter) – Dialoge für richtige/falsche Eingaben, Gewinn, Verlust und ungültige Eingaben

Layout: Alle Elemente werden mit dem pack-Manager angeordnet. Eingabe- und Button-Bereich nutzen zusätzlich tk.Frame mit horizontalem pack(side=tk.LEFT).
Ereignisbehandlung:

Der „Raten"-Button ist mit guess_button_click() verknüpft
Die Enter-Taste im Eingabefeld löst ebenfalls guess_button_click() aus (bind("<Return>"))
Der „Neues Spiel"-Button ruft new_game() auf, setzt alle Spielvariablen zurück und aktualisiert alle Anzeigen

**Aktualisierungsmethoden:**  
MethodeFunktionupdate_hangman_display()Schreibt die aktuelle ASCII-Grafik aus HANGMAN_ART ins Text-Widgetupdate_word_display()Zeigt den aktuellen Hinweis (z. B. _ _ A _ _) im Label anupdate_error_display()Aktualisiert die Fehleranzeige (Fehler: 2/7)update_guessed_display()Zeigt alle bereits geratenen Buchstaben sortiert an
Fehlerbehandlung in der GUI:
Ungültige Eingaben (keine einzelnen Buchstaben, bereits geratene Buchstaben) werden über messagebox.showerror() bzw. messagebox.showwarning() direkt im Fenster zurückgemeldet. Der Spielablauf wird dabei nicht unterbrochen.
![Gewinn-Dialog](screenshots/04_gewonnen_dialog.png)  
![Verlust-Dialog und Totenkopf-Grafik](screenshots/05_verloren_dialog.png)  
![Fehlermeldung bei ungültiger Eingabe](screenshots/06_fehler_eingabe.png)  

**Bedienungsanleitung – GUI-Version**  
Das Spiel wird durch Ausführen von main.py gestartet. Es öffnet sich ein Fenster mit dem Galgen, dem aktuellen Wortstand, der Fehleranzeige und dem Eingabefeld. Der Spieler gibt einen einzelnen Buchstaben ein und bestätigt per „Raten"-Button oder Enter-Taste. Nach jeder Eingabe erscheint ein kurzes Dialogfenster mit der Rückmeldung. Bei Gewinn oder Verlust wird das Lösungswort im Dialog angezeigt. Über „Neues Spiel" kann jederzeit eine neue Runde gestartet werden, über „Beenden" wird die Anwendung geschlossen.

**Versionskontrolle**  
Die Weiterentwicklung erfolgte im bestehenden GitHub-Repository. Für die GUI-Erweiterung wurde ein eigener Branch angelegt und nach Fertigstellung per Pull Request in den Hauptbranch gemergt, sodass der ursprüngliche CLI-Code zu jedem Zeitpunkt nachvollziehbar erhalten bleibt.


