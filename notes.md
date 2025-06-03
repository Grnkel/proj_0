# Vad håller jag på med nu?
* __fixa klass för världen__
    * updateringar, logik (global constraints)
    * funktion att enforcea gränser

# Idéer att testa

* __Ship klassen för punkten__
    * Lägg till pure path-finding strategier som man väljer mellan, olika målsöknings-strategier

    * Den som är målsökande har möjlighet att prediktera var den andra kommer att vara givet alla möjliga svängar, träna ai på detta

    * Varje skepp har ett målskepp som åker perfekt, skeppet reglerar för att följa efter, kan vara så att målskeppet saktar ner om det åker för långt bort
    
    * När den kommer för nära en viss kant så ändrar den riktning , kan använda random eller något beroende på

    * Gör att den kan ha olika punkter som den hoppar mellan lite som gravitation och jorden

    * skepp kan skjuta varandra och att det blir en träff - skeppet försvinner

    * instansera massa skepp som vill skjuta varandra randomly, går det att få ett skepp att fatta att den blir jagad? olika lag av skepp som strider mot varandra, randomly blir arga på varandra och börjar skjuta

    * vill jag skapa en topologisk torus så kan jag använda modulus operatorn på punkternas kordinater.

* __skapa en klass för världen__
    
    * instansera begränsningar, global constraints (hastighet, sväng)


* __jordklot istället för kordinatsystem__

    * skeppen existerar enbart inom ett visst spann (mellan radien av jorden och av atmosfären)

* __höj frameraten så att det är enbart en skala av hur kontinuerlig man vill ha simuleringen__


