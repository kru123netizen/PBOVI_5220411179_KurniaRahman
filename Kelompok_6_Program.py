class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.tahun_keluaran = tahun_keluaran
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        self.jumlah_roda = jumlah_roda
        self.kapasitas_penumpang = kapasitas_penumpang

    def display_info(self):
        print(f"\nInformasi Kendaraan : {self.nama} ({self.tahun_keluaran})")
        print(f"Warna               : {self.warna}")
        print(f"Kecepatan           : {self.kecepatan} km/jam")
        print(f"Bahan Bakar         : {self.bahan_bakar}")
        print(f"Jumlah Roda         : {self.jumlah_roda}")
        print(f"Kapasitas Penumpang : {self.kapasitas_penumpang} orang")

class Kereta(KendaraanDarat):
    def __init__(self, nama, tahun_keluaran, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_gerbong, jenis_layanan_kereta, rute=None):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_gerbong = jenis_gerbong
        self.jenis_layanan_kereta = jenis_layanan_kereta
        self.rute = [] if rute is None else [tuple(stasiun.split(',')) for stasiun in rute.split(';')]

    def info_kereta(self):
        super().display_info()
        print(f"\nJenis Gerbong        : {self.jenis_gerbong}")
        print(f"Jenis Layanan Kereta : {self.jenis_layanan_kereta}")
        print("Rute yang dilalui    :")
        if not self.rute:
            print("Tidak ada rute yang tersedia.")
        else:
            print("Daftar Rute yang Tersedia:")
            for i, rute in enumerate(self.rute, start=1):
                print(f"{i}. {rute}")
            try:
                pilihan = int(input("Masukkan nomor rute yang ingin dihapus : "))
                if 1 <= pilihan <= len(self.rute):
                    rute_to_remove = self.rute[pilihan - 1]
                    self.rute.remove(rute_to_remove)
                    print(f"Rute {rute_to_remove} berhasil dihapus.")
                else:
                    print("Nomor rute tidak valid.")
            except ValueError:
                print("Masukkan nomor rute dengan benar.")


    def tambah_rute(self, keberangkatan, kedatangan):
        new_rute = (keberangkatan, kedatangan)
        self.rute.append(new_rute)
        print(f"Rute {new_rute} berhasil ditambahkan.")

    def kurangi_rute(self, keberangkatan, kedatangan):
        if not self.rute:
            print("Tidak ada rute yang tersedia.")
            return
        print("Daftar Rute:")
        for idx, rute in enumerate(self.rute, start=1):
            print(f"{idx}. {rute}")
        nomor_rute_hapus = int(input("Masukkan nomor rute yang ingin dihapus (0 untuk batal): "))

        if 0 < nomor_rute_hapus <= len(self.rute):
            rute_to_remove = self.rute[nomor_rute_hapus - 1]
            self.rute.remove(rute_to_remove)
            print(f"Rute {rute_to_remove} berhasil dihapus.")
        elif nomor_rute_hapus == 0:
            print("Operasi penghapusan dibatalkan.")
        else:
            print("Nomor rute tidak valid.")


class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.movement_history = []
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            print(f"Mesin mobil {self.nama} dinyalakan.")
            self.engine_started = True
            self.movement_history.append("Mesin dinyalakan.")
        else:
            print(f"Mesin mobil {self.nama} sudah menyala.")

    def stop_engine(self):
        if self.engine_started:
            print(f"Mesin mobil {self.nama} dimatikan.")
            self.engine_started = False
            self.movement_history.append("Mesin dimatikan.")
        else:
            print(f"Mesin mobil {self.nama} sudah mati.")

    def mobil_maju(self):
        if self.engine_started:
            self.movement_history.append("Maju")
            print(f"Mobil {self.nama} bergerak maju.")
        else:
            print("Mesin belum dinyalakan. Silakan nyalakan mesin terlebih dahulu.")

    def mobil_mundur(self):
        if self.engine_started:
            self.movement_history.append("Mundur")
            print(f"Mobil {self.nama} bergerak mundur.")
        else:
            print("Mesin belum dinyalakan. Silakan nyalakan mesin terlebih dahulu.")

    def mobil_belok(self, direction):
        if self.engine_started:
            self.movement_history.append(f"Belok {direction}")
            print(f"Mobil {self.nama} berbelok ke {direction}.")
        else:
            print("Mesin belum dinyalakan. Silakan mulai mesin terlebih dahulu.")

    def gerak_mobil(self):
        if not self.movement_history:
            print(f"Mobil {self.nama} belum melakukan pergerakan.")
        else:
            print(f"Pergerakan {self.nama}:")
            for move in self.movement_history:
                print(move)

class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, wing_type=None):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.front_wing = False
        self.rear_wing = False
        self.set_wing(wing_type)
        self.race_started = False

    def set_wing(self, wing_type):
        if wing_type == 1:
            self.front_wing = True
            self.rear_wing = False
            self.wing_type = "Front Wing"
            print(f"{self.nama} menggunakan Front Wing. Traksi pada roda depan ditingkatkan!")
        elif wing_type == 2:
            self.front_wing = False
            self.rear_wing = True
            self.wing_type = "Rear Wing"
            
    def race_mode(self):
        if self.engine_started:
            self.movement_history.append("Mengaktifkan Race Mode")
            print(f"Mobil {self.nama} masuk ke dalam Race Mode. Boost dapat diaktifkan!")
            self.race_started = True
        else:
            print("Mesin belum dinyalakan. Silakan mulai mesin terlebih dahulu.")

    def boost(self):
        if self.race_started and self.engine_started:
            self.movement_history.append("Menggunakan Boost")
            print(f"Mobil {self.nama} menggunakan Boost.")
        elif self.engine_started:
            print("Race Mode belum dinyalakan. Silahkan aktifkan Race Mode terlebih dahulu")
        else:
            print("Mesin belum dinyalakan. Silakan mulai mesin terlebih dahulu.")

    def stop_race(self):
        self.race_started = False
        
    def info_balap(self):
        super().display_info()
        if self.wing_type:
            print(f"\nJenis Wing          : {self.wing_type}")
            if self.front_wing:
                print("Meningkatkan Traksi pada roda depan")
            elif self.rear_wing:
                print("Meningkatkan Traksi pada roda belakang")


class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, sunroof_type=None):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.sunroof_terbuka = False
        self.sunroof_tertutup = False
        self.shock_breaker = False
        self.set_sunroof(sunroof_type)

    def set_sunroof(self, sunroof_type):
        if sunroof_type == 1:
            self.sunroof_terbuka = True
            self.sunroof_tertutup = False
            self.sunroof_type = "Sunroof Terbuka"
            print(f"{self.nama} menggunakan tipe sunroof terbuka. Sirkulasi udara dalam mobil ditingkatkan!")
        elif sunroof_type == 2:
            self.sunroof_terbuka = False
            self.sunroof_tertutup = True
            self.sunroof_type = "Sunroof Tertutup"
            print(f"{self.nama} menggunakan tipe sunroof tertutup. Keamanan terhadap cuaca ekstrim ditingkatkan!")


    def set_shock_breaker(self, use_shock_breaker):
        self.shock_breaker = use_shock_breaker
        if use_shock_breaker:
            print(f"{self.nama} menggunakan shock breaker. Keseimbangan dan kenyamanan berkendara ditingkatkan!")
        elif not use_shock_breaker:
            print(f"{self.nama} tidak menggunakan shock breaker.")
        else:
            print("Pilihan sunroof tidak valid. Pilih ulang sunroof.")

    def info_crossroad(self):
        super().display_info()
        if self.sunroof_type:
            print("\nTipe Sunroof        :")
            if self.sunroof_terbuka:
                print("Menggunakan tipe sunroof terbuka. Sirkulasi udara dalam mobil ditingkatkan!")
            elif self.sunroof_tertutup:
                print("Menggunakan tipe sunroof tertutup. Keamanan terhadap cuaca ekstrim ditingkatkan!")

        print("Shock Breaker       :")
        if self.shock_breaker:
            print(f"Menggunakan shock breaker. Keamanan pada medan berat ditingkatkan!")
        else:
            print("Tidak menggunakan shock breaker. Hindari medan berat.")

# Program utama
list_kendaraan = []
def tampil():
    
    while True:
        print("\n==============================")
        print("Menu Utama :")
        print("1. Daftar Kendaraan")
        print("2. List Kendaraan")
        print("3. Keluar")
        choice_menu = input("\nPilih Menu : ")

        if choice_menu == "1":
            while True:
                print("\n==============================")
                print("Jenis Kendaraan :")
                print("1. Mobil")
                print("2. Kereta")
                print("0. Keluar")
                choice_kendaraan = input("\nPilih Jenis Kendaraan : ")

                if choice_kendaraan == "1":
                    print("\n==============================")
                    print("Jenis Mobil :")
                    print("1. Mobil Balap")
                    print("2. Mobil Crossroad")
                    choice_mobil = input("\nPilih jenis mobil (1/2) : ")

                    if choice_mobil == "1":
                        tahun = input("\nTahun Keluaran      : ")
                        nama = str(input("Nama Mobil          : "))
                        warna = input("Warna Mobil         : ")
                        kecepatan = input("Kecepatan Mobil     : ")
                        bahan_bakar = input("Bahan Bakar Mobil   : ")
                        roda = input("Jumlah Roda         : ")
                        kapasitas_penumpang = input("Kapasitas Penumpang : ")

                        while True:
                            sayap = input("\nPilih Front Wing atau Rear Wing (1/2) : ")
                            if sayap in ["1", "2"]:
                                mobil_balap = MobilBalap(tahun, nama, warna, kecepatan, bahan_bakar, roda, kapasitas_penumpang, wing_type=int(sayap))
                                list_kendaraan.append(mobil_balap)
                                break
                            else:
                                print("Pilihan sayap tidak valid. Pilih ulang sayap.")

                    elif choice_mobil == "2":
                        tahun = input("\nTahun Keluaran      : ")
                        nama = input("Nama Mobil          : ")
                        warna = input("Warna Mobil         : ")
                        kecepatan = input("Kecepatan Mobil     : ")
                        bahan_bakar = input("Bahan Bakar Mobil   : ")
                        roda = input("Jumlah Roda         : ")
                        kapasitas_penumpang = input("Kapasitas Penumpang : ")

                        while True:
                            atap = input("\nPilih sunroof terbuka atau tertutup (1/2) : ")
                            if atap in ["1", "2"]:
                                mobil_crossroad = MobilCrossroad(tahun, nama, warna, kecepatan, bahan_bakar, roda, kapasitas_penumpang, sunroof_type=int(atap))
                                
                                while True:
                                    pilih_shock_breaker = input("Gunakan shock breaker? (y/n): ").lower()
                                    if pilih_shock_breaker == "y":
                                        mobil_crossroad.set_shock_breaker(True)
                                        break
                                    elif pilih_shock_breaker == "n":
                                        mobil_crossroad.set_shock_breaker(False)
                                        break
                                    else:
                                        print("Pilihan shock breaker tidak valid. Silahkan pilih ulang.")

                                list_kendaraan.append(mobil_crossroad)
                                break
                            else:
                                print("Pilihan sunroof tidak valid. Pilih ulang sunroof.")


                elif choice_kendaraan == "2":
                    tahun = input("\nTahun Keluaran       : ")
                    nama = input("Nama Kereta          : ")
                    warna = input("Warna Kereta         : ")
                    kecepatan = input("Kecepatan Kereta     : ")
                    bahan_bakar = input("Bahan Bakar Kereta   : ")
                    roda = input("Jumlah Roda          : ")
                    kapasitas_penumpang = input("Kapasitas Penumpang  : ")
                    jenis_gerbong = input("Jenis Gerbong        : ")
                    jenis_layanan_kereta = input("Jenis Layanan Kereta : ")
                    kereta = Kereta(nama, tahun, warna, kecepatan, bahan_bakar, roda, kapasitas_penumpang, jenis_gerbong, jenis_layanan_kereta)
                    list_kendaraan.append(kereta)

                else:
                    print("Pilihan tidak valid. Silakan pilih antara 1 dan 2.")
                    continue  
                
                break

        elif choice_menu == "2":
            while True:
                print("\n==============================")
                print("\nList Kendaraan:")
                for idx, kendaraan in enumerate(list_kendaraan, start=1):
                    print(f"{idx}. {kendaraan.nama} ({kendaraan.__class__.__name__})")

                choice_detail = int(input("\nPilih nomor kendaraan untuk melihat detail (0 untuk kembali): "))

                if 0 < choice_detail <= len(list_kendaraan):
                    kendaraan_terpilih = list_kendaraan[choice_detail - 1]
                    
                    if isinstance(kendaraan_terpilih, Kereta):
                        while True:
                            print("\n==============================")
                            print("\nMenu Kereta :")
                            print("1. Tambah Rute")
                            print("2. Kurangi Rute")
                            print("3. Tampilkan Riwayat Rute")
                            print("4. Tampilkan Informasi Kereta")
                            print("0. Kembali ke Menu Utama")

                            choice_action_kereta = input("\nPilih aksi (0-4): ")
                            if choice_action_kereta == "1":
                                keberangkatan = input("Masukkan stasiun keberangkatan : ")
                                kedatangan = input("Masukkan stasiun kedatangan    : ")
                                kendaraan_terpilih.tambah_rute(keberangkatan, kedatangan)
                            elif choice_action_kereta == "2":
                                kendaraan_terpilih.kurangi_rute(keberangkatan, kedatangan)
                            elif choice_action_kereta == "3":
                                print("History Rute:")
                                for rute in kendaraan_terpilih.rute:
                                    print(rute)
                            elif choice_action_kereta == "4":
                                kendaraan_terpilih.info_kereta()
                            elif choice_action_kereta == "0":
                                break
                            else:
                                print("Pilihan tidak valid. Silakan pilih antara 1-5.")


                    if isinstance(kendaraan_terpilih, MobilBalap):
                        kendaraan_terpilih.set_wing(None)
                        while True:
                            print("\n==============================")
                            print("\nMenu Mobil Balap :")
                            print("1. Nyalakan Mesin")
                            print("2. Matikan Mesin")
                            print("3. Bergerak Maju")
                            print("4. Bergerak Mundur")
                            print("5. Berbelok")
                            print("6. Mode Race")
                            print("7. Aktifkan Boost")
                            print("8. Tampilkan Riwayat Pergerakkan")
                            print("9. Lihat Informasi Kendaraan")
                            print("0. Kembali ke Menu Utama")

                            choice_action = input("\nPilih aksi (0-9) : ")
                            if choice_action == "1":
                                kendaraan_terpilih.start_engine()
                            elif choice_action == "2":
                                kendaraan_terpilih.stop_engine()
                                kendaraan_terpilih.stop_race()
                            elif choice_action == "3":
                                kendaraan_terpilih.mobil_maju()
                            elif choice_action == "4":
                                kendaraan_terpilih.mobil_mundur()
                            elif choice_action == "5":
                                direction = input("Masukkan arah belok: ")
                                kendaraan_terpilih.mobil_belok(direction)
                            elif choice_action == "6":
                                kendaraan_terpilih.race_mode()
                            elif choice_action == "7":
                                kendaraan_terpilih.boost()
                            elif choice_action == "8":
                                kendaraan_terpilih.gerak_mobil()
                            elif choice_action == "9":
                                kendaraan_terpilih.info_balap()
                            elif choice_action == "0":
                                break
                            else:
                                print("Pilihan tidak valid. Silakan pilih antara 1-10.")


                    if isinstance(kendaraan_terpilih, MobilCrossroad):
                        kendaraan_terpilih.set_sunroof(None)
                        
                        while True:
                            print("\n==============================")
                            print("\nMenu Mobil Crossroad :")
                            print("1. Nyalakan Mesin")
                            print("2. Matikan Mesin")
                            print("3. Bergerak Maju")
                            print("4. Bergerak Mundur")
                            print("5. Berbelok")
                            print("6. Tampilkan Riwayat Pergerakkan")
                            print("7. Lihat Informasi Kendaraan")
                            print("0. Kembali ke Menu Utama")

                            choice_action = input("\nPilih aksi (0-7): ")
                            if choice_action == "1":
                                kendaraan_terpilih.start_engine()
                            elif choice_action == "2":
                                kendaraan_terpilih.stop_engine()
                            elif choice_action == "3":
                                kendaraan_terpilih.mobil_maju()
                            elif choice_action == "4":
                                kendaraan_terpilih.mobil_mundur()
                            elif choice_action == "5":
                                direction = input("Masukkan arah belok: ")
                                kendaraan_terpilih.mobil_belok(direction)
                            elif choice_action == "6":
                                kendaraan_terpilih.gerak_mobil()
                            elif choice_action == "7":
                                kendaraan_terpilih.info_crossroad()
                            elif choice_action == "0":
                                break
                            else:
                                print("Pilihan tidak valid. Silakan pilih antara 8.")
                            
                elif choice_detail == 0:
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih nomor kendaraan yang valid.")

        elif choice_menu == "3":
            print("Program selesai. Sampai jumpa!")
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")


tampil()