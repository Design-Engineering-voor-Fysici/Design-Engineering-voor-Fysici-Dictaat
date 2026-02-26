# Samenwerken met Git

Voor de woensdagen werken jullie als het goed is op 1 laptop.
Dit maakt werken met GitHub wat simpeler; 1 persoon zet alles klaar op zijn GitHub *repo* (maak een nieuwe branch aan!) en past de notebook aan en pusht dit naar de juiste branch.

Voor de thuiswerkopdracht is het belangrijk dat jullie beiden commits maken!
Voor branches is het dan gewoonlijk om dit aan te houden: main --> opdracht 1 (elektrostatica) --> student 1, 2.
Maar het is ook prima om aan [pair programming](https://www.youtube.com/watch?v=dwUSOq-O4KU) te doen.
Dan hoef je ook niet aparte branches aan te maken voor ieder account, maar werk je op de branch van de opdracht.

Laat dus in je commits ook weten hoe je een sub-opdracht hebt gemaakt!

## Voorbeeld elektro opdrachten

Voor de elektro opdrachten is het de bedoeling dat je samen kiest in wiens *repository* je de opdracht gaat maken. 
Je werkt dus maar in **1** *repository* aan de opdracht! 
Aan het einde kan je van de *repo* waar je in werkt een *PR* aan maken naar je groepsgenoot.

Nu je hebt gekozen in 1 repo te werken, moet de groepsgenoot deze *repo* ook *clonen* naar zijn laptop. 
En maak een *branch* aan voor de opdracht, nu kan je op 2 manieren aan de opdracht werken:
1. Je gaat beide op je eigen laptop werken.
   - Werk op 1 *branch*: mits je op verschillende tijden aan de opdracht werkt, spreek dit dus dan ook af! Elke keer als je dan gaat werken, moet je eerst *git pullen*. Ook voordat je *pusht*, *pull* eerst!
   - Als je tegelijk aan de opdracht wilt werken, maak dan van je opdracht *branch*, 2 nieuwe *branches* aan. Eentje voor jullie beiden, zo voorkom je dat je elkaars werk kan overschrijven op GitHub.

2. Je werkt op 1 laptop samen: pair programming.
   - Werk in de nieuwe opdracht *branch* en schrijf duidelijke *commits* over hoe je samen aan het antwoord bent gekomen.

Dus het zou er dan zo uit zien op 1 laptop:
1 repo --nodig partner uit--> branch: main --> branch: elektro-opdracht1

En zo als je op 2 laptops werkt:
1 repo --nodig partner uit--> branch: main --> branch: elektro-opdracht1 --> 2 branches: dev_student1 + dev_student2