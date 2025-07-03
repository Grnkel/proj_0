# Vad håller jag på med nu?
* __fixa klass för världen__
    * updateringar, logik (global constraints)
    * funktion att enforcea gränser
        * håller på att få saker att ändra riktning enligt en viss algoritm

# Idéer att testa

* __Ship klassen för punkten__
    * Lägg till pure path-finding strategier som man väljer mellan, olika målsöknings-strategier

    * Den som är målsökande har möjlighet att prediktera var den andra kommer att vara givet alla möjliga svängar, träna ai på detta

    * Varje skepp har ett målskepp som åker perfekt, skeppet reglerar för att följa efter, kan vara så att målskeppet saktar ner om det åker för långt bort
    
    * det handlar mer om "pure trajectories" och "regler", sedan hur skepp försöker följa trajectories och blir begränsad av reglerna 
    
    * När den kommer för nära en viss kant så ändrar den riktning , kan använda random eller något beroende på

    * Gör att den kan ha olika punkter som den hoppar mellan lite som gravitation och jorden

    * skepp kan skjuta varandra och att det blir en träff - skeppet försvinner

    * instansera massa skepp som vill skjuta varandra randomly, går det att få ett skepp att fatta att den blir jagad? olika lag av skepp som strider mot varandra, randomly blir arga på varandra och börjar skjuta

    * använd vektorer istället för polärer - en updateringsfunktion som använder sig av båda två och kopplar dem. använd detta för att visualisera vektorfält för hur saker och ting ska färdas runt kartan

* __jordklot istället för kordinatsystem__

    * skeppen existerar enbart inom ett visst spann (mellan radien av jorden och av atmosfären)

* __höj frameraten så att det är enbart en skala av hur kontinuerlig man vill ha simuleringen__

* __gör skiten till mer pararell och höj prestandan__
    * tydligen kunde man vektorisera
    * om det är en supertung beräkning kan man ta multithreading

* __egen klass för tracking som skepp har__
    * det finns en "tracked" och en "tracking" 
    * lägg till error och sånt
    * att man har en "ghost" som på volvo


