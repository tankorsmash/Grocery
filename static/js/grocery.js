$(function() {
    $("#aisle-map a").click(function(e) {
        that = $(this);
        attr_id = that.attr("id");
        aisle_elem = $("#aisle-"+attr_id); 
        if (attr_id) 
        {
            if (aisle_elem.hasClass("active-aisle"))
            {
                aisle_elem.removeClass("active-aisle");
            }
            else
            {
                aisle_elem.addClass("active-aisle");
            };
        };
    });

    $("[id^=aisle-]").hover(function(e) {
        that = $(this);
        attr_id = that.attr("id");
        if (attr_id) 
        {
            attr_id = that.attr("id").replace("aisle-", "");
            map_elem = $("#"+attr_id); 
            if (map_elem.hasClass("active-aisle"))
            {
                map_elem.removeClass("active-aisle");
            }
            else
            {
                map_elem.addClass("active-aisle");
            };
        };
    });
});
