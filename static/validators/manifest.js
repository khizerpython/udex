// Custom validator for max date
$.validator.addMethod("maxDateToday", function(value, element) {
    var today = new Date().toISOString().split('T')[0];
    return value <= today;
}, "Date cannot be in the future.");


$("#create_manifest_form_id").validate({
    rules: {
        from_date: {
            required: true,
        },
        to_date: {
            required: true,
            maxDateToday: true  // 👈 add custom rule here

        },
        
    },
    messages: {
        from_date: {
          required : "This field is required."
        },
        to_date: {
            required : "This field is required.",
            maxDateToday: "Date cannot be in the future."
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