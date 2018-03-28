var URLModule = {
    init: function(url) {
        this._url = url;
    },
    url: function(id) {
        return this._url;
    }
};

$(document).ready(function() {
    var optionsDataTable = {
        dom: "Blfrtip",
        buttons: [
            {
                extend: "copy",
                text: "copy",
                className: "btn-sm",
                exportOptions: {
                    columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                }
            },
            {
                extend: "csv",
                text: "csv",
                className: "btn-sm",
                exportOptions: {
                    columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                }
            },
            {
                extend: "print",
                text: "print",
                className: "btn-sm",
                exportOptions: {
                    columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                }
            }
        ],
        ajax: {
            "url": url_api,
            "type": "GET",
            "data": function() {
                var data;
                if ($('#yourjobs').parent().hasClass('active')) {
                    data = {
                        'parameters': ['jobs user', '42110027']
                    };
                }
                if ($('#groupjobs').parent().hasClass('active')) {
                    data = {
                        'parameters': ['jobs group']
                    };
                }
                if ($('#alljobs').parent().hasClass('active')) {
                    data = {
                        'parameters': ['jobs all']
                    };
                }
                return data;
            }
        },
        columnDefs: [
            {
                "render": function ( data/*, type, row*/ ) {
                    return '<span class="label label-' + setLabel(data) + '">' + data + '</span>'
                },
                "targets": 4
            },
            {
                "render": function ( data/*, type, row*/ ) {
                    return data
                },
                "targets": 0
            }
        ],
        "aoColumns": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            {
                "data" : '',
                "defaultContent": '<span class="fa fa-spinner fa-pulse fa-lg fa-4x"></span>',
                "orderable": false,
                "searchable": false
            }
        ],
        responsive: true,
        "lengthMenu": [[15, 50, -1], [15, 50, "All"]],
        "language":{
            "sProcessing":     gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Processing'),
            "sLengthMenu":     gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Length_Menu'),
            "sZeroRecords":    gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Zero_Records'),
            "sEmptyTable":     gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Empty_Table'),
            "sInfo":           gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Info'),
            "sInfoEmpty":      gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Info_Empty'),
            "sInfoFiltered":   gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Info_Filtered'),
            "sInfoPostFix":    "",
            "sSearch":         gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Search'),
            "sUrl":            "",
            "sInfoThousands":  ",",
            "sLoadingRecords": gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Loading_Records'),
            "oPaginate": {
                "sFirst":    gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_First'),
                "sLast":     gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Last'),
                "sNext":     gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Next'),
                "sPrevious": gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Previous')
            },
            "oAria": {
                "sSortAscending":  gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Sort_Ascending'),
                "sSortDescending": gettext('APPLICATION___HPC___CONTENT___HPC_JOBS_DATATABLE_Sort_Descending')
            }
        }
    };
    var handleDataTableButtons = function() {
        var  datatable = $("#datatable-buttons");
        if ($(datatable).length) {
            $(datatable).DataTable(optionsDataTable);
        }
    };

    var TableManageButtons = function() {
        "use strict";
        return {
            init: function() {
                handleDataTableButtons();
            }
        };
    }();

    TableManageButtons.init();

    $('#datatable-buttons_length').addClass('col-xs-6').css('padding', '0');
    $('#dataTables_filter').addClass('col-xs-6');
    $('.dt-buttons').css('text-align', 'center');
    $('#center___content').css('display', 'block');
    $('#datatable-buttons').find('tbody').on('click', 'td:first-child', function () {
        var tr = $(this).closest('tr');
        var datatable = $('#datatable-buttons').DataTable();
        var row = datatable.row(tr).index();
        var id = datatable.cell(row, 0).data();
        detailJob(row, id);
    });
});

function detailJob(row, id){
    var parameters = ['detail job', id];
    $.getJSON(url_api, {'parameters': parameters}, function(data) {
        var datatable = $('#datatable-buttons').DataTable();
        datatable.cell(row, 9).data('' +
            '<div class="panel panel-default">' +
                '<div class="panel-heading">' +
                    '<span class="label label-' + setLabel(data['JobState']) + '">' + data['JobState'] + '</span> ' +
                    '<b>' + data['JobName'] + '(' + data['JobId'] + ')</b>' +
                    '<div class="pull-right">' +
                        '<button class="btn btn-xs btn-primary" type="button" disabled>' +
                            '<span class="fa fa-play"></span>' +
                        '</button> ' +
                        '<button class="btn btn-xs btn-default" type="button">' +
                            '<span class="fa fa-stop"></span>' +
                        '</button> ' +
                        '<button class="btn btn-xs btn-default" type="button">' +
                            '<span class="fa fa-refresh"></span>' +
                        '</button> ' +
                        '<button class="btn btn-xs btn-default" type="button">' +
                            '<span class="fa fa-remove"></span>' +
                        '</button>' +
                    '</div>' +
                '</div>' +
                '<div class="panel-body">' +
                    '<table class="table table-bordered table-striped table-condensed">' +
                        '<tr><td colspan=2><b>Job Information</b></td></tr>' +
                        '<tr><td>Job Id</td><td>' + data['JobId'] + '</td></tr>' +
                        '<tr><td>Job Name</td><td>' + data['JobName'] + '</td></tr>' +
                        '<tr><td>User</td><td>' + data['UserId'] + '</td></tr>' +
                        '<tr><td>Queue</td><td>' + data['Partition'] + '</td></tr>' +
                        '<tr><td>Group Id</td><td>' + data['GroupId'] + '</td></tr>' +
                        '<tr><td colspan=2><b>Excecution Time</b></td></tr>' +
                        '<tr><td>Run Time</td><td>' + data['RunTime'] + '</td></tr>' +
                        '<tr><td>Time Limit</td><td>' + data['TimeLimit'] + '</td></tr>' +
                        '<tr><td>Submit Time</td><td>' + data['SubmitTime'] + '</td></tr>' +
                        '<tr><td>Eligible Time</td><td>' + data['EligibleTime'] + '</td></tr>' +
                        '<tr><td>Start Time</td><td>' + data['StartTime'] + '</td></tr>' +
                        '<tr><td>End Time</td><td>' + data['EndTime'] + '</td></tr>' +
                        '<tr><td colspan=2><b>Nodes</b></td></tr>' +
                        '<tr><td>Node Count</td><td>' + data['NumNodes'] + '</td></tr>' +
                        '<tr><td>Node List</td><td>' + data['NodeList'] + '</td></tr>' +
                        '<tr><td>Batch Node</td><td>' + data['BatchHost'] + '</td></tr>' +
                        '<tr><td colspan=2><b>Resources</b></td></tr>' +
                        '<tr><td>Num CPUs</td><td>' + data['NumCPUs'] + '</td></tr>' +
                        '<tr><td>Num Tasks</td><td>' + data['NumTasks'] + '</td></tr>' +
                        '<tr><td>CPUs/Task</td><td>' + data['CPUs/Task'] + '</td></tr>' +
                        '<tr><td>Memory</td><td>' + data['mem'] + '</td></tr>' +
                    '</table>' +
                    '<div style="width:80px">File Location</div><div class="panel panel-default"><div class="panel-heading">' + data['Command'] +'</div></div>' +
                    '<div style="width:80px">Output Location</div><div class="panel panel-default"><div class="panel-heading">' + data['StdOut'] + '</div></div>' +
                    '<div style="width:80px">Error Location</div><div class="panel panel-default"><div class="panel-heading">' + data['StdErr'] + '</div></div>' +
                '</div>' +
            '</div>'
        ).page(datatable.page()).draw('page');
    }).fail(function(data) {
        ___HTML___application___hpc___modal___SHOW_LOAD___();
        ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data['MESSAGE']);
    }).always(function() {
        console.log( "complete" );
    });
}

function setLabel(state){
    if(state==='PENDING')
        return "danger";
    if(state==='RUNNING')
        return "info";
    if(state==='SUSPENDED')
        return "warning";
    if(state==='CANCELLED')
        return "warning";
    if(state==='COMPLETING')
        return "primary";
    if(state==='COMPLETED')
        return "success";
    if(state==='CONFIGURING')
        return "info";
    if(state==='FAILED')
        return "danger";
    if(state==='TIMEOUT')
        return "danger";
    if(state==='PREEMPTED')
        return "warning";
    if(state==='NODE_FAIL')
        return "danger";
    if(state==='REVOKED')
        return "danger";
    if(state==='SPECIAL_EXIT')
        return "default";
    return "default";
}

function dropJobs(elem) {
    $('#dropdownMenu1').html($(elem).text() + ' <span class="caret"></span>');
    $(elem).parent().siblings().removeClass('active');
    $(elem).parent().addClass('active');
    $('#datatable-buttons').DataTable().ajax.reload();
}