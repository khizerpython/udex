$.validator.addMethod("select_choices", function (value, element, args) {
    if (value.length == 0) return true;
    if (typeof value == "string") {
        value = [value]
    }
    let verified = value.every((val) => args.indexOf(val) >= 0);
    return verified;
}, "Please select correct option");


$.validator.addMethod("boolean_choices", function (value, element, args) {
    return value == "true" || value == "false";
}, "Please select correct value.");

$.validator.addMethod(
    "regex",
    function (value, element, regexp) {
        var re = new RegExp(regexp);
        return this.optional(element) || re.test(value);
    }
);

// MENUS CHECKS

// CHECK MENUNAME
$.validator.addMethod(
    "checkmenuname",
    function (value, element) {

        var name = value
        let csr = $("input[name=csrfmiddlewaretoken]").val();
        const json_obj = { 'name': name, csrfmiddlewaretoken: csr }
        var submit_method = 'POST'
        submit_url = checkmenuname

        var { status, data } = sendRequest(submit_method, submit_url, json_obj);
        return status

    }
);

// CHECK UPDATE MENUNAME
$.validator.addMethod(
    "checkupdatedmenuname",
    function (value, element) {

        var name = value
        let csr = $("input[name=csrfmiddlewaretoken]").val();
        const id = $(element).attr('data-div-id')
        const json_obj = { 'name': name, csrfmiddlewaretoken: csr, 'id': id }
        var submit_method = 'POST'
        submit_url = checkupdatemenuname
        var { status, data } = sendRequest(submit_method, submit_url, json_obj);
        return status

    }
);


// Check Role Name Uniqueness

// Check name existence
$.validator.addMethod(
    "check_unique_name",
    function (value, element, args) {
        let trimmed_value = value.trim();
        if (trimmed_value == '') return true;
        const url = $(element).data("url");
        var data = { "name": trimmed_value, "csrfmiddlewaretoken": global_csrf_token };
        if (args["include_id"]) {
            const HIDDEN_INPUT_NAME = args.hidden_input_name ? args.hidden_input_name : "hidden_id";

            data["object_id"] = $("input[name='" + HIDDEN_INPUT_NAME + "']").val();
        }
        var { status, _data } = sendRequest("POST", url, data);
        return status
    }
);