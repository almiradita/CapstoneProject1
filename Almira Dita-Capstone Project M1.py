# ALMIRA DITA
# JCDS2104
# CAPSTONE PROJECT MODUL 1
# RENTAL MOBIL


from prettytable import PrettyTable

list_mobil = [
    ['AB 1234 SWA','Toyota','Avanza', '6 Passengers', 'Dengan Sopir', 'Jogja', 200000,'Available'],
    ['AB 2345 SRO', 'Daihatsu','Ayla','4 Passengers','Tanpa Sopir', 'Jogja',120000,'Available'],
    ['AB 5678 WIL','Mitsubishi','Xpander','6 Passengers','Tanpa Sopir','Jogja', 300000,'Available'],
    ['DK 3456 TRO', 'Toyota','Avanza', '6 Passengers','Dengan Sopir','Bali', 275000,'Available'],
    ['DK 4567 SPA','Suzuki','Ertiga', '6 Passengers', 'Dengan Sopir','Bali', 280000,'Available'],
    ['DK 6789 WIM','Mitsubishi','Xpander', '6 Passengers','Tanpa Sopir','Bali', 400000,'Available']
]

t1 = PrettyTable(['No Index','Plat Nomor','Brand','Name','Capacity','Notes','City','Price/day','Status'])
t2 = PrettyTable(['Plat Nomor','Brand','Name','Notes','City','Price/day','Days','Total Price'])

#Function u/ memanggil seluruh daftar mobil
def ListMobil() :
    global t1
    for index in range(len(list_mobil)):
        car = list_mobil[index]
        t1.add_row([index] + car)  # Tambahkan nomor index ke depan data mobil
    
    print(t1)


#Function u/ memanggil daftar mobil berdasarkan wilayah 
def ListMobil_Wilayah(wilayah) :
    global t1
    t1.clear_rows()
    for index in range(len(list_mobil)):
        car = list_mobil[index]
        if car[5] == wilayah :
             t1.add_row([index] + car)
    if t1.rowcount > 0 : # u/ cek apakah ada mobil yang tersedia di wilayah tsb, jika baris > 0 maka mobil di wilayah tsb ada
        print(f'List Mobil di {wilayah}')
        print(t1)
    else :
        print(f'Tidak ada mobil tersedia di wilayah {wilayah}')

#Functin u/ tambah mobil
def tambah_mobil():
    a = input('Plat Nomor :')
    b = input('Car Brand :')
    c = input('Car Name :')
    d = input('Capacity (How many passengers?):')
    e = input('Tanpa / Dengan Sopir?')
    f = input('Wilayah :')
    g = int(input('Price/day :'))
    h = input('Status :')

    list_mobil.append([a,b,c,d,e,f,g,h])


#Function u/ update list mobil
def Update_List(index):
    global list_mobil

    list_mobil[index][0] = input('Plat Nomor :')
    list_mobil[index][4] = input('Tanpa / Dengan Sopir?')
    list_mobil[index][5] = input('Wilayah :')
    list_mobil[index][6] = int(input('Price/day :'))
    list_mobil[index][7] = input('Status :')

    print(f'Informasi mobil pada index ke-{index} berhasil diperbarui\nList Mobil Terbaru')
 
# Function u/ Sewa Mobil
cart = []
def sewa_mobil(cart) :
    global t2
    global total_harga
    total_harga = 0
    for i in cart :
        plat_nomor = list_mobil[i[0]][0]
        brand = list_mobil[i[0]][1]
        name = list_mobil[i[0]][2]
        notes = list_mobil[i[0]][4]
        wilayah = list_mobil[i[0]][5]
        harga = list_mobil[i[0]][6]
        hari = i[1]
        total_bayar = harga * i[1]
        total_harga+=total_bayar

        t2.add_row([plat_nomor,brand,name,notes,wilayah,harga,hari,total_bayar])
       
        
    print(t2)


while True :
    print (
        f''' Rental Mobil Online Tanpa Ribet di Indonesia!
        Pilihan Menu:
        1. Daftar Rental Mobil
        2. Tambah List Mobil
        3. Hapus List Mobil
        4. Update List Mobil
        5. Pesan dan Sewa Mobil
        6. Exit Program''')
    menu = int(input(f'Masukkan pilihan menu yang diinginkan: '))

    if menu == 1:
        print (
        f''' 
        Pilihan Tampilan Daftar Mobil:
        1. Daftar Seluruh Rental Mobil
        2. Daftar Rental Mobil Berdasarkan Wilayah 
        ''')
        menu_mobil = int(input(f'Masukkan pilihan tampilan daftar mobil yang diinginkan: '))

        if menu_mobil == 1 :
            t1.clear_rows()
            print('List Mobil')
            ListMobil()
        
        if menu_mobil == 2 :
             wilayah = input('Dimana anda ingin sewa mobil?')

             ListMobil_Wilayah(wilayah)
        

    elif menu == 2:
        t1.clear_rows()
        tambah_mobil()

        print(f'Mobil berhasil ditambahkan!\nBerikut adalah List Mobil Terbaru')
        ListMobil() #u/ nampilin seluruh daftar mobil termasuk yang baru ditambahkan
        

    elif menu == 3 :
        t1.clear_rows()
        ListMobil()

        hapus_index = int(input(f'Masukkan nomor index mobil yang ingin dihapus :'))
        del list_mobil[hapus_index]

        print(f'Mobil ke-{hapus_index} berhasil dihapus!')

        t1.clear_rows()
        print('List Mobil Terbaru')
        ListMobil()
    
    elif menu == 4 :
        t1.clear_rows()
        print('List Mobil')
        ListMobil()

        index = int(input(f'Masukkan nomor index mobil untuk memperbarui informasi :'))
        Update_List(index) # Function u/ update mobil 

        t1.clear_rows()
        ListMobil()

    elif menu == 5 :
        t1.clear_rows()
        print('List Mobil')
        ListMobil()

        while True :
            order_index = int(input(f'Mohon masukkan nomor index mobil yang ingin disewa :'))
            order_hari = int(input(f'Mohon masukkan jumlah hari untuk menyewa mobil :'))

            if (order_index >= 0) and order_index < len(list_mobil) :
                cart.append([order_index,order_hari])
                

                checker = input('Apakah ingin menambahkan pesanan lagi? (ya/tidak) :')
                if checker.lower() == 'tidak' :
                    break
            else :
                print('Mohon Maaf! Mobil tidak ada di dalam Daftar Rental Mobil')
            
        print('Pesanan Rental Mobil')
        sewa_mobil(cart)

        while True :
            print(f'Total Harga = {total_harga}')
            jumlah_uang = int(input('Masukkan jumlah uang yang ingin dibayar :'))

            if jumlah_uang > total_harga :
                kembalian = jumlah_uang - total_harga
                print(f'Terima Kasih!\nUang kembalian anda adalah {kembalian}')
            # u/ hapus mobil yang sudah dipesan
                for i in cart :
                    list_mobil[i[0]][7] = 'Not Available'
                break
            elif jumlah_uang == total_harga :
                print(f'Terima Kasih!')
                for i in cart :
                    list_mobil[i[0]][7] = 'Not Available'
                break
            else :
                print(f'Uang anda masih kurang {total_harga - jumlah_uang}')

    elif menu == 6:
        break