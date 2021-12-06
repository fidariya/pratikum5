daftar = {'Nama': 'Nomor Telepon'}
nomor = {'Ari': '081267888','Dina':'087677776'}

print('# Nama    | Nomor Telepon')
for daftar in nomor:
    print('# {:6}  | {:15} '.format(daftar ,nomor[daftar]))

print('Menampilkan Kontak Ari | Ari :',nomor['Ari'])

nomor['Riko']='087654544'
print('Menambahkan Kontak Riko')
print('Data Setelah Diubah')
print('# Nama    | Nomor Telepon')
for daftar in nomor:
    print('# {:6}  | {:15} '.format(daftar ,nomor[daftar]))

nomor['Dina']='088999776'
print('Mengumbah Kontak Dina Dengan Nomor 088999776')
print('Data Setelah Diubah')
print('# Nama    | Nomor Telepon')
for daftar in nomor:
    print('# {:6}  | {:15} '.format(daftar ,nomor[daftar]))

print('Menampilkan Semua Nama: ')
print(nomor.keys())
print('Menampilkan Semua Kontak: ')
print(nomor.values())
print('Menampilkan Daftar Nama dan Kontak: ')
print(nomor.items())
