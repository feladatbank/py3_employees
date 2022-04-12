"""
3.feladat:
Az "employees.txt" állomány (file) tartalmazza egy nagyválalat szoftverfejlesztő munkatársainak listáját. A sorok azonos szerkezetűek, az adattagok pontosvesszővel vannak elválasztva. Az állomány egy sora például:


            Maxine Boyle;$97093;1994;Hungary

Ahol az adattagok jelentése rendre a következő:
  - A programozó neve [Maxine Boyle]
  - A programozó éves bruttó jövedelme USD-ben [$97093]
  - A programozó születési éve: [1994]
  - A programozó székhelye (melyik országból dolgozik) [Hungary]

Hozz létre egy osztályt (class) létrehozása NEM KÖTELEZŐ DE több pontot lehet kapni osztéyl használata esetén, ami reprezentálja egy alkalmazott példányait (object) istance. Az osztály konstruktora (constructor) paraméterként kapja meg a beolvasott sort, és ebből határozza meg az adott attribútomokat (property). 

3.1: Olvasd be az állomány tartalmát, és tárold le egy homogén listában. Ennek a listának a felhasználásával oldd meg az alábbi feladatokat, a kiírás legyen a mintának megfelelő!

3.2: Írd ki a terminálra, hogy hány alkalmazott adatai szerepelnek az állományban!

3.3: Íird ki a terminálra, az alkamazottak havi átlagjövedelmét!

3.4: Kérj be a terminálról egy nevet, és ha van ilyen nevű dolgozó a listában, írd ki az életkorát, a székhelyét és a havi jövedelmét HUF-ba átszámolva ami 361.51 HUF/USD árfolyammal kell elvégezni!! Ha nincs ilyen nevű dolgozó a listában, a "nincs" ilyen nevűű alkalmazott a cégnél" szöveget jelenítcsd meg! (Feltételezheted, hogy nincs két azonos nevű alkalmazott, a mintában.)

tipp:

Az éves fizetésből a pénznemet ($) utasítással tudod eltávolítani számmá alakítás előtt. -a.strip() ha adsz neki paramétert, akkor a paraméterben szereplő karaktereket távolítja el a karakterláncből. pl:.

      self.eves_fizetes: int(spl[1].srip('$'))

Minta/output: _____________________________________________________

3.feladat:
3.2: a cégnél 73 programozó dolgozik!
3.3: az alkalmazottak havi átlag jövedelme: $86098.8
3.4: írd be a kerestt nevet:Quinn Stark
    életkor:    27
    székhely:    Hungary
    havi fizetés:    24188634 HUF

____________________________________________________________________



"""
#Britanney Cummings;$55486;1993;Romania
#1

class Munkatársak:
  def __init__(self,sor):
    nev,jovedelem,szuletes,helyileg_hol = sor.strip().split(";")
    self.nev = nev
    self.jovedelem = jovedelem.replace('$', '')
    self.szuletes = int(szuletes)
    self.helyileg_hol = helyileg_hol

with open("employees.txt","r",encoding="latin2") as f:
  lista = [Munkatársak(sor) for sor in f]

#2

print("3.feladat:")
print(f"3.2: a cégnél {len(lista)} programozó dolgozik!")

#3

jovedelmek = [int(sor.jovedelem) for sor in lista]
ossz = sum(jovedelmek)
atlag = ossz / len(jovedelmek)

print(f"3.3: az alkalmazottak havi átlag jövedelme: ${atlag:.1f}")

#4
