* __Varje skepp borde verkligen ha funktionerna inom sig istället__

* __Fixa klass för världen__
    * Uppdateringar, logik (global constraints)
    * Funktion för att enforcea gränser
        * Håller på att få saker att ändra riktning enligt en viss algoritm

* __Ship-klassen för punkten__
    * Lägg till pure path-finding strategier att välja mellan (olika målsökningsstrategier)
    * Varje skepp har ett målskepp som åker "perfekt", och skeppet reglerar för att följa det
        * Målskeppet kan sakta ner om det drar ifrån för mycket
    * Fokusera på "pure trajectories" och "regler" — skepp försöker följa trajectories men begränsas av reglerna
    * När skepp kommer för nära en kant, ändrar det riktning (kan vara slump eller algoritmisk)
    * Skeppet kan ha flera punkter det "hoppar" mellan, likt gravitation kring jorden
    * Skepp kan skjuta varandra — vid träff försvinner det träffade skeppet
        * Går det att få ett skepp att förstå att det blir jagat?
        * Olika lag av skepp som strider mot varandra och randomly börjar skjuta
    * Använd vektorer istället för polära koordinater
        * Skapa en uppdateringsfunktion som kopplar båda
        * Använd för att visualisera vektorfält för navigation på kartan

* __Jordklot istället för koordinatsystem__
    * Skepp existerar enbart inom ett visst spann (mellan jordradien och atmosfären)

* __Gör skiten mer parallell och höj prestandan__
    * Använd vektorisering där det går
    * För tyngre beräkningar — överväg multithreading

* __Egen klass för tracking som skepp har__
    * Finns en "tracked" och en "tracking"
    * Lägg till felmarginaler m.m.
    * Lägg till koncept som "ghost" (likt Volvos system)
