<h1> Tugas Praktikum 3 </h1>
  <h3> Latihan 1 </h3>
    <p> Menampilkan n bilangan acak yang lebih kecil dari 0.5. </br>
    User menginput bilangan N yang mana akan membuat sebuah perulangan dan di setiap perulangan itu menghasilkan nilai random. </br>
    Algoritmanya adalah : </br>
    1. Kita gunakan library python bernama <em>random</em> agar dapat menghasilkan nilai random </br>
    2. Masukkan kode <b>num = int(input("Masukkan nilai N : "))</b> untuk membuat sebuah variabel
    3. Lalu masukan fungsi loop : </br>
    
      > for i in range(num):
      x = random.uniform(0, 0.5)
      print("data ke : {0} => {1}".format(i+1, x))
      print("Selesai") </br>
    
   <b>for i</b> digunakan untuk membuat sebuah perulangan dimana jumlah perulangan itu ditentukan dari <b>range(num):</b></br>
   lalu untuk menghasilkan nilai random pada setiap perulangan terdapat pada kode <b>x = random.uniform(0, 0.5)</b> (penggunaan "random.uniform" untuk menentukan nilai random yang panjang rentang nilainya telah ditentukan, cara penggunaannya adalah : "random.uniform(rentang nilai pertama, rentang nilai terakhir))</br>
   <b>print("data ke: {0} => {1}".format(i+1, x))</b> digunakan untuk menampilkan hasil perulangan beserta nilai randomnya. </br>
   <b>print("Selesai")</b> berfungsi menampilkan kata "Selesai" jika sudah melewati perulangan yang telah ditentukan.</br>
