function tooltips() {

tippy('#createAuthuserButton', {
    content: 'create user',
    placement: 'bottom',
    animation: 'scale',

},
);
tippy('#createAuthuserResetButton', {
    content: 'reset',
    placement: 'bottom',
    animation: 'scale',
},
);

tippy('#updateAuthuserButton', {
    content: 'Update User',
    placement: 'bottom',
    animation: 'scale',
},
);
tippy('#updateAuthuserEditButton', {
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

tippy('#username_help_id', {
    content: 'The min & max length of username should be 3 & 25 respectively. username should start with small OR capital letter follow with special characters @ # . - _',
    placement: 'right',
    animation: 'perspective',
});

tippy('.re-generate-activation-link-click-class', {
    content: 'Re-generate user activation link. The link will be delivered to the registered email of the user.',
    placement: 'right',
    animation: 'perspective',
});


}

tooltips()

