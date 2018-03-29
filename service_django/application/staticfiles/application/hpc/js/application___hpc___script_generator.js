/**
 * Created by Victor on 10/13/2017.
 */
$(function () {
    $('#script-format').on('change', function(){
        if(this.value == 'pbs'){
            $('#script_pbs').parent().removeClass('hidden');
            $('#script_slurm').parent().addClass('hidden');
            $('#script_name_group').find('.input-group-addon').text('.pbs');
        }else{
            $('#script_pbs').parent().addClass('hidden');
            $('#script_slurm').parent().removeClass('hidden');
            $('#script_name_group').find('.input-group-addon').text('.sl');
        }
    });

    if (method == 'GET')
        $("#id_export_env_variables, #id_output, #id_error, #id_mail_begins, #id_mail_ends, #id_mail_abort, #id_merge_stream_0").prop("checked", "checked");

    if($('#id_output').prop("checked"))$('#label-output').addClass('active');
    if($('#id_error').prop("checked"))$('#label-error').addClass('active');
    if($('#id_merge_stream_0').prop("checked"))$('label[for=id_merge_stream_0]').addClass('active');
    if($('#id_merge_stream_1').prop("checked"))$('label[for=id_merge_stream_1]').addClass('active');
    if($('#id_merge_stream_2').prop("checked"))$('label[for=id_merge_stream_2]').addClass('active');
    if($('#id_mail_begins').prop("checked"))$('#active_mail_begins').addClass('active');
    if($('#id_mail_ends').prop("checked"))$('#active_mail_ends').addClass('active');
    if($('#id_mail_abort').prop("checked"))$('#active_mail_abort').addClass('active');

    //Popover config
    $('[data-toggle="popover"]').popover({html: true, delay: {"show": 100, "hide": 100}});

    compose();
    $( "form[name=qsub_create] input[type=checkbox], input[type=radio], input[type=number], input[type=text],textarea" ).on('change', function() {
        compose();
    });
    $( "form[name=qsub_create] input,textarea" ).on('keyup', function() {
        compose();
    });

    /*resize*/
    window.onload = function(){
        resizePage();
    };
    $(window).resize(function () {
        resizePage();
    });
});
function resizePage(){
    var elem;
    if ($(window).width() <= 730) {
        $('#id_cores_per_node').attr('placeholder', gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_PLACEHOLDER_4'));
    }
    else {
        $('#id_cores_per_node').attr('placeholder', gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_PLACEHOLDER_4'));
    }
    if ($(window).width() <= 525) {
        $('#id_cores_per_node').removeAttr('placeholder');
        elem = $("#id_merge_stream_0");
        $("[for='id_merge_stream_0']").html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_3'));
        elem = $("#id_merge_stream_1");
        $("[for='id_merge_stream_1']").html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_4').slice(0,6));
        elem = $("#id_merge_stream_2");
        $("[for='id_merge_stream_2']").html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_5').slice(0,6));
    }else {
        elem = $("#id_merge_stream_0");
        $("[for='id_merge_stream_0']").html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_3'));
        elem = $("#id_merge_stream_1");
        $("[for='id_merge_stream_1']").html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_4'));
        elem = $("#id_merge_stream_2");
        $("[for='id_merge_stream_2']").html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_5'));
    }

    if ($(window).width() <= 485) {
        $('#id_cores_per_node').removeAttr('placeholder');
        $('#id_walltime').attr('placeholder', '- DD:HH:MM:SS -');
        $('#id_mail_address').attr('placeholder', gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_PLACEHOLDER_6_MIN'));
        elem = $("#id_mail_begins");
        $('#active_mail_begins').html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_6')[0]);
        elem = $("#id_mail_ends");
        $('#active_mail_ends').html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_7')[0]);
        elem = $("#id_mail_abort");
        $('#active_mail_abort').html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_8')[0]);
        $('#job-submit').html("<i class='glyphicon glyphicon-ok'></i>" + gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_BUTTON_2_MIN'));
    }
    else {

        $('#id_walltime').attr('placeholder', gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_PLACEHOLDER_5'));
        $('#id_mail_address').attr('placeholder', gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_PLACEHOLDER_6'));
        elem = $("#id_mail_begins");
        $('#active_mail_begins').html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_6'));
        elem = $("#id_mail_ends");
        $('#active_mail_ends').html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_7'));
        elem = $("#id_mail_abort");
        $('#active_mail_abort').html(elem).append(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_INPUT_LABEL_8'));
        $('#job-submit').html("<i class='glyphicon glyphicon-ok'></i>" + gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_BUTTON_2'));
    }
    if ($(window).width() <= 400) {
        $('#btn-merge-stream').text(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_LABEL_9').slice(0,9));
    }
    else {
        $('#btn-merge-stream').text(gettext('APPLICATION___HPC___CONTENT___HPC_SCRIPT_LABEL_9'));
    }
}
