var choice1;
var choice2;
var circle_list = document.getElementsByClassName("type_Circles");

function allDelete(){
  for (var i = 0; i < circle_list.length; i++){
    circle_list[i].classList.add("animated");
    circle_list[i].classList.add("fadeOut");
  }
}

document.getElementById("bC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "休憩";

  allDelete();
}

document.getElementById("dsC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "デートスポット";

  allDelete();
}

document.getElementById("hC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "娯楽";

  allDelete();
}

document.getElementById("pC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "パワースポット";

  allDelete();
}

document.getElementById("shC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "ショッピング";

  allDelete();
}

document.getElementById("tC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "トイレ";

  allDelete();
}

document.getElementById("gC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "グルメ";

  allDelete();
}

document.getElementById("spC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "レジャー・スポーツ";

  allDelete();
}
