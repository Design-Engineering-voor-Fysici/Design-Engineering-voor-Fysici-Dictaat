# Forking

Een *repository* (*repo*) *clonen* is handig om er zelf op jouw laptop aan te werken, maar hoe deel je nu wat jij hebt gedaan met je groepsgenoot?
Dit gaan we oplossen door de opdrachten eerst te *forken* naar je eigen GitHub account.
In essentie kopiëer je dus eerst de *repo* naar jouw account en van daar *clone* je hem naar je eigen omgeving (VSCode of jouw editor). 

Waarom? Nu kan je samen met je groepsgenoot werken aan de opdracht en heb je een plek om je werk te delen, namelijk jouw eigen GitHub *repo*!
Het is natuurlijk niet de bedoeling dat jullie jullie werk *pushen* naar de DEF *repo* ;)

## Voorbeeld

We beginnen op de [DEF-D opdracht repo](https://github.com/Design-Engineering-voor-Fysici/opdrachten-DEF-D), deze gaan jullie *forken*.
*Forken* staat rechtsbovenin aangegeven:
![fork_image](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main/figures/git/1_1_start_fork.png)
Klik op `Fork` dan kom je hier.
![gaan_forken](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/1_2_create_fork.png)
Let op dat je **alleen** de main *branch* *forked* naar jouw account, verzin een *repo* naam en `Create fork`, ik hou de naam hetzelfde: 'opdrachten-DEF-D'.

Nice, je hebt nu de DEF *repo* op je eigen account!
Het zou er nu zo uit moeten zien, dan kan je door naar het volgende onderdeel.
![forken_gelukt](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/1_3_forken_succeeded.png)

Dit is een andere manier om de *repo* te *clonen* van wat je [eerder hebt geleerd](https://contemporary-physicslab.github.io/thermolab/intro-1/).

Nodig nu je groepsgenoot uit voor jouw *repo*, of accepteer die van je groepsgenoot, mits dit nodig is.
**Nodig ook je TA uit**, dit is belangrijk voor nakijken later!
Hoe dit moet staat [hier](https://contemporary-physicslab.github.io/thermolab/intro-1/#je-partner-s-uitnodigen)

### Protecting main

Een goede eigenschap is om je main *branch* te *protecten*.
Dit zorgt er ook voor dat je met *branches* moet werken!
Hiervoor gaan we op de GitHub page naar `settings --> branches --> Add branch rule`.
![protecting main 1](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/protecting_main_1.png)

Druk op `Add branch rule`, geef de goede 'Ruleset Name', zet hem op active en geef de juiste branch targeting criteria, zet deze op default:
![protecting main 2](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/protecting_main_2.png)

Scroll dan naar beneden en vink aan: 'Require a pull request before merging' en zet Required approvals op 1:
![protecting main 3](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/protecting_main_3.png)

Druk dan op `save changes`!