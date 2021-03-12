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

        // Save a substitute
        let form = $('.form-substitute-save');

        window.submitForm = function (e) {
            e.preventDefault();
            var dataForm =  $(this).serializeArray()
            var csrftokenInput = dataForm[0];
            var dataInput = dataForm[1];

            let data = {'product_id': dataInput.value}

            $.ajax({
                headers: {'X-CSRFToken': csrftokenInput.value},
                method: 'POST',
                url: '/save_substitute/',
                data: data,
            }).done(function (response) {
                if (response['status'] === 'error') {
                    let modal = $("#modal_login");
                    let inputRedirect = modal.find("input[name='next']");
                    inputRedirect.val(window.location.pathname + '?substitute_id=' + dataInput.value);
                    modal.modal("show");
                } else if (response['status'] === 'success') {
                    let messageSubstituteSaved = $('#message_substitute_saved');
                    messageSubstituteSaved.modal('show');
                    setTimeout(function () {
                        messageSubstituteSaved.modal('hide');
                    }, 2000);
                }
            });
        }
        form.on('submit', submitForm);
    })

})(jQuery);