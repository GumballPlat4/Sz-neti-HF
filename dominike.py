#c. Ha az óra elején üres a pénztárcája, mennyi van benne az óra végén?
#e. Hány pennyt kapott összesen (feltételezve, hogy csak azt fizették pennyben, amit nem lehet fontban)?
#g. Mi állt a legnagyobb számlán, amit fizettek a pincérnél?
#i. Hányadik vendég fizetett 9 fontot?
#k. Ha volt olyan vendég, aki tíz fontnál többet fizetett, akkor mondjuk meg, hogy hányadik vendég volt az utolsó ilyen
#m. Ha a főnöke minden vendég után fél fontot ad pincérünknek fizetésül, mekkora bevétellel zárta az órát?
def beolvasas():
    lista=[]
    with open ("./adatok/liba_adatok.txt","r",encoding="UTF-8") as fm:
        for sor in fm:
            lista.append(int(sor.strip()))
    return lista


def osszegzes(l):
    penz_mennyiseg = 0
    for osszeg in l:
        penz_mennyiseg += osszeg
  

def pennyt_kapott(l):
    osszes_penny = 0

    for osszeg in l:
        if osszeg < 1:
            osszes_penny += abs(int(osszeg * 100))
            
def legnagyobb_osszeg_l(l,):
    legnagyobb_osszeg = max(l)
    
def hanyadik_fiz_9(l):
    vendeg_sorszam = 1

    for osszeg in l:
        if osszeg == 9:
            print("A(z)", vendeg_sorszam, ". vendég fizetett 9 fontot.")
            return  
        vendeg_sorszam += 1
    else:
        print("Nem található olyan vendég, aki 9 fontot fizetett.")

def volt_aki_tobb_fiz_10(l):
    utolso_tiz_font_felett = None
    for i, osszeg in enumerate(l, start=1):
        if osszeg > 10:
            utolso_tiz_font_felett = i
    
def ha_a_fonok(l):
    bevetel = 0
    utolso_tiz_font_feletti_vendeg = None

    for i, osszeg in enumerate(l, start=1):
        bevetel += osszeg
        if osszeg > 10:
            utolso_tiz_font_feletti_vendeg = i

    
    főnöktől_kapott_fizetés = len(l) * 0.5  
    bevetel += főnöktől_kapott_fizetés

    

    






def kiir(e_p_v,e_p_k,l_o_sz,v_t_t,u_t_f):
    print("Az óra végén a pénztárca mennyisége:", e_p_v)
    print("Az összes penny mennyisége:",e_p_k )
    print("A legnagyobb összeg a pénztárcában:", l_o_sz)
    if v_t_t is not None:
        print("Az utolsó olyan vendég, aki tíz fontnál többet fizetett, a(z)", v_t_t, ". vendég volt.")
    else:
        print("Nem volt olyan vendég, aki tíz fontnál többet fizetett.")
        
    if u_t_f is not None:
        print("Az utolsó tíz fontot meghaladó összeget fizető vendég:", 
            u_t_f, ".")
    else:
        print("Nem volt olyan vendég, aki tíz fontot meghaladó összeget fizetett.")

   


lista=beolvasas()

ennyi_penze_van_ora_vegen=osszegzes(lista)
ennyi_pennyt_kapott_osszesen=pennyt_kapott(lista)
legnagyobb_osszeg_a_szamlan=legnagyobb_osszeg_l(lista)
hanyadik_vendeg_fizetett_9_fontot=hanyadik_fiz_9(lista)
volt_aki_tiznel_tobbet_fizetett=volt_aki_tobb_fiz_10(lista)
ha_a_fonok_minden_vendeg_utan_fel_fontot_ad=ha_a_fonok(lista)



kiir(ennyi_penze_van_ora_vegen,ennyi_pennyt_kapott_osszesen,legnagyobb_osszeg_a_szamlan,hanyadik_vendeg_fizetett_9_fontot,volt_aki_tiznel_tobbet_fizetett,ha_a_fonok_minden_vendeg_utan_fel_fontot_ad)




