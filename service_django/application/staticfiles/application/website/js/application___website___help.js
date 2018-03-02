var ___HTML___application___website___content___center___content___list___RELOAD___ = function () {
    var identifier = "#application___website___content___center #center___content #content___list";
    $.ajax({
        url: $(identifier).attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            $(identifier).html(___HTML___APPLICATION___WEBSITE___LOAD___);
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___application___website___modal___SHOW_LOAD___();
                ___HTML___application___website___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                $(identifier).html(data.___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___LIST___);
                var identifier2 = "#application___website___content___center #center___content #content___content";
                $.ajax({
                    url: $(identifier2).attr("data-url"),
                    type: "get",
                    dataType: "json",
                    beforeSend: function () {
                        $("a.LINK___application___website___content___center___content___list___reload___:first").addClass("active");
                        $(identifier2).html(___HTML___APPLICATION___WEBSITE___LOAD___);
                    },
                    success: function (data) {
                        if (data.___BOOLEAN___ERROR___) {
                            $(identifier2).html("");
                            ___HTML___application___website___modal___SHOW_LOAD___();
                            ___HTML___application___website___modal___SHOW_MESSAGE_ERROR___(data);
                        }
                        else {
                            $(identifier2).html(data.___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___CONTENT___);
                        }
                    }
                });
            }
        }
    });
};

var ___HTML___application___website___content___center___content___content___RELOAD___ = function () {
    var $link = $(this);
    var identifier = "#application___website___content___center #center___content #content___content";
    $.ajax({
        url: $link.attr("data-url"),
        type: "get",
        dataType: "json",
        beforeSend: function () {
            $(".LINK___application___website___content___center___content___list___reload___").removeClass("active");
            $link.addClass("active");
            $(identifier).html(___HTML___APPLICATION___WEBSITE___LOAD___);
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                $(identifier).html("");
                ___HTML___application___website___modal___SHOW_LOAD___();
                ___HTML___application___website___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                $(identifier).html(data.___HTML___APPLICATION___WEBSITE___CONTENT___CENTER___CONTENT___);
            }
        }
    });
};


$(document).ready(function () {
    /* Instructions to excecute when end the load. */
    ___HTML___application___website___content___center___content___list___RELOAD___();
    $("#application___website___content___center").find("#center___content").find("#content___list")
        .off("click", ".LINK___application___website___content___center___content___list___reload___")
        .on("click", ".LINK___application___website___content___center___content___list___reload___", ___HTML___application___website___content___center___content___content___RELOAD___);
});
