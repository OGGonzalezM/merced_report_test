odoo.define('pos_custom.discount_price', function (require) {
"use strict";

var models = require('point_of_sale.models');

var _super_orderline = models.Orderline.prototype;
models.Orderline = models.Orderline.extend({
    initialize: function(attr, options){
        _super_orderline.initialize.apply(this,arguments);
        if (options.json) {
            return;
        }
        this.price   = options.product.list_price;
    },
});

var _super_order = models.Order.prototype;
models.Order = models.Order.extend({
    add_product: function(product, options){
        _super_order.add_product.apply(this, arguments);
        options = options || {};
        var dis = product.list_price - product.price,
            dis_per = (100 * dis) / product.list_price;
        if(dis_per){
            dis_per += (options.discount || 0);
            this.selected_orderline.set_discount(dis_per.toFixed(this.pos.dp['Discount']));
        }
    },
    numberToWords: function(n) {
        const arr = x => Array.from(x);
        const num = x => Number(x) || 0;
        const str = x => String(x);
        const isEmpty = xs => xs.length === 0;
        const take = n => xs => xs.slice(0,n);
        const drop = n => xs => xs.slice(n);
        const reverse = xs => xs.slice(0).reverse();
        const comp = f => g => x => f (g (x));
        const not = x => !x;
        const chunk = n => xs =>
              isEmpty(xs) ? [] : [take(n)(xs), ...chunk (n) (drop (n) (xs))];

        // numToWords :: (Number a, String a) => a -> String
        let numToWords = n => {

          let a = [
            '', 'uno', 'dos', 'tres', 'cuatro',
            'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
          ];

          let b = [
            '', '', 'veinti', 'treinta', 'cuarenta',
            'fifty', 'sesenta', 'setenta', 'ochenta', 'noventa'
          ];

          let g = [
            '', 'mil', 'million', 'billion', 'trillion', 'quadrillion',
            'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion'
          ];

          // this part is really nasty still
          // it might edit this again later to show how Monoids could fix this up
          let makeGroup = ([ones,tens,huns]) => {
            return [
              num(huns) === 0 ? '' : a[huns] + ' ciento(s) ',
              num(ones) === 0 ? b[tens] : b[tens] && b[tens] + '-' || '',
              a[tens+ones] || a[ones]
            ].join('');
          };

          let thousand = (group,i) => group === '' ? group : `${group} ${g[i]}`;

          if (typeof n === 'number')
            return numToWords(String(n));
          else if (n === '0')
            return 'zero';
          else
            return comp (chunk(3)) (reverse) (arr(n))
              .map(makeGroup)
              .map(thousand)
              .filter(comp(not)(isEmpty))
              .reverse()
              .join(' ');
        };

        var noList = n.toString().split('.');
        if (noList.length == 1){
            return numToWords(n);
        }
        else {
            return numToWords(noList[0]) + ' and ' + numToWords(noList[1]);
        }
    },
});

});
