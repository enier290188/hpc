function capitalize(s){
    return s.toLowerCase().replace(/\b./g, function(a){
        return a.toUpperCase();
    });
}

function ___data_background___(state){
    if(state==='PENDING')
        return "red";
    if(state==='RUNNING')
        return "blue";
    if(state==='SUSPENDED')
        return "darker";
    if(state==='CANCELLED')
        return "orange";
    if(state==='COMPLETING')
        return "purple";
    if(state==='COMPLETED')
        return "green";
    if(state==='FAILED')
        return "red";
    if(state==='TIMEOUT')
        return "red";
    if(state==='NODE_FAIL')
        return "red";
    return "";
}

var hpc_jobs_datatable_init = function(){
    var $datatable = $('#datatable-jobs');
    var optionsDataTable = {
        dom: "Blfrtip",
        buttons: [
            {
                extend: "pdf",
                text: "pdf",
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
            url: $datatable.attr('data-url-list'),
            type: "GET",
            data: function() {
                return {
                    'option': 'jobs all'
                }
            },
            dataSrc: function(response) {
                if(response['___BOOLEAN___ERROR___']){
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(response);
                    return [];
                }
                else {
                    for (var i=0; i<response.data.length; i++ ) {
                        if(response.data[i][2].length > 15)
                            response.data[i][2] = response.data[i][2].slice(0,14)+'...';
                        if(response.data[i][3].length > 15)
                            response.data[i][3] = response.data[i][3].slice(0,14)+'...';
                        response.data[i][6] = capitalize(response.data[i][6])
                    }
                    return response.data;
                }

            }

        },
        columnDefs: [
            {
                "render": function ( data/*, type, row*/ ) {
                    return '<span class="label" data-background-color="'+___data_background___(data)+'">' + data + '</span>'
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
        aoColumns: [
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
        lengthMenu: [[10, 50, -1], [10, 50, "All"]],
        language:{
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
        },
        sPaginationType: 'numbers'
    };
    $datatable.DataTable(optionsDataTable);
    $('#datatable-jobs_length').addClass('col-sm-6').css('padding', '0');
    $('#datatable-jobs_filter').addClass('col-sm-6').css('padding', '0');
};

var hpc_jobs_datatable_detail = function() {
    var $datatable = $('#datatable-jobs');
    var tr = $(this).closest('tr');
    if (tr.hasClass('parent')) {
        var datatable = $datatable.DataTable();
        var row = datatable.row(tr).index();
        $.getJSON($datatable.attr('data-url-detail'), {'parameters': [datatable.cell(row, 0).data()]}, function (data) {
            if (data['___BOOLEAN___ERROR___']) {
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                var text = $(data['___HTML___APPLICATION___HPC___MODAL___MESSAGE___']).find('.alert___message___text').text();
                datatable.cell(row, 9).data(text).page(datatable.page()).draw('page');
            }
            else {
                datatable.cell(row, 9).data(data.detail).page(datatable.page()).draw('page');
            }
        }).always(function () {
        });
    }
};

var hpc_jobs_datatable_actionJob = function(){
    var datatable = $('#datatable-jobs').DataTable();
    var tr = $(this).closest('tr').prev();
    var row = datatable.row(tr).index();
    $.ajax({
        url: $(this).attr('data-url'),
        data: {
            'option': $(this).attr('data-option'),
            'jobID': datatable.cell(row, 0).data()
        },
        type: 'post',
        dataType: "json",
        cache: false,
        beforeSend: function () {

        },
        success: function (data) {
            if(data['___BOOLEAN___ERROR___']){
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                datatable.cell(row, 9).data(text).page(datatable.page()).draw('page');
            }
            else {
                datatable.cell(row, 1).data($(data.detail).find('.panel-heading').find('span').text());
                datatable.cell(row, 9).data(data.detail).page(datatable.page()).draw('page');
            }
        }
    });
};

$('#application___hpc___content___center')
    .on('click', '#datatable-jobs tbody td:first-child', hpc_jobs_datatable_detail)
    .on('click', '.panel-heading button:nth-child(1)', hpc_jobs_datatable_actionJob)
    .on('click', '.panel-heading button:nth-child(2)', hpc_jobs_datatable_actionJob)
    .on('click', '.panel-heading button:nth-child(3)', hpc_jobs_datatable_actionJob)
    .on('click', '.panel-heading button:nth-child(4)', hpc_jobs_datatable_actionJob);
