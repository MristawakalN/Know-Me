#!/bin/bash
# belajar coding
# perkenalan

# penghapus texs
clear
# durasi
sleep 1
figlet Perkenalan By Mr.N
echo -e "{===========================}"
echo -e "[•]Kapten:Panglima Jateng"
echo -e "[•]Author:Mr.N"
echo -e "[•]team  :Mavia Teknologi"
echo -e "[•]info  :Ingat Sholat Tod Wkwkwk"
echo -e "{===========================}"
echo
sleep 1
    echo -e "1). Perkenalan"
    echo -e "2). nomor wa"
    echo -e "3). keluar"
    echo -e "========================="
    read -p "Pilih Kakak: " donet
# data no 1
if [ $donet == "1" ]
then
    echo
    read -p "siapa nama kakak" nama
    echo "Hay $nama namaku Mr.N aku anggota dari mavia teknologi kalau make script ku mohon jangan di rekode yaa"
    echo "============================"
    echo
fi
# data no 2
if [ $donet == "2" ]
then
    echo "nih nomor ku jangan di spam kalau gak mau hp mu meledak:v"
    echo "nomor wa: 085823104620 copyright"
    echo "✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓"
    echo
fi
# data no 3
if [ $donet == "3" ]
then
    echo "Babay Kakak"
    exit
fi