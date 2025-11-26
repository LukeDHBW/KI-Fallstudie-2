
import random

# Wörterliste
words = ("Abendbrot", "Abenteuer", "Abfalleimer", "Abschluss", "Abteilung", "Achterbahn", "Ackerbau", "Adlerschwinge",
    "Akkuschrauber", "Aktentasche", "Aktivität", "Albtraum", "Alligator", "Alufolie", "Ameisenbär", "Amselgesang",
    "Ananas", "Andenken", "Angebot", "Anglerfisch", "Anhänger", "Anschlag", "Antilope", "Antwort",
    "Apfelbaum", "Apfelsine", "Apotheke", "Appetit", "Aquarium", "Arbeitsamt", "Architekt", "Armband",
    "Aschenbecher", "Astronaut", "Atemzug", "Aufgabe", "Aufkleber", "Aufzug", "Augenblick", "Augenbraue",
    "Ausbildung", "Ausdruck", "Ausflug", "Ausgang", "Aushilfen", "Ausland", "Aussicht", "Australien",
    "Autobahn", "Automechanik", "Autopilot", "Backofen", "Backstein", "Badezimmer", "Bahnhof", "Bakterie",
    "Balkontür", "Ballermann", "Bambusrohr", "Banane", "Bananenschale", "Bandwurm", "Bankkaufmann", "Barhocker",
    "Barzahlung", "Batterie", "Bauarbeiter", "Bauernhof", "Baumhaus", "Baumkuchen", "Baumstamm", "Baustelle",
    "Becherglas", "Beifahrer", "Beinbruch", "Beispiel", "Benzintank", "Bergbau", "Bergsteiger", "Besucher",
    "Betonmischer", "Bettwäsche", "Bewerbung", "Bewohner", "Bibliothek", "Biergarten", "Bilderbuch", "Bildschirm",
    "Biologie", "Birnenbaum", "Blauwal", "Bleistift", "Blitzschlag", "Blockflöte", "Blumenkohl", "Blumentopf",
    "Blutgruppe", "Bohnensuppe", "Bohrinsel", "Bombenwetter", "Bootsfahrt", "Botschaft", "Brandung", "Bratpfanne",
    "Bratwurst", "Briefkasten", "Briefmarke", "Brieftasche", "Brombeere", "Brötchen", "Brückenkopf", "Brustkorb",
    "Buchhalter", "Buchstabe", "Bügelbrett", "Bügeleisen", "Bundestag", "Buntstift", "Burgherr", "Büroklammer",
    "Bürgermeister", "Busfahrer", "Bushaltestelle", "Butterbrot", "Camping", "Champignon", "Charakter", "Chefarzt",
    "Chemiebaukasten", "Chinesisch", "Chorleiter", "Christbaum", "Computer", "Container", "Dachboden", "Dachdecker",
    "Dackelblick", "Dampfwalze", "Dankbarkeit", "Darmflora", "Datenbank", "Datenschutz", "Daumenkino", "Deckname",
    "Delfinschwimmen", "Denkmal", "Desinfektion", "Deutschland", "Diamant", "Dienstag", "Dienstplan", "Digitaluhr",
    "Dinosaurier", "Direktor", "Diskussion", "Dokument", "Dolmetscher", "Donnerstag", "Doppelbett", "Dorfteich",
    "Dornbusch", "Dosenöffner", "Drachen", "Drahtesel", "Drehbuch", "Drehkreuz", "Dreieck", "Druckerei",
    "Dschungel", "Dudelsack", "Duschkabine", "Duschkopf", "Ebenholz", "Echtheit", "Edelstein", "Ehepartner",
    "Ehrenmann", "Eichhörnchen", "Eidechse", "Eierbecher", "Eieruhr", "Eiffelturm", "Eigentum", "Einbahnstraße",
    "Einbrecher", "Eindruck", "Einfahrt", "Eingang", "Einhorn", "Einkauf", "Einladung", "Einsamkeit",
    "Eiscreme", "Eisenbahn", "Eiswürfel", "Elefant", "Elektriker", "Ellenbogen", "Elternhaus", "Empfang",
    "Endspurt", "Energie", "Engelshaar", "Enkelkind", "Entdeckung", "Entfernung", "Entscheidung", "Entschuldigung",
    "Erdbeere", "Erdbeben", "Erdgeschoss", "Erdmännchen", "Erfahrung", "Erfindung", "Ergebnis", "Erinnerung",
    "Erkältung", "Erlaubnis", "Erlebnis", "Ernährung", "Erntefest", "Eroberung", "Ersatzteil", "Erscheinung",
    "Erwartung", "Erzählung", "Erziehung", "Eselsohr", "Espresso", "Esszimmer", "Etagenbett", "Eukalyptus",
    "Europa", "Explosion", "Fabriktor", "Fachmann", "Fadenkreuz", "Fahrbahn", "Fahrkarte", "Fahrplan",
    "Fahrrad", "Fahrstuhl", "Fahrzeug", "Fallschirm", "Familie", "Fantasie", "Farbfilm", "Farbstift",
    "Fassanstich", "Faustrecht", "Faustschlag", "Federbett", "Federhalter", "Fehler", "Feierabend", "Feiertag",
    "Feldbett", "Feldstecher", "Felsenmeer", "Fenster", "Fensterbank", "Ferienhaus", "Fernbedienung", "Fernglas",
    "Fernseher", "Fernweh", "Ferse", "Fertigung", "Festplatte", "Feuerball", "Feuerfest", "Feuerwehr",
    "Feuerwerk", "Feuerzeug", "Fichtenwald", "Filmstar", "Filtertüte", "Fingerhut", "Finsternis", "Fischerei",
    "Fischkutter", "Fischmarkt", "Fischteich", "Flachland", "Flamingo", "Flaschenpost", "Fleischer", "Fleischerei",
    "Fleißarbeit", "Fliegenpilz", "Flohmarkt", "Flugblatt", "Flughafen", "Flugplatz", "Flugzeug", "Flussbett")

# ASCII-Art für Galgen + Männchen
hangman_art = {
    0: (
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        "
    ),
    1: (
        "         ",
        "        |",
        "        |",
        "        |",
        "        |",
        "       / \\"
    ),
    2: (
        "  +-----+",
        "        |",
        "        |",
        "        |",
        "        |",
        "       / \\"
    ),
    3: (
        "  +-----+",
        "  |     |",
        "        |",
        "        |",
        "        |",
        "       / \\"
    ),
    4: (
        "  +-----+",
        "  |     |",
        "  O     |",
        "        |",
        "        |",
        "       / \\"
    ),
    5: (
        "  +-----+",
        "  |     |",
        "  O     |",
        "  |     |",
        "        |",
        "       / \\"
    ),
    6: (
        "  +-----+",
        "  |     |",
        "  O     |",
        " /|\\    |",
        "        |",
        "       / \\"
    ),
    7: (
        "  +-----+",
        "  |     |",
        " 💀     |",
        " /|\\    |",
        " / \\    |",
        "       / \\"
    ),
}

# Anzeige des Galgens
def display_man(wrong_guesses):
    print("***********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***********")

# Anzeige des aktuellen Wortes
def display_hint(hint):
    print(" ".join(hint))

# Anzeige des vollständigen Wortes
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong = len(hangman_art) - 1
    is_running = True

    while is_running:
        print("-" * 30)  # Visuelle Abtrennung
        display_man(wrong_guesses)
        display_hint(hint)
        print(f"Geratene Buchstaben: {' '.join(sorted(guessed_letters))}")
        
        guess = input("Gib einen Buchstaben ein: ").upper()

        # Eingabe validieren
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Bitte gib einen einzelnen Buchstaben ein.")
            continue

        # Prüfen, ob Buchstabe schon geraten wurde
        if guess in guessed_letters:
            print(f"❗ {guess} wurde bereits geraten.")
            continue

        guessed_letters.add(guess)

        # Prüfen, ob Buchstabe im Wort ist
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"❌ Falsch! Fehler: {wrong_guesses}/{max_wrong}")

        
        if "_" not in hint:
            print("-" * 30)
            display_man(wrong_guesses)
            display_answer(answer)
            print("🎉 GEWONNEN!")
            is_running = False
        elif wrong_guesses >= max_wrong:
            print("-" * 30)
            display_man(wrong_guesses)
            display_answer(answer)
            print("⚰️  VERLOREN!⚰️")
            is_running = False

if __name__ == "__main__":
    main()

