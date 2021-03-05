(function($) {
    "use strict";

    $(document).ready(function () {
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