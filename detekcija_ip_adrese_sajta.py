import socket, time

#sajt = "google.com"

lista = ["google.com", "yahoo.com", "bing.com", "facebook.com"]

for x in lista:
    print("-" * 55)
    print("Domen: " + x + "\t" + "--->" + "\t" + socket.gethostbyname(x))             # "\t" za tab odvajanje
    time.sleep(3)


'''
while True:

    sajt = input("Unesite sajt za IP provjeru: ")

    print("-" * 55)

    print(socket.gethostbyname(sajt))
'''