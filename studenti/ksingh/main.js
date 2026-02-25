const prompt = require("prompt-sync")();
var voti = [];
var voto;
var somma = 0;

do {
  voto = prompt("Inserisci il tuo voto (0 per terminare): ");
  voto = Number(voto);

  if (voto !== 0) {
    //buta il voto inseriito dentro il variabile voto
    voti.push(voto);
    //stampa il voto inserito
    console.log("Hai inserito: " + voto);
  }
} while (
  //vede se percaso il voto inserito è diverso di zero, se lo è continua ma se è uguale a zero il ciclo finisce
  voto !== 0
);

// conta quante volte il ciclo si e andato, cioe quanti numeri sono stati inseriti prima d 0
for (var i = 0; i < voti.length; i++) {
  somma = somma + voti[i];
}

var count = 0;

for (var i = 0; i < voti.length; i++) {
  if (voti[i] === max) {
    count++;
  }
}

var max = Math.max(...voti);

console.log(
  "Hai inserito questi voti: " +
    voti.join(", ") +
    ". La media dei voti inseriti è: " +
    somma / voti.length +
    " il voto piu alto è :" +
    max
);
