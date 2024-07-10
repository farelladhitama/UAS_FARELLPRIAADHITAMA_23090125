class RestoranAntrian:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        """Menambahkan pesanan baru ke dalam antrian."""
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' ditambahkan ke antrian.")

    def dequeue(self):
        """Menghapus pesanan dari depan antrian."""
        if not self.antrian:
            print("Antrian kosong.")
            return None
        pesanan = self.antrian.pop(0)
        print(f"Pesanan '{pesanan}' diproses.")
        return pesanan

if __name__ == "__main__":
    antrian_restoran = RestoranAntrian()

    
    antrian_restoran.enqueue("Nasi Goreng")
    antrian_restoran.enqueue("Mie Ayam")
    antrian_restoran.enqueue("Bakso")

    
    antrian_restoran.dequeue()
    antrian_restoran.dequeue()
    antrian_restoran.dequeue()