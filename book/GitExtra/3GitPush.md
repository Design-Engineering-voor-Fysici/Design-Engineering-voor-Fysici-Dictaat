# Git Push

Nu je de opdrachten allemaal op je eigen GitHub-account hebt en een *branch* voor je opdracht hebt, en je weet hoe je dit op VSCode krijgt, zijn jullie klaar om opdrachten te maken.

Als je lokaal (dus op je laptop *gecloned*) je opdracht hebt gemaakt met de juiste *commits*, gaan we *pushen* naar GitHub.
Als het goed is, is dit al bekend, zo ja: ga dan verder naar het samenwerken.
Zo niet, dan staat het hier ook onder bij het voorbeeld.

**LET OP**, voordat je inlevert, moet je `restart & run all` hebben gedaan in de notebook.
Dit moet zodat alles goed staat en plaatjes goed inladen!

## Voorbeeld

Ik heb hier de kickoff opdracht gedaan:

1. *stage* mijn verandering, dus eerst de vernieuwde notebook: ![stage](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/3_1_staging.png)
2. Dan stage ik ook de foto en dan schrijf ik de *commit message*: ![commit](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/3_2_commit.png)
   - Hoe je dit deed staat [hier](https://teachbooks.io/learn-programming/workflows/git/commits_local#a-closer-look-at-our-commits).
3. Dan *sync (push)* ik mijn VSCode naar GitHub: ![sync](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/3_4_syncing.png)
4. Dat ziet er nu zo uit: ![github gepusht](https://raw.githubusercontent.com/Design-Engineering-voor-Fysici/plaatjes-DEF/main//figures/git/3_3_gepusht.png)


### Terminal (optioneel)

Je kan als je dat wilt ook werken met de command line (ook wel terminal genoemd). 
In dat geval zijn dit de commando's die je gebruikt:

- Gebruik `git status` om te zien of er files zijn die moeten worden toegevoegd aan je *staging*.
- `git add <file>` *staged* de file die je hebt aangepast, dit hoef je niet altijd zelf te doen!
- Dan wordt het `git commit -m <jouw commit message>` om alle *staged files* te *committen*.
- Daarna: `git push`