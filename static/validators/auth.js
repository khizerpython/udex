$("#create_authuser_form_id").validate({
    rules: {
        first_name: {
            required: true,
            minlength: 3,
            maxlength: 30,
            regex:NAME_REGEX,
        },
        last_name: {
            minlength:3,
            maxlength: 30,
            regex:NAME_REGEX,
            required:true
        
        },
        username: {
            minlength:3,
            maxlength: 25,
            regex:USERNAME_REGEX,
            required:true,
            checkusername:true
        
        },
        email: {
            maxlength: 255,
            required:true,
            regex:EMAIL_ADDRESS_REGEX,
            email: true,
            // checkemail:true,
        
        },
        contact_number: {
            minlength:10,
            maxlength: 13,
            regex:CONTACT_NUMBER_REGEX,
            required:true,
        
        },
        gender: {
            required:true,
        },
        dob: {
            required:true,
        
        },
        employee_id: {
            minlength:5,
            // maxlength: 10,
            regex:EMPLOYEE_ID_REGEX,
            required:true,
            checkemployeeid:true
        
        },
        department_id: {
            required:true,
            // checkrole:true,
            select_choices: _all_departments,
        
        },
        role_id: {
            required:true,
            select_choices:_all_roles,
        
        },
        
        designation_id: {
            required:true,
            select_choices:_all_designations,
        
        },
        city_id: {
            required:true,
            select_choices:_all_cities,
        },
    },
    messages: {
        first_name: {
            minlength: "First name should be of atleast 3 characters",
            maxlength: "max_length is 30 , REACHED",
            regex: "Only Alphabets  are allowed. Trailing spaces are not allowed"
        },
        last_name: {
            minlength:"Last name should be of atleast 3 characters",
            maxlength: "max_length is 30 , REACHED",
            regex: "Only Alphabets  are allowed. Trailing spaces are not allowed",
            
        },
        username: {
            minlength:"Username name should be of atleast 3 characters",
            maxlength: "max_length is 25 , REACHED",
            regex: "Invalid Format, only these special characters @ # . _ - and A-Z a-z 0-9 are allowed",
            checkusername: "Username already exists"
            
        },
        email: {
            maxlength: "max_length is 255 , REACHED",
            regex: "Invalid Format, please enter valid email address",
            email: "Should be a valid email address",
            // checkemail: "This email address is already taken"
            
        },
        contact_number: {
            minlength:"Contact number min length is 10",
            maxlength: "Contact number max length is 13 ",
            regex: "Please enter valid contact number",
            
        },
        employee_id: {
            minlength:"min length is 5",
            // maxlength: "max_length is 10 , REACHED",
            regex: "Please enter valid employee ID. only 0-9 digits (length=5) are allowed",
            checkemployeeid:"This Employee ID already exists."
            
        },
        department_id: {
            required:"This field is required.",
            // checkrole:"Only hod can be assign more than 2 departments"
            
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


$("#edit_authuser_form_id").validate({
    rules: {
        first_name: {
            required: true,
            minlength: 3,
            maxlength: 30,
            regex:NAME_REGEX,
        },
        last_name: {
            minlength:3,
            maxlength: 30,
            regex:NAME_REGEX,
            required:true
        
        },
        
        contact_number: {
            minlength:10,
            maxlength: 13,
            regex:CONTACT_NUMBER_REGEX,
            required:true,
        
        },
        
        dob: {
            required:true,
        
        },
        
        department_id: {
            required:true,
            // checkrole:true,
            select_choices:_all_departments
        
        },
        role_id: {
            required:true,
            select_choices:_all_roles
        
        },
        
        designation_id: {
            required:true,
            select_choices:_all_designations
        
        },
        city_id: {
            required:true,
            select_choices:_all_cities
        },
        email: {
            maxlength: 255,
            email: true,
            required:true,
            // checkupdateemail:true,
            regex:EMAIL_ADDRESS_REGEX,
        
        },
    },
    messages: {
        first_name: {
            minlength: "First name should be of atleast 3 characters",
            maxlength: "max_length is 30 , REACHED",
            regex: "Only Alphabets  are allowed. Trailing spaces are not allowed"
        },
        last_name: {
            minlength:"Last name should be of atleast 3 characters",
            maxlength: "max_length is 30 , REACHED",
            regex: "Only Alphabets  are allowed. Trailing spaces are not allowed",
            
        },
        
        contact_number: {
            minlength:"Contact number min length is 10",
            maxlength: "Contact number max length is 13 ",
            regex: "Please enter valid contact number",
            
        },

        department_id: {
            required:"This field is required.",
            // checkrole:"Only hod can be assign more than 2 departments"
            
        },
        email: {
            maxlength: "Contact number should be in proper format",
            regex: "Invalid Format, please enter valid email address",
            email: "Should be a valid email address",
            // checkupdateemail:"This Email Address is already taken",
            regex: "Invalid Format, please enter valid email address",
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
