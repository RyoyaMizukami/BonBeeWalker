document.getElementById("bC").onclick = function(){
  var list = this.classList;
  console.log(list);

  list.add("animated");
  list.add("fadeOut");
  console.log(list);
}
