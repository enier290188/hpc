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
                className: "btn-primary btn-sm",
                exportOptions: {
                    columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                }
            },
            {
                extend: "print",
                text: "print",
                className: "btn-primary btn-sm",
                exportOptions: {
                    columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                }
            },
            {
                extend: "csv",
                text: "csv",
                className: "btn-primary btn-sm",
                exportOptions: {
                    columns: [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] //':visible'
                }
            }
        ],
        ajax: {
            "url": url_list,
            "type": "GET",
            "data": function() {
                var data;
                if ($('#yourjobs').parent().hasClass('active')) {
                    data = {
                        'option': 'jobs user',
                        'parameters': ['uclv_vmarreros']
                    };
                }
                if ($('#groupjobs').parent().hasClass('active')) {
                    data = {
                        'option': 'jobs group'
                    };
                }
                if ($('#alljobs').parent().hasClass('active')) {
                    data = {
                        'option': 'jobs all'
                    };
                }
                return data;
            },
            /*"beforeSend": function () {
                ___HTML___application___hpc___modal___SHOW_LOAD___();
            },*/
            "dataSrc": function(response) {
                if(response.___BOOLEAN___ERROR___){
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(response);
                    return [];
                }
                else{
                    for (i=0; i<response.data.length; i++ ){
                        tmp = response.data[i][1];
                        response.data[i][1] = response.data[i][4];
                        response.data[i][4] = tmp;
                    }
                    return response.data;
                }

            }

        },
        columnDefs: [
            {
                "render": function ( data/*, type, row*/ ) {
                    return '<span class="label label-' + ___get_label___(data) + '">' + data + '</span>'
                },
                "targets": 1
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

    $('#datatable-buttons_length').addClass('col-sm-6').css('padding', '0');
    $('#datatable-buttons_filter').addClass('col-sm-6').css('padding', '0');
    $('#center___content').css('display', 'block');
    var $datatable = $('#datatable-buttons');
    $datatable.find('tbody').on('click', 'td:first-child', function () {
        var tr = $(this).closest('tr');
        if (tr.hasClass('parent')){
            var datatable = $datatable.DataTable();
            var row = datatable.row(tr).index();
            var id = datatable.cell(row, 0).data();
            ___HTML___application___hpc___job___detail___(row, id);
        }
    });
    $datatable.find('tbody').on('click', '.panel-heading button:nth-child(1)', function () {
        console.log('click en mi!');
    });
    $datatable.find('tbody').on('click', '.panel-heading button:nth-child(2)', function () {
        var tr = $(this).closest('tr').prev();
        var datatable = $datatable.DataTable();
        var row = datatable.row(tr).index();
        var id = datatable.cell(row, 0).data();
        stopJob(row, id);
    });
    $datatable.find('tbody').on('click', '.panel-heading button:nth-child(3)', function () {
        console.log('click en mi!!!');
    });
    $datatable.find('tbody').on('click', '.panel-heading button:nth-child(4)', function () {
        console.log('click en mi!!!!');
    });
});

var ___HTML___application___hpc___job___detail___ = function(row, id){
    $.getJSON(url_detail, {'parameters': [id]}, function(data) {
        var datatable = $('#datatable-buttons').DataTable();
        if(data.___BOOLEAN___ERROR___){
            ___HTML___application___hpc___modal___SHOW_LOAD___();
            ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
            var text = $(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___).find('.alert___message___text').text();
            datatable.cell(row, 9).data(text).page(datatable.page()).draw('page');
        }
        else {
            datatable.cell(row, 9).data(data.detail).page(datatable.page()).draw('page');
        }
    }).always(function() {
        console.log( "complete" );
    });
};

var ___HTML___application___hpc___job___stop___ = function(row, id){
    $.getJSON(url_stop, {'parameters': [id]}, function(data) {
        var datatable = $('#datatable-buttons').DataTable();
        if(data.___BOOLEAN___ERROR___){
            ___HTML___application___hpc___modal___SHOW_LOAD___();
            ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
            datatable.cell(row, 9).data(text).page(datatable.page()).draw('page');
        }
        else {
            datatable.cell(row, 4).data($(data.detail).find('.panel-heading').find('span'));
            datatable.cell(row, 5).data($(data.detail).find('.panel-body').find('tr:nth-child(8)').find('td:nth-child(2)'));
            datatable.cell(row, 9).data(data.detail).page(datatable.page()).draw('page');
        }
    }).always(function() {
        console.log( "complete" );
    });
};

var ___HTML___application___hpc___job___continue___ = function(row, id){

};

var ___HTML___application___hpc___job___requeue___ = function(row, id){

};

var ___HTML___application___hpc___job___kill___ = function(row, id){

};

function ___get_label___(state){
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
    if(state==='COMPLETE')
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