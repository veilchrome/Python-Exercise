class kasir:
    totalmkn,porsi,mkn=0

    def __init__(self,totalmkn,porsi,mkn):
        self.totalmkn=totalmkn
        self.porsi=porsi
        self.mkn=mkn

    def tampilan(self):
        print("------------------------------- Program Kasir Sederhana Samet -------------------")
        pembeli = input("Masukkan Nama pembeli: ")
        print("Nama Pembeli :", pembeli)

    #Fungsi Makan
    def fungsimakanan(self):
        # global totalmkn  ## Dont use global is smell code not recommended use self keyword
        # global porsi  ## Dont use global is smell code not recommended use self keyword
        # global mkn  ## Dont use global is smell code not recommended use self keyword
        print("\n ----------------- Menu Makan -------------------")
        print("1. Mie Ayam Bakso - Rp 15000")
        print("2. Soto Mie - Rp 20000")
        print("3. Nasi uduk spesial - Rp 13000")
        nomor= int(input("Masukkan Pilihan: "))
        porsi= int(input("Berapa Porsi: "))

        if nomor==1:
            totalmkn=porsi*15000
            print (porsi, "Porsi Nasi Goreng Telur = Rp", totalmkn)
            mkn=("Mie Ayam Bakso")
        elif nomor==2:
            totalmkn=porsi*20000
            print (porsi, "Porsi Soto Mie = Rp", totalmkn)
            mkn=("Soto Mie")
        elif nomor==3:
            totalmkn=porsi*13000
            print (porsi, " Porsi Nasi uduk spesial = Rp", totalmkn)
            mkn=("Nasi Uduk Spesial")
        else:
            print("Pilihan Tidak ada, Silahkan Masukan lagi!!")
            self.fungsimakanan()
    
    #Fungsi Minum
    def fungsiminuman(self):
        # global totalmnm
        # global mnm
        # global gelas
        print("\n ----------------- Menu Minuman ----------------")
        print("1. Es Teh Manis - Rp 5000")
        print("2. Jeruk Anget - Rp 6000")
        print("3. Kopi Espresso - Rp 15000")
        nomor=int(input("Masukkan Pilihan: "))
        gelas=int(input("Berapa Gelas :"))

        if nomor==1:
            totalmnm=gelas*5000
            print (gelas, " Gelas Es Teh Manis = Rp", totalmnm)
            mnm=(" Gelas Es Teh Manis")
        elif nomor==2:
            totalmnm=gelas*6000
            print (gelas, "Gelas Jeruk Anget = Rp", totalmnm)
            mnm=("Gelas Es Jeruk")
        elif nomor==3:
            totalmnm=gelas*15000
            print (gelas, "Gelas Kopi ESpresso = Rp", totalmnm)
            mnm=("Gelas Kopi Espresso")
        else:
            print("Pilihan Tidak ada, Silahkan Masukan lagi!!")
            self.fungsiminuman()
    
    def output(sefl):
    #Pencetakkan User Input yang memanggil value yang telah diinputkan sebelumnya
        print("\n========================================")
        print("=================== S T R U K   B E L I ======================")
        print("==============================================================")
        print("Nama\t\t:",pembeli)
        print("Beli\t\t:",porsi,mkn,"(Rp", totalmkn, ")")
        print("\t\t ",gelas,mnm,"( Rp", totalmnm, ")")
        print("Tagihan\t\t: Rp", totalsemua)
        print("Dibayar\t\t: Rp", uang)
        print("Kembalian\t: Rp", kembalian)
        print("===============================================================")
        print("===============================================================")
    def total():
        print("\nTotal Harus Dibayar: Rp", totalsemua)
        uang=int(input("Uang TUnai Pembeli: Rp "))
        kembalian=int(uang-totalsemua)
        print("Kembalian :", kembalian)
    #Flow Control   
    fungsimakanan()
    fungsiminuman()
    totalsemua=totalmkn+totalmnm



