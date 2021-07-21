import ftplib

path = "/debian/"           # direktorijum koji nam treba (ide sa /debian/ - kosim crtama)

filename = "README.mirrors.txt"     # fajl koga skidamo, bez promjene imena ili tipa (zadrzava ime i tip kada skinemo)

ftp = ftplib.FTP("ftp.fi.debian.org")      # ostvarivanje konekcije (meta)

ftp.login()              # logovanje na server

ftp.cwd(path)           # ulaz u direktorijum, change working directory (cwd) - da ne bude root, vec onaj koji nama treba (/debian/)

ftp.retrlines("LIST")       # listing ftp servera ("LIST" ili "NLIST")

ftp.retrbinary("RETR " + filename, open(filename, "wb").write)  # preuzimanje, .retrbinary - skidamo bez greske u prenosu, "wb" - write binary

ftp.quit()      # prekid konekcije