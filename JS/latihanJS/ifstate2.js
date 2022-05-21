// if else statement
//pengecekan banyak

//ubah variabel let pada line 5 untuk cek statementnya
let bahasa = "Arab";
let sapa = "Wilujeng";

if(bahasa === "Indonesia") {
    sapa = "Selamat Pagi";
} else if (bahasa === "Spanyol") {
    sapa = "Hola";
} else if (bahasa === "Arab") {
    sapa = "Shabahul Khair";
} else if(bahasa === "Sunda") {
    sapa = "Wilujeng";
} else {
    sapa = "Bahasa tidak dimengerti";
}

console.log(sapa)