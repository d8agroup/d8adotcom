function record_analytics_action(action_category, action_name) {
    _gaq.push(['_trackEvent', action_category, action_name]);
}

$(document).ready(function(){
    /******************************************************************************************************************/
    /* OFF SITE SOCIAL LINK TRACKING                                                                                  */
    /******************************************************************************************************************/
    $('.analytics_action').click(function(event){
        var link = $(this);
        var action_category = link.data('analytics_action_category');
        var action_name = link.data('analytics_action_name');
        record_analytics_action(action_category, action_name);
    });

});