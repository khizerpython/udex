toastr.options = {
    "closeButton": true,
    "debug": false,
    "newestOnTop": false,
    "progressBar": true,
    "positionClass": "toast-top-right",
    "preventDuplicates": false,
    "onclick": null,
    "showDuration": "6000",
    "hideDuration": "6000",
    "timeOut": "6000",
    "extendedTimeOut": "5000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
}

function convertSerializerArrToJson(serialized_array, list_fiels_names = []) {
    var valid_json_format = {};
    list_fiels_names.forEach(element => {
        valid_json_format[element] = [];

    });

    serialized_array.forEach(function (obj, i) {
        if (valid_json_format[obj.name]) {
            if (!valid_json_format[obj.name].push) {
                valid_json_format[obj.name] = [valid_json_format[obj.name]];
            }
            valid_json_format[obj.name].push(obj.value || '');
        } else {
            valid_json_format[obj.name] = obj.value || '';
        }
    });
    return valid_json_format;
}

function convertFormDataObjToJson(form_data, list_fiels_names = []) {
    var valid_json_format = {};
    list_fiels_names.forEach(element => {
        valid_json_format[element] = [];

    });
    for (var [key, value] of form_data.entries()) {
        if (valid_json_format[key]) {
            if (!valid_json_format[key].push) {
                valid_json_format[key] = [value];
            }
            valid_json_format[key].push(value || '');
        } else {
            valid_json_format[key] = value || '';
        }
    }
    return valid_json_format;
}

function getJsonFormatData(data) {
    var indexed_array = {};

    $.map(data, function (n, i) {
        if (indexed_array[n['name']] == undefined) {
            indexed_array[n['name']] = n['value'];
        }
        else {
            if (indexed_array[n['name']].constructor.name !== "Array") {
                var prev_val = indexed_array[n['name']];
                indexed_array[n['name']] = [];
                indexed_array[n['name']].push(prev_val);
            }
            indexed_array[n['name']].push(n['value']);
        }
    });

    return indexed_array;
}

function remove_custom_error_classes() {
    // Quill editor reset 
    $(".quill-editor-default").removeClass("invalid-feedback valid-feedback");
    $(".ql-toolbar").removeClass("invalid-feedback valid-feedback");

    $("div.valid-feedback").text("");
    $("div.invalid-feedback").text("");
    $(".form-validated").removeClass("form-validated");
    $(".valid-feedback").removeClass("valid-feedback");
    $(".invalid-feedback").removeClass("invalid-feedback");
    $(".valid-radio").removeClass("valid-radio");
    $(".invalid-radio").removeClass("invalid-radio");
}

function buildFormData(formData, data, parentKey) {
    if (data && typeof data === 'object' && !(data instanceof Date) && !(data instanceof File)) {
        Object.keys(data).forEach(key => {
            buildFormData(formData, data[key], parentKey ? `${parentKey}[${key}]` : key);
        });
    } else {
        const value = data == null ? '' : data;

        formData.append(parentKey, value);
    }
    return formData
}

function place_errors(errors, errors_div) {
    remove_custom_error_classes();
    Object.keys(errors).forEach(element_name => {
        var errors_ = errors[element_name].join(", ");
        const element = $('#' + errors_div + 'id_' + element_name);
        element.parents("form").addClass("form-validated");
        element.attr("type") == "radio" ? element.parents("fieldset").next("div").addClass("invalid-feedback").text(errors_) : element.siblings("div").addClass("invalid-feedback").text(errors_);
        element.attr("type") == "radio" ? $("input[name='" + element.attr("name") + "']").addClass("invalid-radio") : element.addClass("invalid-feedback");
    
    });
}

function checkFileAttachment(data) {
    var file_content, formData = new FormData();
    if (data.file_path && data.file_path.name != '') {
        file_content = data.file_path;
        delete data.file_path;
        formData.append('file_path', file_content, file_content.name);
    }
    else {
        delete data.file_path
    }
    formData.append("data", CustomEncrypt(data))
    return formData;
}

function handleSuccess(data) {
    const dec_data = CustomDecrypt(data.data);
    if (dec_data.detail) {
        // toastr.success(dec_data.detail);
        const heading = "Success"
        setGenericModal(heading, dec_data.detail)
    }
    return dec_data;
}

function handleError(jqXhr) {
    const dec_data = CustomDecrypt(jqXhr.responseJSON.data);
    // if (jqXhr.status == 401 || jqXhr.status == 501) {
    //     window.location.replace(dec_data.redirect_url);
    // }
    if (dec_data.detail) {
        const heading = "Error"
        // toastr.error(dec_data.detail);
        setGenericModal(heading, dec_data.detail)
    }
    if (dec_data.errors) {
        place_errors(dec_data.errors, dec_data.errors_div)
    }
    return dec_data;
}



// jQuery function to create a notification item
function createNotificationItem(dataHref, iconClass, title, initiatedBy, caseInfo, timestamp) {
    // Create the outer list item
    const $li = $('<li>').addClass('notification-item')
                        .attr('id', 'my_notification_bell_icon')
                        .attr('data-href', dataHref);
  
    // Create the icon element
    const $icon = $('<i>').addClass(iconClass);
  
    // Create the inner div to contain text content
    const $div = $('<div>');
  
    // Create the title (h4) and add to the div
    const $title = $('<h4>').text(title);
    $div.append($title);
  
    // Create the 'initiated by' paragraph and add to the div
    const $initiatedBy = $('<p>').html(`<b>Initiated By:</b> ${initiatedBy}`);
    $div.append($initiatedBy);
  
    // Create the case information and date paragraph and add to the div
    const $caseInfo = $('<p>').html(`<b>${caseInfo}</b> &nbsp; &nbsp; &nbsp; ${timestamp}`);
    $div.append($caseInfo);
  
    // Append the icon and div to the outer list item
    $li.append($icon);
    $li.append($div);
  
    return $li;
  }


{/* <li class="notification-item-hr">
            <hr class="dropdown-divider">
          </li>   */}
function createHrList(){
    $li = $("<li>").addClass("notification-item-hr")
    $hr = $("<hr>").addClass("dropdown-divider")
    $li.append($hr)
    return $li

}  













function updateHeaderNotification() {

    var badge_number = $(".badge-number")

    var iconHeadingBody = $(".notification-icon-body")
    var iconBody = $(".notification-item")
    const submit_url = $("#dashboard_notification_url").val()
    var submit_method = "POST"
    var { status, data } = sendRequest(submit_method, submit_url, {});
    if (status) {

        const iconCls = "bi bi-exclamation-circle text-warning";
        var length = Object.keys(data).length;
        // Icon data length
        badge_number.text("")
        badge_number.text(length)

        // Head title
        iconHeadingBody.text("")
        iconHeadingBody.text("You have " + length + " pending workflows")
        // Body
        $("#notification-list li#my_notification_bell_icon").remove();
        $(".notification-item-hr").remove();

        for (const [key, value] of Object.entries(data)) {
            const $notificationItem = createNotificationItem(dataHref=value.redirect_url, iconClass=iconCls, title=value.data.workflow_topic, initiatedBy=value.data.initiated_by, caseInfo=value.case_id, timestamp=value.created_at);
            $('#notification-list').append($notificationItem);
            const $hrlistitem = createHrList() 
            $('#notification-list').append($notificationItem,$hrlistitem);
          }
    }
  }




function sendRequest(method, url, data) {
    if (typeof method === "undefined" || typeof url === "undefined" || typeof data === "undefined") {
        return { status: false, data: "Invalid request parameters" };
    }
    let formData = checkFileAttachment(data);
    $.ajax({
        type: method,
        url,
        data: formData,
        dataType: 'json',
        processData: false,
        contentType: false,
        async: false,
        headers: { "X-CSRFToken": global_csrf_token },
        success: function (data, status, xhr) {
            let dec_data = handleSuccess(data);
            return_data = { status: true, data: dec_data }
        },
        error: function (jqXhr, textStatus, errorMessage) {
            let dec_data = handleError(jqXhr);
            return_data = { status: false, data: dec_data };
        },
    });
    return return_data
}

function sendRequestPromise(method, url, data) {
    let formData = checkFileAttachment(data);
    return new Promise((resolve, reject) => {
        if (typeof method === "undefined" || typeof url === "undefined" || typeof data === "undefined") {
            return resolve({ status: false, data: "Invalid request parameters" });
        }
        $.ajax({
            type: method,
            url: url,
            data: formData,
            dataType: 'json',
            processData: false,
            contentType: false,
            async: true,
            headers: { "X-CSRFToken": global_csrf_token },
            success: function (data, status, xhr) {
                let dec_data = handleSuccess(data);
                return resolve({ status: true, data: dec_data })
            },
            error: function (jqXhr, textStatus, errorMessage) {
                let dec_data = handleError(jqXhr);
                return resolve({ status: false, data: dec_data });
            },
        });
    });
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


function get_file_attachment_html(id_prefix, show_tooltip = false) {
    const file_input_col_class = show_tooltip ? "col-sm-10" : "col-sm-10";
    var div = $("<div>").addClass(file_input_col_class);
    const file_label = $("<label>").addClass("col-sm-10 col-form-label pt-0").text("Attachment");
    const file_input = $("<input>").addClass("form-control").prop("type", "file").attr("id", id_prefix + "id_file_path").attr("name", "file_path");
    const file_tooltip = show_tooltip == true ? $("<div>").addClass("col-sm-2").append($("<div>").addClass("text-center").append($("<i>").addClass("bi bi-question-circle").attr("id", "modal_attachemnt_help_text").css({ "font-size": "26px" }))) : "";
    const tooltip = $("<div>").css("padding", "15px 0px 0px -1px").addClass('text-center')
    tooltip.append($("<i>").css("font-size", "26px").attr("id", "file_help_id").addClass("bi bi-question-circle"))
    // const my_div = $("<div>").addClass('col-1').append(tooltip)
    return $("<div>").addClass("row mt-3").append(file_label).append(div.append(file_input).append($("<div>"))).append(file_tooltip)
}


$(document).on("click", ".edit-click-class", function () {
    // Clear create form
    var create_form_id = $(this).data("create-form-id");
    $("#" + create_form_id).children().find("button[type='reset']").click();

    var edit_div_id = $(this).data("div-id");
    const fetch_url = $(this).data("detail-url");
    const submit_method = $(this).data("method");
    const object_uuid = $(this).data("object-uuid");
    var { status, data } = sendRequest(submit_method, fetch_url, { "object_uuid": object_uuid, "csrfmiddlewaretoken": global_csrf_token });
    if (status) {
        for (const [key, value] of Object.entries(data)) {
            const obj_inst = $("#" + edit_div_id).children().find("[name='" + key + "']");
            if (key == 'menu_ids') {

                $('#edit_id_menu_ids').multiSelect('select', value);

            }

            if (obj_inst.length > 1) {

                $("#" + edit_div_id).children().find("[name='" + key + "'][value='" + value + "']").prop("checked", true);
            }
            else {
                obj_inst.val(value);


            }
        }
        $("#" + edit_div_id).children().find("[name='hidden_id']").val(object_uuid);


        $(".section").children().children().addClass("d-none");
        $("#" + edit_div_id).removeClass("d-none");

    }
})


$(document).on("click", ".hide-current-display-another", function () {
    
    const edit_div_id = $(this).data("div-id");
    $(this).parent().closest(".section").children().children().removeClass("d-none");
    $("#" + edit_div_id).addClass("d-none");
})

$(document).on("click", ".delete-click-class", function () {
    const body_text = $(this).data("body-text")
    const heading_text = $(this).data("heading-text")
    const button_text = $(this).data("button-text")
    const delete_id = $(this).data("delete-id")
    const delete_url = $(this).data("delete-url")
    const delete_method = $(this).data("delete-method")
    setModal(heading_text, body_text, button_text, delete_id, delete_url, delete_method);
})


$(document).on("click", "[type='reset']", function (e) {
    remove_custom_error_classes();
    // Removing Quill editor content
    $(".ql-editor").find("p").text("");
    return true;
})


function hideModalSubmitButton(element) {
    $(element).attr("disabled", true);
    $(element).css("display", "none");
}


function showModalSubmitButton(element) {
    $(element).removeAttr("disabled");
    $(element).show();
}



function addmultipleassetids(form_id, data) {

    var current_asset_textbox_length = 0;
    let my_Array = []

    for (var i = 0; i < data.asset_id.length; i++) {
        const TEXTBOX_ID = 'initiate_id_asset_' + String(current_asset_textbox_length + 1);


        var assetId = data.asset_id[i];
        const outer_div = $('<div>').addClass('col-sm-11')
        const inner_div = $('<div>').addClass('form-floating mb-3')
        const input_asset_id = $('<input>').addClass('form-control').attr('name', 'asset_id[' + String(current_asset_textbox_length + 1) + ']').attr('placeholder', 'Asset ID').attr('type', 'text').attr('id', TEXTBOX_ID).attr("data-url", check_asset_id_in_asset_movement_workflow_url).val(assetId)

        const label = $('<label>').attr('for', 'asset_id[' + String(current_asset_textbox_length + 1) + ']').text('Asset ID')
        const empty_div = $('<div>')

        const first_div = $('<div>').addClass('col-1')
        const second_div = $('<div>').addClass('mt-2 text-center')
        const i_tag = $('<i>').addClass('bi bi-dash-circle-fill subtract-asset-id').css("font-size", "26px").attr("data-textbox-id", TEXTBOX_ID)

        const first_plus_div = $('<div>').addClass('col-1')
        const second_plus_div = $('<div>').addClass('mt-2 text-center')
        const i_plus_tag = $('<i>').addClass('bi bi-plus-circle-fill add-asset-id').css("font-size", "26px").attr("data-textbox-id", TEXTBOX_ID).attr('data-include-id', 'true').attr('data-form-id', 'reinitiate_asset_movement_workflow')
        const final_subtract_i = first_div.append(second_div.append(i_tag))
        const final_add_i = first_plus_div.append(second_plus_div.append(i_plus_tag))
        current_asset_textbox_length += 1



        final_div = outer_div.append(inner_div.append(input_asset_id, label, empty_div))
        if (i == 0) {

            my_Array.push(final_div, final_add_i)
        } else {
            my_Array.push(final_div, final_subtract_i)
        }

    }

    var asset_id = $("#" + form_id).children().find("[name=workflow_execution_step_id]");

    $.each(my_Array.reverse(), function (index, value) {
        $($("#" + form_id).children()[0]).before(value)
        const check_unique_name = { "include_id": true, hidden_input_name: "workflow_execution_step_id" }
        addValidationToNewFieldOfAssetID(form_id, check_unique_name);
    });

}



function placeWorkflowFormData(form_id, data, quillbot_fields = [], hidden_fields = [], multiple_asset_ids = false) {
    for (const [key, value] of Object.entries(data)) {
        const obj_inst = $("#" + form_id).children().find("[name='" + key + "']");
        if (obj_inst.length > 1) {
            $("#" + form_id).children().find("[name='" + key + "'][value='" + value + "']").prop("checked", true);
        }
        else if (quillbot_fields.includes(key)) {
            var hidden_input = $("#" + form_id + " input[name=" + key + "]");
            hidden_input.val(value); // Setting hidden field with value
            const quill_data_attr_value = hidden_input.data("quill-field");
            $("#" + form_id).children().find("[data-input-field-id=" + quill_data_attr_value + "]").children(".ql-editor").html(value)
        }
        else if (hidden_fields.includes(key)) {
            if (value != "") {
                var hidden_input = $("#" + form_id + " input[name=" + key + "]");
                hidden_input.val(value); // Setting hidden field with value
                hidden_input.parent().parent().removeClass("d-none");
            }
        }
        else {
            obj_inst.val(value);
        }
    }
    if (multiple_asset_ids == true) {
        addmultipleassetids(form_id, data)
    }
}


// $(document).on("click", ".cancel-reinitiate-form-button", function(){
//     remove_custom_error_classes();

//     // Removing Quill editor content
//     $(".ql-editor").find("p").text("");

//     // Reseting form values
//     $(this).parents().closest("form").get(0).reset();

//     // Hidding this form
//     $(this).parents().closest("form").addClass("d-none");

//     // Display another form
//     $("#"+$(this).data("display-form-id")).removeClass("d-none")

//     // Changing tab text from re-initiate to initiate
//     $('.nav-tabs #initiate-tab').text('Initiate');
// })


function cancelReinitiateForm(form, reset_button) {
    remove_custom_error_classes();

    // Removing Quill editor content
    form.find(".ql-editor").find("p").text("");

    // Reseting form values
    form.get(0).reset();

    // Hidding this form
    form.addClass("d-none");

    // Display another form
    $("#" + reset_button.data("display-form-id")).removeClass("d-none")

    // Changing tab text from re-initiate to initiate
    $('.nav-tabs #initiate-tab').text('Initiate');

}

$(document).on("click", ".cancel-reinitiate-form-button", function () {
    var reset_button = $(this)
    var form = $(this).closest('form');
    cancelReinitiateForm(form, reset_button)

})

// Event for carousel slide change.
$(document).on("slid.bs.carousel", "#workflowHistoryCarousel", function () {
    var carousel_item = $('.carousel-inner').find('.active');
    var last_carousel_index = Number($('.carousel-inner').children().last().attr("index"));
    var index = Number(carousel_item.attr("index"));
    var step = index+1;
    // Setting step number
    $('.modal-carousel-nav').find('.step-num').text("STEP "+step)
    // Handling carousel active indicators
    var second_last_indicator = $("._carousel-indicators").children(":nth-last-child(2)")
    var second_indicator = $("._carousel-indicators").children(":nth-child(2)")
    if (second_last_indicator.hasClass('active')){
        if (index<(Number(second_last_indicator.attr("data-bs-slide-to"))) || index == last_carousel_index){
            $("._carousel-indicators").find(".active").removeClass('active');
        }
        // If user pressed next when second last indicator is active, increment the data-bs-slide attr value.
        else{
            $("._carousel-indicators").children('button').each(function(){
                $(this).attr('data-bs-slide-to', Number($(this).attr('data-bs-slide-to'))+1)
            })
        }
    }
    else if(second_indicator.hasClass('active')){
        if (index>(Number(second_indicator.attr("data-bs-slide-to"))) || index == 0){
            $("._carousel-indicators").find(".active").removeClass('active');
        }
        // If user pressed prev when second indicator is active, decrement the data-bs-slide attr value.
        else{
            $("._carousel-indicators").children('button').each(function(){
                $(this).attr('data-bs-slide-to', Number($(this).attr('data-bs-slide-to'))-1)
            })
        }
    }
    else{
        $("._carousel-indicators").find(".active").removeClass('active');
    }

    // Setting active indicator
    var active_indicator = $("._carousel-indicators").find("[data-bs-slide-to='"+index+"']");

    // If last carousel indicator is clicked directly and the active slide is not last
    if (index != last_carousel_index && active_indicator.is(':last-child')){
        $("._carousel-indicators").children('button').each(function(){
            $(this).attr('data-bs-slide-to', Number($(this).attr('data-bs-slide-to'))+1)
        })
        second_last_indicator.addClass('active')
    }
    // If first carousel indicator is clicked directly and the active slide is not first
    else if (index != 0 && active_indicator.is(':first-child')){
        $("._carousel-indicators").children('button').each(function(){
            $(this).attr('data-bs-slide-to', Number($(this).attr('data-bs-slide-to'))-1)
        })
        second_indicator.addClass('active')
    }
    else{
        active_indicator.addClass('active');
    }

    // Disabling next/previous button on last/first slide.
    if ($('.carousel-inner .carousel-item:first').hasClass('active')) {
        $(".carousel-prev-btn").addClass("disabled")
        $(".carousel-next-btn").removeClass("disabled")
    } else if ($('.carousel-inner .carousel-item:last').hasClass('active')) {
        $(".carousel-next-btn").addClass("disabled");
        $(".carousel-prev-btn").removeClass("disabled");
        // If not on first or last step, both button should be enabled.
    } else {
        $('.carousel-control-custom').removeClass("disabled");

    }
});

$("#generic-display-modal").on('shown.bs.modal', function(){
    var leng = $(".carousel-inner").children().length;
    // If history modal has only one step, disable next button.
    if(leng == 1){
        $(this).find('.carousel-next-btn').addClass('disabled');
    }
    // Remove extra indicators for steps number less than 5.
    $("._carousel-indicators>button:gt("+(leng-1)+")").remove();
})

function get_carousel_html(data, get_obj_html){
    var parent_div = $("<div>").addClass("carousel slide").attr("id", "workflowHistoryCarousel");
    var inner_div = $("<div>").addClass("carousel-inner").css({"padding": "1px 2.5rem 1px 2.5rem","overflow-x": "auto"});
    data.forEach((obj, index) => {
        var obj_html = get_obj_html(index, obj); 
        var carousel_div = $("<div>").addClass("carousel-item").html(obj_html).attr("index", index);
        if(index == 0){
            carousel_div.addClass("active");
        }
        carousel_div.appendTo(inner_div);
    })
    parent_div.append(inner_div)
    return parent_div
}

// General function to create carousel header
// Not for Employee Registration/De-registration and Change Management.
function get_carousel_header(obj){
    var temp_div = $("<div>")
    var return_dom = temp_div.clone().addClass("row")
    return_dom.append(temp_div.clone().addClass("col-6 mb-2").html("<strong class='d-block'>Executed at</strong>"+ obj.created_at))
    return_dom.append(temp_div.clone().addClass("col-6 mb-2").html("<strong class='d-block'>Executed by</strong>"+ obj.user_id))
    return_dom.append(temp_div.clone().addClass("col-6 mb-2").html("<strong class='d-block'>Execution Status</strong> "+ obj.status_id))
    if (obj.next_approver){

        return_dom.append(temp_div.clone().addClass("col-6 mb-2").html("<strong class='d-block'>Next Approver</strong> "+ obj.next_approver))
      }
    const attachment_anchor = obj.attachment? $("<a>").attr("href", obj.attachment).prop("target", "blank").text("Download"):$("<span>").text("No Attachment Found")
    return_dom.append(temp_div.clone().addClass("col-12 mb-1").html($("<strong>").text("Attachment: ").add(attachment_anchor)))
    $("</br><hr>").appendTo(return_dom);
    return return_dom;
}

function addValidationToNewFieldOfAssetID(form_id, check_unique_name) {
    $("#" + form_id).validate();
    $("input[name^='asset_id']").each(function () {
        $(this).rules("add", {
            required: true,
            regex: ASSET_ID_REGEX,
            minlength: 3,
            maxlength: 50,
            check_unique_name,
            same_page_asset_ids: true,
            messages: {
                regex: "Only A-z, a-z, 0-9 and (!#-_) special characters and one space in between characters are allowed",
                minlength: "Min length of asset ID is 3",
                maxlength: "Max length of asset ID is 50",
                check_unique_name: "This Asset ID already has a workflow that is in pending state",
                same_page_asset_ids: "Asset id can not be same",

            }
        });
    });
}
