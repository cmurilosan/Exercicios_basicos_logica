let imagemEstrada;
let imagemAtor;
let imagemAtor2;
let imagemCarro;
let imagemCarro2;
let imagemCarro3;
let imagemCarro4;
let imagemCarro5;
let imagemCarro6;

let somDaTrilha;
let somDaColisao;
let somDoPonto;


function preload(){
  imagemEstrada = loadImage("/imagens/estrada.png");
  imagemAtor = loadImage("imagens/ator-1.png");
  imagemAtor2 = loadImage("imagens/ator-2.png");
  imagemAtores = [imagemAtor, imagemAtor2];
  
  imagemCarro1 = loadImage("imagens/carro-1.png");
  imagemCarro2 = loadImage("imagens/carro-2.png");
  imagemCarro3 = loadImage("imagens/carro-3.png");
  imagemCarro4 = loadImage("imagens/carro-4.png");
  imagemCarro5 = loadImage("imagens/carro-5.png");
  imagemCarro6 = loadImage("imagens/carro-6.png");
  imagemCarros = [imagemCarro1, imagemCarro2, imagemCarro3, imagemCarro4, imagemCarro5, imagemCarro6];
  
  somDaTrilha = loadSound("sons/trilha.mp3");
  somDaColisao = loadSound("sons/colidiu.mp3");
  somDoPonto = loadSound("sons/pontos.wav");
}