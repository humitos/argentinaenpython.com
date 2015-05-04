var map;
var osmLayer;
var layerControl;

function add_gpx_layers() {
    var gpxData = [
	// http://osrm.at/acG
	{url: '/assets/data/0-etapa.gpx', name: 'Etapa 0', colorLine: 'violet'},
	// http://osrm.at/acH
	{url: '/assets/data/primera-etapa.gpx', name: 'Primera Etapa', colorLine: 'blue'},
	// http://osrm.at/acF
	{url: '/assets/data/segunda-etapa.gpx', name: 'Segunda Etapa', colorLine: 'yellow'}
    ];

    $.each(gpxData, function(i, gpx) {
	layer = new L.GPX(gpx.url, {
	    async: false,
	    marker_options: {
		startIconUrl: '/assets/img/no-icon.png',
		endIconUrl: '/assets/img/no-icon.png',
		shadowUrl: '/assets/img/no-icon.png'
	    },
	    polyline_options: {
		color: gpx.colorLine
	    }
	});
	name = "<img src='/assets/img/" + gpx.colorLine + "-line.png' /> <span>" + gpx.name + "</span>"
	layerControl.addOverlay(layer, name);
    });
}


function route_destiny() {
    var waypoints = [];

    $.getJSON('/assets/data/cities.json', function(data) {
	$.each(data.next, function(i, city) {
	    waypoints.push({latLng: L.latLng(city.lat, city.lng)});
	});

	var router = L.Routing.osrm();
	router.route(waypoints, function(err, routes) {
	    if (err) {
		console.error(err);
	    } else {
		l = L.Routing.line(routes[0], {
		    styles: [
			{color: 'gray', opacity: 0.3, weight: 3},
			{color: 'gray', opacity: 0.3, weight: 3},
			{color: 'gray', opacity: 0.3, weight: 3}
		    ],
		    addWaypoints: false
		}).addTo(map);
	    }
	});

	$.getJSON('/assets/data/my-position.json', function(data) {
	    var router = L.Routing.osrm();
	    waypoints = [{latLng: L.latLng(data[0], data[1])}, waypoints[0]];
	    router.route(waypoints, function(err, routes) {
		if (err) {
		    console.error(err);
		} else {
		    l = L.Routing.line(routes[0], {
			styles: [
			    {color: 'green', opacity: 0.3, weight: 4},
			    {color: 'green', opacity: 0.3, weight: 4},
			    {color: 'green', opacity: 0.3, weight: 4}
			],
			addWaypoints: false
		    }).addTo(map);
		}
	    });
	});
    });
}

$(document).ready(function (){
    // check if the map id exists before executing the code
    if ($('#map').length) {

        map = L.map(
            'map',
            {fullscreenControl: true}
        );

        // create the tile layer with correct attribution
        var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
        var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
        osmLayer = new L.TileLayer(osmUrl, {minZoom: 4, maxZoom: 14, attribution: osmAttrib});
        map.addLayer(osmLayer);
	map.on('overlayadd', function(e) {
	    map.fitBounds(e.layer);
	});

	layerControl = L.control.layers(null, null, {collapsed: false});
	layerControl.addTo(map);

	add_gpx_layers();

        $.getJSON('/assets/data/cities.json', function(data) {
            var layers = {};
            var redIcon = new L.Icon({
                iconUrl: '/assets/img/marker-icon-red.png',
                shadowUrl: '/assets/img/marker-icon-shadow.png',
                iconSize:     [25, 41], // size of the icon
                shadowSize:   [41, 41], // size of the shadow
                iconAnchor:   [12, 41],  // point of the icon which will correspond to marker's location
                shadowAnchor: [12, 41], // the same for the shadow
                popupAnchor:  [0, -50]    // point from which the popup should open relative to the iconAnchor
            });

	    var greenIcon = new L.Icon({
		iconUrl: '/assets/img/marker-icon-green.png',
		shadowUrl: '/assets/img/marker-icon-shadow.png',
		iconSize:     [25, 41], // size of the icon
		shadowSize:   [41, 41], // size of the shadow
		iconAnchor:   [12, 41],  // point of the icon which will correspond to marker's location
		shadowAnchor: [12, 41], // the same for the shadow
		popupAnchor:  [0, -50]    // point from which the popup should open relative to the iconAnchor
	    });

	    $.each(['previous', 'next'], function(i, when) {
		var markers = [];
		$.each(data[when], function(i, city) {
		    var point = [city.lat, city.lng];
		    if (when == 'next') icon = redIcon
		    else icon = greenIcon
		    var city_name = city.address.split(', ')[0];
		    markers.push(L.marker(point, {icon: icon}).bindPopup(city_name + ', ' + city.state));
		});
		layers[when] = L.featureGroup(markers);
	    });

	    // var baseMaps = {
	    // 	'Map': osmLayer
	    // };

	    name = "<img src='/assets/img/marker-icon-red.png' /> <span>Próximos Destinos</span>";
	    layerControl.addOverlay(layers['next'], name);
	    name = "<img src='/assets/img/marker-icon-green.png' /> <span>Ciudades Visitadas</span>";
	    layerControl.addOverlay(layers['previous'], name);
	});

	$.getJSON("/assets/data/my-position.json", function(point){
	    var icon = L.icon({
		iconUrl: '/assets/img/marker-car.png',
		shadowUrl: '/assets/img/marker-car-shadow.png',

		iconSize:     [64, 36], // size of the icon
		shadowSize:   [82, 49], // size of the shadow
		iconAnchor:   [32, 0],   // point of the icon which will correspond to marker's location
		shadowAnchor: [28, 10],   // the same for the shadow
		popupAnchor:  [0, -10] // point from which the popup should open relative to the iconAnchor
	    });

	    // center the map in my position
	    map.setView(point, 11);

	    var marker = L.marker(point, {icon: icon}).addTo(map);
	    marker.bindPopup("<b><em>humitos</em></b> está <em>por</em> aquí!").openPopup();
	});

	route_destiny();
    }
});
