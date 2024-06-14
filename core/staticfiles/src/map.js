import { getMapParameters } from './js/map/map-init';

const prop = document.getElementById('map').getAttribute('data-map-type');

getMapParameters(prop);
