# Git Conflicts

Dit is iets wat jullie waarschijnlijk gaan meemaken, hier leggen we uit hoe je er mee om moet gaan.
*Conflicts* kunnen best tricky zijn, al kom je er niet uit, vraag het aan je TA!

Een *conflict* gebeurd als 2 *pushes* dezelfde regels hebben aangepast.
Het voorbeeld dat volgt, is alleen voor als je *branch* en je *target branch* aan dezelfde file hebben gewerkt.
Git vraagt dan om een keuze te maken tussen de versies.

**Belangrijk** al kom je er niet uit, vraag hulp aan je TA.

## Voorbeeld

GitHub laat je altijd weten als er een *conflict* is: 

![Er gaat een conflict komen.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_1_er_gaat_conflict_komen.png)

Onderaan de PR zie je de knop: `Resolve conflicts`, druk hierop!

![Resolve conflict knop.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_2_conflict.png)

Dan kom je uit bij de file die *conflicten* geeft, eerst het plaatje dan de uitleg.
Een notebook up GitHub ziet eruit als een tekst file, dus wat je hieronder ziet is een notebook cell.

![Een conflict ziet er zo uit.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_3_conflict_1.png)

De grote rode lijn aan de linkerkant en rechts van de regel-getallen laat zien om welke regels het gaat.
`<<<<<<<` tot en met `=======` gaat om jouw deel en alles daarna van de plek waar naartoe: *merged* of *pusht*! (in dit geval mergen)
Na `=======` is wat er al stond.
Tegenwoordig heeft GitHub de opties om versies te accepteren: 'Accept current change | Accept incoming change | Accept both changes'
Die spreken voor zich, maar pas op met accept both changes, soms is het makkelijker handmatig even alles goed te zetten.

Als alles is 'geresolved' ziet het er zo uit en moet je dit nog **committen**!

![Het conflict is gefixt.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_4_conflict_gefixt.png)


## Grote conflicts in VSCode

Als je samen in 1 branch werkt en *pullt* om te gaan werken aan de opdracht bestaat de kans dat je een *merge conflict* krijgt.
Door *(git) sync* te gebruiken in VSCode doet VSCode automatisch een *pull-rebase-push*.
Dit zou dus de meeste *conflicten* meteen moeten oplossen.

De meeste van deze *conflicten* kan je zelf oplossen, hier is een lijstje van de 2 meest voorkomende:
- *execution count* is anders, kies 1 van de 2 en doe later een *restart run all*
- Python versie

Al zie je deze error in VSCode, dan moet je het volgende stuk even lezen:
![Merge error in VSCode.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_5_er_pull_conflict.png)

Klik dan op "Open Git Log" en dan zie je het volgende:
![We moeten gaan mergen.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_6_1_we_moeten_mergen.png)

En druk op het knopje die omcirkelt is, dit gaat een *merge* file aanmaken en dat ziet er zo uit:

![Zo ziet de merge eruit in VSCode.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_6_2_moeten_mergen.png)

Druk dan op "Resolve in Merge Editor", dit is de VSCode versie van hoe ze omgaan met *merge conflicts*.
Dit zou er bekend uit moeten zien, het lijkt erg op de GitHub versie:
![Zo ziet conflict eruit in VSCode.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_7_herkenbaan_conflict.png)

Ik accepteer de "incoming changes" bij deze omdat dat een betere oplossing is.
Dan fix ik de andere *merge conflicts* en klik ik op "complete merge":
![Merge completen.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_8_links_geaccepteert_complete_merge.png)

Dan zullen we links zien dat we kunnen *mergen*, druk op "continue":
![Merge completen.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_9_mergen.png)

Dan kan je een *commit message* maken en *commit+Syncen*!
![Merge completen.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_10_commit_sync.png)




