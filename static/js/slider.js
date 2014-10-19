function httpGet(theUrl){
	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", theUrl, false );
	xmlHttp.send( null );
};

function hsvToRgb(h, s, v){
    var r, g, b;

    var i = Math.floor(h * 6);
    var f = h * 6 - i;
    var p = v * (1 - s);
    var q = v * (1 - f * s);
    var t = v * (1 - (1 - f) * s);

    switch(i % 6){
	        case 0: r = v, g = t, b = p; break;
	        case 1: r = q, g = v, b = p; break;
	        case 2: r = p, g = v, b = t; break;
	        case 3: r = p, g = q, b = v; break;
	        case 4: r = t, g = p, b = v; break;
	        case 5: r = v, g = p, b = q; break;
	    }

    return [r * 255, g * 255, b * 255];
}

function updateSlider() {
	var slider1 = document.getElementById("slider1");
	var slider2 = document.getElementById("slider2");
	var slider3 = document.getElementById("slider3");

	h = slider1.value;
	s = slider2.value;
	v = slider3.value;
	
	rgb = hsvToRgb(h,s,v);

	r = Math.floor(rgb[0])
	g = Math.floor(rgb[1])
	b = Math.floor(rgb[2])

	host = window.location.host
	httpGet("http://" + host + "/send/red/"+r);
	httpGet("http://" + host + "/send/green/"+g);
	httpGet("http://" + host + "/send/blue/"+b);	
}
