# Mini Project 1
Nama : Muhammad Indra Pratama<br>
NIM : 083<br>
Kelas : C

# Sistem Pengelolaan Jual Beli Akun Game Online
Sebelum saya menjelaskan bagaimana sistem ini berjalan saya akan memperihatkan Flowchart sistem yang akan saya jelaskan nanti.

<img width="3357" height="2102" alt="Flowchart Sistem Pengelolaan Jual Beli Game Online" src="https://github.com/user-attachments/assets/c3e5dff0-ce6b-4ef7-9a01-c914b486ccb9" />

# Operator Yang Ada Di Dalam Sistem
<img width="534" height="208" alt="Screenshot 2026-09-12 005108" src="https://github.com/user-attachments/assets/b43ff24c-4692-4e8b-b9a8-93bc5cb149a5" />

Nah sebelum saya menjelaskan seluruh isi menu" ini. Saya akan menjelaskan sedikit fungsi dari menu yang saya buat ini.
- Disini, untuk variabel akun akan saya kosongkan isi kurung sikunya, karena nanti akan di isi di sistem nantinya.
- Untuk menu yang pertama berfungsi untuk mengisi variabel yang sebelumnya kosong. Untuk detailnya nanti akan saya jelaskan nanti.
- Di menu ke-2, ini berfungsi untuk melihat akun yang sudah kita buat nantinya.
- Di menu ke-3, ini berfungsi untuk mengubah data akun yang telah kita buat nantinya.
- Di menu ke-4, ini berfungsi untuk menghapus akun yang sudah kita buat tadinya.
- Dan dimenu yang terakhir, ini berfungsi untuk menutup sistem.
- Jika kita salah input di menu utama, sistem akan mengeluarkan output "Pilihan tidak valid, coba lagi."

**Dan ini untuk hasil output menunya**

<img width="566" height="398" alt="Screenshot 2026-09-12 004343" src="https://github.com/user-attachments/assets/2b0c79dc-159f-403c-8f13-6c9a658388eb" />

## Fungsi Dari Seluruh Menu
Disini saya akan menjelaskan satu per satu fungsi dari seluruh menu yang sudah Saya jelaskan tadi.

### Tambah Akun

<img width="950" height="437" alt="Screenshot 2026-09-11 203950" src="https://github.com/user-attachments/assets/41232544-78de-4804-832d-8fa16b666a64" />

Ini adalah menu pertama yang saja jelaskan tadi. Disini saya akan menjelaskan fungsi Operator yang saya pakai didalam menu pertama
- Setelah kita masuk ke menu pertama, kita akan langsung menginput Username akun yang ingin kita jual. Setelah kita menginput Username, kita akan menginput nama game akun yang kita masukkan tadi.
- Setelah kita menginput Username dan nama game akun tersebut, kita akan menginput harga akun yang ingin kita jual. Dan kita harus menginput dengan format numerik (nomor), jika kita masih menginput selain dengan format yang ditentukan maka sistem akan mengeluarkan output "Harga hanya boleh berisi angka tanpa huruf atau simbol!".
- Dan setelah kita menginput username, nama game, dan harga jual akun. Disini kita akan menginput status akun, status akun ini hanya bisa di isi format Terjual/Tersedia. Selain itu tidak bisa, jika dipaksa maka akan mengelarkan output "Status hanya boleh 'Tersedia' atau 'Terjual' Tidak ada pilihan lain.".
- Setelah semua input sudah terisi, maka sistem akan menyimpan akun yang sudah dibuat tadi dan akan mengeluarkan output "Akun berhasil ditambahkan.", dan sistem akan kembali ke menu utama.

**Ini untuk hasil output tambah akun.**

<img width="767" height="438" alt="Screenshot 2026-09-12 005131" src="https://github.com/user-attachments/assets/59bdd09c-0727-4a28-9cdd-473b60ce43ae" />

### View Akun
<img width="895" height="153" alt="Screenshot 2026-09-12 005142" src="https://github.com/user-attachments/assets/559f50eb-6219-497d-b93e-0be8eaae6931" />

Dan ini adalah fungsi dari menu ke-2 yaitu View Akun, dan disini kita bisa melihat seluruh akun yang sudah kita buat tadi.
- Setelah kita memilih menu ke-2, maka sistem akan mengeluarkan output seluruh akun yang telah dibuat tadi.
- Jika tidak ada akun yang kita buat, maka sistem akan mengeluarkan output yang berisikan "Tidak ada data akun.", dan sistem akan kembali ke menu utama.
- Dan untuk output akun (jika ada) maka sistem akan mengeluarkan output akun yang berisikan username, nama game, harga jual, dan status penjualan. Setelah itu sistem akan kembali ke menu utama.

**Dan ini untuk output View Akun.**<br>
Ini output jika ada akun yang dibuat.

<img width="549" height="377" alt="Screenshot 2026-09-12 005038" src="https://github.com/user-attachments/assets/c0c492f8-d7d9-4988-9b58-29ffe08bf49b" />

Ini output jika tidak ada membuat akun.

<img width="388" height="257" alt="Screenshot 2026-09-12 005052" src="https://github.com/user-attachments/assets/6f6adb79-c090-42f1-92f7-f03be3b34c9f" />

### Update Data Akun

<img width="875" height="756" alt="Screenshot 2026-09-12 005155" src="https://github.com/user-attachments/assets/f42f164a-bedf-40ab-b1cd-a3376b2995ea" />

Ini adalah Operator di menu ke-3 yaitu Update Data Akun. Disini saya akan menjelaskan bagaimana sistemnya berjalan

- Setelah kita memilih menu ke-3, maka sistem akan mengeluarkan output seluruh akun yang sudah kita buat untuk di ubah datanya.
- Jika tidak ada. Maka sistem akan mengeluarkan output "Tidak ada data akun.", dan sistem akan kembali ke menu utama.
- Jika ada data akun maka kita akan memilih akun mana yang mau kita ubah. Jika kita menginput simbol selain angka, maka sistem akan mengeluarkan output "Input harus berupa angka, tidak boleh huruf atau simbol." .
- Jika kita sudah memilih akun yang mana mau kita ubah, maka sistem akan menyuruh kita untuk menginput username, nama akun, harga jual, dan status akun sama seperti di menu yang pertama.
- Setelah kita sudah merubah data akun yang kita pilih tadi. maka sistem akan mengeluarkan output "Data akun telah diupdate".
- Dan data akun yang kita pilih tadi sudah berubah seperti yang kita input barusan, dan sistem akan kembali ke menu utama.

**Ini untuk output Update Data Akun**<br>
Ini jika ada akun yang dibuat.

<img width="581" height="551" alt="Screenshot 2026-09-12 011200" src="https://github.com/user-attachments/assets/b4076d34-7af2-4f05-b088-1b8e18970416" />

Ini output jika tidak ada membuat akun.

<img width="384" height="416" alt="Screenshot 2026-09-12 011219" src="https://github.com/user-attachments/assets/b361a499-3fce-426f-875e-9911eddc8935" />

### Delete Akun
<img width="735" height="400" alt="Screenshot 2026-09-12 005214" src="https://github.com/user-attachments/assets/f5e283a1-d118-4d30-b998-0ea53e6fdea9" />

Ini adalah menu ke-4 yaitu delete akun. Disini saya akan menjelaskan lagi Operator akan berjalan pada menu ini.
- Disini jika kita tidak ada membuat akun sama sekali sistem akan mengeluarkan output "Tidak ada data akun."
- Jika hanya ada 1 akun saja. Maka sistem akan mengeluarkan output "Hanya ada satu akun, Akun akan langsung dihapus.", Dan sistem langsung menghapus akun yang kita buat tadi.
- Dan Jika ada lebih dari 1 akun. Maka sistem akan memerintahkan kita untuk memilih akun yang kita buat tadi. Dan sama seperti pemilihan akun pada Update Data Akun, sistem akan mengeluarkan output yang sama.
- Dan jika kita salah menginput nomor akun yang tersedia maka sistem akan mengeluarkan output "Nomor akun tidak valid."
- Jika sudah memilih akun yang ingin kita hapus, maka sistem akan mengeluarkan output "Akun Telah Terhapus." .

**Ini untuk output Delete Akun**<br>
Ini output jika tidak ada akun yang dibuat sama sekali.

<img width="367" height="419" alt="Screenshot 2026-09-12 012631" src="https://github.com/user-attachments/assets/f8f91e6f-257f-4ef3-aba4-cb41aa7bf2b2" />

Ini juga output jika hanya ada 1 akun yang dibuat.

<img width="463" height="406" alt="Screenshot 2026-09-12 012701" src="https://github.com/user-attachments/assets/6fbf9354-ed89-4dde-93de-11405dc6b8fe" />

Dan ini untuk output jika ada lebih dari 1 akun.

<img width="566" height="485" alt="Screenshot 2026-09-12 012804" src="https://github.com/user-attachments/assets/55a281d7-869a-4265-afd1-0a8dbe72c871" />

### Keluar
<img width="1123" height="326" alt="Screenshot 2026-09-11 201608" src="https://github.com/user-attachments/assets/ce684a15-ce18-4f0e-a7a2-3150284a411f" />

Ini adalah menu yang terakhir yaitu Keluar. Sebenarnya ini adalah Operator input menu utama. Jadi saya akan menjelaskan Operator yang ada pada gambar diatas
- Untuk line ke 108-115 ini adalah Operator yang akan membawa kita menuju menu-menu yang sudah saya jelaskan tadi.
- Dan untuk line ke 116 ini berfungsi untuk menutup sistem yang berjalan. Sebelum menutup sistem sistem akan mengeluarkan output "Terima kasih telah menjual akun di tempat kami"
- Dan saya juga menambah operator di menu utama jika kita ada salah input di menu utama, maka sistem akan mengeluarkan output "Pilihan tidak valid, coba lagi."

**Dan ini output yang ada pada menu utama**<br>
Akses ke menu pertama

<img width="429" height="232" alt="Screenshot 2026-09-12 014407" src="https://github.com/user-attachments/assets/0c0c54e5-f950-436e-bd18-a40a6039d0d6" />

Ini akses ke menu ke-2

<img width="350" height="221" alt="Screenshot 2026-09-12 014423" src="https://github.com/user-attachments/assets/25ff212b-80ae-4aa3-98d1-11ba9e05e32a" />

Ini akses ke menu ke-3

<img width="393" height="233" alt="Screenshot 2026-09-12 014440" src="https://github.com/user-attachments/assets/fe57b660-cb45-49ee-84af-8d6ac95f94c1" />

Dan ini akses ke menu ke-4

<img width="384" height="222" alt="Screenshot 2026-09-12 014452" src="https://github.com/user-attachments/assets/3a5654b5-aa29-46bb-aa96-4599b14bb55a" />

Ini jika kita memilih menu yang terakhir

<img width="615" height="248" alt="Screenshot 2026-09-12 014502" src="https://github.com/user-attachments/assets/73d41160-f367-4770-9ac2-816a3fdc276d" />

# 
**Ini adalah output tambahan jika kita salah input di menu utama**

<img width="453" height="398" alt="Screenshot 2026-09-12 013056" src="https://github.com/user-attachments/assets/1148d2c6-4704-4aca-83b7-594294949cab" />

#
Jika ada salah typo dalam pengetikan saya minta maaf.<br>
Dan Terima Kasih telah membaca.
