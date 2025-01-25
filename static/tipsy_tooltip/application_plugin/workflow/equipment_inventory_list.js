function tooltips() {

    tippy('#createEquipmentInventoryListWorkflowButton', {
        content: 'initiate workflow',
        placement: 'bottom',
        animation: 'scale',
    
    },
    );
    tippy('#createEquipmentInventoryListWorkflowResetButton', {
        content: 'reset',
        placement: 'bottom',
        animation: 'scale',
    },
    );

    tippy('.reinitiate-button', {
        content: 'Re-initiate',
        placement: 'left',
        animation: 'scale',
    },
    );
    
    tippy('.close-workflow-class', {
        content: 'Close Worklow',
        placement: 'left',
        animation: 'perspective',
    });
    
    tippy('.bi-eye', {
        content: 'History',
        placement: 'left',
        animation: 'perspective',
    });
    tippy('.bi-arrow-clockwise', {
        content: 'Re-initiate',
        placement: 'left',
        animation: 'perspective',
    });
    tippy('#file_help_id', {
        content: ALLOWED_FILE_EXTENSION_ERROR_MESSAGE,
        placement: 'right',
        animation: 'perspective',
    });
    tippy('#reinitiateEquipmentInventoryListWorkflowButton', {
        content: 'Re-initiate',
        placement: 'bottom',
        animation: 'perspective',
    });
    tippy('#reinitiateEquipmentInventoryListWorkflowResetButton', {
        content: 'Cancel',
        placement: 'bottom',
        animation: 'perspective',
    });
    tippy('.reject-workflow-class', {
        content: 'Reject',
        placement: 'left',
        animation: 'perspective',
    });
    tippy('.accept-workflow-class', {
        content: 'Accept',
        placement: 'left',
        animation: 'perspective',
    });
    
    
    }
    
    tooltips()