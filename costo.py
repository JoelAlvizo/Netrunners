
texto=""
cont=0
texto=input()
caraceteres=['a', 'b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
dijitos=['1','2','3','4','5','6','7','8','9']
especiales=['#', '!', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '¡', '+', '*', '_-', '.', ':', ';', ',', '<', '>', '|', '°', 'ñ', 'á', 'é', 'é', 'ó', 'ú']

texto=texto.lower()
for k in caraceteres:
    cont=cont+texto.count(k)

for i in especiales:
    cont=cont+(texto.count(i)*3)

for j in dijitos:
    cont=cont+(texto.count(j)*2)


print(cont)