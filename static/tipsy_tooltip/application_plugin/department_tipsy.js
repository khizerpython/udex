

function tooltips() {
    
tippy('#createDepartmentButton', {
    content: 'create department',
    placement: 'bottom',
    animation: 'scale',

},
);
tippy('#createDepartmentResetButton', {
    content: 'reset',
    placement: 'bottom',
    animation: 'scale',
},
);

tippy('#updateDepartmentButton', {
    content: 'Update',
    placement: 'bottom',
    animation: 'scale',
},
);
tippy('#backToOriginalView', {
    content: 'Back',
    placement: 'bottom',
    animation: 'scale',
},
);


 var edit_button = tippy('.edit-icon-class', {
    content: 'Edit',
    placement: 'left',
    animation: 'scale',
},
);
var delete_button = tippy('.bi-trash', {
    content: 'Delete',
    placement: 'left',
    animation: 'scale',
},
);

var inactive_button = tippy('.bi-x-circle', {
    content: 'Inactive',
    placement: 'left',
    animation: 'perspective',
});

var active_button = tippy('.bi-check-circle', {
    content: 'Active',
    placement: 'left',
    animation: 'perspective',
});

    
}


tooltips()