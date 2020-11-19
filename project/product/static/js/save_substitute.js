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
        let form = $('.form-substitute-save');
        function submitForm(e) {
            e.preventDefault();

            var dataForm =  $(this).serializeArray()
            var dataInput = dataForm[0]

            let data = {'product_id': dataInput.value}

            $.ajax({
                headers: {'X-CSRFToken': csrftoken},
                method: 'POST',
                url: '/save_substitute/',
                data: data,
            }).done(function (data) {
                console.log(data);
                if (data['error_message']) {
                    alert('Veuillez vous connecter afin de pouvoir sauvegarder ce produit.');
                    window.location.replace('/login/');
                } else if (data['good_message']) {
                    alert('Le produit a bien été sauvegardé');
                }
            });
        }
        form.on('submit', submitForm);
    })

})(jQuery);