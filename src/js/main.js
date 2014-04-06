/**
 * Created by Rong on 4/6/2014.
 */




$(document).ready(function () {
    if (hasCookie()) {
        $("#autocomplete").attr("placeholder", getCookieAddr());
    }

});

function plzwaiton(){
    $('#myModal').modal('show');
}
function plzwaitoff(){
    $('#myModal').modal('hide');
}

function getSearch() {

    $("#search").show();
    $("#result").hide();
    $("#profile").show();
    $(".table").empty();
    $(".address").empty();
}

function hasCookie() {
    return typeof ($.cookie('zip')) != 'undefined';
}

function getResult() {
    //TODO

    if (!hasCookie()) {
        alert("We don't provide for NULL address user.");
    }

    $("#search").hide();
    $("#result").show();
    $("#profile").hide();


    var userData = {
        keyword:   document.getElementById("keyword").textContent,
        addr: $.cookie('address'),
        city: $.cookie('city'),
        zip: $.cookie('zip')
    }

    plzwaiton();

    $.ajax({
        type: "POST",
        url: "/gen_order",
        data: userData
    })
        .done(function (data) {
            //alert("Data Saved: " + data);

            var items = [];
            var address = "";
            var amount = data.amount;

            address += data.restaurant.na + "<i>($"+ data.restaurant.services.deliver.mino +" to delivery)</i>" + "<br>";
            address += data.restaurant.addr + "<br>";
            address += data.restaurant.cs_phone;

            data = data.order;
            items.push("<tr> <th   style='width:80%; ' > Top Secret </th><th  style='width:20%'> $ </th></tr>");

            $(data).each(function () {
                    var name = this.name;
                    var price = this.price;
                    items.push("<tr > <td class='blurry-text' style='width:80%'>" + name + " </td><td style='width:20%'> " + price + " x 1 " + "</td></tr>");
                }
            );

            items.push("<tr> <th  style='width:80%'> Bottom Secret </th><th  style='width:20%'> " + amount + " </th></tr>");


            $("<table  />", {
                "width": "100%",
                "class": "my-new-list table table-hover  table-striped  table-bordered",
                html: items.join("")
            }).appendTo(".table");


            $("<h3 />", {
                html: address
            }).appendTo($("#address"));

            var txt = $(".blurry-text");
            txt.hover(function () {


                var result = $(this).css('text-shadow').split(" ");

                var y = result[3];
                var x = result[4];
                var blur = result[5];
                var color = result[0] + result[1] + " " + result[2];
                // result => ['rgb(30, 43, 2)', '-4px', '11px', '8px']
                //console.log("[color]" + color + ",[y]" + y + ",[x]" + x + ",[blur]" + blur);
                blur = blur.replace("px", "");
                if (blur > 0) {
                    blur = blur / 1.5 + "px";
                    //console.log(blur);
                    $(this).css('text-shadow', color + " " + y + " " + x + " " + blur);
                }
            });
	plzwaitoff();
        });


}


var placeSearch, autocomplete;
var componentForm = {
    street_number: 'short_name',
    route: 'long_name',
    locality: 'long_name',
    administrative_area_level_1: 'short_name',
    country: 'long_name',
    postal_code: 'short_name'
};

function initialize() {
    // Create the autocomplete object, restricting the search
    // to geographical location types.
    autocomplete = new google.maps.places.Autocomplete(
        /** @type {HTMLInputElement} */
        (document.getElementById('autocomplete')),
        { types: ['geocode'] });
    // When the user selects an address from the dropdown,
    // populate the address fields in the form.
    google.maps.event.addListener(autocomplete, 'place_changed', function () {
        fillInAddress();
    });
}

// [START region_fillform]
function fillInAddress() {
    // Get the place details from the autocomplete object.
    var place = autocomplete.getPlace();


    componentForm = {
        street_number: 'short_name',
        route: 'long_name',
        locality: 'long_name',
        administrative_area_level_1: 'short_name',
        country: 'long_name',
        postal_code: 'short_name'
    };

    // Get each component of the address from the place details
    // and fill the corresponding field on the form.
    for (var i = 0; i < place.address_components.length; i++) {
        var addressType = place.address_components[i].types[0];
        if (componentForm[addressType]) {
            var val = place.address_components[i][componentForm[addressType]];
            componentForm[addressType] = val;

        }
    }

     $.cookie('address', (componentForm['street_number'] != "undefined" && componentForm['street_number'] != "short_name" ? componentForm['street_number'] + "," : "") + (componentForm['route'] != "long_name" ? componentForm['route'] : "")); 
+    $.cookie('city', componentForm['locality'] != "long_name" ? componentForm['locality'] : ""); 
+    $.cookie('zip', componentForm['postal_code'] != 'short_name' ? componentForm['postal_code'] : ""); 
+    $.cookie('state', componentForm['administrative_area_level_1']!="short_name"?componentForm['administrative_area_level_1']:""); 
   
}
// [END region_fillform]

// [START region_geolocation]
// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var geolocation = new google.maps.LatLng(
                position.coords.latitude, position.coords.longitude);
            autocomplete.setBounds(new google.maps.LatLngBounds(geolocation,
                geolocation));
        });
    }
}
// [END region_geolocation]

function getAddress() {
    var addr = $.cookie('address') + "\n" + $.cookie('city') + "\n" + $.cookie('state') + "\n" + $.cookie('zip');
    document.getElementById("addrInput").value = addr;
}


function getCookieAddr() {
    var addr = $.cookie('address') + " " + $.cookie('city') + " " + $.cookie('state') + " " + $.cookie('zip');
    //alert(addr);
    return  addr;
}

function resetCookie(){
    $.removeCookie('address');
    $.removeCookie('city');
    $.removeCookie('zip');
    $.removeCookie('state');

    $("#autocomplete").attr("placeholder","Enter your address");

}
