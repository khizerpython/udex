function create_edit_button(key, specific_url) {
    var temp_div = $("<div>");
    temp_div.addClass("edit-icon-class seperate-edit-click-class");
    temp_div.attr("data-div-id", "edit_authuser_id")
    temp_div.attr("data-create-form-id", "create_authuser_form_id")
    temp_div.attr("data-method", "POST")
    temp_div.attr("data-detail-url", specific_url)
    temp_div.attr("data-object-uuid", key)
    temp_div.append($("<i>").addClass("bi bi-pencil-square"))
    return temp_div;
}

function create_delete_button(key, name, delete_url) {
    var temp_div = $("<div>");
    temp_div.addClass("delete-icon-class delete-click-class");
    temp_div.attr("data-delete-url", delete_url)
    temp_div.attr("data-delete-id", key)
    temp_div.attr("data-body-text", name)
    temp_div.attr("data-delete-method", "POST")
    temp_div.attr("data-heading-text", "Delete User")
    temp_div.attr("data-button-text", "Delete User")
    temp_div.attr("data-onclick-handler", "deleteAuthUserHandler(this)")
    temp_div.append($("<i>").addClass("bi bi-trash"))
    return temp_div;
}

function create_regenerate_button(key, value) {
    if(value.show_resend_activation_link_button){
        var temp_div = $("<div>");
        temp_div.addClass("edit-icon-class h4 re-generate-activation-link-click-class");
        temp_div.data("generate-url", value.regenerate_url)
        temp_div.data("object-id", key)
        temp_div.data("object-method", "POST")
        temp_div.append($("<i>").addClass("bi bi-arrow-clockwise"))
        return temp_div;
    }
    else{
        return "--"
    }
}

function reconstruct_authuser_table(datatable_id, obj) {
    for (const [key, value] of Object.entries(obj)) {

        var temp_tr = $('<tr>');
        var temp_td = $('<td>');
        temp_tr.append(temp_td.clone().append(value.username))
        temp_tr.append(temp_td.clone().append(value.email))
        temp_tr.append(temp_td.clone().append(value.designation_id))
        temp_tr.append(temp_td.clone().append(value.is_active ? $("<snap>").append($("<i>").addClass("bi-check-circle").css("color", "green")) : $("<snap>").append($("<i>").addClass("bi-x-circle").css("color", "red"))))
        temp_tr.append(temp_td.clone().append(value.is_lock ? $("<snap>").append($("<i>").addClass("bi-check-circle").css("color", "green")) : $("<snap>").append($("<i>").addClass("bi-x-circle").css("color", "red"))))
        temp_tr.append(temp_td.clone().append(value.created_at))
        temp_tr.append(temp_td.clone().append(create_edit_button(key, value.specific_url)));
        temp_tr.append(temp_td.clone().append(create_delete_button(key, value.username, value.delete_url)))
        temp_tr.append(temp_td.clone().append(create_regenerate_button(key, value)))
        $("#" + datatable_id).DataTable().row.add(temp_tr).draw();
        tooltips()
    }
}

function refresh_datatable(datatable_id, data) {
    
    var datatable_inst = $("#" + datatable_id);
    var datatable_url = datatable_inst.data("url");
    
    var { status, data } = sendRequest("GET", datatable_url, data);
    datatable_inst.DataTable().clear().draw();
    reconstruct_authuser_table(datatable_id, data)
}

$("#create_authuser_form_id").on("submit",async function (e) {
    e.preventDefault();
    e.stopPropagation()
    
    if ($("#create_authuser_form_id").valid()) {
        const button = hideSubmitButton($(this).attr("id"));
        var formData = $(this).serializeArray();
        const json_obj = convertSerializerArrToJson(formData, list_fiels_names = ["department_id"]);
        const submit_url = $(this).data("url");
        
        const submit_method = $(this).data("method");
        var { status, data } =await sendRequestPromise(submit_method, submit_url, json_obj);
        
        if (status) {
            remove_custom_error_classes();
            $(this).find("select[name=department_id]").attr("multiple",false)
            $(this).find("select[name=department_id] option:first").prop("selected", true);
            $(this).find("#department_label").removeAttr("style");
            $("#create_authuser_form_id").trigger("reset");
            refresh_datatable("authuser_datatable_id", {});
        }
        showSubmitButton(button);
        return false;

    }

})

// Upon Click on update department from datatable
$(document).on("click", ".seperate-edit-click-class", function () {
    // Clear create form
    var create_form_id = $(this).data("create-form-id");
    $("#"+create_form_id).children().find("button[type='reset']").click();

    var edit_div_id = $(this).data("div-id");
    const fetch_url = $(this).data("detail-url");
    const submit_method = $(this).data("method");
    const object_uuid = $(this).data("object-uuid");
    var { status, data } = sendRequest(submit_method, fetch_url, { "object_uuid": object_uuid, "csrfmiddlewaretoken": global_csrf_token });
    if (data.is_hod_right == true) {
        var form = $("#edit_authuser_form_id")
        // $(form).children().find("select[name=deparment_id]").attr('multiple', true)
        // $(form).children().find("#department_label").hide()
    }
    if (status) {
        for (const [key, value] of Object.entries(data.obj)) {
            const obj_inst = $("#" + edit_div_id).children().find("[name='" + key + "']");


            if (obj_inst.length > 1) {
                $("#" + edit_div_id).children().find("input[value='" + value + "']").prop("checked", true);
            }
            else if(obj_inst.attr('name')=='department_id'){
                obj_inst.val(value);
                var mythis = $(obj_inst)
                designationOfDepartment(mythis)
                var designation_div = $("#" + edit_div_id).children().find("[name='designation_id']");
                const value1 = Object.entries(data.obj).find(([key, value]) => key === 'designation_id')?.[1];
                designation_div.val(value1)
            }
            else {
                
                obj_inst.val(value);
            }
        }
        $("#" + edit_div_id).children().find("[name='hidden_id']").val(object_uuid);
        $("#" + edit_div_id).children().find("[name='username']").attr('data-div-id', data.id);
        $("#" + edit_div_id).children().find("[name='email']").attr('data-div-id', data.id);
        $("#" + edit_div_id).children().find("[name='employee_id']").attr('data-div-id', data.id);

        $(".create-user-parent-div").children().children().addClass("d-none");
        $("#" + edit_div_id).removeClass("d-none");
    }
})


$(document).on("click", ".hide-current-display-another-user-form", function () {
    
    const edit_div_id = $(this).data("div-id");
    $(this).parent().closest(".create-user-parent-div").children().children().removeClass("d-none");
    $("#" + edit_div_id).addClass("d-none");
})

$("#edit_authuser_form_id").on("submit",async function (e) {
    e.preventDefault();
    e.stopPropagation();
    if ($("#edit_authuser_form_id").valid()) {
        const button = hideSubmitButton($(this).attr("id"));
        const formData = $(this).serializeArray();
        const json_obj = convertSerializerArrToJson(formData, list_fiels_names = ["department_id"]);
        const submit_url = $(this).data("url");
        const submit_method = $(this).data("method");
        

        var { status, data } =await sendRequestPromise(submit_method, submit_url, json_obj);
        if (status) {
            remove_custom_error_classes();
            var department = $(this).find("select[name=department_id]")
            department.attr("multiple",false)
            department.find("option:first").prop("selected", true)
            // $(this).find("select[name=department_id] option:first").prop("selected", true);
            $(this).find("#department_label").removeAttr("style");
            $("#edit_authuser_form_id").trigger("reset");
            refresh_datatable("authuser_datatable_id", {});
            $(".hide-current-display-another-user-form").click();
        }
        showSubmitButton(button);
        return false;
        
    }
})



$(document).on("click", "#modal-confirmation", function() {
    hideModalSubmitButton(this)
    const delete_id = $(this).attr("data-delete-id")
    const delete_url = $(this).attr("data-delete-url")
    const delete_method = $(this).attr("data-delete-method")
    const { status, data } = sendRequest(delete_method, delete_url, { "id": delete_id })
    if (status) {
        refresh_datatable("authuser_datatable_id", {});
    }
    $("#generic-modal").modal('hide');

})

var today = datePickerId.max = new Date().toISOString().split("T")[0];
$("input[name=dob]").attr('max',today);


$("body").on("keypress", "input[type=date]", function (e) { e.preventDefault(); })



$(document).on('click change', 'select[name=role_id]', function () {

    $("#create_authuser_form_id").children().find("select[name=department_id]").attr('multiple', false)

    var form = $(this).parents('form:first');

    var selectOption = $(form).children().find("select[name=role_id]");
    var righType = $(selectOption).find(":selected").data('hod-right');
    // var lowercase_role = rolename? rolename.toLowerCase():"";

    if (righType == "True") {
        $('select[name=department_id] option:eq(1)').attr('selected', 'selected');

        // $(form).children().find("select[name=deparment_id]").attr('multiple', true)
        // $(form).children().find("#department_label").hide()

    } else {
        $('select[name=department_id] option:eq(0)').attr('selected', 'selected');
        $(form).children().find("select[name=department_id]").attr('multiple', false)
        $(form).children().find("#department_label").show()
    }


})


$(document).on('click', '.re-generate-activation-link-click-class', function () {
    hideAnyElement($(this).attr("id"));
    const generate_url = $(this).data("generate-url");
    const object_id = $(this).data("object-id");
    const object_method = $(this).data("object-method");
    const json_obj = {"inst_id": object_id};
    var { status, data } = sendRequest(object_method, generate_url, json_obj);
    if (status) {
        refresh_datatable("authuser_datatable_id", {});
    }
    return false;
})



function createDesignationOption(data,designationDiv) {
    $.each(data, function (index, obj) {
        var option = '<option name="designation_option" value="' + obj.pk + '">' + obj.fields.name + '</option>';
        $('#'+designationDiv).append(option);
    });


}



// After click on department get the designations related to that department
$(document).on('change', 'select[name=department_id]', function (e) {
    e.preventDefault()
    var mythis = $(this)
    designationOfDepartment(mythis)

    



})

function designationOfDepartment(mythis){
    console.log("geo g");
    
    let csr = $("input[name=csrfmiddlewaretoken]").val();
    const submit_method = "POST"
    const submit_url = $(mythis).attr('data-url')
    const selectedDepartments = $(mythis).find('option:selected');
    const designationDiv= $(mythis).attr('data-append-div')
    // $('#'+designationDiv+'[value!=""]').remove();
    $('#'+designationDiv+' option[value!=""]').remove();

    const depart_id_array = selectedDepartments.map(function() {
    return $(this).val();
    }).get();

    const json_obj = { 'depart_id': depart_id_array, csrfmiddlewaretoken: csr }


    var { status, data } = sendRequest(submit_method, submit_url, json_obj);
    if (status) {
        createDesignationOption(data,designationDiv)
        
    }

}
