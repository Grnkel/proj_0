# Idéer att testa

* __Ship klassen för punkten__
    * Lägg till pure path-finding strategier som man väljer mellan, olika målsöknings-strategier

    * Den som är målsökande har möjlighet att prediktera var den andra kommer att vara givet alla möjliga svängar, träna ai på detta

    * Varje skepp har ett målskepp som åker perfekt, skeppet reglerar för att följa efter, kan vara så att målskeppet saktar ner om det åker för långt bort
    
    * När den kommer för nära en viss kant så ändrar den riktning , kan använda random eller något beroende på

    * Gör att den kan ha olika punkter som den hoppar mellan lite som gravitation och jorden

    * skepp kan skjuta varandra och att det blir en träff - skeppet försvinner

* __skapa en klass för världen__
    
    * instansera begränsningar, global constraints (hastighet, sväng)

    * lista för alla objekt
    
    * updatera hela världen istället för objekt

* __jordklot istället för kordinatsystem__

    * skeppen existerar enbart inom ett visst spann (mellan radien av jorden och av atmosfären)

