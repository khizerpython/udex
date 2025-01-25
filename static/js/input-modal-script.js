
function cleanInputModal() {
    const modalDOM = $("#input-generic-modal");
    changeAcceptRejectGenericModalToNormalSize()
    modalDOM.find("h5").text("");
    modalDOM.find("#input_body_id").html("");
    modalDOM.find("#input-modal-confirmation").removeAttr("data-object-id");
    modalDOM.find("#input-modal-confirmation").removeAttr("data-object-url");
    modalDOM.find("#input-modal-confirmation").removeAttr("data-object-method");
    modalDOM.find("#input-modal-confirmation").text("");
}

function setInputModal(heading, body_content, buttonText, object_id, submit_url, submit_method, large_modal=false) {
    cleanInputModal();

    if (large_modal) {
        changeAcceptRejectGenericModalToLarge();
    }
    const modalDOM = $("#input-generic-modal");
    modalDOM.find("h5").text(heading);
    modalDOM.find("#input_body_id").html(body_content);
    modalDOM.find("#input-modal-confirmation").text(buttonText);
    modalDOM.find("#input-modal-confirmation").attr("data-form-id", body_content.find("form").attr("id"));
    modalDOM.find("#input-modal-confirmation").attr("data-object-id", object_id);
    modalDOM.find("#input-modal-confirmation").attr("data-object-url", submit_url);
    modalDOM.find("#input-modal-confirmation").attr("data-object-method", submit_method);
    showModalSubmitButton(modalDOM.find("#input-modal-confirmation"))
    $("#input-generic-modal").modal('show');
}



function changeAcceptRejectGenericModalToLarge() {
    $("#input-generic-modal .modal-dialog").addClass("modal-xl");

}


function changeAcceptRejectGenericModalToNormalSize() {
    $("#input-generic-modal .modal-dialog").removeClass("modal-xl");
}