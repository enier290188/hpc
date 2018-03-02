/*
 * Drag Drop Collapsible Tree Table plugin for jQuery v.1.0.0
 * Copyright 2017 Enier Ramos Garcia
 * Licensed under the MIT license
 */

(function ($) {

    $.fn.jquerydragdropcollapsibletreetable = function (method) {
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        }
        else {
            if (typeof method === "object" || !method) {
                return _initTree.apply(this, arguments);
            }
            else {
                $.error("Method with name " + method + " does not exists for JQuery Drag Drop Collapsible Tree Table");
            }
        }
    };

    $.fn.jquerydragdropcollapsibletreetable.defaults = {
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
        onAdd: function () {
        }, //Function(items) Calling when nodes was added. Returns jQuery container that contains all added nodes.
        onMoveStart: function () {
        }, //Function(item, helper) This event is triggered when node moving starts.
        onMoveStop: function () {
        }, //Function(item, helper) This event is triggered when node moving ends.
        onMoveOver: function () {
            return true;
        }, //Function(item, helper, target, position) This event is triggered when node moving over another node that support droping. If you dont want target supporting dropping, return false.
        onMoveOut: function () {
        }, //Function(item, helper, target) This event is triggered when node outs another node that support droping.
        onMove: function () {
            return true;
        }, //Function(item, target, position) This event is triggered when node drops to another node. If you want to prevent moving, return false.
        onMoveEnd: function () {
        } //Function(item) This event is triggered when node drops to another node finish.
    };

    // PUBLIC FUNCTIONS
    // ================

    var methods = {
        option: function (optionName, value) {
            var settings = this.data("jquerydragdropcollapsibletreetable-settings");
            if ($.type(optionName) === "string" && value !== undefined) {
                optionName = {optionName: value};
            }
            if ($.isPlainObject(optionName)) {
                settings = $.extend({}, settings, optionName);
                return this.data("jquerydragdropcollapsibletreetable-settings", settings);
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
            return this.data("jquerydragdropcollapsibletreetable-depth");
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

            //remake drop map if dragging
            if (isDragging) _makeDropMap();

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
            //remake drop map if dragging
            if (isDragging) {
                _makeDropMap();
            }
            return this;
        },
        add: function (items) {
            //tr[]
            //process elements
            this.each(function () {
                _add($(this), items)
            });
            //remake drop map if dragging
            if (isDragging) {
                _makeDropMap();
            }
            return this;
        },
        remove: function () {
            //process elements
            this.each(function () {
                var $this = $(this), $parent = _getParent($this);
                _getBranch($this).remove();
                _initNode($parent, $parent.data("jquerydragdropcollapsibletreetable-depth"));
            });
            //remake drop map if dragging
            if (isDragging) {
                _makeDropMap();
            }
            return this;
        },
        move: function (target, position) {
            var $tr, id, $branch, $oldParent = _getParent(this);
            //branch to move
            $branch = _getBranch(this);
            //node insert before or after
            if (position == 0) {
                $tr = target;
            }
            else {
                $tr = _getBranch(target).not($branch).last();
            }
            //parent id
            id = position === 1 ? _getId(target) : _getParentId(target);
            this.removeClass("jquerydragdropcollapsibletreetable-parent-" + _getParentId(this));
            if (id !== null) {
                this.addClass("jquerydragdropcollapsibletreetable-parent-" + id);
            }
            //moving
            if ($tr.length) {
                if (position == 0) {
                    $branch.insertBefore($tr);
                }
                else {
                    $branch.insertAfter($tr);
                }
            }
            else {
                $branch.prependTo(this.parent());
            }
            //hide if collapsed
            if (_parentCollapsed(this)) {
                $branch.hide();
            }
            //reinit
            if ($oldParent.length) {
                _initNode($oldParent, $oldParent.data("jquerydragdropcollapsibletreetable-depth"));
            }
            var $parent = _getParent(this);
            if ($parent.length) {
                _initNode($parent, $parent.data("jquerydragdropcollapsibletreetable-depth"));
            }
            else {
                _initNode(this);
            }
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
        var $this = $(this), settings = $.extend({}, $.fn.jquerydragdropcollapsibletreetable.defaults, options);
        //process elements
        return $this.each(function () {
            var $this = $(this);
            //settings
            $this.data("jquerydragdropcollapsibletreetable-settings", settings);
            //event handlers
            $this
                .off("click", ">tbody>tr>td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container>.jquerydragdropcollapsibletreetable-expander")
                .off("mousedown", ">tbody>tr>td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container");
            $this
                .on("click", ">tbody>tr>td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container>.jquerydragdropcollapsibletreetable-expander", _expanderClick)
                .on("mousedown", ">tbody>tr>td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container", _nodeMouseDown);
            //init nodes
            _initNode(methods.getRoots.call($this), 1);
        });
    }

    function _expand($this) {
        //event callback
        var settings = $this.closest("table").data("jquerydragdropcollapsibletreetable-settings");
        if (!settings.onExpand.call($this)) {
            return;
        }
        //node class
        $this.addClass("expanded");
        //expander class
        $this
            .find(">td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container>.jquerydragdropcollapsibletreetable-expander")
            .removeClass("jquerydragdropcollapsibletreetable-expander-collapsed")
            .addClass("jquerydragdropcollapsibletreetable-expander-expanded");
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
        var settings = $this.closest("table").data("jquerydragdropcollapsibletreetable-settings");
        if (!settings.onCollapse.call($this)) {
            return;
        }
        //node class
        $this.removeClass("expanded");
        //expander class
        $this
            .find(">td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container>.jquerydragdropcollapsibletreetable-expander")
            .removeClass("jquerydragdropcollapsibletreetable-expander-expanded")
            .addClass("jquerydragdropcollapsibletreetable-expander-collapsed");
        //hide items
        _getBranch($this).not($this).hide();
    }

    function _add($this, items) {
        var $target = _getBranch($this).last().next(), childs = [], parentId = _getId($this);
        //cell count
        var $table = $this, cellCount;
        if ($table.prop("tagName") !== "TABLE") {
            $table = $table.closest("table");
        }
        cellCount = $table.find(">thead>tr,>tbody>tr").first().find(">th,>td").length;
        //adding
        $.each(items, function (i, item) {
            var $tr = $(item);
            //if already exists
            if ($table.find(">tbody>tr.jquerydragdropcollapsibletreetable-" + _getId($tr)).length) {
                return;
            }
            //parent id
            if (parentId !== null) {
                $tr.addClass("jquerydragdropcollapsibletreetable-parent-" + parentId);
            }
            //cell count
            var cnt = $tr.find(">td").length;
            if (cnt < cellCount) {
                for (i = $tr.find(">td").length; i < cellCount; i++) {
                    $tr.append("<td>");
                }
            }
            else {
                if (cnt > cellCount) {
                    $tr.find(">td").eq(cellCount - 1).nextAll().remove();
                }
            }
            //add to dom
            if ($target.length) {
                $tr.insertBefore($target);
            }
            else {
                $table.find(">tbody").append($tr);
            }
            //add to result
            childs.push($tr[0]);
        });
        //childs to jquery
        childs = $(childs);
        //init node with childs
        if (parentId === null) {
            _initNode(childs);
        }
        _initNode($this, $this.data("jquerydragdropcollapsibletreetable-depth"));
        //callbask
        var settings = $this.closest("table").data("jquerydragdropcollapsibletreetable-settings");
        settings.onAdd.call($this, childs);
    }

    function _getParent($this) {
        return $this.parent().find(">.jquerydragdropcollapsibletreetable-" + _getParentId($this));
    }

    function _getChildNodes($this) {
        return $this.parent().find(">.jquerydragdropcollapsibletreetable-parent-" + _getId($this));
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
        var template = /jquerydragdropcollapsibletreetable-([A-Fa-f0-9_]+)/;
        if (template.test($this.attr("class"))) {
            return template.exec($this.attr("class"))[1];
        }
        return null;
    }

    function _getParentId($this) {
        var template = /jquerydragdropcollapsibletreetable-parent-([A-Fa-f0-9_]+)/;
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
            var $this = $(this).data("jquerydragdropcollapsibletreetable-depth", depth);
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
            var $td = $this.find(">td.jquerydragdropcollapsibletreetable-sortable"), $container = $td.find(">.jquerydragdropcollapsibletreetable-container");
            if ($container.length === 0) {
                $container = $("<div class='jquerydragdropcollapsibletreetable-container'>").html($td.html());
                $td.html("").append($container);
            }
            //expander
            $container.find(".jquerydragdropcollapsibletreetable-expander").remove();
            var $expander = $("<span class='jquerydragdropcollapsibletreetable-expander'>").prependTo($container);
            if ($this.data("count")) {
                if ($this.hasClass("expanded")) {
                    $expander.addClass("jquerydragdropcollapsibletreetable-expander-expanded");
                }
                else {
                    $expander.addClass("jquerydragdropcollapsibletreetable-expander-collapsed");
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
        if ($this.hasClass("jquerydragdropcollapsibletreetable-expander-expanded") || $this.hasClass("jquerydragdropcollapsibletreetable-expander-collapsed")) {
            methods.toggle.call($this.closest("tr"));
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
        var settings = $this.closest("table").data("jquerydragdropcollapsibletreetable-settings");
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

    // MOVING FUNCTIONS
    // ================

    //move vars
    var $moveItem = null, $moveHelper = null, $moveOver = null, $indicator, downX, downY, offX, offY, isDragging = false, isTarget = false, dropMap, position, expandTimer = false;
    //move events
    function _nodeMouseDown(e) {
        //left mouse button
        if (e.button !== 0) {
            return;
        }
        //move enabled?
        var $this = $(this), settings = $this.closest("table").data("jquerydragdropcollapsibletreetable-settings");
        if (!settings.enableMove) {
            return;
        }
        //node expander?
        var $el = $(e.target);
        if ($el.hasClass("jquerydragdropcollapsibletreetable-expander")) {
            return;
        }
        //handle
        if ((settings.moveHandle !== false) && ($this.find(settings.moveHandle)[0] != $el[0])) {
            return;
        }
        //move
        $moveItem = $this.closest("tr");
        downX = e.pageX;
        downY = e.pageY;
        var offset = $this.offset();
        offX = offset.left - e.pageX;
        offY = offset.top - e.pageY;
        $(document).on("mouseup", _nodeMouseUp).on("mousemove", _nodeMouseMove);
        return false;
    }

    function _nodeMouseUp(e) {
        if (isDragging) {
            _dragStop();
        }
        $(document).off("mouseup", _nodeMouseUp).off("mousemove", _nodeMouseMove);
    }

    function _nodeMouseMove(e) {
        var d = Math.max(Math.abs(e.pageX - downX), Math.abs(e.pageY - downY)), settings = $moveItem.closest("table").data("jquerydragdropcollapsibletreetable-settings");
        if (d >= settings.moveDistance && !isDragging) {
            _dragStart(e);
        }
        else {
            if (isDragging) {
                _dragMove(e);
            }
        }
    }

    function _dragStart(e) {
        isDragging = true;
        //make drop map
        _makeDropMap();
        //make helper
        $moveHelper = $moveItem.find(">td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container").clone().addClass("dragging").css({
            "left": e.pageX + offX,
            "top": e.pageY + offY,
            "cursor": "no-drop"
        });
        $moveHelper.find(">.jquerydragdropcollapsibletreetable-expander").remove();
        $moveHelper.appendTo("body");
        //make indicator
        if ($(".jquerydragdropcollapsibletreetable-move-indicator").length) {
            return;
        }
        $indicator = $("<div class='jquerydragdropcollapsibletreetable-move-indicator'>").appendTo("body");
        //event callback
        var $jquerydragdropcollapsibletreetable = $moveItem.closest("table"), settings = $jquerydragdropcollapsibletreetable.data("jquerydragdropcollapsibletreetable-settings");
        settings.onMoveStart.call($jquerydragdropcollapsibletreetable, $moveItem, $moveHelper);
    }

    function _dragStop() {
        isDragging = false;
        //auto expand
        if (expandTimer !== false) {
            window.clearTimeout(expandTimer);
            expandTimer = false;
        }
        //remove helper
        $moveHelper.remove();
        //remove indicator
        $indicator.remove();
        //event callback
        var $jquerydragdropcollapsibletreetable = $moveItem.closest("table"), settings = $jquerydragdropcollapsibletreetable.data("jquerydragdropcollapsibletreetable-settings");
        settings.onMoveStop.call($jquerydragdropcollapsibletreetable, $moveItem);
        //drop
        if (isTarget) {
            _dragDrop();
        }
    }

    function _dragMove(e) {
        //move helper
        $moveHelper.css({
            "left": e.pageX + offX,
            "top": e.pageY + offY
        });
        //get node over
        var info = _getNodeAt(e.pageX, e.pageY);
        //if node over not changed, do nothing
        if ($moveOver === info.node && position === info.position) {
            return;
        }
        //if node over before not null, do out
        if ($moveOver !== null) {
            _dragOut();
        }
        //set current node over and position
        $moveOver = info.node;
        position = info.position;
        //if node over not null, do over
        if ($moveOver !== null) {
            _dragOver(info);
        }
    }

    function _dragOver(info) {
        //auto expand
        if (info.position == 1) {
            var $el = info.node;
            if (expandTimer === false && _isCollapsed($el)) {
                expandTimer = window.setTimeout(function () {
                    //methods.expand because loaded check needed
                    methods.expand.call($el);
                    expandTimer = false;
                }, 500);
            }
        }
        else {
            if (expandTimer !== false) {
                window.clearTimeout(expandTimer);
                expandTimer = false;
            }
        }
        //default
        isTarget = true;
        //event callback
        var $jquerydragdropcollapsibletreetable = $moveItem.closest("table"), settings = $jquerydragdropcollapsibletreetable.data("jquerydragdropcollapsibletreetable-settings");
        if (settings.onMoveOver.call($jquerydragdropcollapsibletreetable, $moveItem, $moveHelper, info.node, info.position) === false) {
            isTarget = false;
        }
        //move helper
        if (isTarget) $moveHelper.css({
            "cursor": "move"
        });
        //indicator
        if (isTarget) $indicator.css({
            "display": "block",
            "left": info.node.find(">td.jquerydragdropcollapsibletreetable-sortable>.jquerydragdropcollapsibletreetable-container").offset().left,
            "top": info.top
        });
    }

    function _dragOut() {
        //auto expand
        if (expandTimer !== false) {
            window.clearTimeout(expandTimer);
            expandTimer = false;
        }
        //target
        isTarget = false;
        //move helper
        $moveHelper.css({
            "cursor": "no-drop"
        });
        //indicator
        $indicator.hide();
        //event callback
        var $jquerydragdropcollapsibletreetable = $moveItem.closest("table"), settings = $jquerydragdropcollapsibletreetable.data("jquerydragdropcollapsibletreetable-settings");
        settings.onMoveOut.call($jquerydragdropcollapsibletreetable, $moveItem, $moveHelper, $moveOver);
    }

    function _dragDrop() {
        //do out
        _dragOut();
        //callback
        var $jquerydragdropcollapsibletreetable = $moveItem.closest("table"), settings = $jquerydragdropcollapsibletreetable.data("jquerydragdropcollapsibletreetable-settings"), doMove = settings.onMove.call($jquerydragdropcollapsibletreetable, $moveItem, $moveOver, position);
        if (doMove !== false) {
            methods.move.call($moveItem, $moveOver, position);
        }
        //do move end
        settings.onMoveEnd.call($jquerydragdropcollapsibletreetable, $moveItem);
    }

    //move additional functions
    function _makeDropMap() {
        var idMoveItem = _getId($moveItem);
        var idParentMoveItem = _getParentId($moveItem);
        var branch = [];
        _getBranch($moveItem).each(function () {
            branch.push(_getId($(this)));
        });
        var idBeforeElementToBranch = null;
        var idAfterElementToBranch = null;
        var isElementIntoBranch = false;
        $moveItem.parent().find("tr").each(function () {
            var $this = $(this), id = _getId($this);
            if ((id !== null)) {
                if ($.inArray(id, branch) === -1) {
                    if (isElementIntoBranch === false) {
                        idBeforeElementToBranch = id;
                    }
                    else {
                        idAfterElementToBranch = id;
                        return false; //break the loop
                    }
                }
                else {
                    if (isElementIntoBranch === false) {
                        isElementIntoBranch = true;
                    }
                }
            }
        });
        dropMap = [];
        $moveItem.parent().find("tr").each(function () {
            var $this = $(this), id = _getId($this), idParent = _getParentId($this);
            if (id !== null) { // ((id !== null) && ($.inArray(id, branch) === -1))
                var o = $this.offset();
                var isMoveItem = false;
                var isBranch = false;
                var isBeforeElementToBranch = false;
                var isAfterElementToBranch = false;
                var isParentBeforeElementToBranchEqualToParentMoveItem = false;
                var isParentAfterElementToBranchEqualToParentMoveItem = false;
                if (id === idMoveItem) {
                    isMoveItem = true;
                }
                if ($.inArray(id, branch) > -1) {
                    isBranch = true;
                }
                if (id === idBeforeElementToBranch) {
                    isBeforeElementToBranch = true;
                }
                if (id === idAfterElementToBranch) {
                    isAfterElementToBranch = true;
                }
                if ((isBeforeElementToBranch === true) && ((idParent === null && idParentMoveItem === null) || (idParent === idParentMoveItem))) {
                    isParentBeforeElementToBranchEqualToParentMoveItem = true;
                }
                if ((isAfterElementToBranch === true) && ((idParent === null && idParentMoveItem === null) || (idParent === idParentMoveItem))) {
                    isParentAfterElementToBranchEqualToParentMoveItem = true;
                }
                dropMap.push([
                    o.left, //0
                    o.top, //1
                    $this.width(), //2
                    $this.height(), //3
                    $this, //4
                    isMoveItem, //5
                    isBranch, //6
                    isBeforeElementToBranch, //7
                    isAfterElementToBranch, //8
                    isParentBeforeElementToBranchEqualToParentMoveItem, //9
                    isParentAfterElementToBranchEqualToParentMoveItem //10
                ]);
            }
        });
    }

    function _getNodeAt(x, y) {
        var data = null, info = {
            node: null,
            position: null,
            top: null
        };
        //node data
        $.each(dropMap, function (i, v) {
            if ((x >= v[0]) && (y >= v[1]) && (x <= v[0] + v[2]) && (y <= v[1] + v[3])) {
                data = v;
                info.node = v[4];
                return false;
            }
        });
        //position
        if (data !== null) {
            if (data[5] === true || data[6] === true) {
                info.node = null;
            }
            else {
                var h1 = data[3] / 4, h2 = h1 * 3, y1 = y - data[1];
                if (0 <= y1 && y1 <= h1) {
                    if (data[8] === true && data[10] === true) {
                        info.node = null;
                    }
                    else {
                        info.position = 0;
                        info.top = data[1];
                    }
                }
                else {
                    if (h1 < y1 && y1 < h2) {
                        info.position = 1;
                        info.top = data[1] + data[3] / 2;
                    }
                    else {
                        if (h2 <= y1 && y1 <= data[3]) {
                            if (data[7] === true && data[9] === true) {
                                info.node = null;
                            }
                            else {
                                info.position = 2;
                                info.top = data[1] + data[3];
                            }
                        }
                        else {
                            info.node = null;
                        }
                    }
                }
            }
        }
        return info;
    }

})(jQuery);
