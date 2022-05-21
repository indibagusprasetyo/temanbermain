//String


let sapa = "Good Morning";
console.log(typeof(sapa));

//bebas mau " " atau ' ', terkecuali quotes didalam quotes
const tanya = "'How are you?' Dina Asked";
console.log(tanya);

//contoh error :
//buka comment dibawah ini
// const jawab = '"I think it's awesome!" I answered confidently'

//solusinya :
const jawab = '"I think it\'s awesome" I answered confiently';
console.log(jawab);

//operator plus (+) pada string concatenation menggunakan sapa dari line ke 4
let sapaLagi = sapa + sapa;
console.log(sapaLagi);

//String interpolation ``
const namaSaya = "Adolf Hitler";
console.log(`Hello, My name is ${namaSaya}.`);