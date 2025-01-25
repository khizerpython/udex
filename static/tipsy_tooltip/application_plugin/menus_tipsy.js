
function tooltips() {
tippy('#createMenuButton', {
    content: 'create menu',
    placement: 'bottom',
    animation: 'scale',

},
);
tippy('#createMenuResetButton', {
    content: 'reset',
    placement: 'bottom',
    animation: 'scale',
},
);

tippy('#updateMenuButton', {
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


tippy('.edit-icon-class', {
    content: 'Edit',
    placement: 'left',
    animation: 'scale',
},
);
tippy('.bi-trash', {
    content: 'Delete',
    placement: 'left',
    animation: 'scale',
},
);

tippy('.bi-x-circle', {
    content: 'Inactive',
    placement: 'left',
    animation: 'perspective',
});

tippy('.bi-check-circle', {
    content: 'Active',
    placement: 'left',
    animation: 'perspective',
});

tippy('.bi-eye', {
    content: 'Details',
    placement: 'left',
    animation: 'perspective',
});
tippy('.bi-eye-fill', {
    content: 'Details',
    placement: 'left',
    animation: 'perspective',
});

}

tooltips()


