from ftplib import FTP

server = input("Unesite IP FTP Servera: ")

konekcija = FTP(server)

print("FTP RoorDir Listing - v 0.1")
print("Logujem se...")

konekcija.login()               # logujemo se anonimno, nemamo nista u zagradama (ako nam server to dozvoljava)

prazna_lista = []

f = open("ftp_izvjestaj.txt", "w")

konekcija.dir(prazna_lista.append)

for x in prazna_lista:
    f.write(x + "\n")


print(konekcija.retrlines("LIST"))          # za printanje u terminalu preko .retrlines("LIST")

print("Zatvaram FTP konekciju...")

f.close()

konekcija.close()








# domaci zadatak: napraviti listu javnih servera, preko for loop-a izvrsiti 4-5 konekcija i upisati rezulatate u txt