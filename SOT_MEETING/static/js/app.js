(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i += 1) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            var safeMethod = /^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type);
            if (!safeMethod && !this.crossDomain) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        }
    });

    $('#ajaxBtn').on('click', function () {
        var $result = $('#ajaxResult');
        $result.text('Running local AJAX test...');

        $.ajax({
            url: window.location.href,
            method: 'GET',
            success: function () {
                $result.text('AJAX success: local request completed.');
            },
            error: function () {
                $result.text('AJAX error: request failed.');
            }
        });
    });
})();
