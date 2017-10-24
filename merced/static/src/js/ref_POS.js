odoo.define('pos_product_ref', function (require) {

"use strict";

	var module = require('point_of_sale.models');


    var BillScreenWidget = screens.ReceiptScreenWidget.extend({
        template: 'BillScreenWidget',
        show: function(){
        this._super();
        var self = this;
        this.render_receipt();
    },