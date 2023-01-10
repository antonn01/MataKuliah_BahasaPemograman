# Inheritance memungkinkan kita untuk mewarisi atribut dan metode dari suatu kelas dasar (base)atau induk(parent). Hal ini sangat berguna karena kita membuat sub-kelas yang dapat menggunakan semua fungsi dari parent class. Selain itu, kita dapat menimpa atau menambahkan fungsi yang baru tanpa mempengaruhi parent class. Untuk memahami konsep inheritance dengan mudah, kita dapat menganalogikan sifat seorang anak mewarisi sifat orang tuanya. Sama hal nya pada Python yang memiliki dua kelas, yaitu:
# 1.	Parent class (super atau base class)
# 2.	Child class (subclass atau derived class)
# Class yang mewarisi sifat disebut sebagai Child class, sedangkan class yang diwarisi sifat nya adalah Parent class, Inheritance memiliki kemampuan untuk membuat Sub-classes yang berisi spesialisasi dari Parent class. Selanjutnya, inheritance dapat di bagi lagi menjadi empat tipe. Yaitu single, multilevel, hierarchical, dan multiple inheritance. 
# •	Single Inheritance

# Pada inheritance, child class dapat mengakses seluruh metode yang telah didefinisikan pada parent   class. Selain itu, child class dapat meliputi metode spesifik yang dimilikinya.
# Dalam bahasa pemrograman berorientasi objek pada Python, class turunan dapat mewarisi class utama dengan cara memanggil kembali kelas utama di dalam tanda kurung.

# •	Multilevel inheritance
#   Multilevel inheritance adalah kondisi dimana ketika suatu class mewariskan class yang lainnya. Tidak ada batasan hingga berapa banyak jumlah level yang dapat digunakan pada multilevel inheritance pada Python. 

# •	Hierarchical Inheritance
#   Hierarchical inheritance memungkinkan kita menurunkan lebih dari satu child class untuk mewarisi sifat dari parent class.

# •	Multiple inheritance
#   Multiple inheritance memungkinkan satu kelas turunan untuk mewarisi lebih dari satu kelas utama.

# Encapsulation adalah salah satu konsep fundamental pada pemrograman berorientasi objek. Encapsulation menggambarkan suatu ide untuk membungkus data dan metode yang bekerja pada suatu data di dalam satu unit. Hal ini memberikan batasan dalam mengakses suatu variabel dan metode secara langsung. Sehingga, dapat mencegah modifikasi data yang tidak disengaja. Hal tersebut sangatlah penting, karena dapat mencegah perubahan yang tidak disengaja. Bukan tidak dapat di ubah, namun, variabel objek tersebut hanya dapat di ubah dengan metode objek.
# Python tidak memiliki kata kunci private seperti pada bahasa pemrograman yang lain. Sebagai gantinya, hal ini dapat dilakukan oleh encapsulation. Variable class yang tidak boleh di akses secara langsung diawali oleh dua tanda garis bawah 

# •	Single underscore: variable private, tidak seharusnya di akses secara langsung. Namun, tidak    menghentikan Python untuk mengeksekusi perintah (kecuali konvensi).
# •	Double underscore: Private variable, sulit untuk di akses, namun masih memungkinkan.
# •	Keduanya masih dapat di akses. Python memiliki variable private secara konvensi.

# Polymorphism adalah kemampuan untuk mengambil bentuk yang berbeda. Polymorphism dalam Python memungkinkan kita untuk mendefinisikan metode pada child class dengan menggunakan nama yang sama seperti pada parent class.
# Polymorphism di bangun berdasarkan dua suku kata, yaitu Poly (banyak) dan Morphism (bentuk). Artinya adalah fungsi yang sama dapat digunakan pada tipe yang berbeda. Sehingga membuat membuat programming lebih intuitif dan mudah. Dalam bahasa pemrograman berorientasi objek pada Python, kita memiliki cara-cara yang berbeda untuk mendefinisikan polymorphism.
# Class child mewarisi seluruh method dari parent class. Namun, ada beberapa kasus di mana metode tersebut tidak cocok dengan child class. Oleh karena itu, kita harus mengimplementasikan kembali metode yang pada child class yang dinamakan Method Overriding. 

# Ada beberapa metode untuk menggunakan polymorphism pada pemrograman berorientasi objek Python. Kita dapat menggunakan fungsi berbeda, metode class atau objek untuk mendefinisikannya.

# •	Polymorphism dengan function
#   Kita dapat membuat fungsi yang dapat mengambil objek apapun untuk mengimplememtasikan polymorphism.

# •	Polymorphism dengan class
#   Kita dapat menggunakan konsep polymorphism ketika membuat metode class. Python memungkinkan class yang berbeda untuk menggunakan metode dengan nama yang sama. Kemudian kita dapat memanggil metode tersebut dengan mengabaikan objek yang sedang kita gunakan. 

# •	Polymorphism dengan Inheritance
# Polymorphism pada pemrograman berorientasi objek Python mendefinisikan child class yang memiliki kesamaan nama metode pada parent class. Pada inheritance, child class mewarisi metode dari parent class. Selain itu, memungkinkan untuk memodifikasi metode di dalam child class yang telah diwarisi dari parent class. 
