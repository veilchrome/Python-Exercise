class kasir:

    ## Tipe data Number
    totalmk=0,
    porsi=0
    gelas=0
    totalsemua=0
    totalmkn=0
    totalmnm=0
    uang=0
    nomor=0
    kembalian=0

    ## String
    mkn=""
    mnm=""
    pembeli=""

 
    def tampilan(self):
        print("------------------------------- Program Kasir Sederhana Samet -------------------")
        self.pembeli = input("Masukkan Nama pembeli: ")
        print("Nama Pembeli :", self.pembeli)

    #Fungsi Makan
    def fungsimakanan(self):
        # global totalmkn  ## Dont use global not recommended, use self keyword
        # global porsi  ## Dont use global not recommended, use self keyword
        # global mkn  ## Dont use global not recommended, use self keyword
        print("\n ----------------- Menu Makan -------------------")
        print("1. Mie Ayam Bakso - Rp 15000")
        print("2. Soto Mie - Rp 20000")
        print("3. Nasi uduk spesial - Rp 13000")
        self.nomor= int(input("Masukkan Pilihan: "))
        self.porsi= int(input("Berapa Porsi: "))

        if self.nomor==1:
            self.totalmkn=self.porsi*15000
            print (self.porsi, "Porsi Nasi Goreng Telur = Rp  ",format(self.totalmkn))
            self.mkn="Mie Ayam Bakso"
        elif self.nomor==2:
            self.totalmkn=self.porsi*20000
            print (self.porsi, "Porsi Soto Mie = Rp", format(self.totalmkn))
            self.mkn="Soto Mie"
        elif self.nomor==3:
            self.totalmkn=self.porsi*13000
            print (self.porsi, " Porsi Nasi uduk spesial = Rp", format(self.totalmkn))
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
        
        self.nomor=int(input("Masukkan Pilihan: "))
        self.totalsemuagelas=int(input("Berapa Gelas :"))

        if self.nomor==1:
            self.totalmnm=self.gelas*5000
            print (self.gelas, " Gelas Es Teh Manis = Rp", self.totalmnm)
            self.mnm=(" Gelas Es Teh Manis")

        elif self.nomor==2:
            self.totalmnm=self.gelas*6000
            print (self.gelas, "Gelas Jeruk Anget = Rp", self.totalmnm)
            self.mnm=("Gelas Es Jeruk")

        elif self. nomor==3:
            self.totalmnm=self.gelas*15000
            print (self.gelas, "Gelas Kopi ESpresso = Rp", self.totalmnm)
            self.mnm=("Gelas Kopi Espresso")

        else:
            print("Pilihan Tidak ada, Silahkan Masukan lagi!!")
            self.fungsiminuman()
    

    def total(self):
        self.totalsemua=self.totalmkn+self.totalmnm
        print("\nTotal Harus Dibayar: Rp", self.totalsemua)
        try:
            self.uang=int(input("Uang Tunai Pembeli: Rp "))
            self.kembalian=self.uang-self.totalsemua
            print("Kembalian :", self.kembalian)
        except:
                if self.uang<self.totalsemua:
                    print("Uang anda tidak cukup")

    def output(self):
    #Pencetakkan User Input yang memanggil value yang telah diinputkan sebelumnya
        print("\n========================================")
        print("=================== S T R U K   B E L I ======================")
        print("==============================================================")
        print("Nama\t\t:",self.pembeli)
        print("Beli\t\t:",self.porsi,self.mkn,"(Rp", self.totalmkn, ")")
        print("\t\t ",self.gelas,self.mnm,"( Rp", self.totalmnm, ")")
        print("Tagihan\t\t: Rp", self.totalsemua)
        print("Dibayar\t\t: Rp", self.uang)
        print("Kembalian\t: Rp", self.kembalian)
        print("===============================================================")
        print("===============================================================")

## Call object
cetak=kasir()

#Manggil fungsi
cetak.tampilan()
cetak.fungsimakanan()
cetak.fungsiminuman()
cetak.total()
cetak.output()


