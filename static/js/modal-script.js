
function cleanModal() {
    const modalDOM = $("#generic-modal");
    modalDOM.find("h5").text("");
    modalDOM.find("#sub_body_id").text("");
    modalDOM.find("#modal-confirmation").removeAttr("onClick");
    modalDOM.find("#modal-confirmation").removeAttr("data-delete-id");
    modalDOM.find("#modal-confirmation").removeAttr("data-delete-url");
    modalDOM.find("#modal-confirmation").removeAttr("data-delete-method");
    modalDOM.find("#modal-confirmation").text("");
}

function setModal(heading, bodyText, buttonText, delete_id, delete_url, delete_method) {
    cleanModal()
    const modalDOM = $("#generic-modal");
    modalDOM.find("h5").text(heading);
    modalDOM.find("#sub_body_id").text(bodyText);
    modalDOM.find("#modal-confirmation").text(buttonText);
    modalDOM.find("#modal-confirmation").attr("data-delete-id", delete_id);
    modalDOM.find("#modal-confirmation").attr("data-delete-url", delete_url);
    modalDOM.find("#modal-confirmation").attr("data-delete-method", delete_method);
    showModalSubmitButton(modalDOM.find("#modal-confirmation"))
    $("#generic-modal").modal('show');
}


