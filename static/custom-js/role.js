
function create_edit_button(key, specific_url) {
    var temp_div = $("<div>");
    temp_div.addClass("edit-icon-class separate-edit-click-class");
    temp_div.attr("data-div-id", "edit_role_id")
    temp_div.attr("data-create-form-id", "create_role_form_id")
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
    temp_div.attr("data-heading-text", "Delete Right")
    temp_div.attr("data-button-text", "Delete Right")
    temp_div.attr("data-onclick-handler", "deleteRoleHandler(this)")
    temp_div.append($("<i>").addClass("bi bi-trash"))
    return temp_div;
}

function create_menu_button(menus, role_name) {
    var temp_div = $("<div>");
    temp_div.css("cursor", "pointer");
    temp_div.addClass("show-menus-of-roles");
    temp_div.attr("data-menus", menus)
    temp_div.attr("data-role-name", role_name)
    temp_div.attr('onClick', 'displayMenusHandler(this);');
    temp_div.append($("<i>").addClass("bi bi-eye"))
    return temp_div;
}


function reconstruct_role_table(datatable_id, obj) {
    for (const [key, value] of Object.entries(obj)) {
        
        var temp_tr = $('<tr>'); 
        var temp_td = $('<td>');
        temp_tr.append(temp_td.clone().append(value.name))
        temp_tr.append(temp_td.clone().append(value.order))
        temp_tr.append(temp_td.clone().append(value.is_active? $("<snap>").append($("<i>").addClass("bi-check-circle").css("color", "green")): $("<snap>").append($("<i>").addClass("bi-x-circle").css("color", "red"))))
        temp_tr.append(temp_td.clone().append(value.updated_at))
        var edit_div = create_edit_button(key, value.specific_url);
        temp_tr.append(temp_td.clone().append(edit_div))
        var delete_div = create_delete_button(key, value.name, value.delete_url);
        temp_tr.append(temp_td.clone().append(delete_div))
        var menus_div = create_menu_button(value.menu_ids__name != undefined? value.menu_ids__name.constructor.name == "Array"? value.menu_ids__name.join("|"):value.menu_ids__name + "|": "", value.name);
        temp_tr.append(temp_td.clone().append(menus_div))
        $("#"+datatable_id).DataTable().row.add(temp_tr).draw();
        tooltips()
      }
}


function refresh_datatable(datatable_id, data){
    var datatable_inst = $("#"+datatable_id);
    var datatable_url = datatable_inst.data("url");
    var {status, data} = sendRequest("GET", datatable_url, data);
    datatable_inst.DataTable().clear().draw();
   reconstruct_role_table(datatable_id, data)
}

$("#create_role_form_id").on("submit",async function(e){
    
    e.preventDefault();
    e.stopPropagation()

    if(!$("#create_role_form_id").valid()){
        return false
    }
    const button = hideSubmitButton($(this).attr("id"));
    var formData = $(this).serializeArray();
    const json_obj = convertSerializerArrToJson(formData, list_fiels_names=["menu_ids"]);
    const submit_url = $(this).data("url");
    const submit_method = $(this).data("method");
    var {status, data} =await sendRequestPromise(submit_method, submit_url, json_obj);
    if (status){
        remove_custom_error_classes();
        $("#create_reset_button").trigger('click')
        refresh_datatable("roles_datatable_id", {});
    }
    showSubmitButton(button);
    return false;
})

$("#edit_role_form_id").on("submit",async function(e){
    e.preventDefault();
    e.stopPropagation();

    if(!$("#edit_role_form_id").valid()){
        return false
    }
    const button = hideSubmitButton($(this).attr("id"));
    var formData = $(this).serializeArray();
    var json_obj = convertSerializerArrToJson(formData, list_fiels_names=["menu_ids"]);
    const submit_url = $(this).data("url");
    const submit_method = $(this).data("method");
    var {status, data} =await sendRequestPromise(submit_method, submit_url, json_obj);
    if (status){
        remove_custom_error_classes();
        // $('#edit_id_menu_ids').multiSelect('deselect_all')
        $("#edit_role_form_id").trigger("reset");
        refresh_datatable("roles_datatable_id", {});
        $(".hide-current-display-another-role").click();
    }
    showSubmitButton(button);
    return false;
})



$(document).on("click", ".hide-current-display-another-role", function () {
    $('#edit_id_menu_ids').multiSelect('deselect_all')
    const edit_div_id = $(this).data("div-id");
    $(this).parent().closest(".section").children().children().removeClass("d-none");
    $("#" + edit_div_id).addClass("d-none");
})


$(document).on("click", "#modal-confirmation", function() {
    hideModalSubmitButton(this)
    
    const delete_id = $(this).attr("data-delete-id")
    const delete_url = $(this).attr("data-delete-url")
    const delete_method = $(this).attr("data-delete-method")
    const {status, data} = sendRequest(delete_method, delete_url, {"id": delete_id})
    if (status){
        refresh_datatable("roles_datatable_id", {});
    }
    $("#generic-modal").modal('hide');
    
})



function displayMenusHandler(e){
    var menus = $(e).data("menus");
    const role_name = $(e).data("role-name");
    const splited_menus = menus.split("|");

    const first_div = $("<div>").append($("<strong>").html(role_name)).append(" has the following menu(s)")
    var ol = $("<ol>").addClass("horizontal")
    splited_menus.forEach(element => {
        if (element !== "") {
            ol.append($("<li>").html(element))
        }
    });
    const second_div = $("<div>").append(ol)
    final_div = $("<div>").append(first_div).append(second_div)
    setGenericModal(role_name.toUpperCase(), final_div.html())
}

$("#create_reset_button").on('click', function(){
    
    $('#create_id_menu_ids').multiSelect('deselect_all');
})

$("div[class=ms-selectable]").on('click', function(){
    $(this).parent('div').siblings('div[class=invalid-feedback]').html('')
})



$(document).on("click", ".separate-edit-click-class", function(){
    // Clear create form
    var create_form_id = $(this).data("create-form-id");
    $("#"+create_form_id).children().find("button[type='reset']").click();
    
    var edit_div_id = $(this).data("div-id");
    const fetch_url = $(this).data("detail-url");
    const submit_method = $(this).data("method");
    const object_uuid = $(this).data("object-uuid");
    var {status, data} = sendRequest(submit_method, fetch_url, {"object_uuid": object_uuid, "csrfmiddlewaretoken": global_csrf_token});
    if (status){
        for (var [key, value] of Object.entries(data)) {
            const obj_inst = $("#"+edit_div_id).children().find("[name='"+key+"']");
            if(key=='menu_ids'){
                
                $('#edit_id_menu_ids').multiSelect('select', value);
                
            }
                
            if (obj_inst.length > 1){
                
                $("#"+edit_div_id).children().find("[name='"+key+"'][value='"+ value +"']").prop("checked", true);
            }
            else{
                if (obj_inst.attr('name')=='is_hod_right'){
                    value=String(value)
                    obj_inst.val(value);
                }
                else{

                    obj_inst.val(value);
                }
               
            
            }
        }
        $("#"+edit_div_id).children().find("[name='hidden_id']").val(object_uuid);
       

        $(".section").children().children().addClass("d-none");
        $("#"+ edit_div_id).removeClass("d-none");
        
    }
})