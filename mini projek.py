class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def tambah_di_antara(self, prev_node, data):
        if not prev_node:
            print("Node sebelumnya tidak ditemukan.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def hapus_di_awal(self):
        if not self.head:
            print("LinkedList sudah kosong.")
            return
        self.head = self.head.next

    def hapus_di_akhir(self):
        if not self.head:
            print("LinkedList sudah kosong.")
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def hapus_di_antara(self, prev_node):
        if not prev_node or not prev_node.next:
            print("Node sebelumnya tidak ditemukan.")
            return
        prev_node.next = prev_node.next.next

    def bubble_sort(self, arr, key):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j][key] > arr[j+1][key]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def cetak_daftar_buah(self, key=None, ascending=True):
        if not self.head:
            print("LinkedList kosong.")
            return
        buah_list = []
        current_node = self.head
        while current_node:
            buah_list.append(current_node.data)
            current_node = current_node.next
        if key and key in ['harga', 'stok']:
            sorted_buah_list = self.bubble_sort(buah_list, key)
            if not ascending:
                sorted_buah_list.reverse()
            print("=========================== Daftar Buah di Toko =============================================")
            print("{:<15} {:<10} {:<10} {:<15} {:<30}".format("Nama", "Harga", "Stok", "Jenis", "Kualitas"))
            for buah in sorted_buah_list:
                print("{:<15} {:<10} {:<10} {:<15} {:<30}".format(buah['nama'], buah['harga'], buah['stok'], buah['jenis'], buah['kualitas']))
        else:
            print("Atribut yang diizinkan untuk pengurutan hanya 'harga' dan 'stok'.")
            print("\nDaftar Buah di Toko:")
            for buah in buah_list:
                print("{:<15} {:<10} {:<10} {:<15} {:<30}".format(buah['nama'], buah['harga'], buah['stok'], buah['jenis'], buah['kualitas']))

class TokoBuah:
    def __init__(self):
        self.daftar_buah = LinkedList()

        self.daftar_buah.tambah_di_awal({'nama': 'Semangka', 'harga': 10000, 'stok': 20, 'jenis': 'Semangka Kuning', 'kualitas': 'Local'})
        self.daftar_buah.tambah_di_awal({'nama': 'Anggur', 'harga': 15000, 'stok': 15, 'jenis': 'Anggur Hijau', 'kualitas': 'Impor'})
        self.daftar_buah.tambah_di_awal({'nama': 'Jeruk', 'harga': 8000, 'stok': 50, 'jenis': 'Jeruk Purut', 'kualitas': 'local'})
        self.daftar_buah.tambah_di_awal({'nama': 'Durian', 'harga': 12000, 'stok': 10, 'jenis': 'Durian Montong', 'kualitas': 'impor'})

    def tambah_buah(self, nama, harga, stok, jenis, kualitas):
        data_buah = {'nama': nama, 'harga': harga, 'stok': stok, 'jenis': jenis, 'kualitas': kualitas}
        self.daftar_buah.tambah_di_akhir(data_buah)
        print(f"{nama} berhasil ditambahkan ke dalam daftar buah.")

    def lihat_daftar_buah(self, key=None, ascending=True):
        self.daftar_buah.cetak_daftar_buah(key, ascending)

    def perbarui_buah(self, nama, harga=None, stok=None, jenis=None, kualitas=None):
        current_node = self.daftar_buah.head
        while current_node:
            if current_node.data['nama'] == nama:
                if harga is not None:
                    current_node.data['harga'] = harga
                if stok is not None:
                    current_node.data['stok'] = stok
                if jenis is not None:
                    current_node.data['jenis'] = jenis
                if kualitas is not None:
                    current_node.data['kualitas'] = kualitas
                print(f"Informasi buah {nama} berhasil diperbarui.")
                return
            current_node = current_node.next
        print(f"{nama} tidak ditemukan dalam daftar buah.")

    def hapus_buah(self, nama):
        if not self.daftar_buah.head:
            print("Daftar buah kosong.")
            return
        if self.daftar_buah.head.data['nama'] == nama:
            self.daftar_buah.hapus_di_awal()
            print(f"{nama} berhasil dihapus dari daftar buah.")
            return
        prev_node = self.daftar_buah.head
        while prev_node.next:
            if prev_node.next.data['nama'] == nama:
                self.daftar_buah.hapus_di_antara(prev_node)
                print(f"{nama} berhasil dihapus dari daftar buah.")
                return
            prev_node = prev_node.next
        print(f"{nama} tidak ditemukan dalam daftar buah.")

    def fibonacci_search(self, key1, key2, value1, value2):
        if not self.daftar_buah.head:
            print("Daftar buah kosong.")
            return

        buah_list = []
        current_node = self.daftar_buah.head
        while current_node:
            buah_list.append(current_node.data)
            current_node = current_node.next

        def fibonacci(n):
            fib = [0, 1]
            while fib[-1] < n:
                fib.append(fib[-1] + fib[-2])
            return fib

        value1 = value1.lower()  
        value2 = value2.lower()  

        fib = fibonacci(len(buah_list))
        offset = 0
        while fib:
            index = min(offset + fib.pop(), len(buah_list) - 1)
            if buah_list[index][key1].lower() == value1 and buah_list[index][key2].lower() == value2:  
                return buah_list[index]
            elif buah_list[index][key1].lower() < value1 or (buah_list[index][key1].lower() == value1 and buah_list[index][key2].lower() < value2):  
                offset = index
            else:
                fib.pop()
        return None

if __name__ == "__main__":
    toko = TokoBuah()

    while True:
        print("\nPilihan abang ku:")
        print("1. Tambah Buah")
        print("2. Lihat Daftar Buah")
        print("3. Perbarui Buah")
        print("4. Hapus Buah")
        print("5. Urutkan Daftar Buah")
        print("6. Cari Buah")
        print("7. Keluar")

        pilihan = input("Pilih nomor menu yang diinginkan: ")

        if pilihan == "1":
            nama = input("Masukkan nama buah: ")
            harga = int(input("Masukkan harga buah: "))
            stok = int(input("Masukkan stok buah: "))
            jenis = input("Masukkan jenis buah: ")
            kualitas = input("Masukkan kualitas buah: ")
            toko.tambah_buah(nama, harga, stok, jenis, kualitas)
        elif pilihan == "2":
            print("\nDaftar Buah di Toko:")
            toko.lihat_daftar_buah()
        elif pilihan == "3":
            nama = input("Masukkan nama buah yang ingin diperbarui: ")
            harga = int(input("Masukkan harga baru buah: "))
            stok = int(input("Masukkan stok baru buah: "))
            jenis = input("Masukkan jenis baru buah: ")
            kualitas = input("Masukkan kualitas baru buah: ")
            toko.perbarui_buah(nama, harga, stok, jenis, kualitas)
        elif pilihan == "4":
            nama = input("Masukkan nama buah yang ingin dihapus: ")
            toko.hapus_buah(nama)
        elif pilihan == "5":
            key = input("Masukkan atribut untuk mengurutkan (harga, stok): ")
            order = input("Urutkan secara ascending (asc) atau descending (desc): ")
            ascending = True if order.lower() == "asc" else False
            toko.lihat_daftar_buah(key, ascending)
        elif pilihan == "6":
            key1 = "nama"
            value1 = input("Masukkan nama buah yang ingin dicari: ")
            key2 = "jenis"
            value2 = input("Masukkan jenis buah yang ingin dicari: ")
            result = toko.fibonacci_search(key1, key2, value1, value2)
            if result:
                print("Buah ditemukan:")
                print(result)
            else:
                print("Buah tidak ditemukan.")
        elif pilihan == "7":
            print("Terima kasih! Sudah Datang TETAP MENYALA ABANG KU")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
