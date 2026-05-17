import math
import datetime

print ("#3 Diskutera i grupp\n")
x=100
y=200
z = y - x / 2
'''
print("Det blir " + (y - x) " kronor över.")
Felet beror på att (y - x) är ett heltal (int), och Python kan inte lägga ihop en text (str) med ett tal direkt.
'''
print("Det blir " + str(y - x) + " kronor över.")
print("Varje person får " + str(z))
print("\n")

print("#4 Använda variabler och datatype")
x = input(f"Skriv in ett helttal: ")
print(f"Ditt tal är {x} och av typen {type(x)}" )
xx = int(x)
print(f"Omvnadle den till intergeri: {xx} och av typen {type(xx)}")

y=input("Ange ett annan tal: ")
print(f"Summan av både talet är {int(x) + int(y)}")
print("\n")


rea_procent = 75.0
ny_pris = int(2000 - (2000 * (rea_procent / 100)))
print("Orginal priset för jacka är 2000kr")
print(f"Just nut är det REA på 75% - jackan kostnar nu {ny_pris}kr")
print("\n")


print("Orginal priset för jacka är 2000kr")
rea_procent = int(input("Hur mycket billigare vill du att jackan skall kostan, Skriv in procent tal: "))
ny_pris = int(2000 - (2000 * (rea_procent / 100)))
print(f"jackan kostnar nu {ny_pris}kr med {rea_procent}% i rabatt")
print("\n")


print("## Övn 5")
'''
1a Det är ca 470 km mellan Stockholm och Göteborg. Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg. Du behöver fråga användaren hur fort man ska köra, i km/h. Svara i timmar.
'''
print("\n") 
print("Sträckan mellan Stockholm och Göteborg är 470km")
s = 470
v = input("Ange vilken hastighet km/tim som körs: ")
t = s/int(v)
ts = t * 60

print(f"Det kommer att ta ca{t//1}({t}tim) eller {ts}min att komma fram")


print("\n")
print("Formen för Pythagoras sats säger 'I varje rätvinklig triangel råder, enligt Pythagoras sats, följande samband mellan längden på triangelns sidor': a(2) + b(2) = c(2) ")
h = math.sqrt(3**2 + 4**2)
print(f"Ex triangel med sidorn 3,4,och 5 har följande hypotenusan: {h}")
print("\n")

today = datetime.date.today()

sevenDays = today + datetime.timedelta(days=7)

print(f"\nDaten datum är: {today}")
print(f"Kommande datum för dag 7: {sevenDays}")
