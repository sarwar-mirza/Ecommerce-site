$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


// QUANTITY PLUS & AJAX 

$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    //console.log(id)
    var eml = this.parentNode.children[2]          // quantity update

    $.ajax({                                       // passing server
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {                //views.py - calling 
            eml.innerText = data.quantity

            document.getElementById("amount").innerText = data.amount  // html ID - ("amount")
            document.getElementById("totalamount").innerText = data.totalamount  // html ID - ("totalamount")
        }
    })
})




// QUANTITY MINUS & AJAX 

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    //console.log(id)
    var eml = this.parentNode.children[2]          // quantity update

    $.ajax({                                       // passing server
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {                //views.py - calling 
            eml.innerText = data.quantity

            document.getElementById("amount").innerText = data.amount  // html ID - ("amount")
            document.getElementById("totalamount").innerText = data.totalamount  // html ID - ("totalamount")
        }
    })
})


//REMOVE 
$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this

    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function(data) {

            document.getElementById("amount").innerText = data.amount  // html ID - ("amount")
            document.getElementById("totalamount").innerText = data.totalamount  // html ID - ("totalamount")

            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})