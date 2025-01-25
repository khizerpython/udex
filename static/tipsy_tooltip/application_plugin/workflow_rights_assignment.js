
function tooltips() {
    
    tippy('#edit_role_button', {
        content: 'Click to update workflow rights',
        placement: 'bottom',
        animation: 'perspective',
    });
    
    tippy('#edit_reset_button', {
        content: 'Back',
        placement: 'bottom',
        animation: 'perspective',
    });
    
    tippy('.bi-pencil-square', {
        content: 'Edit workflow rights',
        placement: 'left',
        animation: 'perspective',
    });
    
    }
    
    
    tooltips()