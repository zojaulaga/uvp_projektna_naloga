import csv
import os
import re
import requests


def prenesi_in_shrani(url, pot_do_datoteke):
    """Prenese spletno stran in jo shrani v lokalno mapo."""
    mapa = os.path.dirname(pot_do_datoteke)
    if mapa:
        os.makedirs(mapa, exist_ok=True)
    #Ce datoteka že obstaja, je ne prenasamo še enkrat
    if os.path.exists(pot_do_datoteke):
        return
    
    glave = {"User-Agent": "Mozilla/5.0"}
    odziv = requests.get(url, headers=glave)
    if odziv.status_code == 200:
        with open (pot_do_datoteke, "w", encoding="utf-8") as d:
            d.write(odziv.text)
        print(f"Prenesena stran: {pot_do_datoteke}")
    else:
        print(f"Napaka pri prenosu {url}: {odziv.status_code}")
        
def preberi_datoteko(pot_do_datoteke):
    """Prebere vsebino shranjene HTML datoteke."""
    with open(pot_do_datoteke, "r", encoding="utf-8") as d:
        return d.read()
    
def izlusci_dirkace(vsebina_html, sezona):
    """Iz HTML vsebine z regularnimi izrazi izlušči podatke o dirkačih."""
    vzorec = (
        r'<tr[^>]*>\s*'
        r'<td[^>]*>(?P<mesto>\d+)</td>\s*'
        r'<td[^>]*>.*?<span class="max-lg:hidden">(?P<ime>[^<]+)</span>\s*<span class="max-md:hidden">(?P<priimek>[^<]+)</span>.*?</td>\s*'
        r'<td[^>]*>(?P<drzava>[A-Z]{3})</td>\s*'
        r'<td[^>]*>.*?/team/[^"]*">(?P<ekipa>[^<]+)</a>.*?</td>\s*'
        r'<td[^>]*>(?P<tocke>\d+(?:\.\d+)?)</td>\s*'
        r'</tr>'
    )

    seznam = []
    for zadetek in re.finditer(vzorec, vsebina_html, re.DOTALL):
        podatki = zadetek.groupdict()
        polno_ime = f"{podatki['ime'].strip()} {podatki['priimek'].strip()}"
        seznam.append({
            "sezona": int(sezona),
            "mesto": int(podatki["mesto"]),
            "dirkac": polno_ime,
            "drzava": podatki["drzava"].strip(),
            "ekipa": podatki["ekipa"].strip(),
            "tocke": float(podatki["tocke"])    
        })
    return seznam

def zapisi_v_csv(seznam_podatkov, pot_csv):
    """Shrani seznam slovarjev v CSV datoteko."""
    if not seznam_podatkov:
        print("Ni podatkov za shranjevanje.")
        return
    
    stolpci = ["sezona", "mesto", "dirkac", "drzava", "ekipa", "tocke"]
    with open(pot_csv, "w", encoding="utf-8", newline="") as d:
        pisec = csv.DictWriter(d, fieldnames=stolpci)
        pisec.writeheader()
        pisec.writerows(seznam_podatkov)
    print(f"Vsi podatki so uspešno shranjeni v {pot_csv}")
    
def main():
    print("Začenjam zajem podatkov...")
    vsi_dirkaci = []
    sezone = range(2021, 2025)
    
    for leto in sezone:
        url = f"https://www.formula1.com/en/results.html/{leto}/drivers.html"
        lokalna_pot = f"strani/dirkaci_{leto}.html"
        
        # 1.prenos strani
        prenesi_in_shrani(url, lokalna_pot)
        
        #2. branje shranjene strani
        vsebina = preberi_datoteko(lokalna_pot)
        
        #3. luščenje podatkov za doloceno leto
        dirkaci_leta = izlusci_dirkace(vsebina, leto)
        print(f"Sezona {leto}: najdenih {len(dirkaci_leta)} dirkačev")
        vsi_dirkaci.extend(dirkaci_leta)
        
    #4. zapis vseh sezon v en csv
    zapisi_v_csv(vsi_dirkaci, "dirkaci_f1.csv")
    
if __name__ == "__main__":
    main()