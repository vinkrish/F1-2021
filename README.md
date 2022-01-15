# F1-2021

The idea behind this analysis is to show who is the better driver in a given car, we cannot argue who is the best f1 driver considering they all drive different cars so the logical way to compare best driver is by comparing how they performed in their respective car against their own teammates.

Removed Haas from both qualifying and race results as I don't consider Mazepin as a challenger for Schumacher, Schumacher does exceptionally well for Haas so no disrespect.

## About Code

`f1_2021_qualifying_results.py` parses all qualifying results from motorsport website.  
`f1_2021_race_results.py` parses all race results from motorsport website.

`f1_2021_qualifying_winners.py` finds qualifying winner by comparing qualifying time among teammates and having largest gap.  
`f1_2021_race_winners.py` finds race winner by comparing race time among teammates and having largest gap.

`f1_2021_qualifying_winner.py` finds how many qualifying a respective driver outperformed teammate and stood first by having largest gap among all drivers.  
`f1_2021_race_winner.py` finds how many races a respective driver outperformed teammate and stood first by having largest gap among all drivers.

## Criteria for Qualifying Winner:

Only considering qualifying time gap less than 1000 ms or 1 sec, if not the driver is not competitive enough for being in same car.

> eg: First race, Charles Leclerc won qualifying coz his gap of 537 ms compared to Carlos Sainz is the largest among drivers of same car. Even though Lance Stroll has a gap of 1.8 sec gap to Sebastian Vettel we are not considering this coz any large gap of this magnitude gives false result as we all know it's not a realistic gap.

### Qualifying Winner

Max Verstappen is the winner with 7 wins, followed by Lando Norris with 5 wins.

| Driver | Races |
| ------ | ----- |
| Max Verstappen | ['spanish-gp', 'monaco-gp', 'hungarian-gp', 'italian-gp', 'turkish-gp', 'qatar-gp', 'abu-dhabi-gp'] |
| Lando Norris | ['portuguese-gp', 'azerbaijan-gp', 'styrian-gp', 'austrian-gp', 'saudi-arabia-gp'] |
| Pierre Gasly | ['british-gp', 'united-states-gp', 'mexican-gp'] |
| Charles Leclerc | ['bahrain-gp', 'belgian-gp'] |
| Lewis Hamilton | ['emilia-romagna-gp', 'russian-gp'] |
| George Russell | ['french-gp', 'dutch-gp'] |
| Kimi Raikkonen | ['brazilian-gp'] |

## Criteria for Race Winner:

Only considering race time gap less than 60000 ms or 60 sec (no logic here just random number assumed), if not the driver is not competitive enough for being in same car.

> eg: First race, Max Verstappen won race coz his gap of 51302 ms compared to Sergio Perez is the largest among drivers of same car. Even though Hamilton won the actual race his gap to Bottas was 37383 ms, we are not considering large gap of more than 60000 ms or 1 min as it gives false result involving bad drivers in the circuit.
### Race Winner

Max Verstappen is the winner with 8 wins, followed by Lewis Hamilton with 3 wins.

| Driver | Races |
| ------ | ----- |
| Max Verstappen | ['bahrain-gp', 'spanish-gp', 'styrian-gp', 'austrian-gp', 'dutch-gp', 'russian-gp', 'united-states-gp', 'qatar-gp'] |
| Lewis Hamilton | ['portuguese-gp', 'saudi-arabia-gp', 'abu-dhabi-gp'] |
| Lando Norris | ['emilia-romagna-gp', 'monaco-gp'] |
| Valtteri Bottas | ['azerbaijan-gp', 'turkish-gp'] |
| Kimi Raikkonen | ['hungarian-gp', 'brazilian-gp'] |
| George Russell | ['french-gp'] |
| Charles Leclerc | ['british-gp'] |
| Lance Stroll | ['italian-gp'] |
| Fernando Alonso | ['mexican-gp'] |

#### Final Thoughts

Max came out winner in both qualifying and race, it means either Perez is not competitive enough or Max is exceptionally good - Acceptance of this analysis is left to your own understanding of the sport!