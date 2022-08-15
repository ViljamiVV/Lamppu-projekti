

function luuppi () {
	var a = 0;
	var b = 0;

    $(document).ready(function() {
    $.getJSON("data.json", function(sisalto) {
    
	$.each(sisalto, function(avain, arvo) {
		
		if (avain == "bb") {
			b = arvo;
		
		}
		
		else if (avain == "aa") {
			a = arvo;
		}
	
	
	if (a > b) {
		$("#lahtotilanne").attr("src", "polttimoPaalla.gif");
	}
				
	else if (b > a) {
		$("#lahtotilanne").attr("src", "polttimoKiinni.gif");
	} 

});
});
});	
}

setInterval(luuppi, 1000);










































/* 	ilman silmukkaa

$(document).ready(function() {
	a = 0;
	b = 0;

	$.getJSON("data.json", function(sisalto) {
    
    	// console logataan json tiedoston sisalto
	//console.log(sisalto);	 

	// iteroidaan .each() funktiolla json objekti läpi ja annetaan arvot aa:lle ja bb:lle
	$.each(sisalto, function(avain, arvo) {
		//alert(avain + " : " + arvo);	// 
		
		if (avain == "bb") {
			b = arvo;
			console.log("bb: " + b);
		}
		
		else if (avain == "aa") {
			a = arvo;
			console.log("aa: " + a);		
		}
	
	// verrataan kumpi on uudempi napin painallus ja vaihetaan niin kuva
	if (a > b) {
		$("#lahtotilanne").attr("src", "polttimoPaalla.gif");
	}
				
	else if (b > a) {
		$("#lahtotilanne").attr("src", "polttimoKiinni.gif");
	} 


});
});
});


*/




