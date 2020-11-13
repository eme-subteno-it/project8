(function($) {
    "use strict";

    $(document).ready(function () {
        let resultSearch = $('.result-search').find('figure')

        resultSearch.on('click', function () {
            let productName = $(this).find('figcaption').html()
            console.log(productName);
        })
    })

})(jQuery);