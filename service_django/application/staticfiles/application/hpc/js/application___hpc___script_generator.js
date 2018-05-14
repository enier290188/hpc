/**
 * Created by Victor on 10/13/2017.
 */
$(function () {
    //Popover config
    $('[data-toggle="popover"]').popover({html: true, delay: {"show": 200, "hide": 200}});

    var $scriptForm = $('form[name=hpc_script_create]'),
        $mail_begin = $scriptForm.find('input[name="mail_begin"]'),
        $mail_end = $scriptForm.find('input[name="mail_end"]'),
        $mail_abort = $scriptForm.find('input[name="mail_abort"]'),
        $mail_requeue = $scriptForm.find('input[name="mail_requeue"]');
    if($mail_begin.prop("checked")) $mail_begin.parent().addClass('active');
    if($mail_end.prop("checked")) $mail_end.parent().addClass('active');
    if($mail_abort.prop("checked")) $mail_abort.parent().addClass('active');
    if($mail_requeue.prop("checked")) $mail_requeue.parent().addClass('active');

    compose();

    $scriptForm.find('fieldset').eq(3).find('input[type=checkbox]').on('change', function() {
        var $father = $(this).parent();
        if($father.hasClass('active'))
            $father.removeClass('active');
        else
            $father.addClass('active');
        compose();
    });

    $scriptForm.find('select, input[type=checkbox], input[type=radio], input[type=number], input[type=text], textarea').on('change', function() {
        compose();
    });
    $scriptForm.find('input, textarea').on('keyup', function() {
        compose();
    });

    /*resize*/
    $(window).resize(function () {
        console.log("Ok");
    });
});

var entityMap = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
    '/': '&#x2F;',
    '`': '&#x60;',
    '=': '&#x3D;'
};

function escapeHtml (string) {
    /*return String(string).replace(/[&<>"'`=\/]/g, function (s) {
        return entityMap[s];
    });*/
    return string;
}
function compose() {
    var scriptForm = $('form[name=hpc_script_create]'),
        job_name = scriptForm.find('input[name="job_name"]').val(),
        export_variables = scriptForm.find('input[name="export_variables"]').prop('checked'),
        partition = scriptForm.find('select[name="partition"]').val(),
        nodes = scriptForm.find('input[name="nodes"]').val(),
        ntasks = scriptForm.find('input[name="ntasks"]').val(),
        tasks_per_node = scriptForm.find('input[name="tasks_per_node"]').val(),
        cpus_per_task = scriptForm.find('input[name="cpus_per_task"]').val(),
        mem = scriptForm.find('input[name="mem"]').val(),
        size = scriptForm.find('select[name="size"]').val(),
        mem_per_cpu = scriptForm.find('input[name="mem_per_cpu"]').val(),
        size_per_cpu = scriptForm.find('select[name="size_per_cpu"]').val(),
        time = scriptForm.find('input[name="time"]').val(),
        test = scriptForm.find('input[name="test"]').prop('checked'),
        require_gpus = scriptForm.find('input[name="require_gpus"]').prop('checked'),
        nodelist = scriptForm.find('input[name="nodelist"]').val(),
        exclude = scriptForm.find('input[name="exclude"]').val(),
        output = scriptForm.find('input[name="output"]').val(),
        error = scriptForm.find('input[name="error"]').val(),
        mail_user = scriptForm.find('input[name="mail_user"]').val(),
        mail_begin = scriptForm.find('input[name="mail_begin"]').prop("checked"),
        mail_end = scriptForm.find('input[name="mail_end"]').prop("checked"),
        mail_abort = scriptForm.find('input[name="mail_abort"]').prop("checked"),
        mail_requeue = scriptForm.find('input[name="mail_requeue"]').prop("checked"),
        script_body = scriptForm.find('textarea[name=script_body]').val();
    const rc='\n';
    var script_slurm = "#!/bin/sh " + rc;
    script_slurm += "#Submit this script with: sbatch thefilename" +rc;

    if (job_name !== '' || !export_variables || partition !== '') {
        script_slurm += rc + "### General options ### " + rc;
        if (job_name !== '') script_slurm += '#SBATCH --job-name=' + escapeHtml(job_name) + rc;
        if (export_variables) script_slurm += '#SBATCH --export=ALL' + rc; else script_slurm += '#SBATCH --export=NONE' + rc;
        if (partition !== '') script_slurm += '#SBATCH --partition=' + partition + rc;
    }

    if (nodes !== '' || ntasks !== '' || tasks_per_node !== '' || cpus_per_task !== '' || mem !== '' && parseInt(mem) > 0
        || mem_per_cpu !== '' && parseInt(mem_per_cpu) > 0 || time !== '' || test || require_gpus || nodelist !== '' || exclude !== '') {
        script_slurm += rc + "### Resource handling ###" + rc;
        if (nodes !== '') script_slurm += '#SBATCH --nodes=' + escapeHtml(nodes) + rc;
        if (ntasks !== '') script_slurm += '#SBATCH --ntasks=' + ntasks + rc;
        if (tasks_per_node !== '') script_slurm += '#SBATCH --tasks-per-node=' + tasks_per_node + rc;
        if (cpus_per_task !== '') script_slurm += '#SBATCH --cpus-per-task=' + cpus_per_task + rc;
        if (mem !== '' && parseInt(mem) > 0) script_slurm += '#SBATCH --mem=' + mem + size + rc;
        if (mem_per_cpu !== '') script_slurm += '#SBATCH --mem-per-cpu=' + mem_per_cpu + size_per_cpu + rc;
        if (time !== '') script_slurm += '#SBATCH --time=' + escapeHtml(time) + rc;
        if (test) script_slurm += '#SBATCH --test-only' + rc;
        if (require_gpus) script_slurm += '#SBATCH --gres=gpu:2' + rc;
        if (nodelist !== '') script_slurm += '#SBATCH --nodelist=' + escapeHtml(nodelist) + rc;
        if (exclude !== '') script_slurm += '#SBATCH --exclude=' + escapeHtml(exclude) + rc;
    }

    if (output !== '' || error !== '') {
        script_slurm += rc + "### Stream options ###" + rc;
        if (output !== '') script_slurm += '#SBATCH --output=' + escapeHtml(output) + rc;
        if (error !== '') script_slurm += '#SBATCH --error=' + escapeHtml(error) + rc;
    }

    if (mail_user !== "") {
        script_slurm += rc + "### Mail options ###" + rc;
        script_slurm += '#SBATCH --mail-user=' + mail_user + rc;
        if (mail_begin && mail_end && mail_abort && mail_requeue) {
            script_slurm += '#SBATCH --mail-type=ALL' + rc;
        }
        else if (mail_begin || mail_end || mail_abort || mail_requeue)
        {
            if (mail_begin) script_slurm += '#SBATCH --mail-type=BEGIN' + rc;
            if (mail_end) script_slurm += '#SBATCH --mail-type=END' + rc;
            if (mail_abort) script_slurm += '#SBATCH --mail-type=ABORT' + rc;
            if (mail_requeue) script_slurm += '#SBATCH --mail-type=REQUEUE' + rc;
        }
        else
            script_slurm += '#SBATCH --mail-type=NONE' + rc;
    }
    script_slurm += rc + "### Bash script ###" + rc + 'cd $SLURM_SUBMIT_DIR' + rc + script_body + rc + "exit 0" + rc;
    $('#script_slurm').replaceWith(`<pre id="script_slurm" class="prettyprint linenums lang-bsh">${script_slurm}</pre>`);
    prettyPrint();
}