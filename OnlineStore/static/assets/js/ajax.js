$('.minus, .plus').click(function () {
  var $input = $(this).parent().find('input');
  var count = parseInt($input.val());
  
  if ($(this).hasClass('minus')) {
    count = count < 2 ? 1 : count - 1;
  } else {
    count = count + 1;
  }
  
  $input.val(count);

  var cartItemId = $input.attr('data-cart-item-id');
  var newQuantityInput = document.getElementById('new-quantity-input');
  var cartItemIdInput = document.getElementById('cart-item-id-input');
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var cartId = $('#cart-total-price').data('cart-id'); // Получение значения cart.id
  
  newQuantityInput.value = count;
  cartItemIdInput.value = cartItemId;
  
  $.ajax({
    url: 'update_cart_item/',
    method: "POST",
    data: {
      cart_id: cartId,
      new_quantity: newQuantityInput.value,
      cart_item_id: cartItemIdInput.value,
      csrfmiddlewaretoken: csrfToken,
},
    success: function (data) {
      var newQuantity = data.cart_item_quantity;
      var newTotalPrice = data.cart_item_total_price;
      var newCartTotalPrice = data.cart_total_price;

      $('#cart-item-count').text(data.cart_item_count);
      $input.val(newQuantity);
      $('.cart-item-total-price[data-cart-item-id="' + cartItemId + '"]').text(newTotalPrice);
      $('#cart-total-price').text(newCartTotalPrice);

      console.log('Successful uptated');
    },

    error: function () {
      console.log('Failed to update cart item');
    },
  });
});