function create_edit_button(key, specific_url) {
    var temp_div = $("<div>");
    temp_div.addClass("edit-icon-class separate-edit-click-class");
    temp_div.attr("data-div-id", "edit_menu_id")
    temp_div.attr("data-create-form-id", "create_menu_form_id")
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
    temp_div.attr("data-heading-text", "Delete Menu")
    temp_div.attr("data-button-text", "Delete Menu")
    temp_div.attr("data-onclick-handler", "deleteMenuHandler(this)")
    temp_div.append($("<i>").addClass("bi bi-trash"))
    return temp_div;
}

function create_menu_button(menus, menu_name, key) {
    var temp_div = $("<div>");
    temp_div.css("cursor", "pointer");
    temp_div.attr("data-menus", menus);
    temp_div.attr("data-id", key)
    temp_div.attr("data-menu-name", menu_name)
    temp_div.attr("data-child-method", "POST")
    temp_div.attr('onClick', 'displayMenusHandler(this);');
    temp_div.append($("<i>").addClass("bi bi-eye"))
    return temp_div;
}



function reconstruct_menu_table(datatable_id, obj) {
    for (const [key, value] of Object.entries(obj)) {

        var temp_tr = $('<tr>');
        var temp_td = $('<td>');
        temp_tr.append(temp_td.clone().append(value.name))
        temp_tr.append(temp_td.clone().append(value.url))
        temp_tr.append(temp_td.clone().append(value.is_active ? $("<snap>").append($("<i>").addClass("bi-check-circle").css("color", "green")) : $("<snap>").append($("<i>").addClass("bi-x-circle").css("color", "red"))))
        temp_tr.append(temp_td.clone().append(value.updated_at))
        // temp_tr.append(temp_td.clone().append(value.is_parent ? $("<snap>").append($("<i>").addClass("bi-check-circle").css("color", "green")) : $("<snap>").append($("<i>").addClass("bi-x-circle").css("color", "red"))))
        var edit_div = create_edit_button(key, value.specific_url);
        temp_tr.append(temp_td.clone().append(edit_div))
        var delete_div = create_delete_button(key, value.name, value.delete_url);
        temp_tr.append(temp_td.clone().append(delete_div))
        var menus_div = create_menu_button(value.parent_id__name ? value.parent_id__name.constructor.name == "Array" ? value.parent_id__name.join("|") : value.parent_id__name + "|" : "", value.name, key);
        temp_tr.append(temp_td.clone().append(menus_div))
        $("#" + datatable_id).DataTable().row.add(temp_tr).draw();
        tooltips()
    }
}

function refresh_datatable(datatable_id, data) {
    var datatable_inst = $("#" + datatable_id);
    var datatable_url = datatable_inst.data("url");
    var { status, data } = sendRequest("GET", datatable_url, data);
    datatable_inst.DataTable().clear().draw();
    reconstruct_menu_table(datatable_id, data)
}

function refresh_children_menus_select(menu_select_id, menu_dict) {
    $("#" + menu_select_id).children().remove();
    for (const [key, value] of Object.entries(menu_dict)) {
        $("#" + menu_select_id).append($('<option>', {
            value: key,
            text: value.name
        }));
    }
}

// Menu Creation js
$("#create_menu_form_id").on("submit",async function (e) {
    e.preventDefault();
    e.stopPropagation()
    if ($("#create_menu_form_id").valid()) {
        console.log("yes valid");
        
        const button =  hideSubmitButton($(this).attr("id"));
        var formData = $(this).serializeArray();
        const json_obj = convertSerializerArrToJson(formData, list_fiels_names = []);
        const submit_url = $(this).data("url");
        const submit_method = $(this).data("method");
        var { status, data } =await sendRequestPromise(submit_method, submit_url, json_obj);
        if (status) {
            $('select[name=parent_id]').find('option').remove()
            $('select[name=inner_menu_of]').find('option').remove()
            $('select[name=parent_id]').append('<option value' + '' + '>Select Parent Menu</option>')
            $('select[name=inner_menu_of]').append('<option value' + '' + '>Select Inner Menu Of</option>')
            for (const [key, value] of Object.entries(data.menu_dict)) {
                var parent_id = $('select[name=parent_id]').append('<option value=' + key + '>' + value + '</option>')
                    ;
            }
            for (const [key, value] of Object.entries(data.inner_menu_dict)) {
                var parent_id = $('select[name=inner_menu_of]').append('<option value=' + key + '>' + value + '</option>')
                    ;
            }

            remove_custom_error_classes();
            $("#create_menu_form_id").trigger("reset");
            refresh_children_menus_select("menu_list_id", data.menu_dict);
            refresh_datatable("menu_datatable_id", {});
        }
        showSubmitButton(button);
        return false;
    }

})


$(document).on("click", ".separate-edit-click-class", function () {
    // Clear create form
    var create_form_id = $(this).data("create-form-id");
    $("#" + create_form_id).children().find("button[type='reset']").click();

    var edit_div_id = $(this).data("div-id");
    const fetch_url = $(this).data("detail-url");
    const submit_method = $(this).data("method");
    const object_uuid = $(this).data("object-uuid");



    var { status, data } = sendRequest(submit_method, fetch_url, { "object_uuid": object_uuid, "csrfmiddlewaretoken": global_csrf_token });
    if (status) {

        for (const [key, value] of Object.entries(data.parent_serialized_obj)) {
            const obj_inst = $("#" + edit_div_id).children().find("[name='" + key + "']");
            if (obj_inst == 'parent_id') {
                obj_inst.val(value).attr('disabled', 'disabled')
            }
            if (obj_inst.length > 1) {
                $("#" + edit_div_id).children().find("[name='" + key + "'][value='" + value + "']").prop("checked", true);
            }
            else {
                obj_inst.val(value);
            }

        }
        $("#" + edit_div_id).children().find("[name='hidden_id']").val(object_uuid);
        $("#" + edit_div_id).children().find("[name='name']").attr('data-div-id', data.id);
        $(".create-menu-form-parent-div").children().children().addClass("d-none");
        $("#" + edit_div_id).removeClass("d-none");

    }
})

$(document).on("click", ".hide-current-display-another-menu-form", function () {
    
    const edit_div_id = $(this).data("div-id");
    console.log($(this).parent());
    
    $(".create-menu-form-parent-div").children().children().removeClass("d-none");
    $("#" + edit_div_id).addClass("d-none");
})

// Menu Update Js
$("#edit_menu_form_id").on("submit",async function (e) {
    e.preventDefault();
    e.stopPropagation();
    if ($("#edit_menu_form_id").valid()) {
        const button =  hideSubmitButton($(this).attr("id"));
        const formData = $(this).serializeArray();
        const json_obj = convertSerializerArrToJson(formData, list_fiels_names = ["children_id"]);
        const submit_url = $(this).data("url");
        const submit_method = $(this).data("method");
        var { status, data } =await sendRequestPromise(submit_method, submit_url, json_obj);

        if (status) {
            $('select[name=parent_id]').find('option').remove()
            $('select[name=inner_menu_of]').find('option').remove()
            $('select[name=parent_id]').append('<option value' + '' + '>Select Parent Menu</option>')
            $('select[name=inner_menu_of]').append('<option value' + '' + '>Select Inner Menu Of</option>')
            for (const [key, value] of Object.entries(data.menu_dict)) {
                var parent_id = $('select[name=parent_id]').append('<option value=' + key + '>' + value + '</option>')

                    ;
            }
            for (const [key, value] of Object.entries(data.inner_menu_dict)) {
                var parent_id = $('select[name=inner_menu_of]').append('<option value=' + key + '>' + value + '</option>')

                    ;
            }



            remove_custom_error_classes();

            refresh_children_menus_select("menu_list_id", data.menu_dict);

            $("#edit_menu_form_id").trigger("reset");
            refresh_datatable("menu_datatable_id", {});
            $(".hide-current-display-another-menu-form").click();
            $("#create_menu_form_id").trigger('reset')
            var label = $('label[class=form-label]')
            label.next('div').html('')
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
        refresh_datatable("menu_datatable_id", {});
    }
    $("#generic-modal").modal('hide');
})


function displayMenusHandler(e) {
    var menus = $(e).data("menus");
    var id = $(e).data("id")
    const url = datachildmenus
    const method = $(e).data("child-method")
    const { status, data } = sendRequest(method, url, { "id": id })
    var child_menus = data.child_menus


    if (status == true) {
        const menu_name = $(e).data("menu-name");
        let modall = $("<div>").append($("<strong>").html(menu_name)).append(" has the following Child Menus").append($("</strong>"))
        // setGenericModal(modall)
        // let secdiv = $("<div>").append($("<ol>")).addClass("horizontal");
        var ol = $("<ol>").addClass("horizontal")
        for (let i = 0; i < data.child_menus.length; i++) {
            

            var menus = data.child_menus[i].name
            var element = data.child_menus[i].name
            ol.append($("<li>").html(element))
            
        }
        const secdiv = $("<div>").append(ol)
        setGenericModal(menu_name.toUpperCase(), $("<div>").append(modall).append(secdiv))

    } else {
        const menu_name = $(e).data("menu-name");
        const splited_menus = menus.split("|");
        const first_div = $("<div>").append("This Menu has the no Child Menus")
        var ol = $("<ol>").addClass("horizontal")
        splited_menus.forEach(element => {
        });
        const second_div = $("<div>").append(ol)
        final_div = $("<div>").append(first_div).append(second_div)
        setGenericModal(menu_name.toUpperCase(), final_div.html())
    }
}


$(document).on("click", "#flexSwitchCheckChecked", function () {
    if ($(this).attr('value', true)) {
        $('select[name=parent_id]').attr('disabled', false)

    } else {
        $('select[name=parent_id]').attr('disabled', true)

    }
});


$(document).on("click", "#flexRadioDefault1", function () {

    $('select[name=parent_id]').attr('disabled', false)

}
);

$(document).on("click", "#flexRadioDefault2", function () {
    $('select[name=parent_id]').attr('disabled', true)

}
);