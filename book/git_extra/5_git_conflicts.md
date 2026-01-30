# Git Conflicts

Dit is iets wat jullie waarschijnlijk gaan meemaken, hier leggen we uit hoe je er mee om moet gaan.
Conflicts kunnen best tricky zijn, dus als je er niet uitkomt vraag het aan je TA!

Een conflict gebeurd als 2 pushes dezelfde regels hebben aangepast.
Git vraagt dan om een keuze te maken tussen de versies.

**Belangrijk** al kom je er niet uit, vraag hulp aan je TA.

## Voorbeeld

GitHub laat je altijd weten als er een conflict is: ![conflict komt](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_1_er_gaat_conflict_komen.png)
Onderaan de PR zie je de knop: `Resolve conflicts`, druk hierop!
![conflict](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_2_conflict.png)

Dan kom je uit bij de file die conflicten geeft, eerst het plaatje dan de uitleg.
![conflict ziet er zo uit](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_3_conflict_1.png)
De grote rode lijn aan de linkerkant en rechts van de regel-getallen laat zien om welke regels het gaat.
`<<<<<<<` tot en met `=======` gaat om jouw deel en alles daarna van de plek waar naartoe: merged of pusht! (in dit geval mergen)
Na `=======` is wat er al stond.
Tegenwoordig heeft GitHub de opties om versies te accepteren: 'Accept current change | Accept incoming change | Accept both changes'
Die spreken voor zich, maar pas op met accept both changes, soms is het makkelijker handmatig even alles goed te zetten.

Als alles is 'geresolved' ziet het er zo uit en moet je dit nog **committen**!
![conflict gefixt](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/5_4_conflict_gefixt.png)