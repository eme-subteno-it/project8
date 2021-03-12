(function($) {
    "use strict";

    /**
     * Function to get a cookie already create
     * @param {string} name cookie's name
     */
    window.getCookie = function (name) {
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

    /**
     * Function to create a cookie
     * @param {string} key The cookie's key
     * @param {string} value the cookie's value
     * @param {string} expiry the cookie's delay count in day ex : '1' = expire in one day
     */
    window.setCookie = function (key, value, expiry) {
        var expires = new Date();
        expires.setTime(expires.getTime() + (expiry * 24 * 60 * 60 * 1000));
        document.cookie = key + '=' + value + ';path=/' + ';expires=' + expires.toUTCString();
        console.log('Je suis bien rentrée dans la fonction ')
    }

    /**
     * Function to delete a cookie
     * @param {string} key The cookie's key
     */
    window.eraseCookie = function (key) {
        var keyValue = getCookie(key);
        setCookie(key, keyValue, '-1');
    }
})(jQuery);