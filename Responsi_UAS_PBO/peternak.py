import random
import mysql.connector

class Peternakan:
    def __init__(self, nama, alamat, jumlah_maksimal_hewan, jenis_peternakan, tahun_dibuat):
        self._nama = nama  
        self.alamat = alamat
        self.jumlah_maksimal_hewan = jumlah_maksimal_hewan
        self.__jenis_peternakan = jenis_peternakan  
        self.tahun_dibuat = tahun_dibuat
        self.daftar_hewan = []

        
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="peternakan",
            port=3306
        )
        self.cursor = self.db_connection.cursor()

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS hewan (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(255) NOT NULL,
                umur INT NOT NULL,
                harga FLOAT NOT NULL,
                jumlah INT NOT NULL
            )
        """)
        self.db_connection.commit()

    def __del__(self):
        self.cursor.close()
        self.db_connection.close()

    def insert_hewan(self, nama, umur, harga, jumlah):
        query = "INSERT INTO hewan (nama, umur, harga, jumlah) VALUES (%s, %s, %s, %s)"
        values = (nama, umur, harga, jumlah)
        self.cursor.execute(query, values)
        self.db_connection.commit()

    def update_hewan(self, id, nama, umur, harga, jumlah):
        query = "UPDATE hewan SET nama=%s, umur=%s, harga=%s, jumlah=%s WHERE id=%s"
        values = (nama, umur, harga, jumlah, id)
        self.cursor.execute(query, values)
        self.db_connection.commit()

    def delete_hewan(self, id):
        query = "DELETE FROM hewan WHERE id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        self.db_connection.commit()

    def select_all_hewan(self):
        self.cursor.execute("SELECT * FROM hewan")
        result = self.cursor.fetchall()
        return result

    def informasi_peternakan(self):
        print("===== Informasi Peternakan =====")
        print(f"Nama Peternakan: {self._nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Jumlah Maksimal Hewan: {self.jumlah_maksimal_hewan}")
        print(f"Jenis Peternakan: {self.__jenis_peternakan}")
        print(f"Tahun Dibuat: {self.tahun_dibuat}")
        print("===============================")

    def menu_hewan(self):
        while True:
            print("\nMenu Hewan:")
            print("1. Informasi Hewan")
            print("2. Beli Hewan Ternak")
            print("3. Jual Hewan Ternak")
            print("4. Total Semua Hewan Ternak")
            print("5. Jenis Hewan Ternak")
            print("6. Kembali")

            pilihan_hewan = input("Pilih menu (1-6): ")

            if pilihan_hewan == "1":
                self.informasi_hewan()
            elif pilihan_hewan == "2":
                self.beli_hewan()
            elif pilihan_hewan == "3":
                self.jual_hewan()
            elif pilihan_hewan == "4":
                self.total_semua_hewan()
            elif pilihan_hewan == "5":
                JenisHewan.tampilkan_jenis()
            elif pilihan_hewan == "6":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")

    def informasi_hewan(self):
        print("\n===== Informasi Hewan Ternak =====")
        for hewan in self.daftar_hewan:
            print(f"Nama: {hewan['nama']}, Umur: {hewan['umur']}, Harga: {hewan['harga']}, Jumlah: {hewan['jumlah']}")
        print("===============================")

    def beli_hewan(self):
        print("\n===== Beli Hewan Ternak =====")
        nama_hewan = input("Nama Hewan: ")
        umur_hewan = int(input("Umur Hewan: "))
        harga_hewan = float(input("Harga Hewan: "))
        jumlah_hewan = int(input("Jumlah Hewan: "))

        if self.total_hewan() + jumlah_hewan > self.jumlah_maksimal_hewan:
            print("Peternakan kamu sudah penuh. Tambah kandang baru untuk membeli lebih banyak hewan.")
        else:
            self.daftar_hewan.append({'nama': nama_hewan, 'umur': umur_hewan, 'harga': harga_hewan, 'jumlah': jumlah_hewan})
            self.insert_hewan(nama_hewan, umur_hewan, harga_hewan, jumlah_hewan)  
            print(f"Berhasil membeli {jumlah_hewan} {nama_hewan}.")
        print("===============================")

    def jual_hewan(self):
        print("\n===== Jual Hewan Ternak =====")
        nama_hewan = input("Nama Hewan: ")
        jumlah_hewan = int(input("Jumlah Hewan: "))

        for hewan in self.daftar_hewan:
            if hewan['nama'] == nama_hewan:
                if hewan['jumlah'] >= jumlah_hewan:
                    hewan['jumlah'] -= jumlah_hewan
                    print(f"Berhasil menjual {jumlah_hewan} {nama_hewan}.")
                    
                    
                    self.update_hewan(hewan.get('id'), hewan['nama'], hewan['umur'], hewan['harga'], hewan['jumlah'])
                else:
                    print(f"Tidak cukup {nama_hewan} untuk dijual.")
                break
        else:
            print(f"{nama_hewan} tidak ditemukan.")
        print("===============================")

    def total_semua_hewan(self):
        print("\n===== Total Semua Hewan Ternak =====")
        hewan_list = self.select_all_hewan()
        total = sum(hewan[4] for hewan in hewan_list)
        print(f"Total Semua Hewan Ternak: {total}")
        print("===============================")

    def total_hewan(self):
        return sum(hewan['jumlah'] for hewan in self.daftar_hewan)


class Hewan(Peternakan):
    def __init__(self, jenis):
        super().__init__("Peternakan Ujung Kulon", "Jl. Sutan Maujalo, kelurahan sidangkal, kecamatan padangsidimpuan selatan, kota padangsidimpuan", 200, "Ternak Sapi", 2019)
        self.jenis = jenis


class JenisHewan(Hewan):
    jenis_hewan = set()

    def __init__(self, jenis):
        super().__init__(jenis)
        self.jenis_hewan.add(jenis)

    @classmethod
    def tampilkan_jenis(cls):
        print("\n===== Jenis Hewan Ternak =====")
        for jenis in cls.jenis_hewan:
            print(jenis)
        print("===============================")


class Karyawan(Peternakan):
    def __init__(self, nama, alamat, hobi, umur, pendidikan):
        super().__init__("Peternakan Ujung Kulon", "Jl. Sutan Maujalo, kelurahan sidangkal, kecamatan padangsidimpuan selatan, kota padangsidimpuan", 200, "Ternak Sapi", 2019)
        self.nama = nama
        self.alamat = alamat
        self.hobi = hobi
        self.umur = umur
        self.pendidikan = pendidikan
        self.jobdesk_status = {'Memberi Makan Hewan Ternak': False,
                               'Memandikan Hewan Ternak': False,
                               'Menjaga Hewan Ternak': False}

    def data_diri_karyawan(self):
        print("\n===== Data Diri Karyawan =====")
        print(f"Nama: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Hobi: {self.hobi}")
        print(f"Umur: {self.umur}")
        print(f"Pendidikan: {self.pendidikan}")
        print("===============================")

    def jobdesk(self):
        print("\n===== Jobdesk Karyawan =====")
        for job, status in self.jobdesk_status.items():
            if status:
                print(f"{job}: Sudah dilakukan")
            else:
                print(f"{job}: Belum dilakukan")
        print("===============================")

    def perintah_karyawan(self):
        print("\n===== Perintah Karyawan =====")
        print("1. Beri Makan Hewan Ternak")
        print("2. Mandikan Hewan Ternak")
        print("3. Jaga Hewan Ternak")
        print("4. Kembali")

        pilihan_perintah = input("Pilih perintah (1-4): ")

        if pilihan_perintah == "1":
            self.beri_makan_hewan()
        elif pilihan_perintah == "2":
            self.mandikan_hewan()
        elif pilihan_perintah == "3":
            self.jaga_hewan()
        elif pilihan_perintah == "4":
            pass
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

    def beri_makan_hewan(self):
        self.jobdesk_status['Memberi Makan Hewan Ternak'] = True
        print(f"Hewan Ternak sudah diberi makan oleh {self.nama}.")

    def mandikan_hewan(self):
        self.jobdesk_status['Memandikan Hewan Ternak'] = True
        print(f"Hewan Ternak sudah dimandikan oleh {self.nama}.")

    def jaga_hewan(self):
        print("\n===== Jaga Hewan Ternak =====")
        menjaga = input(f"Apakah {self.nama} akan menjaga Hewan Ternak? (ya/tidak): ")
        if menjaga.lower() == "ya":
            print("Hewan kamu aman.")
        else:
            print("Hewan kamu telah dicuri seseorang.")
            # Simulate a random decrease in the number of cows
            random_decrease = random.randint(1, 5)
            for hewan in self.daftar_hewan:
                if hewan['jumlah'] >= random_decrease:
                    hewan['jumlah'] -= random_decrease
                    self.update_hewan(hewan['id'], hewan['nama'], hewan['umur'], hewan['harga'], hewan['jumlah'])  # Update data di database
            print(f"{random_decrease} sapi telah hilang.")
        print("===============================")


def main():
    print("===== Selamat datang di aplikasi peternakku =====")
    peternakan = Peternakan("Peternakan Ujung Kulon", "Jl. Sutan Maujalo, kelurahan sidangkal, kecamatan padangsidimpuan selatan, kota padangsidimpuan", 200, "Ternak Sapi", 2019)
    hewan = Hewan("Sapi")
    karyawan = Karyawan("Yudi", "Jl.Melati Seberang", "Balapan", 25, "S1 Teknik Informatika")

    while True:
        print("\nMenu Utama:")
        print("1. Tentang Peternakan")
        print("2. Hewan yang Ada pada Peternakan")
        print("3. Tentang Karyawan")
        print("4. Keluar")

        pilihan_utama = input("Pilih menu (1-4): ")

        if pilihan_utama == "1":
            peternakan.informasi_peternakan()
        elif pilihan_utama == "2":
            peternakan.menu_hewan()
        elif pilihan_utama == "3":
            while True:
                print("\nMenu Karyawan:")
                print("1. Data Diri Karyawan")
                print("2. Jobdesk")
                print("3. Perintah Karyawan")
                print("4. Tambah Karyawan")
                print("5. Kembali")

                pilihan_karyawan = input("Pilih menu (1-5): ")

                if pilihan_karyawan == "1":
                    karyawan.data_diri_karyawan()
                elif pilihan_karyawan == "2":
                    karyawan.jobdesk()
                elif pilihan_karyawan == "3":
                    karyawan.perintah_karyawan()
                elif pilihan_karyawan == "4":
                    karyawan_tambahan = Karyawan(input("Nama: "), input("Alamat: "), input("Hobi: "), int(input("Umur: ")), input("Pendidikan: "))
                    peternakan.daftar_hewan.extend(karyawan_tambahan.daftar_hewan)
                    print(f"{karyawan_tambahan.nama} telah ditambahkan sebagai karyawan.")
                elif pilihan_karyawan == "5":
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
        elif pilihan_utama == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
