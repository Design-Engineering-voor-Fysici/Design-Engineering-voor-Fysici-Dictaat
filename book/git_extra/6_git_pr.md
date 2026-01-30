# Git Pull Request

Om nu jullie opdracht na te laten kijken en terug te mergen met de `main` branch gaan we een pull request (PR) doen.
De pull request doe je als je klaar bent.
GitHub kijkt dan of alles klopt en runt checks die wij hebben toegevoegd.

## Nakijken

Om na te kijken gebruiken wij het review-systeem van Git in de PRs.
Als de PR is aangemaakt kan je rechts bovenin een reviewer aanklikken en zet je de link van de PR in BS.
Dit moet jullie TA worden, deze gaat dan nakijken en laat wat comments achter en vraagt misschien om verandering als we vinden dat het nog niet helemaal correct is.
Als dit zo is, dan moeten jullie aanpassingen gaan maken, dit kan gewoon weer in dezelfde branch met nieuwe commits (vb: commentaar verwerken).
Zodra je alles hebt verbeterd, vraag je opnieuw de review aan van je TA.

## Voorbeeld

Nu alles is gesynct op mijn GitHub account ga ik een pull request doen van mijn `opdracht` branch naar `main`.

1. Ik klik op 'Compare & pull request': ![pr](../figures/git/6_1_compare.png)
2. Nu zijn we in het pull request menu: ![pr menu](../figures/git/6_2_in_pr.png)
   - **Als je de fork niet bent geleaved** Verander de base repository naar die van jezelf! ![change_base](../figures/git/6_3_verander_base_repo.png)
3. Bij reviewers moet je jouw nakijker toevoegen, in mijn geval is dit MartijnSonneveld
4. Martijn heeft nagekeken en was niet tevreden: ![niet goed](../figures/git/6_4_review_niet_geaccepteerd.png)
5. Ik maak veranderingen en commit en push die, daarna kan ik nog een review aanvragen van Martijn: ![nieuwe review](../figures/git/6_5_rerequest_review.png)
6. Deze keer vond Martijn het goed! Nu willen we mergen met de `main` branch, squash en merge om precies te zijn!
   - ![merge](../figures/git/6_6_merge.png)
   - ![squashmerge](../figures/git/6_7_squash_merge1.png)
   - ![squashmerge2](../figures/git/6_8_squash_merge2.png)
   - Dan deleten we de branch: ![delete](../figures/git/6_9_delete_branch.png)
 