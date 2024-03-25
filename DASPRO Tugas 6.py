#!/usr/bin/env python
# coding: utf-8

# In[18]:


# 1 


Nama = input("Masukkan nama orang yang dicurigai: ")
Umur = int(input("Masukkan Umur: "))
T_tinggal = input("Masukkan tempat tinggal: ")
Uang_tabungan = int(input("Masukkan uang tabungan dalam dolar: "))

pangkat_anggota_1 = "Don"
pangkat_anggota_2 = "Underboss"
pangkat_anggota_3 =  "Capo"

if Umur >= 40: 
    if T_tinggal == "Nevada" or T_tinggal == "New York" or T_tinggal == "Havana":
        if Uang_tabungan >= 10000000:
            print(f"{Nama} kemungkinan adalah seorang anggota mafia dengan pangkat {pangkat_anggota_1}. ")
                    
elif (Umur >= 25 and Umur <= 40):
    if T_tinggal == "New Jersey" or T_tinggal == "Manhattan" or T_tinggal == "Nevada":
        if Uang_tabungan >= 1000000 and Uang_tabungan <= 2000000:
            print(f"{Nama} kemungkinan adalah seorang anggota mafia dengan pangkat {pangkat_anggota_2}. ")
                                
elif Umur >= 18 and Umur <= 24:
    if T_tinggal == "California" or T_tinggal == "Detroit" or T_tinggal == "Boston":
        if Uang_tabungan < 1000000:
            print(f"{Nama} kemungkinan adalah seorang anggota mafia dengan pangkat {pangkat_anggota_3} ")

else:
    print(f"{Nama} tidak mencurigakan.") 

    


# In[5]:


# 2 

Nilai_1 = int(input("Masukan nilai coding : "))
Nilai_2 = input("Masukan nilai interview : ")

if Nilai_1 > 80:
    Nilai_1 = "LOLOS"
elif Nilai_1 >= 60 and Nilai_1 <= 80:
    Nilai_1 = "DIPERTIMBANGKAN"
elif Nilai_1 < 60 :
    Nilai_1 = "GAGAL"
    
if Nilai_2 == "A" or Nilai_2 == "B":
    Nilai_2 = "LOLOS"
else:
    Nilai_2 = "GAGAL"
    
if Nilai_1 == "LOLOS" or Nilai_1 == "DIPERTIMBANGKAN":
    if Nilai_2 == "LOLOS":
        print("Selamat Kamu Berhasil Menjadi Calon Programmer")
    else:
        print("Maaf Kamu Belum Berhasil Menjadi Calon Programmer")
else:
    print("Maaf Kamu Belum Berhasil Menjadi Calon Programmer")


# In[9]:


# 3


No_punggung = int(input("Masukan Nomor Punggung"))


if No_punggung % 2 == 0:
    if No_punggung >= 50 and No_punggung <= 100:
        posisi = "Capten team"
    else:
        posisi = "Target attacker"
else:
    if No_punggung % 3 == 0 or No_punggung % 5 == 0:
        posisi = "Keeper"
    elif No_punggung > 90:
        posisi = "Playmaker"
    else:
        posisi = "Defender"


print("Nomor punggung", No_punggung, "adalah untuk", posisi)

