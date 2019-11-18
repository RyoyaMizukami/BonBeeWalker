var choice1="娯楽";
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

  console.log(choice1, choice2);

  document.getElementById("0300C").onclick = function(){
    var list = this.classList;

    list.add("animated");
    list.add("fadeOut");
    choice2 = 300;
    execPost(choice1, choice2);
  }

  document.getElementById("300700C").onclick = function(){
    var list = this.classList;

    list.add("animated");
    list.add("fadeOut");
    choice2 = 700;
    execPost(choice1, choice2);
  }

  document.getElementById("7001000C").onclick = function(){
    var list = this.classList;

    list.add("animated");
    list.add("fadeOut");
    choice2 = 1000;
    execPost(choice1, choice2);
  }
}

function execPost(type, money){
  var form = document.createElement('form');
  form.setAttribute("action", "/post");
  form.setAttribute("method", "post");
  form.style.display = "none";
  document.body.appendChild(form);

  var input1 = document.createElement('input');
  input1.setAttribute('type', 'hidden');
  input1.setAttribute('name', 'budget');
  input1.setAttribute('value', money);
  form.appendChild(input1);

  var input2 = document.createElement('input');
  input2.setAttribute('type', 'hidden');
  input2.setAttribute('name', 'type');
  input2.setAttribute('value', type);
  form.appendChild(input2);

   form.submit();
}

document.getElementById("bC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "休憩";

  allDelete();
  fadeinMoney();
}

document.getElementById("dsC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "デートスポット";

  allDelete();
  fadeinMoney();
}

document.getElementById("hC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "娯楽";

  allDelete();
  fadeinMoney();
}

document.getElementById("pC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "パワースポット";

  allDelete();
  fadeinMoney();
}

document.getElementById("shC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "ショッピング";

  allDelete();
  fadeinMoney();
}

document.getElementById("tC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "トイレ";

  allDelete();
  fadeinMoney();
}

document.getElementById("gC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "グルメ";

  allDelete();
  fadeinMoney();
}

document.getElementById("spC").onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");
  choice1 = "レジャー・スポーツ";

  allDelete();
  fadeinMoney();
}
