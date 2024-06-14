export function getMapParameters(prop) {
    fetch(`/api/v1/map/${prop}/`)
        .then(res => res.json())
        .then(res => setMapParameters(res))
        .catch(res => alert('Ошибка!'))
}

function setMapParameters(response) {
  var myMap = new ymaps.Map("map", {
    center: [42.871834, 74.654897],
    zoom: 13
});
}
