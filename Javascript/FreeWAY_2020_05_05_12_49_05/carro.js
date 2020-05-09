let xCarros = [550, 550, 550, -50, -50, -50];
let yCarros = [40, 96, 150, 210, 270, 318];
let velocidadeCarros = [6, 4, 5.3, 4.5, 3.6, 2.9];
let comprimentoCarro = 50;
let alturaCarro = 40;

//direção
const direcao = [1, 1, 1, -1, -1, -1];
const xCarroInicial = [550, 550, 550, -50, -50, -50];


//carro 1 -->[0]
//carro 2 -->[1]
//carro 3 -->[2]

function mostraCarro(){
  for (let i = 0; i < imagemCarros.length; i++){
    image(imagemCarros[i], xCarros[i], yCarros[i], comprimentoCarro, alturaCarro);
  }
}

function movimentaCarro(x){
  for(let i = 0; i < xCarros.length; i++){
    xCarros[i] -= velocidadeCarros[i] * direcao[i];
  } 
}

function voltaPosicaoInicialCarro(){
  for(let i = 0; i < xCarros.length; i++){
    if(passouTodaATela(xCarros[i])){
    xCarros[i] = xCarroInicial[i];
    }
  }
} 

function passouTodaATela (xCarro){
  return xCarro > 550 || xCarro < (-1) * comprimentoCarro;
}

