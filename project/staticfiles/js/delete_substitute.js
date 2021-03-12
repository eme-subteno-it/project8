(function($) {
    "use strict";

    $(document).ready(function () {
        // Delete a substitute
        let form = $('.form-substitute-delete');
        function submitForm(e) {
            e.preventDefault();

            var dataForm =  $(this).serializeArray()
            var csrftokenInput = dataForm[0];
            var dataInput = dataForm[1];

            let data = {'product_id': dataInput.value}

            $.ajax({
                headers: {'X-CSRFToken': csrftokenInput.value},
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