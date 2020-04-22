$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(event){
        event.preventDefault();
        console.log('TEST123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        $('.basket-items ul').append('<li>'+product_name+': '+ nmb +'шт. '+ 'по '+
        product_price+'руб.'+'&nbsp &nbsp &nbsp &nbsp'+
        '<a href="" class="delete-item"><b>[x]</b></a>'+'</li>')
    });

    function shovingBasket() {
        $('.basket-items').toggleClass('d-none d-sm-none');
    };
    
    $('.btn-outline-success, basket-items').mouseover(function() {
        shovingBasket();
     });
 
     $('.btn-outline-success, .basket-items').mouseout(function() {
         shovingBasket();
     });

    $(document).on('click','.delete-item', function(e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })
    /* БОЛЬШОЙ КОД оптимизированный функцией shovingBasket, но рабочий
    $('.btn-outline-success').mouseover(function() {
        $('.basket-items').removeClass('d-none d-sm-none');
    })

    $('.btn-outline-success').mouseout(function() {
        $('.basket-items').addClass('d-none d-sm-none');
    })

    $('.basket-items').mouseover(function() {
        $('.basket-items').removeClass('d-none d-sm-none');
    })

    $('.basket-items').mouseout(function() {
        $('.basket-items').addClass('d-none d-sm-none');
    })
    */
});