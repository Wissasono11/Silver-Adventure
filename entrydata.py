import pandas as pd

# Membuat ulang data untuk masing-masing tabel setelah reset
dokter = pd.DataFrame({
    'kd_dokter': [f'D{str(i).zfill(3)}' for i in range(1, 11)],
    'nama_dokter': [f'Dokter {i}' for i in range(1, 11)],
    'alamat_dokter': [f'Alamat Dokter {i}' for i in range(1, 11)],
    'spesialisasi_dokter': ['Umum', 'Anak', 'Bedah', 'Kulit', 'THT', 'Mata', 'Gigi', 'Saraf', 'Jantung', 'Paru']
})

ruang = pd.DataFrame({
    'kd_ruang': [f'R{str(i).zfill(3)}' for i in range(1, 11)],
    'nama_ruang': [f'Ruang {i}' for i in range(1, 11)],
    'nama_gudung': [f'Gedung {chr(65+i)}' for i in range(10)]
})

petugas = pd.DataFrame({
    'kd_petugas': [f'P{str(i).zfill(3)}' for i in range(1, 11)],
    'nama_petugas': [f'Petugas {i}' for i in range(1, 11)],
    'alamat_petugas': [f'Alamat Petugas {i}' for i in range(1, 11)],
    'jam_jaga': [f'{8+i%3*8}:00 - {16+i%3*8}:00' for i in range(1, 11)]
})

pasien = pd.DataFrame({
    'kd_pasien': [f'PS{str(i).zfill(3)}' for i in range(1, 11)],
    'nama_pasien': [f'Pasien {i}' for i in range(1, 11)],
    'alamat_pasien': [f'Alamat Pasien {i}' for i in range(1, 11)],
    'tgl_datang': [f'2025-04-{str(i+10).zfill(2)}' for i in range(1, 11)],
    'keluhan': ['Demam', 'Batuk', 'Sakit Perut', 'Pusing', 'Nyeri Dada', 'Mual', 'Sesak Napas', 'Pilek', 'Luka', 'Radang'],
    'kd_dokter': [f'D{str(i).zfill(3)}' for i in range(1, 11)]
})

rawat_inap = pd.DataFrame({
    'kd_rawatinap': [f'RI{str(i).zfill(3)}' for i in range(1, 11)],
    'kd_ruang': [f'R{str(i).zfill(3)}' for i in range(1, 11)],
    'kd_pasien': [f'PS{str(i).zfill(3)}' for i in range(1, 11)]
})

pembayaran = pd.DataFrame({
    'kd_pembayaran': [f'PM{str(i).zfill(3)}' for i in range(1, 11)],
    'kd_petugas': [f'P{str(i).zfill(3)}' for i in range(1, 11)],
    'kd_pasien': [f'PS{str(i).zfill(3)}' for i in range(1, 11)],
    'jumlah_harga': [100000 + i*5000 for i in range(10)]
})

# Simpan ke dalam satu file Excel dengan multiple sheet
with pd.ExcelWriter('D:/Coding/Phyton/Codewars Adventure/excel/antri_database_rumah_sakit.xlsx') as writer:
    dokter.to_excel(writer, sheet_name='dokter', index=False)
    ruang.to_excel(writer, sheet_name='ruang', index=False)
    petugas.to_excel(writer, sheet_name='petugas', index=False)
    pasien.to_excel(writer, sheet_name='pasien', index=False)
    rawat_inap.to_excel(writer, sheet_name='rawat_inap', index=False)
    pembayaran.to_excel(writer, sheet_name='pembayaran', index=False)

'/mnt/data/entri_database_rumah_sakit.xlsx'

