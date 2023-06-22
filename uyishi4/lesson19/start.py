#def faylni_ochish(fayl_nomi):
#    try:
#        with open(fayl_nomi, 'r') as f:
#            fayl_malumotlari = f.read()
#        return fayl_malumotlari
#    except FileNotFoundError:
#        print("Xatolik: Fayl topilmadi!")   
#        fayl_nomi = 'fayl.txt'
#    fayl_malumotlari = faylni_ochish(fayl_nomi)
#    print(fayl_malumotlari)


# def eng_uzun_soz(fayl_nomi):
#     try:
#         with open(fayl_nomi, 'r') as f:
#             fayl_malumotlari = f.read()
#             'sozlar = fayl_malumotlari.split()'
#             eng_uzun = max('sozlar, key=len')
#         return eng_uzun
#     except FileNotFoundError:
#         print("Xatolik: Fayl topilmadi!")

# fayl_nomi = 'test2.txt'
# eng_uzun = eng_uzun_soz(fayl_nomi)
# print("Eng uzun so'z: ", eng_uzun)





# import os

# fayl_nomi = "test2.txt"

# if os.path.exists(fayl_nomi):
#     os.remove(fayl_nomi)
#     print(f"{fayl_nomi} fayli o'chirildi.")
# else:
#     print(f"{fayl_nomi} fayli topilmadi.")




# fayl_nomi = "test2.txt"
# matn = "O'zbekiston kelajagi buyuk davlat"

# with open(fayl_nomi, "a") as f:
#     f.write(matn)
#     print(f"{matn} faylga qo'shildi.")





# fayl_nomi = "test2.txt"

# with open(fayl_nomi, "r") as f:
#     matn = f.read()
#     print(matn)




# fayl_nomi = "test2.txt"

# with open(fayl_nomi, "r") as f:
#     matn = f.read(5)
#     print(matn)