$("#create_role_form_id").validate({
    rules: {
        name: {
            required: true,
            minlength: 3,
            maxlength: 30,
            regex:NAME_REGEX,
            check_unique_name: {"include_id": false}
        },
        order: {
            required: true,
            number: true,
            min: 0,
            max: 100
        },
        menu_ids: { 
            select_choices: _menus, 
            required: false,
        },
        is_hod_right: {  
            required: true,
            select_choices: _rights_list_json, 
        },
    },
    messages : {
        name: {
            regex: "Name should contain only small and capital characters with whitespace(s) between them",
            minlength: "Name should be at least 3 characters",
            maxlength: "Name should not be greater than 30 characters",
            check_unique_name: "Role with this name already exists"
        },
        order: {
            number: "Enter your order as a numerical value",
            min: "Value of order must not be in negative",
            max: "Value of order must not be greater than 100",
        }
    },
    errorPlacement: function(error, element) { 
        element.parents("form").addClass("form-validated");
        element.siblings("div").not(".ms-container").addClass($(error).attr("class")).text($(error).text());
    },
    success: function(success, element) {
        $(element).siblings("div").not(".ms-container").attr("class", "");
        $(element).siblings("div").not(".ms-container").addClass("valid-feedback");
    },
    unhighlight: function(element, unhighlight_class) {
        $(element).siblings("div").removeClass(unhighlight_class);
        $(element).removeClass(unhighlight_class);
        $(element).siblings("div").not(".ms-container").addClass("valid-feedback");
        $(element).addClass("valid-feedback");
    },
    errorClass: "invalid-feedback",
    validClass: "valid-feedback",
});

$("#edit_role_form_id").validate({
    rules: {
        name: {
            required: true,
            minlength: 3,
            maxlength: 30,
            regex:NAME_REGEX,
            check_unique_name: {"include_id": true}
        },
        order: {
            required: true,
            number: true,
            min: 0,
            max: 100,
        },
        is_active: {
            required: true,
            boolean_choices: true,
        },
        menu_ids: { 
            select_choices: _menus, 
            required: false,
        },
        is_hod_right: {  
            required: true,
            select_choices: _rights_list_json, 
        },
    },
    messages : {
        name: {
            minlength: "Name should be at least 3 characters",
            maxlength: "Name should be at greater than 30 characters",
            regex: "Name should contain only small and capital characters with whitespace(s) between them",
            check_unique_name: "Role with this name already exists"
        },
        order: {
            number: "Enter your order as a numerical value",
            min: "Value of order must not be in negative",
            max: "Value of order must not be greater than 100",
        },
        is_active: {
            boolean_choices: "Given value is not a proper value boolean value",
        }
    },
    errorPlacement: function(error, element) { 
        element.parents("form").addClass("form-validated");
        element.siblings("div").not(".ms-container").addClass($(error).attr("class")).text($(error).text());
        $(element).attr("type") == "radio"? element.parents("fieldset").next("div").addClass($(error).attr("class")).text($(error).text()):element.siblings("div").not(".ms-container").addClass($(error).attr("class")).text($(error).text());
        $(element).attr("type") == "radio"? $("input[name='"+$(element).attr("name")+"']").removeClass("invalid-feedback").addClass(""): "";
    },
    success: function(success, element) {
        $(element).siblings("div").not(".ms-container").attr("class", "");
        $(element).siblings("div").not(".ms-container").addClass("valid-feedback");
    },
    unhighlight: function(element, unhighlight_class) {
        $(element).siblings("div").not(".ms-container").removeClass(unhighlight_class);
        $(element).removeClass(unhighlight_class);
        $(element).siblings("div").not(".ms-container").addClass("valid-feedback");

        $(element).attr("type") == "radio"? $("input[name='"+$(element).attr("name")+"']").addClass("valid-radio"):$(element).addClass("valid-feedback");
    },
    errorClass: "invalid-feedback",
    validClass: "valid-feedback",
});