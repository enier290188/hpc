var hpc_script_modal_help = function(){
    var $btn = $(this);
    $.ajax({
        url: $btn.attr("data-url"),
        type: "GET",
        dataType: "json",
        beforeSend: function () {
            ___HTML___application___hpc___modal___SHOW_LOAD___();
        },
        success: function (data) {
            if (data['___BOOLEAN___ERROR___']) {
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
            }
            else {
                var $application___hpc___modal = $("#application___hpc___modal");
                $application___hpc___modal.html(data['___HTML___APPLICATION___HPC___MODAL___']);
                $application___hpc___modal.find(".modal___message").html(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']);
                ___HTML___application___hpc___modal___EVENTS_ON___();
            }
        }
    });
};

var hpc_script_submit = function(evt){
    evt.preventDefault();
    var $form = $(this);
    var $btn = $form.find('div.form-group').find('button.active');
    var formData = new FormData(this);
    $.ajax({
        url: $form.attr("action"),
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
            var $application___hpc___content___center = $("#application___hpc___content___center");
            if (data['___BOOLEAN___ERROR___']) {
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                $application___hpc___content___center.html(data['___HTML___APPLICATION___HPC___CONTENT___CENTER___']);
                ___HTML___application___hpc___content___SCROLL_DESTROY___();
                ___HTML___application___hpc___content___SCROLL_CREATE___();
            }
            else {
                $application___hpc___content___center.html(data['___HTML___APPLICATION___HPC___CONTENT___CENTER___']);
                ___HTML___application___hpc___modal___SHOW_MESSAGE_OK___(data);
                ___HTML___application___hpc___content___SCROLL_DESTROY___();
                ___HTML___application___hpc___content___SCROLL_CREATE___();
            }
        }
    });
};

var hpc_script_run = function(){
    var $form = $('.form-hpc-script-submit'),
        $btn = $(this);
    var formData = new FormData($form[0]);
    formData.append('run', true);
    formData.append('csrfmiddlewaretoken', $form.find("input[name='csrfmiddlewaretoken']").val());
    $.ajax({
        url: $form.attr("action"),
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
            var $application___hpc___content___center = $("#application___hpc___content___center");
            if (data['___BOOLEAN___ERROR___']) {
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                $application___hpc___content___center.html(data['___HTML___APPLICATION___HPC___CONTENT___CENTER___']);
                ___HTML___application___hpc___content___SCROLL_DESTROY___();
                ___HTML___application___hpc___content___SCROLL_CREATE___();
            }
            else {
                $application___hpc___content___center.html(data['___HTML___APPLICATION___HPC___CONTENT___CENTER___']);
                ___HTML___application___hpc___modal___SHOW_MESSAGE_OK___(data);
                ___HTML___application___hpc___content___SCROLL_DESTROY___();
                ___HTML___application___hpc___content___SCROLL_CREATE___();
            }
        }
    });
};

$("#application___hpc___content")
    .on("submit", ".form-hpc-script-submit", hpc_script_submit)
    .on("click", ".form-hpc-script-run", hpc_script_run)
    .on("click", ".btn-hpc-script-modal-help", hpc_script_modal_help);