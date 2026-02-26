# GitHub Checks

Wij hebben 2 checks toegevoegd aan GitHub.
Dus als jullie een pull request aanmaken gaan deze al runnen.
**Ze moeten pas goed zijn als je klaar bent met de opdracht!**
Dus schrik niet als ze aan het begin van de dag falen.

Als je niet zeker weet waarom de check faalt, kan je er altijd op klikken.
Dan zie je de file waarbij het fout gaat.

![Er is een check fout.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/8_1_check_is_fout.png)

![De check is fout, hier kan je naar kijken.](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/8_2_notebookcheck.png)



## Check Jupyter Notebook Cell Order

Deze check zorgt ervoor dat elke notebook in de repo op volgorde is gerund.
Dat wil zeggen dat je dus `restart & run all` moet doen.
De cell run order moet dus 1, 2, 3 etc. zijn.
Dit doen we zo dat jullie zeker weten dat alles goed staat.
**Als de file die de error geeft, niet de file is van de opdracht, moet je dat vermelden met een comment in de pull request.**

## Check Notebook Image References

Deze check kijkt of de plaatjes die je hebt toegevoegd ook daadwerkelijk in de folder staan.
Dit hebben we toegevoegd omdat het nog wel eens het geval is dat de foto niet goed wordt geüpload.
