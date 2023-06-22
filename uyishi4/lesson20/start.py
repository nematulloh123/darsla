#1
# try:
#     # Bu kodning ichida NameError xatolik berishi mumkin
#     print(nonexistent_variable')
# except NameError:
#     # Agar NameError xatolik berib kelgan bo'lsa, undan xabardor bo'lib qolib ketamiz
#     print("Bunday o'zgaruvchi topilmadi.")
# else:
#     # Agar xatolik bo'lmasa, kodni davom ettiramiz
#     print("Kod muvaffaqiyatli bajarildi!")


#2
# try:
#     num1 = float(input("Birinchi sonni kiriting: "))
#     num2 = float(input("Ikkinchi sonni kiriting: "))
#     result = num1 / num2
#     print(f"{num1} / {num2} = {result}")
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")


#3
# while True:
#     try:
#         num = float(input("Iltimos, son kiriting: "))
#         if num < 0:
#             raise ValueError
#         break
#     except ValueError:
#         print("Iltimos, faqat musbat son kiriting!")

# print("Kiritilgan son:", num)

#4
# filename = "mavjud_emas.txt"

# try:
#     with open(filename, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f"Fayl topilmadi: {filename}")


#5
# import math

# try:
#     num = float(input("Sonni kiriting: "))
#     if num < 0:
#         raise ValueError("Manfiy son kiritildi.")
#     result = math.sqrt(num)
#     print(f"{num} ning ildizi {result} ga teng.")
# except ValueError as err:
#     print(f"Xatolik: {err}")
# except:
#     print("Noto'g'ri qiymat kiritildi.")