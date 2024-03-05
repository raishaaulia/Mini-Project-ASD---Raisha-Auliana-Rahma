class Node:
    def __init__(self, paket):
        self.data = paket
        self.next = None 

class PengirimanData:
    def __init__(self):
        self.head = None

    def add_first(self, paket):
        new_node = Node(paket)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, paket):
        new_node = Node(paket)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def add_after(self, prev_node, paket):
        if prev_node is None:
            print("Node sebelumnya tidak ditemukan.")
            return
        new_node = Node(paket)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            prev_node = self.head
            last_node = self.head.next
            while last_node.next is not None:
                prev_node = last_node
                last_node = last_node.next
            prev_node.next = None

    def delete_after(self, prev_node):
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next

    def update_paket(self, kode_pengiriman):
        current_node = self.head
        while current_node:
            if current_node.data.kode_pengiriman == kode_pengiriman:
                print("\n=========================================")
                print("Update Paket dengan Kode", kode_pengiriman)
                print("==========================================")
                current_node.data.nama_pengirim = input("Masukkan Nama Pengirim baru: ")
                current_node.data.alamat_pengirim = input("Masukkan Alamat Pengirim baru: ")
                current_node.data.nama_penerima = input("Masukkan Nama Penerima baru: ")
                current_node.data.alamat_penerima = input("Masukkan Alamat Penerima baru: ")
                current_node.data.detail_barang = input("Masukkan Detail Barang baru: ")
                current_node.data.biaya_pengiriman = input("Masukkan Biaya Pengiriman baru: ")
                print("Paket telah diperbarui.")
                return
            current_node = current_node.next
        print("Paket dengan kode", kode_pengiriman, "tidak ditemukan.")


    def print_list(self):
        if self.head is None:
            print("\nList Pendataan Kosong.")
        else:
            print("\n========================")
            print("List Pendataan Pengiriman")
            print("=========================")
            current_node = self.head
            while current_node:
                print("Kode Pengiriman:", current_node.data.kode_pengiriman)
                print("Nama Pengirim:", current_node.data.nama_pengirim)
                print("Alamat Pengirim:", current_node.data.alamat_pengirim)
                print("Nama Penerima:", current_node.data.nama_penerima)
                print("Alamat Penerima:", current_node.data.alamat_penerima)
                print("Detail Barang:", current_node.data.detail_barang)
                print("Jasa Pengirim:", current_node.data.jasa_pengirim)
                print("Biaya Pengiriman:", current_node.data.biaya_pengiriman)
                print("-----------------------------")
                current_node = current_node.next

class Paket:
    def __init__(self, kode_pengiriman, nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, detail_barang, biaya_pengiriman, jasa_pengirim="JNE"):
        self.kode_pengiriman = kode_pengiriman
        self.nama_pengirim = nama_pengirim
        self.alamat_pengirim = alamat_pengirim
        self.nama_penerima = nama_penerima
        self.alamat_penerima = alamat_penerima
        self.detail_barang = detail_barang
        self.jasa_pengirim = jasa_pengirim
        self.biaya_pengiriman = biaya_pengiriman

def main():
    data = PengirimanData()

    while True:
        print("\n=================================")
        print("Sistem Pendataan Pengiriman Paket")
        print("=================================")
        print("1. Tambah Paket")
        print("2. Hapus Paket")
        print("3. Update Paket")
        print("3. Tampilkan Semua Pengiriman")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            print("\n=========================")
            print("Penempatan Pendataan Paket")
            print("=========================")
            print("1. Tambah di Awal")
            print("2. Tambah di Akhir")
            print("3. Tambah di Tengah")

            pilihan_tambah = input("Masukkan pilihan penempatan: ")

            kode_pengiriman = input("Masukkan Kode Pengiriman: ")
            nama_pengirim = input("Masukkan Nama Pengirim: ")
            alamat_pengirim = input("Masukkan Alamat Pengirim: ")
            nama_penerima = input("Masukkan Nama Penerima: ")
            alamat_penerima = input("Masukkan Alamat Penerima: ")
            detail_barang = input("Masukkan Detail Barang: ")
            biaya_pengiriman = input("Masukkan Biaya Pengiriman: ")

            paket_baru = Paket(kode_pengiriman, nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, detail_barang, biaya_pengiriman)

            if pilihan_tambah == '1':
                data.add_first(paket_baru)
            elif pilihan_tambah == '2':
                data.add_last(paket_baru)
            elif pilihan_tambah == '3':
                prev_kode = input("Masukkan Kode Node Sebelumnya: ")
                prev_node = None
                current_node = data.head
                while current_node is not None:
                    if current_node.data.kode_pengiriman == prev_kode:
                        prev_node = current_node
                        break
                    current_node = current_node.next
                if prev_node is None:
                    print("Node sebelumnya tidak ditemukan.")
                else:
                    data.add_after(prev_node, paket_baru)
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '2':
            print("\n=========================")
            print("Penempatan Pendataan Paket")
            print("=========================")
            print("1. Hapus di Awal")
            print("2. Hapus di Akhir")
            print("3. Hapus di Tengah")

            pilihan_hapus = input("Masukkan pilihan penghapusan: ")

            if pilihan_hapus == '1':
                data.delete_first()
            elif pilihan_hapus == '2':
                data.delete_last()
            elif pilihan_hapus == '3':
                kode_node = input("Masukkan Kode Node yang akan dihapus setelahnya: ")
                prev_node = None
                current_node = data.head
                while current_node is not None:
                    if current_node.data.kode_pengiriman == kode_node:
                        prev_node = current_node
                        break
                    current_node = current_node.next
                if prev_node is None:
                    print("Node tidak ditemukan.")
                else:
                    data.delete_after(prev_node)
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '3':
            kode_pengiriman = input("Masukkan kode pengiriman yang akan diupdate: ")
            data.update_paket(kode_pengiriman)

        elif pilihan == '4':
            data.print_list()

        elif pilihan == '5':
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
