$("#create_airway_bill_location_form").validate({
    rules: {
        name: {
            required: true,
        },
        description: {
            required: true,
        },
        position: {
            required: true,
        },
        
        
        
    },
    messages: {
        name: {
            required: "Location Name is required",
            
        },
        description: {
            required: "Location Description is required",
            
        },
        position: {
            required: "Location Position is required",
            
        },

    },
    errorPlacement: function(error, element) { 
        element.parents("form").addClass("form-validated");
        element.siblings("div").addClass($(error).attr("class")).text($(error).text());
        
    },
    success: function(success, element) {
        $(element).siblings("div").attr("class", ""); 
        $(element).siblings("div").addClass("valid-feedback");
    },
    unhighlight: function(element, unhighlight_class) {
        $(element).siblings("div").removeClass(unhighlight_class);
        $(element).removeClass(unhighlight_class);
        $(element).siblings("div").addClass("valid-feedback");
        $(element).addClass("valid-feedback");
    },
    errorClass: "invalid-feedback",
    validClass: "valid-feedback",
})