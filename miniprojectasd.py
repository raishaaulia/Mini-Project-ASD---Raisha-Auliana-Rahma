class Paket:
    def __init__(self, kode_pengiriman, nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, detail_barang, biaya_pengiriman, jasa_pengirim = "JNE"):
        self.kode_pengiriman = kode_pengiriman
        self.nama_pengirim = nama_pengirim
        self.alamat_pengirim = alamat_pengirim
        self.nama_penerima = nama_penerima
        self.alamat_penerima = alamat_penerima
        self.detail_barang = detail_barang
        self.jasa_pengirim = jasa_pengirim
        self.biaya_pengiriman = biaya_pengiriman

class PengirimanData:
    def __init__(self):
        self.data_pengiriman = []

    def tambah_paket(self, paket):
        self.data_pengiriman.append(paket)

    def hapus_paket(self, kode_pengiriman):
        if kode_pengiriman in self.data_pengiriman:
            del self.data_pengiriman[kode_pengiriman]
            print("Paket dengan kode, kode_pengiriman, telah dihapus.\n")
        else:
            print("Paket dengan kode, kode_pengiriman, tidak ditemukan.\n")

    def tampilkan_pengiriman(self):
        if self.data_pengiriman:
            print("\n---------------------")
            print("Data Pengiriman Paket")
            print("---------------------")
            for paket in self.data_pengiriman:
                print("Kode Pengiriman:", paket.kode_pengiriman)
                print("Nama Pengirim:", paket.nama_pengirim)
                print("Alamat Pengirim:", paket.alamat_pengirim)
                print("Nama Penerima:", paket.nama_penerima)
                print("Alamat Penerima:", paket.alamat_penerima)
                print("Detail Barang:", paket.detail_barang)
                print("Jasa Pengirim:", paket.jasa_pengirim)
                print("Biaya Pengiriman:", paket.biaya_pengiriman)
                print()
        else:
            print("Tidak ada data pengiriman paket.\n")

    def update_paket(self, kode_pengiriman):
        for paket in self.data_pengiriman:   
            kode_pengiriman = input("\nMasukkan Kode Pengiriman: ")
            if kode_pengiriman == paket.kode_pengiriman:
                print("------------------------")
                print("Update Paket dengan Kode", kode_pengiriman)
                print("------------------------")
                paket.nama_pengirim = input("Masukkan Nama Pengirim baru: ")
                paket.alamat_pengirim = input("Masukkan Alamat Pengirim baru: ")
                paket.nama_penerima = input("Masukkan Nama Penerima baru: ")
                paket.alamat_penerima = input("Masukkan Alamat Penerima baru: ")
                paket.detail_barang = input("Masukkan Detail Barang baru: ")
                paket.biaya_pengiriman = input("Masukkan Biaya Pengiriman baru: ")
                print("Paket telah diperbarui.")
                return 
            else:
                print("Paket dengan kode", kode_pengiriman, "tidak ditemukan", "\n")

def main():
    data = PengirimanData()

    while True:
        print("\n=================================")
        print("Sistem Pendataan Pengiriman Paket")
        print("=================================")
        print("1. Tambah Paket")
        print("2. Hapus Paket")
        print("3. Tampilkan Semua Pengiriman")
        print("4. Update Data Paket")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            kode_pengiriman = input("\nMasukkan Kode Pengiriman: ")
            nama_pengirim = input("Masukkan Nama Pengirim: ")
            alamat_pengirim = input("Masukkan Alamat Pengirim: ")
            nama_penerima = input("Masukkan Nama Penerima: ")
            alamat_penerima = input("Masukkan Alamat Penerima: ")
            detail_barang = input("Masukkan Detail Barang: ")
            biaya_pengiriman = input("Masukkan Biaya Pengiriman: ")

            paket_baru = Paket(kode_pengiriman, nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, detail_barang, biaya_pengiriman)
            data.tambah_paket(paket_baru)
            print("Paket telah ditambahkan.")

        elif pilihan == '2':
            kode_pengiriman = input("\nMasukkan kode pengiriman yang akan di hapus: ")
            data.hapus_paket(kode_pengiriman)

        elif pilihan == '3':
            data.tampilkan_pengiriman()

        elif pilihan == '4':
            data.update_paket(kode_pengiriman)

        elif pilihan == '5':  
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
