function compose() {

    //Recojer campos de formularios
    var jobName = $('input[name="job_name"]').val();
    var exportEnvVariables = $('input[name="export_env_variables"]').prop('checked');
    var nodes = $('input[name="nodes"]').val();
    console.log("#"+nodes+"#")
    var coresPerNode = $('input[name="cores_per_node"]').val();
    var memoryPerNode = $('input[name="memory_per_node"]').val();
    var requireGpus = $('input[name="require_gpus"]').prop('checked');
    var test = $('input[name="test"]').prop('checked');
    var queueSelection = $('select[name="queue_selection"]').val();
    var walltime = $('input[name="walltime"]').val();
    var output_stream = $('input[name="output"]').prop("checked");
    var error_stream = $('input[name="error"]').prop("checked");
    var id_merge_stream_1 = $('label[for="id_merge_stream_1"]').hasClass('active');
    var id_merge_stream_2 = $('label[for="id_merge_stream_2"]').hasClass('active');
    var mailBegin = $('input[name="mail_begin"]').prop("checked");
    var mailEnd = $('input[name="mail_end"]').prop("checked");
    var mailAbort = $('input[name="mail_abort"]').prop("checked");
    var mailRequeue = $('input[name="mail_requeue"]').prop("checked");
    var mailAddress = $('input[name="mail_user"]').val();
    var scriptBody = $('textarea[name=script_body]').val();
    console.log(mailAddress, mailBegin, mailEnd, mailAbort, mailRequeue)

    var rc='\n';
    var script_pbs = "#!/bin/sh " + rc;
    var script_slurm = "#!/bin/sh " + rc;
    script_pbs += "#Submit this script with: qsub thefilename" + rc;
    script_slurm += "#Submit this script with: sbatch thefilename" +rc;

    script_pbs += ("### General Options ### " + rc);
    script_slurm += ("### General Options ### " + rc);
    if(jobName.length>0) {
        script_pbs += ('#PBS -N ' + jobName + ' # job name' + rc);
        script_slurm += ('#SBATCH -J "' + jobName + '" # job name' + rc);
    }
    if (exportEnvVariables) {
        script_pbs += ('#PBS -V ' + rc);
        script_slurm += ('#SBATCH --export=ALL' + rc);
    }
    script_pbs += ("### Resource Handling ###" + rc);
    script_slurm += ("### Resource Handling ###" + rc);
    if (nodes === '' || coresPerNode === '' || memoryPerNode === '' || test ) {
        script_pbs += '#PBS -l ';
        if(nodes === ''){
            script_slurm += '#SBATCH --nodes=' + nodes + ' # number of nodes' + rc;
            script_pbs += 'nodes=' + nodes;
        }
        if (coresPerNode === ''){
            script_slurm += '#SBATCH --ntasks=' + coresPerNode + ' # number of processor cores' + rc;
            if(nodes === '') {
                script_pbs += ':ppn=' + coresPerNode + ',';
            }
            else{
                script_pbs += ' procs=' + coresPerNode + ',';
            }
        }
        if (memoryPerNode === ''){
            script_slurm += '#SBATCH --mem-per-cpu=' + memoryPerNode + 'M   # memory per CPU core' + rc;
            script_pbs += 'pmem=' + memoryPerNode + 'MB,';
        }
        if (memoryPerNode === ''){
            script_slurm += '#SBATCH --time=' + walltime + ' # walltime' + rc;
            script_pbs += 'walltime=' + walltime + ',';
        }
        if (test>0){
            script_slurm += '#SBATCH --qos=test' + rc;
            script_pbs += 'qos=test,';
        }
        script_pbs = script_pbs.slice(0, -1) + rc;
    }

    if (requireGpus) {
        script_pbs += ('#PBS -W \'-x GRES:gpu\'' + rc);
        script_slurm += '#SBATCH --gres=gpu:2' +rc;
    }
    script_pbs += ('#PBS -q ' + queueSelection + ' # queue' + rc);
    script_slurm += '#SBATCH -p ' + queueSelection + ' # partition' + rc;
    /*if (walltime !== "00:00:00" || walltime.length>0)
        script_pbs += ('#PBS -l walltime=' + walltime + rc);
    */
    script_pbs += "### Output Stream Options ###" + rc;
    var temp = "#PBS -k ";
    if (output_stream && error_stream) {
        temp += 'n';
    }
    else if (!output_stream && error_stream) {
        temp += 'o';
    }
    else if (output_stream && !error_stream) {
        temp += 'e';
    }
    else if (!output_stream && !error_stream) {
        temp = '';
    }
    if (temp !== "") {
        script_pbs += (temp + rc);
    }
    if(id_merge_stream_1)
        script_pbs += '#PBS -j eo' + rc;
    if(id_merge_stream_2)
        script_pbs += '#PBS -j oe' + rc;

    temp = "#PBS -m ";
    if (mailAddress !== "") {
        script_pbs += "### Mail Options ###" + rc;
        script_slurm += "### Mail Options ###" + rc;
        script_slurm += '#SBATCH --mail-user=' + mailAddress + ' # email address' + rc;
        script_pbs += '#PBS -M ' + mailAddress + rc;
        if (!mailBegin && !mailEnd && !mailAbort) {
            temp = "";
        }
        else {
            if (mailBegin) {
                temp += 'b';
                script_slurm += '#SBATCH --mail-type=BEGIN' + rc;
            }
            if (mailEnd) {
                temp += 'e';
                script_slurm += '#SBATCH --mail-type=END' + rc;
            }
            if (mailAbort) {
                temp += 'a';
                script_slurm += '#SBATCH --mail-type=FAIL' + rc;
            }
            temp += rc;
        }
        script_pbs += temp;
    }
    script_pbs += (rc + "### Bash script ###" + rc + 'cd $PBS_O_WORKDIR' + rc + 'cores=$(awk \'END {print NR}\' $PBS_NODEFILE)'+ rc + scriptBody + rc + "exit 0" + rc);
    script_slurm += (rc + "### Bash script ###" + rc + 'cd $PBS_O_WORKDIR' + rc + 'cores=$(awk \'END {print NR}\' $PBS_NODEFILE)'+ rc + scriptBody + rc + "exit 0" + rc);

    $("#script_pbs").replaceWith('<pre id="script_pbs" class="prettyprint linenums lang-bsh">' + script_pbs + '</pre>');
    $("#script_slurm").replaceWith('<pre id="script_slurm" class="prettyprint linenums lang-bsh">' + script_slurm + '</pre>');
    prettyPrint();
}