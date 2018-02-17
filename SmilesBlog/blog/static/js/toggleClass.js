var toggleMonth = function(month) {
    $(month).children('.events').slideToggle('slow');
    $(month).find('.month-data div.collapsed').toggle();
    $(month).find('.month-data div.expanded').toggle();
}

// expand the current month
toggleMonth($('#{{now.year}}-{{now.month}}'));

// intercept click to toggle month
$('.month-data').click(function() {
    var month = $(this).parent();
    toggleMonth(month);
});
