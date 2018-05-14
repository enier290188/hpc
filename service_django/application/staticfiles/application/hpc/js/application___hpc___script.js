var ___HTML___application___hpc___module___hpc_script___modal___HELP___ = function(){
    var $btn = $(this);
    $.ajax({
        url: $btn.attr("data-url"),
        type: "GET",
        dataType: "json",
        beforeSend: function () {
            ___HTML___application___hpc___modal___SHOW_LOAD___();
        },
        success: function (data) {
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $application___hpc___modal = $("#application___hpc___modal");
                $application___hpc___modal.html(data.___HTML___APPLICATION___HPC___MODAL___);
                $application___hpc___modal.find(".modal___message").html(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___);
                ___HTML___application___hpc___modal___EVENTS_ON___();
            }
        }
    });
};

var ___HTML___application___hpc___module___hpc_script___SUBMIT___ = function(evt){
    evt.preventDefault();
    var $form = $(this);
    var $application___hpc___content___center = $("#application___hpc___content___center"),
        $application___hpc___modal = $("#application___hpc___modal");
    var $btn = $form.find('div.form-group').find('button.active');
    $btn.removeClass('active');
    var value = $btn.attr('value'),
        formData = new FormData(this);
    formData.append('submit', value);
    $.ajax({
        url: $form.attr("action") + "?search=",
        data: formData,
        type: $form.attr("method"),
        dataType: "json",
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function () {
            ___HTML___application___hpc___modal___SHOW_LOAD___();
        },
        success: function (data) {
            ___HTML___application___hpc___content___SCROLL_DESTROY___();
            ___HTML___application___hpc___content___SCROLL_CREATE___();
            if (data.___BOOLEAN___ERROR___) {
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                ___HTML___application___hpc___modal___SHOW_MESSAGE_OK___(data);
            }
        }
    });
};

$(function () {
    const $application___hpc___content___center = $("#application___hpc___content___center");
    $application___hpc___content___center
        .on("submit", ".form___application___hpc___module___hpc_script___submit", ___HTML___application___hpc___module___hpc_script___SUBMIT___)
        .on("click", ".btn___application___hpc___module___hpc_script___modal___help", ___HTML___application___hpc___module___hpc_script___modal___HELP___);
});
