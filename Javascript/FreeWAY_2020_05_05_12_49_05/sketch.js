function setup() {
  createCanvas(500, 400);
  somDaTrilha.loop();
  somDaTrilha.setVolume(0.2);
}

function draw() {
  background(imagemEstrada); 
  mostraAtor();
  mostraCarro();
  movimentaCarro();
  movimentaAtor();
  movimentaAtor2();
  voltaPosicaoInicialCarro()
  verificaColisao1();
  verificaColisao2();
  incluiPontos();
  marcaPontos()
}

