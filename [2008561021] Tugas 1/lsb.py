from PIL import Image

# Fungsi untuk menyisipkan pesan ke dalam citra
def sisipkan_pesan(citra_cover, pesan, citra_sisipkan):
    # Membuka citra cover
    cover = Image.open(citra_cover)
    
    # Mengkonversi pesan ke dalam bentuk binary
    pesan_binary = ''.join(format(ord(c), '08b') for c in pesan)
    panjang_pesan = len(pesan_binary)
    
    # Mengecek apakah pesan dapat disisipkan dalam citra
    if panjang_pesan > cover.width * cover.height:
        raise ValueError("Pesan terlalu panjang untuk disisipkan dalam citra ini")
    
    data_indeks = 0

    # Menyisipkan pesan ke dalam citra
    for x in range(cover.width):
        for y in range(cover.height):
            if data_indeks < panjang_pesan:
                pixel = list(cover.getpixel((x, y)))
                for bit_indeks in range(3):  # Mengganti 3 bit terakhir pada tiap komponen warna (R, G, B)
                    if data_indeks < panjang_pesan:
                        pixel[bit_indeks] = pixel[bit_indeks] & ~1 | int(pesan_binary[data_indeks])
                        data_indeks += 1
                cover.putpixel((x, y), tuple(pixel))
            else:
                break

    # Menyimpan citra yang sudah disisipkan pesan
    cover.save(citra_sisipkan)

# ekstrak pesan
# def ekstrak_pesan(citra_sisipkan):
#     citra = Image.open(citra_sisipkan)
    
#     pesan_binary = ''
#     karakter = 0
#     karakter_indeks = 0

#     for x in range(citra.width):
#         for y in range(citra.height):
#             pixel = list(citra.getpixel((x, y)))
#             for bit_indeks in range(3):  # Mengambil 3 bit terakhir dari tiap komponen warna (R, G, B)
#                 karakter = (karakter << 1) | (pixel[bit_indeks] & 1)
#                 karakter_indeks += 1
#                 if karakter_indeks % 8 == 0:
#                     pesan_binary += format(karakter, '08b')
#                     karakter = 0

#     # Mengonversi pesan biner kembali ke bentuk teks
#     pesan = ''.join(chr(int(pesan_binary[i:i+8], 2)) for i in range(0, len(pesan_binary), 8))
    
#     return pesan



# Meminta input dari pengguna
while True:
    print("Menu:")
    print("1. Sisipkan Pesan ke Dalam Citra")
    # print("2. Ekstrak Pesan dari Citra")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2(dalam pengembangan)/3): ")

    if pilihan == "1":
        pesan = input("Masukkan pesan yang akan disisipkan dalam citra: ")
        citra_cover = input("Masukkan nama file citra cover (BMP) dengan kedalaman warna 24-bit: ")
        citra_sisipkan = "citra_sisipkan_pesan.bmp"
        sisipkan_pesan(citra_cover, pesan, citra_sisipkan)
        print("Pesan telah disisipkan dalam citra dan disimpan sebagai citra_sisipkan_pesan.bmp")
    # elif pilihan == "2":
    #     citra_sisipkan = input("Masukkan nama file citra yang berisi pesan (BMP): ")
    #     pesan_terekstrak = ekstrak_pesan(citra_sisipkan)
    #     print("Pesan yang berhasil diekstrak dari citra:")
    #     print(pesan_terekstrak)
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
