# vef2018verk2
## skila 11.feb
#### 1. MVC (3%)

##### a. Útskýrðu MVC í bakendavefþróun (lágmark 50 orð)

##### b. Hvað er AJAX og HTML5 WebSockets? (lágmark 25 orð)

##### c. Útskýrðu MV* í framendavefþróun, SPA og client-side MVC (lágmark 50 orð)

#### 2. Flask Structure (7%)

Búið til vefapp með Flask.
Bókalisti (3 bækur) þar sem hægt er að velja bókarheiti af lista (t.d. með smell) og fá
nánari upplýsingar um bók (ný vefsíða með nánri upplýsingum um bók og tengil aftur á
listann). Viðmót og útlit á vefsíðu á vera í algjöru lágmarki.


Model: Halda þarf utan um nafn bókar, útgáfufyrirtæki og útgáfuár. Aðferðir sem sjá
um að sækja bókalista og bókalýsingu. Það þarf ekki að nota db eða flat file
system fyrir gögn, það er nóg að nota lista.


Controller: Tekur við input frá notanda (request) bregst við og uppfærir model eftir
þörfum og renderar View. Notaðu routing.


View: Inniheldur alla “display logic” við framsetningu gagna (myndun HTML). Hefur
beinan aðgang að Model (get data). Notaðu Jinja template kerfið og
smávegis CSS fyrir vefútlit.


Skoðaðu mismunandi skipulag (e. structure). Notaðu Package, klasa (e classes) eftir þörfum
og skipulagðu vefinn og skrárnar í samræmi við MVC til að leysa verkefnið. Skoðaðu
BluePrint fyrir routing (ekki skylda í þessu verkefni)*
