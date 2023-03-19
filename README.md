# KB_Informed-Search

![Screenshot from 2023-03-17 04-59-10](https://user-images.githubusercontent.com/92865110/225761813-a15b0b44-35f3-4bb6-89e8-db61659ba34a.png)

## Implementasi
1. Greedy Best\-First Search
2. A\* Search

## Analisis Algoritma
<img width="3072" alt="Informed Search - KB Kelompok Agfi" src="https://user-images.githubusercontent.com/92865110/225768657-8e56bfe2-5d6f-4d52-a00a-8e1f6ecc5c47.png">
Pada kedua algoritma memiliki path yang sama, tetapi terdapat perbedaan pada kedua algoritma. Algoritma __Greedy Best-First Search__ hanya mempertimbangkan __Nilai heuristic__ untuk beranjak ke node selanjutnya. Sedangkan __A* Search__, Algoritma ini mempertimbangkan jarak dan nilai heuristic untuk beranjak ke node selanjutnya. Perbandingan fungsinya adalah sebagai berikut

Greedy Best First Search :
> f(n) = g(n)

A\* Search :
> f(n) = g(n) + h(n)

Hasil Algoritma A* Search :
Magetan -> Surabaya
```
Jalur ditemukan:

Magetan->Madiun->Nganjuk->Jombang->Surabaya
Total distance traveled: 182
```
