# Git Branches

Als je de repo met de opdracht hebt geforkt dan kan je ook ook alle branches mee krijgen, voor DEF-D heb je alleen de branch main.
Een branch is een kopie van de repo, dit kan een kopie zijn van main, maar ook weer van een andere branch.
Jullie gaan een kopie van main maken.
Een branch wordt gebruikt om aan verschillende functionaliteiten te werken, voor ons betekent dat: een branch voor elke opdracht!
Jullie eerste branch zou iets zijn als: `introductie`.

![branche](../figures/git/branches.png)

## Voorbeeld: Branch maken

Nu je de repo op je eigen account hebt geforkt, klikken we op de dropdown van de branches:
![branch plek](../figures/git/4_plek_branches.png)
Dan om de nieuwe `opdracht` branch aan te maken typen we in de dropdown: 'opdracht' en klikken we: 'create branch'
![branch maken](../figures/git/5_maak_branches.png)
In hetzelfde dropdown menu als eerst kan je nu switchen tussen de branches.

## Voorbeeld: naar je branch switchen in VSCode

Om dit in VSCode te doen, gaan we eerst jullie repo clonen naar VSCode en dan de goeie branch in.
In de terminal kan je dit typen nadat je gecloned hebt: `git checkout <opdracht>`.

Het kan ook via deze manier:
1. ga naar het menu van de repo in VSCode: ![switch to branch](../figures/git/6_howto_switch_to_branch.png)
2. klik dan op de nieuwe `opdracht` branch: ![switch branch](../figures/git/7_switch_branch.png)

Pas als je in de goede branch zit, ga je werken aan je opdracht!

### Terminal (extra info)

Branch maken en meteen ernaar toe switchen:
`git checkout -b name_of_your_new_branch`
