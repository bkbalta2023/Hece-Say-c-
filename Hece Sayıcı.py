#Türkçe kelimelerde hece sayısı kelimede bulunan ünlü harf sayısına eşittir.

cumle = input("Cümle giriniz: ")
sesli = "aeıioöuü"
sayac = 0

for i in cumle:
    if i in sesli:
        sayac += 1
print(sayac)
