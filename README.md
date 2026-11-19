# **Cara Menggunakan Enviroment Python**

### 1. Buat Folder/Direktori Projek dan didalam Direktori Folder tersebut

```bash
touch main.py .gitignore README.md requirements.txt
```

Atau buat manual di file manager bawaan juga bisa.

### 2. Buat Enviroment dan mengaktifkannya

Untuk membuatnya

```bash
python3 -m venv .venv
```

Untuk mengaktifkan

```bash
source .venv/bin/activate
```

Untuk mematikan enviroment
```bash
deactivate
```

### 3. Menginstall Libary yang diperlukan

Untuk install libary

```bash
python -m pip install [NAMA_LIBARY]
```

Untuk melihat libary yang terinstall

```bash
python -m pip list
```

### 4. Menyimpan daftar Libary yang terinstall dan memakainya

```bash
python -m pip freeze > requirements.txt
```

Nanti untuk user lain dapat menginstall dengan libary tersebut dengan perintah sebagai berikut

```bash
python -m pip install -r requirements.txt
```

### 5. Menjalankan/Kompilasi suatu file kode


```bash
python main.py
```