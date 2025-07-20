$("#create_manifest_form_id").on("submit", async function (e) {
    e.preventDefault();
    e.stopPropagation();
    if ($("#create_manifest_form_id").valid()) {
        const button = hideSubmitButton($(this).attr("id"));
        const formData = $(this).serializeArray();
        const json_obj = convertSerializerArrToJson(formData, list_fiels_names = []);
        const submit_url = $(this).data("url");
        const submit_method = $(this).data("method");

        var { status, data } = await sendRequestPromise(submit_method, submit_url, json_obj);

        if (status) {
            $('#example1')
            var table = $('#example1').DataTable();

            // Clear all rows once, **before** the loop
            table.clear();

            data.forEach((obj, index) => {
                let row = [
                    // <td><input type="checkbox" name="Add" id="chk1" /></td>
                    // <td><input type="checkbox" name="Remove" id="chk2" /></td>
                    obj.tracking_number || "",
                    `<input type="checkbox" name="Add" class="add-to-manifest" value="${obj.id || ""}" data-url="${obj.manifest_check_airwaybill || ""}" />`, // Editable input field
                    `<input type="checkbox" name="Remove" class="remove-from-manifest" value="${obj.id || ""}" />`, // Editable input field
                    obj.shipper_company_name || "",
                    obj.shipper_address || "",
                    obj.shipper_city || "",
                    obj.shipper_post_code || "",
                    obj.country || "Pakistan",
                    obj.reciever_company_name || "",
                    obj.reciever_address || "",
                    obj.reciever_city || "",
                    obj.reciever_post_code || "",
                    obj.reciever_mobile_number || "",
                    obj.reciever_country || "",
                    obj.reciever_post_code || "",
                    obj.pieces || "",
                    obj.weight || "",
                    
                    // obj.data?.dimensions?.volumetric_weight || "",
                    obj.quantites || "",
                    obj.bill_total || "",
                    // obj.data?.invoice_details?.quantity || "",
                    // obj.data?.invoice_details?.total || "",
                    obj.hs_title.join(" , ") || "",
                    obj.hs_code.join(" , ") || "",
                    obj.bag_number || "",
                    obj.tracking_number || "",
                    
                    obj.service_id || "",
                    obj.reciever_contact_person || "",
                    obj.notes || ""
                ];

                table.row.add(row); // Add plain array, not HTML
            });

            // Draw once, after all rows are added
            table.draw();


        }
        showSubmitButton(button);
        return false;
    }
})



$(document).on('keydown', '.notes-input', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault(); // Prevent form submission or other default behavior
            const $input = $(this);
            const value = $input.val().trim();
            // Replace input with plain text inside the cell
            const $cell = $input.closest('.dtr-data');
            
            $cell.text(value);
        }
    });

    // Handle checkbox click
$(document).on('click', '.remove-from-manifest', function () {
    
    var table = $('#example1').DataTable();
    // Get the row of the clicked checkbox
    var row = $(this).closest('tr');
    
    // Remove the row from DataTable (not just DOM)
    table.row(row).remove().draw();
});


$(document).on('click', '.add-to-manifest', function () {
    var submit_method = "POST"
    var submit_url = $(this).attr("data-url")
    var value = $(this).val()
    json_obj = {"id": value}
    var { status, data } = sendRequest(submit_method, submit_url, json_obj);
        if (status) {
           
        }
});