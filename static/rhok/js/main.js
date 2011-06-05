if (typeof Cmatic === 'undefined' || !Cmatic)  {
    // Cmatic global namespace object
    var Cmatic = {};
}

Cmatic.utils = (function ($) {
    obj = {
       hasJS: function() {
           $('html').removeClass('no-js');
        } 
    };

    return obj;
})(jQuery);

