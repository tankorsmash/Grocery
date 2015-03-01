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
});
