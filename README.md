# KB_Informed-Search

![Screenshot from 2023-03-17 04-59-10](https://user-images.githubusercontent.com/92865110/225761813-a15b0b44-35f3-4bb6-89e8-db61659ba34a.png)

## Implementasi
1. Greedy Best\-First Search
2. A\* Search

## Analisis Algoritma

### Greedy-Best Search Tree
<img width="1472" alt="Informed Search - KB Kelompok Agfi (2)" src="https://user-images.githubusercontent.com/92865110/230703503-51615be6-90cb-4609-a863-8853be2920e2.png">

### A* Search Tree
<img width="3168" alt="Informed Search - KB Kelompok Agfi (4)" src="https://user-images.githubusercontent.com/92865110/230703798-c49fdf01-31d1-40da-b2ad-3aae456051f0.png">


 Baik algoritma Greedy Best-First Search (GBFS) maupun algoritma A* umumnya digunakan untuk menemukan jalur terpendek dalam sistem berbasis grafik atau grid. Namun, ada beberapa perbedaan utama antara kedua pendekatan tersebut. Perbandingan fungsinya adalah sebagai berikut
<br/>
<br/>

Greedy Best First Search :
> f(n) = g(n)



A\* Search :
> f(n) = g(n) + h(n)

<br/>

- GBFS adalah algoritma yang selalu memilih jalur yang tampaknya paling dekat dengan tujuan, berdasarkan beberapa fungsi heuristik yang memperkirakan jarak yang tersisa dari simpul saat ini ke tujuan. Itu tidak mempertimbangkan jarak total yang ditempuh untuk mencapai simpul saat ini. Hal ini dapat menghasilkan solusi yang kurang optimal jika fungsi heuristik tidak akurat, karena dapat memilih jalur yang terlihat lebih dekat ke tujuan tetapi membutuhkan jarak yang lebih jauh untuk mencapainya.

- A* adalah algoritma pencarian jarak terpendek yang mempertimbangkan estimasi jarak tersisa ke tujuan dan jarak sebenarnya yang ditempuh untuk mencapai simpul saat ini. Ia menggunakan kombinasi fungsi heuristik dan jarak total yang ditempuh sejauh ini (juga dikenal sebagai biaya/cost) untuk memilih node berikutnya yang akan dijelajahi. Ini memastikan bahwa A* selalu memilih jalur yang paling menjanjikan ke tujuan, dengan mempertimbangkan perkiraan jarak yang tersisa dan jarak sebenarnya yang ditempuh.

Dengan nilai heuristik h(x) adalah jarak garis lurus ke Surabaya yang berarti kota tujuan adalah Kota Surabaya. Kita anggap Magetan adalah kota awal.

- Dengan GBFS, kota yang terhubung dengan Magetan adalah Ngawi dengan nilai h(x) = 130, Madiun dengan nilai h(x) = 126 dan Ponorogo dengan nilai h(x) = 128. Dari ketiga kota tersebut, kota dengan nilai h(x) paling kecil adalah Madiun. Sehingga kota yang di tempuh selanjutnya adalah kota Madiun. Kemudian dilakukan pencarian kota dengan nilai h(x) paling kecil yang terhubung dengan kota Madiun. Begitu seterusnya hingga tercapai kota tujuan atau terjadi *loop.*

- Algoritma A* hampir sama dengan GBFS, namun pencarian kota selanjutnya juga melibatkan jarak ke kota selanjutnya. Menggunakan contoh kota Magetan, nilai f(n) dari Ngawi adalah 32 (jarak ke kota Magetan) ditambah dengan heuristik dari kota Magetan, yaitu 130. Sehingga nilai f(n) dari Ngawi adalah 130 + 32 = 162. Nilai f(n) dari Madiun adalah 148 dan nilai f(n) dari Ponorogo adalah 162. Dari ketiga kota tersebut diambil kota dengan nilai f(n) paling kecil, yaitu kota Madiun. Begitu seterusnya hingga tercapai kota tujuan atau terjadi *loop.*


Dalam hal efisiensi, A* bisa lebih tidak efisien secara komputasi daripada GBFS, karena memerlukan penghitungan fungsi heuristik dan biaya untuk setiap node. Namun, A* lebih cenderung menemukan solusi optimal, sementara GBFS mungkin mengembalikan solusi kurang optimal dalam beberapa kasus.

Secara keseluruhan, pilihan antara GBFS dan A* bergantung pada masalah khusus yang dipecahkan dan syarat yang dibutuhkan. Jika masalah memerlukan pencarian solusi optimal dan fungsi heuristik akurat, A* adalah pilihan yang lebih baik. Namun, jika efisiensi komputasi menjadi prioritas dan solusi perkiraan yang kurang optimal dapat diterima, GBFS mungkin lebih tepat.

Hasil Algoritma A* Search :
Magetan -> Surabaya
```
Jalur ditemukan:

Magetan->Madiun->Nganjuk->Jombang->Surabaya
Total distance traveled: 182
```

Hasil Algoritma Greedy : 
Magetan -> Surabaya

```
Jalur ditemukan:
Magetan->Madiun->Nganjuk->Jombang->Surabaya
Jarak total: 394
```
