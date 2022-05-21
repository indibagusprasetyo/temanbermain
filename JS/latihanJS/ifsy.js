//if else Truhthy & Falsy
//setiap nilai pada JS mewarisi sifat boolean, nilai ini dikenal dengan truthy dan falsy
// truthy adalah nilai yang dievaluasi menghasilkan true, bergitu falsy juga bernilai false.

/* Tipe data Truthy & Falsy =

-Number 0
-BigInt On
-String Kosong " " / ` `
-null
-undenfined
-NaN, Not a Number
*/

let nama =" ";
if (nama) {
    console.log(`Halo, ${nama}`); // jika null dianggap falsy
} else {
    console.log("Nama Masih Kosong")
}