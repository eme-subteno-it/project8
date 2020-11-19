(function($) {
    "use strict";

    $(document).ready(function () {
        // let resultSearch = $('.result-search').find('figure')

        // resultSearch.on('click', function () {
        //     let productName = $(this).find('figcaption').html()
        //     console.log(productName);
        // })

        let buttonSave = $('.save_substitute');
        console.log(buttonSave);
        function submitForm(e) {
            e.preventDefault();
            var datas =  $(this).serializeArray()
            console.log(datas)
            var dataInput = datas[0]

            $.ajax({
                method: 'POST',
                url: "{% url 'save_substitute' %}",
                data: dataInput.value,
            }).done(function (data) {
                console.log(data);
            });
        }
        buttonSave.on('submit', submitForm);
    })

})(jQuery);