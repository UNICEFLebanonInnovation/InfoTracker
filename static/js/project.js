$(document).ready(function(){

    $('.search-filter').change(function(e){
        $('#changelist-search').submit();
    });

    $('.field-frequency').each(function(i, val){
        var item = $(this);
        var input = item.find('input');
        input.hide();
        var frequency = parseInt(input.val());

        for (i = 0; i < frequency; i++) {
            add_badge(item, i);
        }
    });

    $('.field-frequency').dblclick(function(e){
        var item = $(this);
        var input = item.find('input');
        var frequency = parseInt(input.val());
        input.val(frequency + 1);
        add_badge(item, frequency);
    });

});

function add_badge(item, frequency){

    var badge_info = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-info"></div>';
    var badge_primary = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-primary"></div>';
    var badge_warning = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-warning"></div>';
    var badge_danger = '<div class="mb-2 mr-2 badge badge-dot badge-dot-lg badge-danger"></div>';


        var badge = ''
        if(frequency > 0 && frequency <= 4) {
            badge = badge_info;
        }
        if(frequency > 4 && frequency <= 8) {
            badge = badge_primary;
        }
        if(frequency > 8 && frequency <= 12) {
            badge = badge_warning;
        }
        if(frequency > 12) {
            badge = badge_danger;
        }

        console.log(frequency);
        console.log(badge);
        item.append(badge);
}