# Git Push

Nu je de opdrachten allemaal op je eigen GitHub account hebt en een branch voor je opdracht, en je weet hoe je dit op VSCode krijgt, zijn jullie klaar om opdrachten te maken.

Als je lokaal (dus op VSCode) je opdracht hebt gemaakt met de juiste commits, gaan we pushen naar GitHub.
Als het goed is, is dit al bekend, zo ja: ga dan verder naar het samenwerken.
Zo niet, dan staat het hier ook onder bij het voorbeeld.

LET OP, voordat je inlevert, moet je `restart & run all` hebben gedaan inde notebook.

## Voorbeeld

Ik heb hier de kickoff opdracht gedaan:

1. stage al mijn verandering, dus een foto en de geupdate notebook: ![stage](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/3_1_staging.png)
2. ik schrijf de commit message: ![commit](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/3_2_commit.png)
3. dan sync (push) ik mijn VSCode naar github, dat ziet er nu zo uit: ![github gepusht](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/3_3_gepusht.png)


### Terminal

- Gebruik `git status` om te zien of er files zijn die moeten worden toegevoegd aan je staging.
- `git add <file>` staged de file die je hebt aangepast, dit hoef je niet altijd zelf te doen!
- Dan wordt het `git commit -m <jouw commit message>` om alle staged files te committen.
- Daarna: `git push`