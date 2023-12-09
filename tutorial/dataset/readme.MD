salin dataset folder Audio dan Lable ke folder ini 

jalankan semua script yang ada pada script.ipynb

maka akan muncul folder baru wav yang merupakan hasil pre processing audio

NOTED: jika terdapat error pada  train ubah nfft size ke 2048
search pada pocketspinx

fe->fft_size = (int16)ps_config_int(config, "nfft"); ganti ke (int16)2048

work, tapi gatau apakah ada cara yang lebih baik