var map = L.map('map', {
	scrollWheelZoom: true,
	zoomControl: true,
	fullscreenControl: true,
	fullscreenControlOptions: {
		position: 'bottomleft'}
}).setView([-9, -75], 5);

var esri_WorldTopo = L.tileLayer('http://server.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; <a href="http://server.arcgisonline.com/arcgis/rest/services/USA_Topo_Maps/MapServer"</a> ESRI - Topo'
}).addTo(map);

var esri_WorldImagery = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; <a href="http://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer"</a> ESRI - Imagery'
});

var esri_WorldTerrain = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; <a href="http://server.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer"</a> ESRI - Terrain'
});

var baseLayers = {
	"ESRI World Topo": esri_WorldTopo,
	"ESRI World Imagery": esri_WorldImagery,
	"ESRI World Terrain": esri_WorldTerrain
};

function style(feature) {
    return {
        color: '#5EA4D4',
        opacity: 0.75,
        weight: 2,
        fillColor: '#5EA4D4',
        fillOpacity: 0.25,
        radius: 2
    };
};

L.control.layers(baseLayers).addTo(map);

function rendererPoints(){
    jsonLayer.clearLayers();
    jsonLayer = new L.GeoJSON(rows, {style: style,
    onEachFeature: function (feature, layer) {
		layer.bindPopup(feature.properties.ALTITUD);
	}});
    map.addLayer(jsonLayer);
    console.log("plus1");	
};

jsonLayer = new L.GeoJSON(rows, {style: style,
	onEachFeature: function (feature, layer) {
		layer.bindPopup(feature.properties.QDR_CODIGO);
	}});
map.addLayer(jsonLayer);

map.fitBounds(jsonLayer.getBounds());
// map.setZoom(6)