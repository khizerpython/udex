
function cleanGenericModal() {
    changeGenericModalToNormalSize()
    const modalDOM = $("#generic-display-modal");
    modalDOM.find("h5").text("");
    modalDOM.find("#generic-display-modal-body-id").text("");
}

function setGenericModal(heading, bodyHTML, large_modal=false) {
    cleanGenericModal();
    if (large_modal) {
        changeGenericModalToLarge();
    }

    const modalDOM = $("#generic-display-modal");
    modalDOM.find("h5").text(heading);
    modalDOM.find("#generic-display-modal-body-id").html(bodyHTML);
    $("#generic-display-modal").modal('show');
}

function changeGenericModalToLarge() {
    $("#generic-display-modal .modal-dialog").addClass("modal-xl");
    $("#generic-display-modal-body-id").css({"height":"70vh", "overflow-y":"auto"})

    // Setting history modal navigations
    // var footer = $("#generic-display-modal").find(".modal-footer");
    // var closebtn = footer.find('.btn-secondary');
    // var closebtn_clone = closebtn.clone()
    // var carousel_nav = $("<div>").addClass("modal-carousel-nav flex-md-row flex-column")
    // footer.before(carousel_nav)
    // var prev_button = $("<button>").addClass("btn btn-primary carousel-prev-btn disabled carousel-control-custom").attr("data-bs-target", "#workflowHistoryCarousel").attr("data-bs-slide", "prev");
    // prev_button.append($("<span>").text("Prev"))
    // var indicators_div = $("<div>").addClass("_carousel-indicators")
    // for (var i=0; i<5; i++){
    //     var indicators = $("<button>").attr({
    //         "type":"button",
    //         "data-bs-target":"#workflowHistoryCarousel",
    //         "data-bs-slide-to":i,
    //     })
    //     if(i == 0){
    //         indicators.addClass("active");
    //     }
    //     indicators.appendTo(indicators_div)
    // }
    // var next_button = $("<button>").addClass("btn btn-primary carousel-next-btn carousel-control-custom").attr("data-bs-target", "#workflowHistoryCarousel").attr("data-bs-slide", "next");
    // next_button.append($("<span>").text("Next"))
    // var nav_div = $("<div>").addClass("d-flex justify-content-center col-md-5");
    // var step_number = $("<div>").addClass("d-flex")
    // step_number.append($("<span>").addClass("step-num").text("STEP 1"))
    // nav_div.append(prev_button, indicators_div, next_button)
    // carousel_nav.append(step_number, nav_div)
    // Append Close btn
    // carousel_nav.append($("<div>").addClass("d-flex").append(closebtn_clone))
    // Hide modal footer for history modal
    // footer.addClass('d-none')

}
function changeGenericModalToNormalSize() {
    $("#generic-display-modal .modal-dialog").removeClass("modal-xl");
    $("#generic-display-modal-body-id").css({"height":"", "overflow-y":""})
    // Display modal footer
    $("#generic-display-modal").find(".modal-footer").removeClass('d-none')
    // Remove history modal navigation
    $("#generic-display-modal").find(".modal-carousel-nav").remove()

}
