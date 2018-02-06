# vef2018verk2
## skila 11.feb sunnudag
#### 1. MVC (3%)

##### a. Útskýrðu MVC í bakendavefþróun (lágmark 50 orð)
Hugbúnaða arkitekta mynstur oft notuð til að þróa notanda tengi sem skiptir forrit í þrjá parta. Þetta er gert til að skipta innri framsetninguna af upplýsingun frá leiðinnar upplýsingar eru sýndir og samþykkt til notandan.
MVC hönnunar mynstrið nota þessi aðskilda aðferð til að endurnýta kóða betur og styðja samsíða þróun.

Þessi samsíða þróun þýðir að framenda forritarar og bakenda forritarar geta unnið á sínu eigin megin að forritinu án þess að þurfa eða trufla hvor aðra.

##### b. Hvað er AJAX og HTML5 WebSockets? (lágmark 25 orð)
Websockets vonar til að koma með nær-tefjalaust samskipti á netinu með tvístefnu tengingar yfir eina TCP tengingu.
Flest vafrar eins og firefox styðja websockets vegna það hefur fengið mikla vinsæld eftir 2011.
Þessi tefjalaust tvístefnt samskipti leyfir forritara að búa til forrit sem gefa upplýsingar til baka vegna tengingin er nú viðvarandi.

AJAX var búið til óvart og var svo notuð til að gera hluti sem eru utan upprunalega tilgangin.
Það gefur vafrar hæfileikan til að uppfæra upplýsingar án þess að endurhlaða alla vefsíðunna.
AJAX er miklu eldra tækni miðað við WebSockets og hefur miklu meiri stuðning og ytri tól til að nota með AJAX. 

##### c. Útskýrðu MV* í framendavefþróun, SPA og client-side MVC (lágmark 50 orð)
MV* getur verið MVC(model-view-controller), MVP(model-view-presenter) og MVVM(model-view-view-model). Þeir öll haga eins með hvernig þeir skipta í sundur forrit vegna þess þeir eru öll afleidd frá MVC.
SPA stendur fyrir single-page application, það er vef forrit sem virkilega endurskrifar vefsíðuna í staðin fyrir að ná nýjar síður sem létur vefsíðuna haga meira eins og tölvuforrit fyrir notandan.
Client side MVC þýðir að það bara bara byggt á notanda-hliðina að vef forriti.

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
