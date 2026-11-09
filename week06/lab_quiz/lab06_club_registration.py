kulup = ("Yazılım", "Tasarım", "Pazarlama")
tum_ogrenciler = []
tum_ogrenciler.append(["  Baran  ".strip() , ["Yazılım"]])
tum_ogrenciler.append([" Furkan ".strip(), ["Tasarım"]])
tum_ogrenciler.append([" Orhan ".strip() , ["Pazarlama"]])
tum_ogrenciler.insert(0, ["Başkan", ["Yazılım"]])
print("Toplam Kayıtlı Öğrenci Sayısı:" ,len(tum_ogrenciler))

tum_ogrenciler.remove(["Orhan", ["Pazarlama"]])
sonuncu = tum_ogrenciler.pop(2)
print("Sistemden en son çıkan öğrenci: ", sonuncu[0])

tum_ogrenciler.append(["Burak Tan", ["Tasarım"]])
alfabetik_ogrenciler = sorted(tum_ogrenciler)
print(alfabetik_ogrenciler)
print(tum_ogrenciler)

tum_ogrenciler.sort()
print(tum_ogrenciler)