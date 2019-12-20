var map;
var marker;
var infoWindow;

function initMap(){
  var target = document.getElementById('target');

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

        document.getElementById('search').addEventListener('click', function() {

          var place = document.getElementById('keyword').value;
          var geocoder = new google.maps.Geocoder();

          geocoder.geocode({
            address: place
          }, function(results, status){
            if (status == google.maps.GeocoderStatus.OK){

              var bounds = new google.maps.LatLngBounds();

              for(var i in results){
                if(results[0].geometry){
                  var latlng = results[0].geometry.location;
                  var address = results[0].formatted_address;
                  bounds.extend(latlng);
                  setMarker(latlng);
                  setInfoW(place, address);
                  markerEvent();
                }
              }
            } else if (status == google.maps.GeocoderStatus.Zero_RESULTS){
              alert('見つかりませんでした');
            } else {
              console.log(status);
              alert('エラーが発生しました。')
            }
          });

        });

        // マーカーのセットを実施する
      function setMarker(setplace) {
        // 既にあるマーカーを削除
        deleteMakers();

        var iconUrl = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png';
          marker = new google.maps.Marker({
            position: setplace,
            map: map,
            icon: iconUrl
          });
        }

        //マーカーを削除する
        function deleteMakers() {
          if(marker != null){
            marker.setMap(null);
          }
          marker = null;
        }

        // マーカーへの吹き出しの追加
        function setInfoW(place, latlng, address) {
          infoWindow = new google.maps.InfoWindow({
          content: "<a href='http://www.google.com/search?q=" + place + "' target='_blank'>" + place + "</a><br><br>" + latlng + "<br><br>" + address + "<br><br><a href='http://www.google.com/search?q=" + place + "&tbm=isch' target='_blank'>画像検索 by google</a>"
        });
      }

      // クリックイベント
      function markerEvent() {
        marker.addListener('click', function() {
          infoWindow.open(map, marker);
        });
      }
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
  }
}
