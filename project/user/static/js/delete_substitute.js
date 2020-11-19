(function($) {
    "use strict";

    $(document).ready(function () {
        
        // Get cookies
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');

        // Save a substitute
        let form = $('.form-substitute-delete');
        function submitForm(e) {
            e.preventDefault();

            var dataForm =  $(this).serializeArray()
            var dataInput = dataForm[0]

            let data = {'product_id': dataInput.value}

            $.ajax({
                headers: {'X-CSRFToken': csrftoken},
                method: 'POST',
                url: '/delete_substitute/',
                data: data,
            }).done(function (response) {
                if (response['error_message']) {
                    alert('Ce produit ne peut pas être supprimé.');
                } else if (response['good_message']) {
                    let countProduct = $('.count_product');
                    let num = parseInt(countProduct.html());
                    countProduct.html(num -1);

                    let product = $('#'+data['product_id'])
                    product.remove()
                }
            });
        }
        form.on('submit', submitForm);
    })

})(jQuery);