
function tooltips() {
    
tippy('#create_role_button', {
    content: 'Click to create right',
    placement: 'bottom',
    animation: 'perspective',
});

tippy('#create_reset_button', {
    content: 'Click to reset form',
    placement: 'bottom',
    animation: 'perspective',
});

tippy('#edit_role_button', {
    content: 'Click to edit right',
    placement: 'bottom',
    animation: 'perspective',
});

tippy('#edit_reset_button', {
    content: 'Back',
    placement: 'bottom',
    animation: 'perspective',
});

tippy('.edit-click-class', {
    content: 'Edit record',
    placement: 'left',
    animation: 'perspective',
});
tippy('.separate-edit-click-class', {
    content: 'Edit record',
    placement: 'left',
    animation: 'perspective',
});

tippy('.delete-click-class', {
    content: 'Delete record',
    placement: 'left',
    animation: 'perspective',
});

tippy('.bi-x-circle', {
    content: 'Record is inactive',
    placement: 'left',
    animation: 'perspective',
});

tippy('.bi-check-circle', {
    content: 'Record is active',
    placement: 'left',
    animation: 'perspective',
});

tippy('#role_creation_order_help_id', {
    content: 'This field will be used to sort rights in the overall application for a better user experience.',
    placement: 'left',
    animation: 'perspective',
});


tippy('.show-menus-of-roles', {
    content: 'Click to see assigned menu(s) of this right',
    placement: 'left',
    animation: 'perspective',
});
}


tooltips()