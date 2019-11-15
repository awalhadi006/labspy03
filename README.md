<h1> Tugas Praktikum 3 </h1>
  <h3> Latihan 1 </h3>
    <p> Menampilkan n bilangan acak yang lebih kecil dari 0.5. </br>
    User menginput bilangan N yang mana akan membuat sebuah perulangan dan di setiap perulangan itu menghasilkan nilai random. </br>
    Algoritmanya adalah : </br>
    1. Kita gunakan library python bernama <em>random</em> agar dapat menghasilkan nilai random </br>
    2. Masukkan kode <b>num = int(input("Masukkan nilai N : "))</b> untuk membuat sebuah variabel
    3. Lalu masukan fungsi loop : </br>
    
      for i in range(num):
          x = random.uniform(0, 0.5)
          print("data ke : {0} => {1}".format(i+1, x))
      print("Selesai")
    
   3. <b>for i</b> digunakan untuk membuat sebuah perulangan dimana jumlah perulangan itu ditentukan dari <b>range(num):</b></br>
   lalu untuk menghasilkan nilai random pada setiap perulangan terdapat pada kode <b>x = random.uniform(0, 0.5)</b> (penggunaan "random.uniform" untuk menentukan nilai random yang panjang rentang nilainya telah ditentukan, cara penggunaannya adalah : "random.uniform(rentang nilai pertama, rentang nilai terakhir)).</br>  
   4. <b>print("data ke: {0} => {1}".format(i+1, x))</b> digunakan untuk menampilkan hasil perulangan beserta nilai randomnya. </br>
   5. <b>print("Selesai")</b> berfungsi menampilkan kata "Selesai" jika sudah melewati perulangan yang telah ditentukan.</br>
   contoh hasil program : </p>
   
   ![Latihan 1](https://user-images.githubusercontent.com/24362384/68924489-8d563900-07b3-11ea-8615-768ce60a769a.PNG)

  <h3> Latihan 2 </h3>
    <p> Membuat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan, dan berhenti mengumpulkan data ketika data yang di input bernilai 0. </br>
    Algoritmanya adalah : </br>
    1. <b>num []</b> kode ini adalah sebagai variabel penampung data yang akan kita input nanti. </br>
    2. Setelah kita menentukan variabel, maka kita akan memasukkan fungsi loop seperti dibawah ini : </br>
    
    while num!=0=
        a = int(input("Masukkan bilangan : "))
        num.append(a)
        if a == 0:
            break
    print("Nilai terbesar adalah : ",max(num))
    
   3. <b>while num!=0</b> digunakan untuk menentukan perulangan. </br>
   4. <b>a = int(input("Masukkan bilangan : "))</b> digunakan untuk memasukkan data. </br>
   5. <b>num.append(a)</b> digunakan untuk memasukkan nilai a yang sebelumnya telah di input kedalam penampun nilai. </br>
   6. <b>if a == 0: </b></br>
      <b>break</b></br>
      kode ini digunakan untuk membuat sebuah pernyataan, jika nilai a = 0, maka akan menghentikan pengulangan dan akan lanjut ke kode selanjutnya. </br>
   7. <b>print("Nilai terbesar adalah : ",max(num))</b> kode ini digunakan jika user telah menginput nilai berupa 0, maka akan tampil nilai terbesar dari data yang telah di input sebelumnya. </br>
   contoh hasil program : </p></br>
   
   ![Latihan 2](https://user-images.githubusercontent.com/24362384/68925863-b2987680-07b6-11ea-91c2-79f9a8aed950.PNG)
   
   <h3> Program 1 </h3>
   <p>Masukkan variable untuk modal awal dengan value 100jt, x untuk di bulan pertama dan kedua dan z sebagai bulan keberapa pada perulangan. Lalu membuat list sampai dengan 8 menggunakan format int, pada list pertama kedua masukkan x karena di bulan pertama kedua belum mendapatkan laba, pada list ketiga keempat mendapatkan laba 1%, pada list ke lima enam tujuh mendapatkan laba 5%, pada list ke 8 mendapatkan laba 2%. Lalu dari list tersebut menggunakan for dengan list, jika sudah dari list tersebut akan di hitung semua menggunakan function sum. </br>
   contoh hasil program : </br>
   
   ![Program 1](https://user-images.githubusercontent.com/24362384/68926095-4407e880-07b7-11ea-8e20-eb0e4fd5e476.PNG)
  
  <p> Kurang lebihnya mohon maaf. Sekian dan terima kasih. </p>
