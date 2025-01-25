$("#create_menu_form_id").validate({
    rules: {
        name: {
            required: true,
            minlength: 3,
            maxlength: 30,
            regex: ROLE_NAME_REGEX,
            checkmenuname:true
        },
        url: {
            minlength: 1,
            maxlength: 255,
            regex: URL_NAME_REGEX,
            required: true

        },
        parent_id: { 
            // select_choices: _parent_menus, 
        },
        inner_menu_of: { 
            // select_choices: _all_menus, 
        },
        
    },
    messages: {
        name: {
            minlength: "Menu should be of at least 3 characters",
            maxlength: "max_length is 30 , REACHED",
            regex : "Invalid Format, only A-Z, a-z are allowed and special character & is allowed",
            checkmenuname: "Menu name already exists",
        },
        url: {
            maxlength: "max_length is 256 , REACHED",
            minlength: "URL name should be at least 1 characters",
            regex : "Invalid Format, only A-Z, a-z and _ is allowed "

        },


    },
    errorPlacement: function (error, element) {
        element.parents("form").addClass("form-validated");
        element.siblings("div").addClass($(error).attr("class")).text($(error).text());

    },
    success: function (success, element) {
        $(element).siblings("div").attr("class", "");
        $(element).siblings("div").addClass("valid-feedback");
    },
    unhighlight: function (element, unhighlight_class) {
        $(element).closest("form").addClass("form-validated")
        $(element).siblings("div").removeClass(unhighlight_class);
        $(element).removeClass(unhighlight_class);
        $(element).siblings("div").addClass("valid-feedback");
        $(element).addClass("valid-feedback");
    },
    errorClass: "invalid-feedback",
    validClass: "valid-feedback",
})


// Update menu js

$("#edit_menu_form_id").validate({
    rules: {
        name: {
            required: true,
            minlength: 3,
            maxlength: 30,
            regex: ROLE_NAME_REGEX,
            checkupdatedmenuname:true
        },
        url: {
            minlength: 1,
            maxlength: 255,
            regex: URL_NAME_REGEX,
            required: true

        },
        parent_id: { 
            // select_choices: _parent_menus, 
        },
        inner_menu_of: { 
            // select_choices: _all_menus,
        },
    },
    messages: {
        name: {
            minlength: "Menu should be of at least 3 characters",
            maxlength: "max_length is 30 , REACHED",
            regex : "Invalid Format, only A-Z, a-z are allowed and special character & is allowed",
            checkupdatedmenuname:"Menu name already exists"
        },
        url: {
            maxlength: "max_length is 256 , REACHED",
            minlength: "URL name should be at least 1 character",
            regex : "Invalid Format, only A-Z, a-z and _ is allowed "

        },


    },
    errorPlacement: function (error, element) {
        element.parents("form").addClass("form-validated");
        element.siblings("div").addClass($(error).attr("class")).text($(error).text());

    },
    success: function (success, element) {
        $(element).siblings("div").attr("class", "");
        $(element).siblings("div").addClass("valid-feedback");
    },
    unhighlight: function (element, unhighlight_class) {
        $(element).closest("form").addClass("form-validated")
        $(element).siblings("div").removeClass(unhighlight_class);
        $(element).removeClass(unhighlight_class);
        $(element).siblings("div").addClass("valid-feedback");
        $(element).addClass("valid-feedback");
    },
    errorClass: "invalid-feedback",
    validClass: "valid-feedback",
})