var choice1;
var choice2;
var circle_list = document.getElementsByClassName("type_Circles");
var money_list = document.getElementsByClassName("money_Circles");


function allDelete(){
  for (var i = 0; i < circle_list.length; i++){
    circle_list[i].classList.add("animated");
    circle_list[i].classList.add("fadeOut");
    circle_list[i].style.cssText = "display: none;"
  }
}

function fadeinMoney(){
  for (var i = 0; i < money_list.length; i++){
    money_list[i].classList.add("animated")
    money_list[i].classList.add("fadeIn");
    money_list[i].style.display = "block";
  }
}

function execPost(type, money){
  form.setAttribute("action", "/post");
  form.setAttribute("method", "post");
  form.style.display = "none";
  document.body.appendChild(form);

  if (data !== undefined){
    var input = document.createElement('input');
    input.setAttribute('type', type);
    input.setAttribute('budget', money);
    }

   form.submit();
}

document.getElementById("bC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "休憩";

  allDelete();
  fadein_money();
}

document.getElementById("dsC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "デートスポット";

  allDelete();
  fadein_money();
}

document.getElementById("hC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "娯楽";

  allDelete();
  fadein_money();
}

document.getElementById("pC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "パワースポット";

  allDelete();
  fadein_money();
}

document.getElementById("shC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "ショッピング";

  allDelete();
  fadein_money();
}

document.getElementById("tC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "トイレ";

  allDelete();
  fadein_money();
}

document.getElementById("gC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "グルメ";

  allDelete();
  fadein_money();
}

document.getElementById("spC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "レジャー・スポーツ";

  allDelete();
  fadein_money();
}

document.getElementById("0300C").onclick = function(){
  list.add("animated");
  list.add("fadeOut");
  choice2 = 300;
  execPost(choice1, choice2);
}

document.getElementById("300700C").onclick = function(){
  list.add("animated");
  list.add("fadeOut");
  choice2 = 700;
  execPost(choice1, choice2);
}

document.getElementById("7001000C").onclick = function(){
  list.add("animated");
  list.add("fadeOut");
  choice2 = 1000;
  execPost(choice1, choice2);
}
