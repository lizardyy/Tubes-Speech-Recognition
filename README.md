## Cara Menjalankan Aplikasi
1. Gunakan WSL untuk pengalaman yang lebih baik
2. masuk ke direktori tutorial
```
cd tutorial
```

### Preparation Dataset
Waktu pre prosess tidak masalah menggunakan Windows
1. buat folder dataset 
2. di dalam folder dataset buat folder, **Audio** yang berisi data audio **Female_1** (ubah nama folder ke Gender_No)
3. Buat folder **wav** yang berisi hal yang sama dengan sebelumnya (folder ini untuk output hasil pre-proses audio)
4. Buat folder **Label** yang berisi data label dengan folder **Female_1** (ubah nama folder ke Gender_No)
5. jalankan **script.ipynb** maka akan terdapat audio baru di wav dengan format sebagai berikut wav/Female_1/Female_1_1.wav. 

### Training
Pada tahap ini disarankan menggunakan WSL
dapat mengikuti langkah pada link berikut jika memang kurang lengkap [Tutorial Pocketsphinx](https://cmusphinx.github.io/wiki/tutorialam/), disarankan membuka juga website tutorial agar lebih jelas
Requirement
- git
- cmake (version 3.14 or higher)
- perl
- python3
- python3-numpy (only if using LDA or MLLR)
- python3-scipy (only if using MLLT)
tinggal sudo-apt get jika di wsl
1. clone github pocketsphinx dan sphinxtrain

```
cd tutorial
git clone --depth 1 https://github.com/cmusphinx/an4.git
git clone --depth 1 https://github.com/cmusphinx/sphinxtrain.git
git clone --depth 1 https://github.com/cmusphinx/pocketsphinx.git
```
2. NOTE: ada yang perlu diganti karena dataset kita merupakan audio yang panjang (spekulasi: maybe saya salah) pada file berikut
```
Tubes-Speech-Recognition\tutorial\pocketsphinx\src\fe\fe_interface.c dan
Tubes-Speech-Recognition\tutorial\sphinxtrain\src\libs\libsphinxbase\fe\fe_interface.c


fe->fft_size = (int16)ps_config_int(config, "nfft"); 

Menjadi

fe->fft_size = (int16)2048;
```
kabari saya jika masih error, jika belum bisa nanti akan terdapat error di etc/logdir/000.comp_feat dengan error
```
sample nfft tidak mencukupi gitulah kurang lebih
```

3. jalankan perintah cmake

```
cmake -S sphinxtrain -B sphinxtrain/build
cmake --build sphinxtrain/build
cmake -S pocketsphinx -B pocketsphinx/build
cmake --build pocketsphinx/build
cp pocketsphinx/build/pocketsphinx_batch sphinxtrain/build
```

3. disarankan menggunakan config yang sudah ada, tinggal mengedit sesuai yang diperlukan pada file **etc/sphinx_train.cfg**, run di folder tutorial
```
python ../sphinxtrain/scripts/sphinxtrain -t dataset setup
```
hal pertama yang perlu diubah ketika setup mulai dari awal yaitu
```
$CFG_WAVFILE_SRATE = Sesuaikan dengan audio dataset (44100)
$DEC_CFG_LANGUAGEMODEL  = "$CFG_BASE_DIR/etc/${CFG_DB_NAME}.lm.bin";
$CFG_LANGUAGEMODEL  = "$CFG_LIST_DIR/$CFG_DB_NAME.lm.bin";
```

4. untuk melakukan run, 
```
python ../sphinxtrain/scripts/sphinxtrain run
```

### Predict

Requirement
- pocketsphinx di python
Jika berhasil running akan terdapat model yang berhasil dibangun pada folder dataset/etc/model_parameter
- jalankan main.py untuk live speech
- jalankan main.ipynb jika ingin mengetest salah satu audio
- ubah model, lm, dan dict sesuai dengan yang terdapat pada folder etc / model yang sudah dibangun
