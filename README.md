# KB_Informed-Search

![Screenshot from 2023-03-17 04-59-10](https://user-images.githubusercontent.com/92865110/225761813-a15b0b44-35f3-4bb6-89e8-db61659ba34a.png)

## Implementasi
1. Greedy Best\-First Search
2. A\* Search

## Analisis Algoritma
<img width="3072" alt="Informed Search - KB Kelompok Agfi" src="https://user-images.githubusercontent.com/92865110/225768657-8e56bfe2-5d6f-4d52-a00a-8e1f6ecc5c47.png">
 Baik algoritma Greedy Best-First Search (GBFS) maupun algoritma A* umumnya digunakan untuk menemukan jalur terpendek dalam sistem berbasis grafik atau grid. Namun, ada beberapa perbedaan utama antara kedua pendekatan tersebut. Perbandingan fungsinya adalah sebagai berikut

Greedy Best First Search :
> f(n) = g(n)

A\* Search :
> f(n) = g(n) + h(n)

- GBFS adalah algoritma yang selalu memilih jalur yang tampaknya paling dekat dengan tujuan, berdasarkan beberapa fungsi heuristik yang memperkirakan jarak yang tersisa dari simpul saat ini ke tujuan. Itu tidak mempertimbangkan jarak total yang ditempuh untuk mencapai simpul saat ini. Hal ini dapat menghasilkan solusi yang kurang optimal jika fungsi heuristik tidak akurat, karena dapat memilih jalur yang terlihat lebih dekat ke tujuan tetapi membutuhkan jarak yang lebih jauh untuk mencapainya.

- A* adalah algoritma pencarian jarak terpendek yang mempertimbangkan estimasi jarak tersisa ke tujuan dan jarak sebenarnya yang ditempuh untuk mencapai simpul saat ini. Ia menggunakan kombinasi fungsi heuristik dan jarak total yang ditempuh sejauh ini (juga dikenal sebagai biaya/cost) untuk memilih node berikutnya yang akan dijelajahi. Ini memastikan bahwa A* selalu memilih jalur yang paling menjanjikan ke tujuan, dengan mempertimbangkan perkiraan jarak yang tersisa dan jarak sebenarnya yang ditempuh.

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
