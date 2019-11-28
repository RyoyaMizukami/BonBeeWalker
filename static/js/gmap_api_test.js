function initMap(){
  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(
      function(position){
        var mapLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);

        // 最初にどこに注目しておくか
        var map = new google.maps.Map(document.getElementById('map'),{
          center: mapLatLng,
          zoom: 18,
          streetViewControl: false,
          fullscreenControl: false,
          mapTypeControl: false
        });

        // html側で指定したID:pac-inputの要素をinputに格納
        var input = document.getElementById('pac-input')
        // autocomplete変数にgmapAPI内にあるAutocompleteメソッドにinput変数を渡したものを格納
        var autocomplete = new google.maps.places.Autocomplete(input);
        // autocomplete変数にboundsという変数が渡されたらmapを返す？ここ曖昧。
        autocomplete.bindTo('bounds', map);

        // 必要なデータフィールドのみを指定。→　いらないのは消せってことかな。
        // ここではplace_id(要る)、geometry(必要になるかも)、name(多分要る)って感じですかね
        autocomplete.setFields(['place_id', 'geometry', 'name']);

        map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

        var infowindow = new google.maps.InfoWindow();
        var infowindowContent = document.getElementById('infowindow-content');
        infowindow.setContent(infowindowContent);

        // マーカーを地図上に表示
        var marker = new google.maps.Marker({map:map});

        marker.addListener('click', function(){
          infoWindow.open(map, marker);
        });

        autocomplete.addListener('place_changed', function() {
          infowindow.close();

          var place = autocomplete.getPlace();

          if (!place.geometry){
            return;
          }

          // 多分だけど、入力された場所が画面外にだったら移動、
          // そうじゃなかったら中心に持ってくる的な
          if (place.geometry.viewport){
            map.fitBounds(place.geometry.viewport);
          } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
          }

          // 検索された地名のplaceidを使ってマーカー立てる？
          marker.setPlace({
            placeId: place.place_id,
            location: place.geometry.location
          });

          marker.setVisible(true);

          infowindowContent.children['place-name'].textContent = place.name;
          infowindowContent.children['place-id'].textContent = place.place_id;
          infowindowContent.children['place-address'].textContent = place.formatted_address;
          infowindow.open(map, marker);
        });
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
