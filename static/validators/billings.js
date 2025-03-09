$.validator.addMethod("select_choices", function (value, element, args) {
    if (value.length == 0) return true;
    if (typeof value == "string") {
        value = [value]
    }
    let verified = value.every((val) => args.indexOf(val) >= 0);
    return verified;
}, "Please select correct option");

var vaildationrules = {
    rules: {
        service_id: {
            required: true,
            select_choices:_all_services
        },
        shipper_company_name: {
            required: true,
        },
        shipper_contact_person: {
            required: true,
        },
        shipper_reference: {
            required: true,
        },
        shipper_address: {
            required: true,
        },
        shipper_state: {
            required: true,
        },
        shipper_city: {
            required: true,
        },
        shipper_post_code: {
            required: false,
        },
        shipper_mobile_number: {
            required: true,
        },
        shipper_phone_number: {
            required: true,
        },
        shipper_ntn_cnic: {
            required: true,
        },
        shipper_email_address: {
            required: true,
        },
        //reciever 
        reciever_company_name: {
            required: true,
        },
        reciever_contact_person: {
            required: true,
        },
        reciever_address: {
            required: true,
        },
        reciever_country: {
            required: true,
        },
        reciever_state: {
            required: true,
        },
        reciever_city: {
            required: true,
        },
        reciever_post_code: {
            required: false,
        },
        reciever_mobile_number: {
            required: true,
        },
        reciever_phone_number: {
            required: true,
        },
        reciever_email: {
            required: true,
        },
        reciever_fax: {
            required: true,
        },
        // Shipment details
        payment_id: {
            required: true,
            select_choices:_all_payments
        },
        shipment_id: {
            required: true,
            select_choices:_all_shipments
        },
        fedex_number: {
            required: true,
        },
        weight: {
            required: true,
        },
        pieces: {
            required: true,
        },
        // Dimensions
        length: {
            required: true,
        },
        width: {
            required: true,
        },
        height: {
            required: true,
        },
        // Invoice Detail
        hs_title: {
            required: true,
        },
        quantity: {
            required: true,
        },
        price: {
            required: true,
        },
        total: {
            required: true,
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
        password :{
            required: "This field is required",
            regex: "Please write a valid password"
        }      
        



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
}

$("#create_billings_form_id").validate(vaildationrules)
$("#update_billings_form_id").validate(vaildationrules)