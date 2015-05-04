// This script is really ugly, but I don't have time right now to
// improve it and I just wanted it to work with OSM and avoid Google
// Maps :)

$(document).ready(function() {
    // create the tile layer with correct attribution
    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    // osmLayer = new L.TileLayer(osmUrl, {minZoom: 4, maxZoom: 14, attribution: osmAttrib});

    var gpxData = [
	// http://osrm.at/acG
	{url: '/assets/data/0-etapa.gpx', name: 'zero', colorLine: 'green'},
	// http://osrm.at/acH
	{url: '/assets/data/primera-etapa.gpx', name: 'first', colorLine: 'blue'},
	// http://osrm.at/acF
	{url: '/assets/data/segunda-etapa.gpx', name: 'second', colorLine: 'yellow'}
    ];

    maps = [];

    $.each(gpxData, function(i, gpx) {
	map = L.map(
	    'map-' + gpx.name,
            {fullscreenControl: true}
	);
	osmLayer = new L.TileLayer(osmUrl, {minZoom: 4, maxZoom: 14, attribution: osmAttrib});
	map.addLayer(osmLayer);
	maps.push(map);

	layer = new L.GPX(gpx.url, {
	    async: false,
	    marker_options: {
		startIconUrl: '/assets/img/no-icon.png',
		endIconUrl: '/assets/img/no-icon.png',
		shadowUrl: '/assets/img/no-icon.png'
	    },
	    polyline_options: {
		color: gpx.colorLine,
	    }
	});
	
	layer.addTo(map);
	map.addLayer(layer);
	map.fitBounds(layer.getBounds());
    })
});
