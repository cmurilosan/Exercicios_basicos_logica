let xAtor = 100;
let yAtor = 368;
let meusPontos = 0;

let xAtor2 = 400;
let yAtor2 = 368;
let pontosAtor2 = 0;

let colisao = false;
let raio = 15;

//image(variavel imagem, xPosiçao, yPosiçao, largura, altura )

function mostraAtor(){
   image(imagemAtor, xAtor, yAtor, 30, 30);
   image(imagemAtor2, xAtor2, yAtor2, 30, 30);  
}

function movimentaAtor2(){
  if(keyIsDown(UP_ARROW)){
     yAtor2 -= 3;
  }
  if(keyIsDown(DOWN_ARROW)){
    if(yAtor2 < 368){
      yAtor2 += 3;
    }
  }
  if(keyIsDown(LEFT_ARROW)){
    if(xAtor2 > 0){
      xAtor2 -= 3;
    }
  }
  if(keyIsDown(RIGHT_ARROW)){
    if(xAtor2 < 500- 2*raio){
      xAtor2 += 3;
    }
  }
}

function movimentaAtor(){
  if(keyIsDown(87)){
     yAtor -= 3;
  }
  if(keyIsDown(83)){
    if(yAtor < 368){
      yAtor += 3;
    }
  }
  if(keyIsDown(65)){
    if(xAtor > 0){
      xAtor -= 3;
    }
  }
  if(keyIsDown(68)){
    if(xAtor < 500- 2*raio){
      xAtor += 3;
    }
  }
}

function verificaColisao1(){
  //collideRectCircle(x1, y1, width1, height1, cx, cy, diameter)
  for(i = 0; i < imagemCarros.length; i++){
  colisao = collideRectCircle(xCarros[i], yCarros[i], comprimentoCarro, alturaCarro, xAtor + raio, yAtor + raio,  raio);
    if (colisao){
      voltaAtorPosicaoInicial();
      somDaColisao.play();
      if (meusPontosMaiorQueZero()){
        meusPontos -= 1;      
      }
    }
  }
}
function voltaAtorPosicaoInicial(){
  yAtor = 368;
}

function verificaColisao2(){
  //collideRectCircle(x1, y1, width1, height1, cx, cy, diameter)
  for(i = 0; i < imagemCarros.length; i++){
  colisao = collideRectCircle(xCarros[i], yCarros[i], comprimentoCarro, alturaCarro, xAtor2 + raio, yAtor2 + raio,  raio);
    if (colisao){
      voltaAtorPosicaoInicial2();
      somDaColisao.play();
      if (pontosAtor2MaiorQueZero()){
        pontosAtor2 -= 1;      
      }
    }
  }
}
function voltaAtorPosicaoInicial2(){
  yAtor2 = 368;
}

function incluiPontos(){
  textAlign(CENTER);
  textSize(25);
  fill(color(255,240,60));
  text(meusPontos, 115, 26);
  text(pontosAtor2, 385, 26);
}

function marcaPontos(x){
    if (yAtor < 16){
    voltaAtorPosicaoInicial();
    meusPontos += 1;
    somDoPonto.play()
  } if (yAtor2 < 16){
    voltaAtorPosicaoInicial2();
    pontosAtor2 += 1;
    somDoPonto.play()
  }
}

function meusPontosMaiorQueZero(){
  return meusPontos > 0;
}

function pontosAtor2MaiorQueZero(){
  return pontosAtor2 > 0;
}
