class kasir:
    totalmkn,porsi,gelas,totalsemua,totalmkn,totalmnm,uang=0
    mkn,mnm=""

 
    def tampilan(self):
        print("------------------------------- Program Kasir Sederhana Samet -------------------")
        pembeli = input("Masukkan Nama pembeli: ")
        print("Nama Pembeli :", pembeli)

    #Fungsi Makan
    def fungsimakanan(self):
        # global totalmkn  ## Dont use global not recommended, use self keyword
        # global porsi  ## Dont use global not recommended, use self keyword
        # global mkn  ## Dont use global not recommended, use self keyword
        print("\n ----------------- Menu Makan -------------------")
        print("1. Mie Ayam Bakso - Rp 15000")
        print("2. Soto Mie - Rp 20000")
        print("3. Nasi uduk spesial - Rp 13000")
        nomor= int(input("Masukkan Pilihan: "))
        porsi= int(input("Berapa Porsi: "))

        if nomor==1:
            self.totalmkn=porsi*15000
            print (porsi, "Porsi Nasi Goreng Telur = Rp{} ",format(self.totalmkn))
            self.mkn="Mie Ayam Bakso"
        elif nomor==2:
            self.totalmkn=porsi*20000
            print (porsi, "Porsi Soto Mie = Rp{}", format(self.totalmkn))
            self.mkn="Soto Mie"
        elif nomor==3:
            self.totalmkn=porsi*13000
            print (porsi, " Porsi Nasi uduk spesial = Rp{}", format(self.totalmkn))
            self.mkn="Nasi Uduk Spesial"
        else:
            print("Pilihan Tidak ada, Silahkan Masukan lagi!!")
            self.fungsimakanan()
    
    #Fungsi Minum
    def fungsiminuman(self):
      
        print("\n ----------------- Menu Minuman ----------------")
        print("1. Es Teh Manis - Rp 5000")
        print("2. Jeruk Anget - Rp 6000")
        print("3. Kopi Espresso - Rp 15000")
        nomor=int(input("Masukkan Pilihan: "))
        gelas=int(input("Berapa Gelas :"))

        if nomor==1:
            totalmnm=gelas*5000
            print (gelas, " Gelas Es Teh Manis = Rp", totalmnm)
            self.mnm=(" Gelas Es Teh Manis")
        elif nomor==2:
            totalmnm=gelas*6000
            print (gelas, "Gelas Jeruk Anget = Rp", totalmnm)
            self.mnm=("Gelas Es Jeruk")
        elif nomor==3:
            totalmnm=gelas*15000
            print (gelas, "Gelas Kopi ESpresso = Rp", totalmnm)
            self.mnm=("Gelas Kopi Espresso")
        else:
            print("Pilihan Tidak ada, Silahkan Masukan lagi!!")
            self.fungsiminuman()
    

    def total(self):
        totalsemua=self.totalmkn+self.totalmnm
        print("\nTotal Harus Dibayar: Rp", totalsemua)
        self.fuang=int(input("Uang Tunai Pembeli: Rp "))
        kembalian=int(self.uang-self.totalsemua)
        print("Kembalian :", kembalian)

    def output(self):
    #Pencetakkan User Input yang memanggil value yang telah diinputkan sebelumnya
        print("\n========================================")
        print("=================== S T R U K   B E L I ======================")
        print("==============================================================")
        print("Nama\t\t:",pembeli)
        print("Beli\t\t:",porsi,mkn,"(Rp", self.totalmkn, ")")
        print("\t\t ",self.gelas,mnm,"( Rp", self.totalmnm, ")")
        print("Tagihan\t\t: Rp", self.totalsemua)
        print("Dibayar\t\t: Rp", self.uang)
        print("Kembalian\t: Rp", self.kembalian)
        print("===============================================================")
        print("===============================================================")


    
    #Manggil fungsi
    fungsimakanan()
    fungsiminuman()



