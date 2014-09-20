function httpGet(theUrl){
	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", theUrl, false );
	xmlHttp.send( null );
};

function updateSlider() {
	var slider1 = document.getElementById("slider1");
	var slider2 = document.getElementById("slider2");
	var slider3 = document.getElementById("slider3");

	r = slider1.value;
	g = slider2.value;
	b = slider3.value;

	//httpGet("http://192.168.23.117:5000/send/red/"+r);
	//httpGet("http://192.168.23.117:5000/send/green/"+g);
	//httpGet("http://192.168.23.117:5000/send/blue/"+b);	
}