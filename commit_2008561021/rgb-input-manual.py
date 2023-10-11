from PIL import Image

# Fungsi untuk membaca nilai RGB dari pixel pada citra
def baca_nilai_rgb(citra, x, y):
    pixel = citra.getpixel((x, y))
    return pixel

# Fungsi untuk menulis nilai RGB ke pixel pada citra cover
def tulis_nilai_rgb(citra_cover, x, y, nilai_rgb):
    citra_cover.putpixel((x, y), nilai_rgb)


# Baca citra yang akan diambil nilai RGB-nya
citra_sumbero = input("Masukkan citra sumber(with extension): ")
print("Open file: " + citra_sumbero)
citra_sumber = Image.open(citra_sumbero, 'r')

# Baca citra cover
citra_covero = input("Masukkan citra cover(with extension): ")
print("Open file: " + citra_covero)
citra_cover = Image.open(citra_covero, 'r')

# Tentukan titik di mana Anda ingin membaca nilai RGB
x_sumber = int(input("Masukkan koordinat X untuk citra sumber: "))
y_sumber = int(input("Masukkan koordinat Y untuk citra sumber: "))

# Baca nilai RGB dari citra sumber
nilai_rgb_sumber = baca_nilai_rgb(citra_sumber, x_sumber, y_sumber)

# Tentukan titik di mana Anda ingin menulis nilai RGB pada citra cover
x_cover = int(input("Masukkan koordinat X untuk citra cover: "))
y_cover = int(input("Masukkan koordinat Y untuk citra cover: "))

# Baca nilai RGB dari citra cover
nilai_rgb_cover = baca_nilai_rgb(citra_sumber, x_cover, y_cover)

# Cetak nilai RGB dari pixel
print(f"Nilai RGB dari pixel citra sumber ({x_sumber}, {y_sumber}): {nilai_rgb_sumber}")
print(f"Nilai RGB dari pixel citra cover ({x_cover}, {y_cover}): {nilai_rgb_cover}")

# Tulis nilai RGB ke citra cover
tulis_nilai_rgb(citra_cover, x_cover, y_cover, nilai_rgb_sumber)

# Simpan citra cover yang telah diperbarui
citra_cover.save("citra_cover_terupdate2.bmp")

# Tutup citra
citra_sumber.close()
citra_cover.close()
