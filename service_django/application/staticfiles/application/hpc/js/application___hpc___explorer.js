var hpc_explorer_init = function(){
    const
        $hpc__content__center = $('#application___hpc___content___center'),
        $hpc__modal =  $('#application___hpc___modal'),

        $hpc__tbody =  $hpc__content__center.find('#explorer___content').find('#tableFileSystem').find('tbody'),
        $hpc__pwd = $hpc__content__center.find('#explorer___content').find('#printWorkingDirectory'),
        $hpc__buttons = $hpc__content__center.find('#explorer___content').find('#actionsFileSystem'),
        $hpc__buttons__header = $hpc__content__center.find('#center___header').find('#actionsInHeader');
    var cp = false,
        cp_array = [];

    function getCookie(c_name) {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

    var hpc__module__explorer__button__disabled__all = function(){
        $hpc__buttons.find('a').each(function(){
            $(this).attr('disabled', 'disabled');
        });
        $hpc__buttons__header.find('a').each(function (){
            $(this).attr('disabled', 'disabled');
        });
    };

    var hpc__module__explorer__button__disabled = function(){
        $hpc__buttons__header.find('a').each(function (){
            $(this).removeAttr('disabled');
        });
        var i = 0, count = 0, d = false, f = false;
        $hpc__tbody.find('tr').each(function(){
            if($(this).hasClass('primary')) {
                i++;
                if ($(this).hasClass('directory'))
                    d = true;
                if ($(this).hasClass('file'))
                    f = true;
            }
            count++;
        });
        var $actions = $hpc__buttons.find('a');
        $actions.each(function(){
            $(this).attr('disabled', 'disabled');
        });
        if(path !== home)
            $actions.eq(0).removeAttr('disabled');
        if(i === 1) {
            $actions.eq(3).removeAttr('disabled');
            $actions.eq(4).removeAttr('disabled');
            if (d)
                $actions.eq(1).removeAttr('disabled');
            if (f) {
                $actions.eq(2).removeAttr('disabled');
                $actions.eq(9).removeAttr('disabled');

            }
        }
        if(i > 0){
            $actions.eq(5).removeAttr('disabled');
            $actions.eq(8).removeAttr('disabled');
        }
        if(cp)
            $actions.eq(6).removeAttr('disabled');
        if(i === count)
            $actions.eq(7).removeClass('select-all').removeAttr('disabled').find('span').eq(3).text(' unSelect All');
        else
            $actions.eq(7).addClass('select-all').removeAttr('disabled').find('span').eq(3).text(' Select All');
    };

    var hpc__module__explorer__list = function(){
        hpc__module__explorer__button__disabled__all();
        $.getJSON(url_list, {'path': path}, function(data) {
            if(data.___BOOLEAN___ERROR___){
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                var text = $(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___).find('.alert___message___text').text();
            }
            else {
                $hpc__tbody.html(data.list);
                $hpc__pwd.find('strong').text(path);
                hpc__module__explorer__button__disabled();
            }
        }).always(function() {});
    };

    hpc__module__explorer__list();

    var hpc__module__explorer__tr__dblclick = function (event) {
        if($(this).hasClass('directory')) {
            path = path + '/' + $(this).attr('data-name');
            $hpc__tbody.html('<tr><td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td></tr>');
            hpc__module__explorer__list();
        }
    };

    var hpc__module__explorer__table__tr__active = function (event) {
        if(event.ctrlKey) {
            if ($(this).hasClass('primary'))
                $(this).removeClass('primary');
            else
                $(this).addClass('primary');
        }
        else{
            $(this).parent().find('tr').each(function(){
                $(this).removeClass('primary');
            });
            $(this).addClass('primary');
        }
        hpc__module__explorer__button__disabled();
    };

    var hpc__module__explorer__modal__generic = function(btn){
        var $btn =$(this);
        if($btn.attr('disabled'))
            return;
        var option = $btn.attr('data-option');
        var data = {
            option: option,
            path: path
        };
        if($btn.attr('data-option') === 'edit') {
            data.file_name = $hpc__tbody.find('tr.primary').attr('data-name');
        }
        $.ajax({
            url: $btn.attr('data-url'),
            type: 'GET',
            data: data,
            dataType: 'json',
            beforeSend: function () {
                ___HTML___application___hpc___modal___SHOW_LOAD___();
            },
            success: function (data) {
                if (data.___BOOLEAN___ERROR___) {
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                }
                else {
                    $hpc__modal.html(data.___HTML___APPLICATION___HPC___MODAL___);
                    $hpc__modal.find('.modal___message').html(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___);
                    if(option === 'goto')
                        $hpc__modal.find('.modal___form').find('span').text(home);
                    ___HTML___application___hpc___modal___EVENTS_ON___();
                }
            }
        });
    };

    var hpc__module__explorer__button__click__not__modal = function(event) {
        if($(this).attr('disabled')!=='disabled'){
            $(this).attr('disabled', 'disabled');
            var index = Array.prototype.indexOf.call(this.parentNode.children, this);
            if(index === 0){
                var tmp = path.split('/');
                if(tmp.length)
                    tmp.pop();
                path = tmp.join('/');
                $hpc__tbody.html('<tr><td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td></tr>');
                hpc__module__explorer__list();
            }
            if(index === 1){
                path += '/' + $hpc__tbody.find('tr.primary').attr('data-name');
                $hpc__tbody.html('<tr><td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td></tr>');
                hpc__module__explorer__list();
            }
            if(index === 4){
                var name = $hpc__tbody.find('tr.primary').attr('data-name');
                $.ajax({
                    url: $(this).attr('data-url'),
                    method: 'GET',
                    data: {
                        path: path,
                        name: name
                    },
                    xhrFields: {
                        responseType: 'blob'
                    },
                    success: function (data) {
                        var a = document.createElement('a');
                        var url = window.URL.createObjectURL(data);
                        a.href = url;
                        a.download = name;
                        a.click();
                        window.URL.revokeObjectURL(url);
                    }
                });
                /*
                var name = $hpc__tbody.find('tr.primary').attr('data-name');
                var link = document.createElement('a');
                link.download = name;
                link.href = $(this).attr('data-url') + '?path=' + path + '&name=' + name;
                document.body.appendChild(link);
                link.click();*/
            }
            if(index === 7){
                var tr = $hpc__tbody.find('tr');
                if($(this).hasClass('select-all'))
                    tr.each(function(){
                        $(this).addClass('primary');
                    });
                else
                    tr.each(function(){
                        $(this).removeClass('primary');
                    });
                hpc__module__explorer__button__disabled();
            }
        }
    };

    var hpc__module__explorer__modal__upload__validation = function() {
        var $hpc__modal__body = $hpc__modal.find('.modal-body'),
            $hpc__modal__footer = $hpc__modal.find('.modal-footer');
        var files = $hpc__modal__body.find('#files').get(0).files,
            $input = $hpc__modal__body.find('#files_selected');
        if (files.length > 1) $input.val(files.length + ' archivos seleccionados');
        if (files.length === 1) $input.val('Un archivo seleccionado: '+files[0].name);
        if (files.length === 0) $input.val('');
        var i = 0,
            error = false;
        if (files.length > 0 && files.length < 11){
            for(i; i<files.length; i++) {
                if (files[i].size > 1024 * 1024 * 40) {
                    error = true;
                    $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> &OpenCurlyDoubleQuote;Los archivos no deben exceder los 40mb.&CloseCurlyDoubleQuote;');
                    break;
                }
                console.log(files[i]);
                for (var j = 0; j < files[i].name.length; j++) {
                    if (files[i].name[j] === '\\'){
                        error = true;
                        $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> &OpenCurlyDoubleQuote;El caracter <b>\\</b> no puede estar contenido en el nombre de los archivos.&CloseCurlyDoubleQuote;');
                        break;
                    }
                }
                if (j !== files[i].name.length)
                    break;
            }
            if(i === files.length){
                error = false;
                $hpc__modal__body.find('.help-block').html('');
            }
        }
        else{
            error = true;
            $hpc__modal__footer.find('button.btn-primary').attr('disabled', 'disabled');
            if(files.length === 0)
                $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> &OpenCurlyDoubleQuote;Seleccione al menos un archivo.&CloseCurlyDoubleQuote;');
            else
                $hpc__modal__body.find('.help-block').html('<span class="fa fa-exclamation-circle fa-fw"></span> &OpenCurlyDoubleQuote;No puede subir más de 10 archivos simultaneamente.&CloseCurlyDoubleQuote;');
        }
        var elem = $hpc__modal__body.find('.btn');
        var formGroup = $hpc__modal__body.find('.form-group');
        if (error) {
            $hpc__modal__footer.find('button').eq(0).attr('disabled', 'disabled');
            if (elem.hasClass('btn-default')) elem.removeClass('btn-default').addClass('btn-danger');
            if (!formGroup.hasClass('has-error')) formGroup.addClass('has-error')
        }
        else {
            $hpc__modal__footer.find('button').eq(0).removeAttr('disabled');
            if (elem.hasClass('btn-danger')) elem.removeClass('btn-danger').addClass('btn-default');
            if (formGroup.hasClass('has-error')) formGroup.removeClass('has-error')
        }
    };

    var hpc__module__explorer__modal__submit__edit = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        formData.append('file_name', $hpc__tbody.find('tr.primary').attr('data-name'));
        $.ajax({
            url: $form.attr('action') + '?save=',
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $form.find('.modal-header').append('' +
                    '<div style="position: absolute; top: 16px; right: 60px">' +
                    '   <span class="fa fa-spinner fa-pulse"></span> Guardando...' +
                    '</div>'
                );
            },
            success: function (data) {
                var $div = $form.find('.modal-header').find('div');
                if (data.___BOOLEAN___ERROR___) {
                    $div.html('<span class="fa fa-warning fa-fw"></span> Error en servidor');
                }
                else {
                    $btn.attr('disabled', 'disabled');
                    $div.html('<span class="fa fa-check-circle fa-fw"></span> Guardado');
                }
                setTimeout(function(){
                    $div.remove();
                }, 4000);
            }
        });
    };

    var hpc__module__explorer__modal__submit__upload = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        $.ajax({
            url: $form.attr('action') + '?upload=',
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__module__explorer__button__disabled__all();
                ___HTML___application___hpc___modal___ACTION_CLOSE___();
            },
            success: function (data) {
                if(data.___BOOLEAN___ERROR___){
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    var text = $(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___).find('.alert___message___text').text();
                }
                else {
                    $hpc__tbody.html(data.list);
                    $hpc__pwd.find('strong').text(path);
                    hpc__module__explorer__button__disabled();
                }
            }
        });
    };

    var hpc__module__explorer__modal__submit__generic = function(evt){
        evt.preventDefault();
        var $form = $(this);
        var $btn =$form.find('.modal-footer').find('button').eq(0);
        if($btn.attr('disabled'))
            return;
        var formData = new FormData(this);
        formData.append('path', path);
        formData.append('option', $form.attr('data-option'));
        if ($(this).attr('data-option')==='rename')
            formData.append('name', $hpc__tbody.find('tr.primary').attr('data-name'));
        $.ajax({
            url: $form.attr('action') + '?' + $form.attr('data-option') + '=',
            data: formData,
            type: $form.attr('method'),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__module__explorer__button__disabled__all();
            },
            success: function (data) {
                if(data.___BOOLEAN___ERROR___){
                    ___HTML___application___hpc___modal___SHOW_LOAD___();
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    var text = $(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___).find('.alert___message___text').text();
                }
                else {
                    $hpc__tbody.html(data.list);
                    $hpc__pwd.find('strong').text(path);
                    hpc__module__explorer__button__disabled();
                }
            }
        });
    };

    var hpc__module__explorer__modal__click__goto = function(){
        var dir = $hpc__modal.find('#modal-goto').find('input[name=goto]').val();
        path = '/' + path.split('/')[1] + '/' + path.split('/')[2] + '/' + path.split('/')[3];
        if (dir)
            path += '/' + $hpc__modal.find('#modal-goto').find('input[name=goto]').val();
        hpc__module__explorer__list();
        hpc__module__explorer__button__disabled();
    };

    var hpc__module__explorer__modal__click__delete = function() {
        var $btn = $('#modal-delete').find('.modal-footer').find('button').eq(0);
        var values = [path];
        $.each($hpc__tbody.find('tr.primary'), function(index, elem){
            values.push($(elem).attr('data-name'));
        });
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
        $.ajax({
            url: $btn.attr('data-url'),
            data: {
                'values': values
            },
            type: 'post',
            dataType: 'json',
            cache: false,
            beforeSend: function () {
                $hpc__tbody.html('' +
                    '<tr>' +
                        '<td colspan="3"><span class="fa fa-spinner fa-pulse"></span> Cargando...</td>' +
                    '</tr>'
                );
                hpc__module__explorer__button__disabled__all();
                ___HTML___application___hpc___modal___ACTION_CLOSE___();
            },
            success: function (data) {
                if(data.___BOOLEAN___ERROR___){
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                    var text = $(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___).find('.alert___message___text').text();
                }
                else {
                    $hpc__tbody.html(data.list);
                    $hpc__pwd.find('strong').text(path);
                    hpc__module__explorer__button__disabled();
                }
            }
        });
    };

    var hpc__module__explorer__modal__execute = function() {
        var $btn =$(this);
        if($btn.attr('disabled'))
            return;
        var data = {
            path: path,
            file: $hpc__tbody.find('tr.primary').attr('data-name')
        };
        $.ajax({
            url: $btn.attr('data-url'),
            type: 'GET',
            data: data,
            dataType: 'json',
            beforeSend: function () {
                ___HTML___application___hpc___modal___SHOW_LOAD___();
            },
            success: function (data) {
                if (data.___BOOLEAN___ERROR___) {
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                }
                else {
                    $hpc__modal.html(data.___HTML___APPLICATION___HPC___MODAL___);
                    $hpc__modal.find('.modal___message').html(data.___HTML___APPLICATION___HPC___MODAL___MESSAGE___);
                    ___HTML___application___hpc___modal___EVENTS_ON___();
                }
            }
        });

    };

    var hpc__module__explorer__modal__click__execute = function () {
        var url = $('#modal-execute').find('.modal-footer').find('button').eq(0).attr('data-url');
        var values = [path, $hpc__tbody.find('tr.primary').attr('data-name')];
        $.ajax({
            url: url,
            data: {
                'values': values
            },
            type: 'post',
            dataType: 'json',
            cache: false,
            beforeSend: function () {
                ___HTML___application___hpc___modal___ACTION_CLOSE___();
            },
            success: function (data) {
                ___HTML___application___hpc___modal___SHOW_LOAD___();
                if(data.___BOOLEAN___ERROR___){
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_ERROR___(data);
                }
                else {
                    ___HTML___application___hpc___modal___SHOW_MESSAGE_OK___(data);
                }
            }
        });
    };

    $hpc__tbody
        .on('click', 'tr', hpc__module__explorer__table__tr__active)
        .on('dblclick', 'tr', hpc__module__explorer__tr__dblclick);

    $hpc__buttons
        .on('click', 'a.not-modal', hpc__module__explorer__button__click__not__modal)
        .on('click', 'a.has-modal', hpc__module__explorer__modal__generic)
        .on('click', 'a.btn-execute', hpc__module__explorer__modal__execute);

    $hpc__buttons__header
        .on('click', 'a.has-modal', hpc__module__explorer__modal__generic);

    $hpc__modal
        .on('change', '#files', hpc__module__explorer__modal__upload__validation)
        .on('submit', '.hpc___modal___submit___edit', hpc__module__explorer__modal__submit__edit)
        .on('click', '.hpc___modal___click___goto', hpc__module__explorer__modal__click__goto)
        .on('click', '.hpc___modal___click___delete', hpc__module__explorer__modal__click__delete)
        .on('click', '.hpc___modal___click___execute', hpc__module__explorer__modal__click__execute)
        .on('submit', '.hpc___modal___submit___upload', hpc__module__explorer__modal__submit__upload)
        .on('submit', '.hpc___modal___submit___generic', hpc__module__explorer__modal__submit__generic);

    var eblur = function(){
        $(this).siblings().eq(0).removeClass('border-shadow');
    };
    var efocus = function(){
        $(this).siblings().eq(0).addClass('border-shadow');
    };
    $hpc__modal
        .on('blur', '#modal-goto input[name=goto]', eblur)
        .on('focus', '#modal-goto input[name=goto]', efocus);

    var ekeyup = function(){
        var $btn = $hpc__modal.find('.modal-footer').find('button').eq(0);
        // var expreg = new RegExp('.*(/|\\\\).*');
        var expreg = new RegExp('.*/.*');
        if($(this).val().length>0){
            if(expreg.test($(this).val()))
                $btn.attr('disabled', 'disabled');
            else
                $btn.removeAttr('disabled');
        }else
            if(!$btn.attr('disabled'))
                $btn.attr('disabled', 'disabled');
    };
    $hpc__modal
        .on('keyup', '#modal-file #id_generic', ekeyup)
        .on('keyup', '#modal-folder #id_generic', ekeyup)
        .on('keyup', '#modal-rename #id_generic', ekeyup)
};