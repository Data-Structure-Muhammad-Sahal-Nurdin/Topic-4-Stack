# (1)Import library os untuk membersihkan layar console
import os


# (2)Class stack
class Stack:
    def __init__(self):
        self.items = []

    # (3)Memeriksa apakah stack kosong
    def isEmpty(self):
        return self.items == []

    # (4)Menambah objek/data ke dalam stack
    def push(self, item):
        self.items.append(item)

    # (5)Mengeluarkan data dari stack
    def pop(self):
        return self.items.pop()

    # (6)Menampilkan objek terakhir dari stack

    # (7)Mehitung panjang stack
    def size(self):
        return len(self.items)

    # (8)Menu dari aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("=========================")
            print("| Menu aplikasi stack |")
            print("=========================")
            print("1. Push objek")
            print("2. Pop objek")
            print("3. Cek Empty")
            print("4. Tampil objek terakhir")
            print("5. Panjang dari stack")
            print("=========================")
        pilihan = str(input(("Silakan masukan pilihan anda: ")))
        if (pilihan == "1"):
            os.system("clear")
            obj = str(input("Masukan objek yang ingin anda tambahkan: "))
            self.push(obj)
            print("Object " + obj + " telah ditambahkan")
            x = input("")
        elif (pilihan == "2"):
            os.system("clear")
            print("Objek " + self.pop() + " dihapus")
            x = input("")
        elif (pilihan == "3"):
            os.system("clear")
            print(self.isEmpty())
            x = input("")
        elif (pilihan == "4"):
            os.system("clear")
            print("Objek terakhir: " + self.peek())
            x = input("")
        elif (pilihan == "5"):
            os.system("clear")
            print("Panjang dari stack adalah: " + str(self.size()))
            x = input("")
        else:
            pilih = "n"


if __name__ == "__main__":
    s = Stack()
    s.mainmenu()
