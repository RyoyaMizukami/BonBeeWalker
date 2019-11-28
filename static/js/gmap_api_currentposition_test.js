function initMap(){
  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(
      function(position){
        var mapLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        var map = new google.maps.Map(document.getElementById('map'),{
          center: mapLatLng,
          zoom: 18
        });

        var marker = new google.maps.Marker({map: map});
      },
      function(error){
        switch (error.code) {
          case 1:
            alert("位置情報の利用が許可されていません。");
            break;
          case 2:
            alert("現在地が取得できませんでした。");
            break;
          case 3:
            alert("タイムアウトになりました。");
            break;
          default:
            alert("その他のエラー(エラーコード:" + error.code + ")");
            break;
        }
      }
    );
  } else {
    alert("この端末では位置情報が取得できません。");
  }
}
