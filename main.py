import requests

# Inisiasi link url
url = 'https://brone.ub.ac.id'

# kirim permintaan, simpan jawabannya di variabel hasil
hasil = requests.get(url)

# cetak angka status dari jawaban itu
print(hasil.status_code)