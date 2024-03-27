def adatok_beolvasasa():
    osszegek = []
    with open('adatok.txt', 'r') as file:
        for line in file:
            osszeg = float(line.strip())
            osszegek.append(osszeg)
    return osszegek

#b. Volt-e olyan, hogy a pincér vásárolt valamit, vagy mindig csak neki fizettek?
def volt_e_vasarlas(osszegek):
    for osszeg in osszegek:
        if osszeg < 0:
            return True
    return False

#input
osszegek = adatok_beolvasasa()

if volt_e_vasarlas(osszegek):
    print("A pincér vásárolt valamit.")
else:
    print("A pincérnek mindig csak fizettek.")

#d. Hány alkalommal kapott biztosan pennyt is, nem csak fontot?    
def pennyt_kapott(osszegek):
    penny_szamlalo = 0
    for osszeg in osszegek:
        if osszeg < 0 and abs(osszeg) < 1:
            penny_szamlalo += 1
    return penny_szamlalo

penny_szamlalo = pennyt_kapott(osszegek)

#f. Hány esetben kapott legalább öt fontot?
def fontot_kapott(osszegek):
    font_szamlalo = 0
    for osszeg in osszegek:
        if osszeg > 5:  
            font_szamlalo += 1
    return font_szamlalo

font_szamlalo = fontot_kapott(osszegek)

#h. Ha az óra elején már volt 8 font 23 penny a tárcájában, mennyi pénz volt benne az óra végén?
def penztarcaban_maradt(osszegek):
    penztarcaban = kezdeti_osszeg
    for osszeg in osszegek:
        penztarcaban += osszeg
    return penztarcaban

kezdeti_osszeg = 8.23





#j. Ha volt olyan vendég, aki tíz fontnál többet fizetett, akkor mondjuk meg, hogy hányadik vendég volt az első ilyen!
def elso_tiz_font_feletti_vendeg(osszegek):
    for i, osszeg in enumerate(osszegek):
        if osszeg > 10:
            return i + 1
    return None

elso_tiz_font_feletti = elso_tiz_font_feletti_vendeg(osszegek)

    
#l. Volt-e olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát?
def otfontossal_kiegyenlitheto(osszegek):
    for osszeg in osszegek:
        if osszeg % 5 == 0 and osszeg >= 5:
            return True
    return False

if otfontossal_kiegyenlitheto(osszegek):
    print("Volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")
else:
    print("Nem volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")

def kiir(vasrl, b_k, f_k, p_m, e_10_f_f, o_k):
    print(f"A pincér vásárolt valamit: {vasrl}")
    print(f"A pincér, {b_k}, alkalommal kapott biztosan pennyt")
    print(f"{f_k} alkalommal kapott biztosan pennyt is, nem csak fontot")
    print(f"Az óra végén, {p_m}, font volt a pénztárcában.")
    if elso_tiz_font_feletti is not None:
        print(f"Az első tíz fontnál többet fizető vendég a(z)", {e_10_f_f}, ". vendég volt")
    else:
        print("Nem volt olyan vendég, aki tíz fontnál többet fizetett.")
    print(f"{o_k} olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát")
    
    

#számítás
vasarlas=volt_e_vasarlas(osszegek)
biztosan_kapott=pennyt_kapott(osszegek)
font_kap=fontot_kapott(osszegek)
penz_maradt=penztarcaban_maradt(osszegek)
elso_10_font_f=elso_tiz_font_feletti_vendeg(osszegek)
otfont_kiegy=otfontossal_kiegyenlitheto(osszegek)

#output
kiir(vasarlas, biztosan_kapott, font_kap, penz_maradt, elso_10_font_f, otfont_kiegy)