function showbootstrapLoader(button) {
    
    var new_button  = $("#bootstrap-loader");
    $(button).replaceWith(new_button.show());
    return button
}

function hidebootstrapLoader(new_button,button) {
    
    $("#bootstrap-loader").after(new_button);
    $("#bootstrap-loader").hide()
    
    
}