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

        var csrftokenList = getCookie('csrftoken');
        let btnDisplaySub = $('.btn-nb');

        btnDisplaySub.on('click', function () {
            btnDisplaySub.removeClass('active');
            $(this).addClass('active');

            let url = window.location.pathname.split('/').filter(Boolean)
            let product_id = $(url).get(-1)
            let data = {'number': $(this).html(), 'product_search_id': parseInt(product_id)}

            let containerSubstitute = $('.substitutes-cart');
            containerSubstitute.empty();

            $.ajax({
                headers: {'X-CSRFToken': csrftokenList},
                method: 'POST',
                url: '/change_number_list/',
                data: data,
            }).done(function (response) {
                containerSubstitute.append(response);
                let formSave = containerSubstitute.find('.form-substitute-save');
                formSave.on('submit', window.submitForm);
            });
        })
    })

})(jQuery);