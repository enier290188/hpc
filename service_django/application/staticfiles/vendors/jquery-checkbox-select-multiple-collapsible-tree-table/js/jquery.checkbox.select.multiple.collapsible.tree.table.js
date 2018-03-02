/*
 * Checkbox Select Multiple Collapsible Tree Table plugin for jQuery v.1.0.0
 * Copyright 2017 Enier Ramos Garcia
 * Licensed under the MIT license
 */

(function ($) {

    $.fn.jquerycheckboxselectmultiplecollapsibletreetable = function (method) {
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        }
        else {
            if (typeof method === "object" || !method) {
                return _initTree.apply(this, arguments);
            }
            else {
                $.error("Method with name " + method + " does not exists for JQuery Checkbox Select Multiple Collapsible Tree Table");
            }
        }
    };

    $.fn.jquerycheckboxselectmultiplecollapsibletreetable.defaults = {
        source: null, //Function(id, complete)|Url Result should be in add() function format. For Url "json" format is used.
        enableMove: false, //Boolean To let user move nodes set it in true.
        moveDistance: 1, //Integer Tolerance, in pixels, for when moving should start. If specified, moving will not start until after mouse is dragged beyond distance.
        moveHandle: false, //Selector|Element Restricts moving start click to the specified element.
        onExpand: function () {
            return true;
        }, //Function() Calling when node expands. Return false if you dont want the node been expanded.
        onCollapse: function () {
            return true;
        }, //Function() Calling when node collapses. Return false if you dont want the node been collapsed.
    };

    // PUBLIC FUNCTIONS
    // ================

    var methods = {
        option: function (optionName, value) {
            var settings = this.data("jquerycheckboxselectmultiplecollapsibletreetable-settings");
            if ($.type(optionName) === "string" && value !== undefined) {
                optionName = {optionName: value};
            }
            if ($.isPlainObject(optionName)) {
                settings = $.extend({}, settings, optionName);
                return this.data("jquerycheckboxselectmultiplecollapsibletreetable-settings", settings);
            }
            if ($.type(optionName) === "string") {
                return settings[optionName];
            }
            return settings;
        },
        getId: function () {
            return _getId(this);
        },
        getParentId: function () {
            return _getParentId(this);
        },
        getDepth: function () {
            return this.data("jquerycheckboxselectmultiplecollapsibletreetable-depth");
        },
        toggle: function () {
            return this.each(function () {
                var $this = $(this);
                if (_isExpanded($this)) {
                    methods.collapse.call($this);
                }
                else {
                    if (_isCollapsed($this)) {
                        methods.expand.call($this);
                    }
                }
            });
        },
        expand: function () {
            var changed = false;
            //process elements
            this.each(function () {
                var $this = $(this);
                //collapsed?
                if (!_isCollapsed($this)) {
                    return;
                }
                //loaded?
                if (!$this.data("loaded") && !_load($this)) {
                    return;
                }
                //expand
                _expand($this);
                changed = true;
            });
            return this;
        },
        collapse: function () {
            var changed = false;
            //process elements
            this.each(function () {
                var $this = $(this);
                //expanded?
                if (!_isExpanded($this)) {
                    return;
                }
                //collapse
                _collapse($this);
                changed = true;
            });
            return this;
        },
        getRoots: function () {
            var items = [];
            this.find(">tbody>tr").each(function () {
                if (_getParentId($(this)) === null) {
                    items.push(this);
                }
            });
            return $(items);
        },
        getChildNodes: function () {
            var items = $();
            this.each(function () {
                items = items.add(_getChildNodes($(this)));
            });
            return items;
        },
        getBranch: function () {
            var items = $();
            this.each(function () {
                items = items.add(_getBranch($(this)));
            });
            return items;
        },
        getParent: function () {
            var items = $();
            this.each(function () {
                items = items.add(_getParent($(this)));
            });
            return items;
        },
        isCollapsed: function () {
            var result = false;
            this.each(function () {
                result = _isCollapsed($(this));
                if (result) {
                    return false;
                }
            });
            return result;
        },
        isExpanded: function () {
            var result = false;
            this.each(function () {
                result = _isExpanded($(this));
                if (result) {
                    return false;
                }
            });
            return result;
        }
    };

    // PRIVATE FUNCTIONS
    // =================

    function _initTree(options) {
        //settings
        var $this = $(this), settings = $.extend({}, $.fn.jquerycheckboxselectmultiplecollapsibletreetable.defaults, options);
        //process elements
        return $this.each(function () {
            var $this = $(this);
            //settings
            $this.data("jquerycheckboxselectmultiplecollapsibletreetable-settings", settings);
            //event handlers
            $this
                .off("click", ">tbody>tr>td.jquerycheckboxselectmultiplecollapsibletreetable-sortable>.jquerycheckboxselectmultiplecollapsibletreetable-container>.jquerycheckboxselectmultiplecollapsibletreetable-expander")
                .on("click", ">tbody>tr>td.jquerycheckboxselectmultiplecollapsibletreetable-sortable>.jquerycheckboxselectmultiplecollapsibletreetable-container>.jquerycheckboxselectmultiplecollapsibletreetable-expander", _expanderClick);
            //init nodes
            _initNode(methods.getRoots.call($this), 1);
            //It is neccesary to do before to init nodes
            //checkbox checked or unchecked
            $("#" + $this.parent().attr("id") + " > table.table > tbody > tr > td.jquerycheckboxselectmultiplecollapsibletreetable-sortable label")
                .off("click", "input[type='checkbox']")
                .on("click", "input[type='checkbox']", _checkboxCheckedUnchecked);
        });
    }


    function _expand($this) {
        //event callback
        var settings = $this.closest("table").data("jquerycheckboxselectmultiplecollapsibletreetable-settings");
        if (!settings.onExpand.call($this)) {
            return;
        }
        //node class
        $this.addClass("expanded");
        //expander class
        $this
            .find(">td.jquerycheckboxselectmultiplecollapsibletreetable-sortable>.jquerycheckboxselectmultiplecollapsibletreetable-container>.jquerycheckboxselectmultiplecollapsibletreetable-expander")
            .removeClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-collapsed")
            .addClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-expanded");
        //render items
        _getBranch($this).not($this).each(function () {
            var $this = $(this);
            if (_parentCollapsed($this)) {
                $this.hide();
            }
            else {
                $this.show();
            }
        });
    }

    function _collapse($this) {
        //event callback
        var settings = $this.closest("table").data("jquerycheckboxselectmultiplecollapsibletreetable-settings");
        if (!settings.onCollapse.call($this)) {
            return;
        }
        //node class
        $this.removeClass("expanded");
        //expander class
        $this
            .find(">td.jquerycheckboxselectmultiplecollapsibletreetable-sortable>.jquerycheckboxselectmultiplecollapsibletreetable-container>.jquerycheckboxselectmultiplecollapsibletreetable-expander")
            .removeClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-expanded")
            .addClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-collapsed");
        //hide items
        _getBranch($this).not($this).hide();
    }

    function _getParent($this) {
        return $this.parent().find(">.jquerycheckboxselectmultiplecollapsibletreetable-" + _getParentId($this));
    }

    function _getChildNodes($this) {
        return $this.parent().find(">.jquerycheckboxselectmultiplecollapsibletreetable-parent-" + _getId($this));
    }

    function _getBranch($this) {
        var items = $this;
        if ($this.prop("tagName") !== "TR") {
            return items.not($this);
        }
        _getChildNodes($this).each(function () {
            items = items.add(_getBranch($(this)));
        });
        return items;
    }

    function _getId($this) {
        var template = /jquerycheckboxselectmultiplecollapsibletreetable-([A-Fa-f0-9_]+)/;
        if (template.test($this.attr("class"))) {
            return template.exec($this.attr("class"))[1];
        }
        return null;
    }

    function _getParentId($this) {
        var template = /jquerycheckboxselectmultiplecollapsibletreetable-parent-([A-Fa-f0-9_]+)/;
        if (template.test($this.attr("class"))) {
            return template.exec($this.attr("class"))[1];
        }
        return null;
    }

    function _isCollapsed($this) {
        return $this.data("count") && !$this.hasClass("expanded");
    }

    function _isExpanded($this) {
        return $this.data("count") && $this.hasClass("expanded");
    }

    function _initNode($this, depth, forceExpand) {
        if (depth === undefined) {
            depth = 1;
        }
        $this.each(function () {
            var $this = $(this).data("jquerycheckboxselectmultiplecollapsibletreetable-depth", depth);
            //child nodes
            var $child = _getChildNodes($this);
            //child count
            var count = $child.length;
            if ($this.data("count") === undefined || $this.data("loaded") || $this.data("count") == count) {
                if (!$this.data("loadNeeded")) {
                    $this.data({
                        loaded: true,
                        count: count
                    });
                    if (count && forceExpand) {
                        $this.addClass("expanded");
                    }
                }
            }
            else {
                $this.data("loadNeeded", true);
            }
            //container
            var $td = $this.find(">td.jquerycheckboxselectmultiplecollapsibletreetable-sortable"), $container = $td.find(">.jquerycheckboxselectmultiplecollapsibletreetable-container");
            if ($container.length === 0) {
                $container = $("<div class='jquerycheckboxselectmultiplecollapsibletreetable-container'>").html($td.html());
                $td.html("").append($container);
            }
            //expander
            $container.find(".jquerycheckboxselectmultiplecollapsibletreetable-expander").remove();
            var $expander = $("<span class='jquerycheckboxselectmultiplecollapsibletreetable-expander'>").prependTo($container);
            if ($this.data("count")) {
                if ($this.hasClass("expanded")) {
                    $expander.addClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-expanded");
                }
                else {
                    $expander.addClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-collapsed");
                }
            }
            //indent
            $container.css("marginLeft", depth * $expander.width());
            //hide if collapsed
            if (_parentCollapsed($this)) {
                $this.hide();
            }
            //init child nodes
            _initNode($child, depth + 1, forceExpand);
        });
    }

    function _expanderClick() {
        var $this = $(this);
        if ($this.hasClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-expanded") || $this.hasClass("jquerycheckboxselectmultiplecollapsibletreetable-expander-collapsed")) {
            methods.toggle.call($this.closest("tr"));
        }
    }

    function _checkboxCheckedUnchecked() {
        var $tbody = $(this).parent().parent().parent().parent().parent();
        var $tr = $(this).parent().parent().parent().parent();
        var pk = $tr.jquerycheckboxselectmultiplecollapsibletreetable("getId");
        var parent = $tr.jquerycheckboxselectmultiplecollapsibletreetable("getParentId");
        //
        if ($(this).attr("checked")) {
            // no checked
            $(this).attr("checked", false);
            //
            var branchLength = $tr.jquerycheckboxselectmultiplecollapsibletreetable("getBranch").length;
            if (branchLength > 0) {
                var trIsFound = false;
                $($tbody.find("tr")).each(function (index, element) {
                    var pkTemporalCurrent = $(element).jquerycheckboxselectmultiplecollapsibletreetable("getId");
                    var parentTemporalCurrent = $(element).jquerycheckboxselectmultiplecollapsibletreetable("getParentId");
                    //
                    if (trIsFound == false) {
                        if (pk == pkTemporalCurrent) {
                            trIsFound = true;
                        }
                        else {
                            return true; //continue the loop
                        }
                    }
                    if (trIsFound == true) {
                        var elementCheckbox = $(element).find("input[type='checkbox']");
                        $(elementCheckbox).attr("checked", false);
                        $(elementCheckbox).prop("checked", false);
                        branchLength -= 1;
                        if (branchLength == 0) {
                            return false; //break the loop
                        }
                    }
                });
            }
        }
        else {
            // checked
            $(this).attr("checked", true);
            //
            if (parent != null) {
                var trIsFound = false;
                var pkTemporal = pk;
                var parentTemporal = parent;
                $($($tbody.find("tr")).get().reverse()).each(function (index, element) {
                    var pkTemporalCurrent = $(element).jquerycheckboxselectmultiplecollapsibletreetable("getId");
                    var parentTemporalCurrent = $(element).jquerycheckboxselectmultiplecollapsibletreetable("getParentId");
                    //
                    if (trIsFound == false) {
                        if (pk == pkTemporalCurrent) {
                            trIsFound = true;
                        }
                        else {
                            return true; //continue the loop
                        }
                    }
                    if (trIsFound == true) {
                        if (parentTemporal == pkTemporalCurrent) {
                            var elementCheckbox = $(element).find("input[type='checkbox']");
                            $(elementCheckbox).attr("checked", true);
                            $(elementCheckbox).prop("checked", true);
                            if (parentTemporalCurrent == null) {
                                return false; //break the loop
                            }
                            pkTemporal = pkTemporalCurrent;
                            parentTemporal = parentTemporalCurrent;
                        }
                    }
                });
            }
        }
    }

    function _parentCollapsed($this) {
        if (_getParentId($this) === null) {
            return false;
        }
        var $parent = _getParent($this);
        if (_isCollapsed($parent)) {
            return true;
        }
        return _parentCollapsed($parent);
    }

    function _load($this) {
        var settings = $this.closest("table").data("jquerycheckboxselectmultiplecollapsibletreetable-settings");
        _getBranch($this).not($this).remove();
        //function
        if ($.isFunction(settings.source) && !$this.hasClass("loading")) {
            $this.addClass("loading");
            settings.source.call($this, _getId($this), function (items) {
                $this.removeData("loadNeeded").data("loaded", true);
                _add($this, items);
                $this.removeClass("loading");
                methods.expand.call($this);
            });
        }
        //url
        if ($.type(settings.source) === "string" && !$this.hasClass("loading")) {
            $this.addClass("loading");
            $.post(
                settings.source,
                {id: _getId($this)},
                function (items) {
                    $this.removeDate("loadNeeded").data("loaded", true);
                    _add($this, items);
                    $this.removeClass("loading");
                },
                "json"
            );
        }
        return false;
    }

})(jQuery);
