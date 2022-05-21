// logical operator
let a = 10;
let b = 12;

// AND OPERATOR
console.log(a < 15 && b > 10); // (true && true) --> true *(lihat kembali tabel kebenaran)
console.log(a > 15 && b > 10); // (false && true) --> false

// OR OPERATOR
console.log(a < 15 || b > 10); // (true || true) --> true *(lihat kembali tabel kebenaran)
console.log(a > 15 || b > 10); // (false || true) --> true

// NOT OPERATOR
console.log(!(a < 15)); // !(true) --> false
console.log(!(a < 15 && b > 10)); // !(true && true) --> !(true) --> false
console.log(!(a > 15 && b > 10)); // !(false && true) --> !(false) --> true