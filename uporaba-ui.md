# Poročilo o uporabi umetne inteligence

Pri izdelavi projektne naloge sem orodje UI (ChatGPT) uporabljala kot pomoč pri iskanju ustreznih funkcij knjižnic Pandas in Matplotlib ter pregledu kode.

### Primer 1: Izračun deleža točk po sezonah (Pandas)

**Moje vprašanje:**
- *Kako v Pandas za vsako vrstico izračunam delež točk glede na seštevek točk samo tiste sezone, ne da bi morala delati ločene zanke?*

**Odgovor UI:**
- Najbolj eleganten in hiter način v knjižnici Pandas je uporaba metode .groupby() v kombinaciji z metodo .transform('sum'). S tem se izognemo zankam (for), koda pa je hitra in berljiva.

Rešitev v eni vrstici
df['delez_tock'] = df['tocke'] / df.groupby('sezona')['tocke'].transform('sum')

Kako to deluje po korakih?

df.groupby('sezona')['tocke']:
Podatke razdeli v skupine glede na stolpec 'sezona' in izbere stolpec 'tocke'.

.transform('sum'):
Za vsako sezono izračuna skupno vsoto točk:
$$\text{Vsota sezone} = \sum \text{točke v tej sezoni}$$
Za razliko od navadne metode .sum() (ki bi skrčila tabelo na število sezon), .transform('sum') ohrani prvotno število vrstic in vsaki posamezni vrstici pripiše skupno vsoto njene sezone.

df['tocke'] / ...:
Točke posamezne vrstice deli z vsoto točk tiste sezone:
$$\text{Delež} = \frac{\text{točke vrstice}}{\text{vsota točk sezone}}$$

**Moje vprašanje:**
- *Kako v Matplotlib na točkastem grafu s funkcijo annotate avtomatsko označim točko z največjo vrednostjo točk (ime dirkača in sezono)?*

**Odgovor UI:**
Za avtomatsko označitev točke z največjo vrednostjo moramo nalogo razdeliti na $3$ preproste korake:

Poiščemo celotno vrstico z rekordom (Pandas).
Izluščimo besedilo in koordinate $(x, y)$.
Povemo funkciji plt.annotate(), kaj in kam naj nariše (Matplotlib).

1. Korak: Kako najdemo vrstico z največ točkami?
Če bi uporabili samo:
df["tocke"].max()

bi dobili le številko (npr. $575$). S tem ne vemo, kdo je ta dirkač, v kateri sezoni je to dosegel ali kje na $x$-osi se nahaja.
Zato uporabimo metodo .idxmax():

df["tocke"].idxmax() poišče indeks (številko vrstice), kjer se nahaja največja vrednost.
Nato s pomočjo df.loc[...] izberemo celotno vrstico s tem indeksom:

rekord = df.loc[df["tocke"].idxmax()]

Spremenljivka rekord zdaj vsebuje celotno vrstico: ime dirkača, sezono, mesto in točke.

2. Korak: Katere podatke potrebujemo za graf?
Za oznako na grafu potrebujemo dvoje:

Besedilo, ki ga želimo izpisati:
Uporabimo formatiran niz ($f\text{-string}$):
f"{rekord['dirkac']} ({rekord['sezona']})"

To ustvari napis, npr. "Verstappen (2023)".

Točne koordinate $(x, y)$ točke na grafu:

$x\text{-koordinata}$: rekord["mesto"]
$y\text{-koordinata}$: rekord["tocke"]
Skupaj tvorita par: (rekord["mesto"], rekord["tocke"]).

3. Korak: Kako deluje funkcija plt.annotate()?
Funkcija plt.annotate() sprejme več parametrov, ki točno določajo, kako bo oznaka videti:
plt.annotate(
    f"{rekord['dirkac']} ({rekord['sezona']})",  # 1. Kaj naj piše
    (rekord["mesto"], rekord["tocke"]),          # 2. Točka na grafu (x, y)
    xytext=(10, -5),                             # 3. Odmik besedila
    textcoords="offset points",                  # 4. Način odmika
    fontweight="bold"                            # 5. Oblika pisave
)

Pomen posameznih delov:

xy = (x, y): To so koordinate pike na grafu, ki jo želimo označiti.
textcoords="offset points" in xytext=(10, -5): Če besedila ne bi zamaknili, bi se izpisalo točno čez piko. S tem parametrom rečemo: “Premakni besedilo za $10$ pik desno in $5$ pik navzdol od same točke.”
fontweight="bold": Odebeli napis, da izstopa.

