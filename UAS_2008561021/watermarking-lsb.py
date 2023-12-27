import os
import shutil
import cv2
import sys
import numpy as np
import itertools
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

class LSB():
    # Bagian encoding:
    def encode_image(self, img, msg):
        # Dapatkan panjang pesan
        length = len(msg)
        
        # Periksa apakah pesan terlalu panjang
        if length > 255:
            print("Teks terlalu panjang! (Jangan melebihi 255 karakter)")
            return False
        
        # Buat salinan gambar asli untuk menyimpan gambar yang sudah diencode
        encoded = img.copy()
        
        # Dapatkan lebar dan tinggi gambar
        width, height = img.size
        
        # Inisialisasi indeks untuk mengiterasi melalui pesan
        index = 0
        
        # Iterasi melalui setiap piksel dalam gambar
        for row in range(height):
            for col in range(width):
                # Dapatkan nilai RGB dari piksel
                if img.mode != 'RGB':
                    r, g, b, a = img.getpixel((col, row))
                elif img.mode == 'RGB':
                    r, g, b = img.getpixel((col, row))
                
                # Tentukan nilai ASCII yang akan disematkan dalam piksel
                # Piksel pertama (baris=0, kolom=0) digunakan untuk menyimpan panjang pesan
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index - 1]
                    asc = ord(c)
                else:
                    asc = b
                
                # Letakkan nilai RGB baru ke dalam gambar yang sudah diencode
                encoded.putpixel((col, row), (r, g, asc))
                
                # Pindah ke karakter berikutnya dalam pesan
                index += 1
        
        # Kembalikan gambar yang sudah diencode
        return encoded

    #decoding part :
    def decode_image(self,img):
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                if img.mode != 'RGB':
                    r, g, b ,a = img.getpixel((col, row))
                elif img.mode == 'RGB':
                    r, g, b = img.getpixel((col, row))  
                # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = b
                elif index <= length:
                    msg += chr(b)
                index += 1
        lsb_decoded_image_file = "lsb_" + original_image_file
        return msg


#driver part :
#deleting previous folders :
if os.path.exists("Encoded_image/"):
    shutil.rmtree("Encoded_image/")
if os.path.exists("Decoded_output/"):
    shutil.rmtree("Decoded_output/")
#creating new folders :
os.makedirs("Encoded_image/")
os.makedirs("Decoded_output/")
original_image_file = ""    # to make the file name global variable
lsb_encoded_image_file = ""

while True:
    m = input("To encode press '1', to decode press '2', press any other button to close: ")

    if m == "1":
        os.chdir("Original_image/")
        original_image_file = input("Enter the name of the file with extension : ")
        lsb_img = Image.open(original_image_file)
        print("Description : ",lsb_img,"\nMode : ", lsb_img.mode)
        secret_msg = input("Enter the message you want to hide: ")
        print("The message length is: ",len(secret_msg))
        os.chdir("..")
        os.chdir("Encoded_image/")
        lsb_img_encoded = LSB().encode_image(lsb_img, secret_msg)
        lsb_encoded_image_file = "lsb_" + original_image_file
        lsb_img_encoded.save(lsb_encoded_image_file)
        print("Encoded images were saved!")
        os.chdir("..")

    elif m == "2":
        os.chdir("Encoded_image/")
        lsb_img = Image.open(lsb_encoded_image_file)
        os.chdir("..") #going back to parent directory
        os.chdir("Decoded_output/")
        lsb_hidden_text = LSB().decode_image(lsb_img)
        file = open("lsb_hidden_text.txt","w")
        file.write(lsb_hidden_text) # saving hidden text as text file
        file.close()
        file.close()
        print("Hidden texts were saved as text file!")
        os.chdir("..")

    else:
        print("Closed!")
        break