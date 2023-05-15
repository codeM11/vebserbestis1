matris = [[0] * 5 for _ in range(5)]  # 5x5 sıfırlar matrisi yaradırıq

for i in range(5):
    matris[i][i] = 2  # Baş diaqonal elementləri 2-ə dəyişirik

# Matrisi çap etmək üçün formatlı şəkildə yazdırırıq
for list in matris:
    for element in list:
        print(element, end=" ")
    print()
