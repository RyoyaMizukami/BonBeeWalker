var type = document.getElementById("type_button");
var money = document.getElementById("money_button");
var both = document.getElementById("both_button");
var button_list = document.getElementsByClassName("button");
var pulldown_type = document.getElementById("pulldown_type");
var pulldown_money = document.getElementById("pulldown_money");
var submit_button = document.getElementById("submit_button");
var return_button = document.getElementById("return_button");

function allDelete(){
  for(var i = 0; i < button_list.length; i++){
    button_list[i].classList.add("animated");
    button_list[i].classList.add("fadeOut");
    button_list[i].style.cssText = "display: none;";
  }
}

function DisplaySubmitButton(){
  submit_button.classList.add("animated");
  submit_button.classList.add("fadeIn");
  submit_button.style.display = "flex";
  submit_button.classList.remove("fadeIn");
}

function DisplayReturnButton(){
  return_button.classList.remove("fadeOut");
  return_button.classList.add("fadeIn");
  return_button.style.display = "flex";
}

function CreateOnlyType(){
  pulldown_type.classList.add("animated");
  pulldown_type.classList.add("fadeIn");
  pulldown_type.style.cssText = "display: flex;";
  pulldown_type.classList.remove("fadeIn");
  DisplaySubmitButton();
  DisplayReturnButton();
}

function CreateOnlyMoney(){
  pulldown_money.classList.add("animated");
  pulldown_money.classList.add("fadeIn");
  pulldown_money.style.cssText = "display: flex;";
  pulldown_money.classList.remove("fadeIn");
  DisplaySubmitButton();
  DisplayReturnButton();
}

function CreateBoth(){
  pulldown_type.classList.add("animated");
  pulldown_type.classList.add("fadeIn");
  pulldown_type.style.cssText = "display: flex;";
  pulldown_type.classList.remove("fadeIn");
  pulldown_money.classList.add("animated")
  pulldown_money.classList.add("fadeIn");
  pulldown_money.style.cssText = "display: flex;";
  pulldown_money.classList.remove("fadeIn");
  DisplaySubmitButton();
  DisplayReturnButton();
}

/*
function ReturnThePast(){
  pulldown_type.classList.add("fadeOut");
  pulldown_type.style.cssText = "display: none;";
  pulldown_money.classList.add("fadeOut");
  pulldown_money.style.cssText = "display: none;";
  submit_button.classList.add("fadeOut");
  submit_button.style.cssText = "display: none;";
  return_button.style.cssText = "display: none;";
  for(var i = 0; i < button_list.length; i++){
    button_list[i].classList.add("animated");
    button_list[i].classList.add("fadeIn");
    button_list[i].style.removeProperty = "display: none;";
  }
}
*/

function ReloadPage(){
  location.reload(true);
}


type.onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");

  allDelete();
  CreateOnlyType();
  console.log('comfirmed onclick!');
}

money.onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");

  allDelete();
  CreateOnlyMoney();
  console.log('comfirmed onclick!');
}

both.onclick = function(){
  var list = this.classList;

  list.add("animated");
  list.add("fadeOut");

  allDelete();
  CreateBoth();
  console.log('comfirmed onclick!');
}

return_button.onclick = function(){
  ReloadPage();
}
