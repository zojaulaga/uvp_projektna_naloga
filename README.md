# ANALIZA PODATKOV FORMULE 1 (2021–2024)

V okviru predmeta **Uvod v programiranje** sem pripravila projektno nalogo, v kateri sem analizirala rezultate dirkačev in ekip v svetovnem prvenstvu Formule 1 za zadnja štiri zaključena prvenstva (sezone 2021, 2022, 2023 in 2024). Podatki so bili zajeti z uradne spletne strani [Formula 1](https://www.formula1.com/).

## STRUKTURA REPOZITORIJA
* `README.md` – glavna predstavitvena datoteka z opisom projekta, navodili in ugotovitvami
* `zajem_podatkov.py` – skripta za prenos spletnih strani in luščenje podatkov z regularnimi izrazi
* `strani/` – mapa s shranjenimi surovimi HTML datotekami posameznih sezon
* `dirkaci_f1.csv` – končna CSV datoteka z vsemi obdelanimi podatki
* `analiza.ipynb` – Jupyter Notebook z analizo podatkov, izračuni in grafičnimi prikazi
* `uporaba-ui.md` – poročilo o uporabi umetne inteligence pri izdelavi naloge
* `.gitignore` – datoteka, ki določa, katere datoteke Git prezre

## NAVODILA ZA ZAGON
1. Za delovanje analize potrebujete nameščene knjižnice `pandas`, `matplotlib`, `requests` in `jupyter`.
2. Če želite sami ponovno prenesti strani iz spleta in ustvariti CSV datoteko, v terminalu poženite datoteko `zajem_podatkov.py`.
3. Celotna analiza podatkov, izračuni in grafični prikazi so na voljo v datoteki `analiza.ipynb`.

## PRIDOBIVANJE IN OBDELAVA PODATKOV
* V skripti `zajem_podatkov.py` se najprej s spletne strani Formule 1 prenesejo HTML strani posameznih sezon in se shranijo v mapo `strani/`.
* Nato s pomočjo regularnih izrazov iz prenesenih strani izluščim podatke o uvrstitvi, imenu dirkača, nacionalnosti, ekipi in osvojenih točkah.
* Na koncu skripta te podatke uredi in jih shrani v datoteko `dirkaci_f1.csv`.

## ANALIZA
V datoteki `analiza.ipynb` sem uvozila podatke iz `dirkaci_f1.csv` ter uporabila knjižnici Pandas in Matplotlib za:
* čiščenje, filtriranje in urejanje podatkov,
* pregled in primerjavo najuspešnejših dirkačev skozi sezone,
* analizo osvojenih točk glede na državo dirkača,
* primerjavo uspešnosti ekip (npr. stabilnost Ferrarija in Mercedesa ter vzpon McLarna),
* prikaz točkovnega sistema in vpliva uvrstitev na končni točkovni izkupiček.

## UGOTOVITVE
* Max Verstappen je v teh štirih letih zbral daleč največ točk (več kot 1.860 točk) in imel izjemno sezono 2023.
* Največji delež točk so skupaj zbrali britanski dirkači (34,0 %), saj ima Velika Britanija več vrhunskih dirkačev.
* Nizozemska je na drugem mestu po številu točk (23,8 %), pri čemer je prav vse točke osvojil Max Verstappen.
* Sezona 2021 je bila točkovno najbolj izenačena med vodilnima dirkačema, medtem ko sta bili sezoni 2022 in 2023 precej manj napeti.
* V sezoni 2024 je McLaren naredil velik točkovni skok in se močno približal vrhu.
* Točkovni sistem močno nagrajuje prva mesta, saj dirkači od 10. mesta naprej ne dobijo nobenih točk.
