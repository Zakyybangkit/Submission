# Submission

==========================================
Deskripsi
==========================================

Repository ini berisi file file yang dibutuhkan dalam submission tugas Belajar Analisis Data dengan Python. Data dalam repository ini menggunakan data Bike Sharing Dataset untuk melakukan pengambilan kesimpulan terhadap pertanyaan pertanyaan bisnis untuk data dan pembuatan dashboardnya.

=========================================
Files
=========================================

	- Dashboard
	  - Dashboard.py (File yang berisi sintax python penyusun dashboard)
          - Main_Data.CSV (Data yang digunakan untuk dashboard)
	- Data
          - day.csv (Peminjaman sepeda berdasarkan hari)
	  - hour.csv (Peminjaman sepeda berdasarkan jam)
          - Readme.txt (Penjelasan mengenai kedua file data di atas)
	- Notebook.inpy (sintax visualisasi dan explanatory Data pada google collab)
        - Requirements.txt (Berisi hal hal yang diperlukan dalam sintax pembuatan dashboard dan analisis data)
	- url.txt (berisi link url dashboard)

	
=========================================
Dataset characteristics (day.csv)
=========================================	
Both hour.csv and day.csv have the following fields, except hr which is not available in day.csv
	
	- instant: record index
	- dteday : date
	- season : season (1:springer, 2:summer, 3:fall, 4:winter)
	- yr : year (0: 2011, 1:2012)
	- mnth : month ( 1 to 12)
	- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
	- weekday : day of the week
	- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
	+ weathersit : 
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
	- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
	- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
	- hum: Normalized humidity. The values are divided to 100 (max)
	- windspeed: Normalized wind speed. The values are divided to 67 (max)
	- casual: count of casual users
	- registered: count of registered users
	- cnt: count of total rental bikes including both casual and registered
	

=========================================
Dashboard
=========================================
![image](https://github.com/Zakyybangkit/Submission/assets/162093636/f15c775f-6c6c-4d75-b9be-3aefaa07678b)


