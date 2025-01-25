function tooltips() {

    tippy('#createChangeManagementWorkflowButton', {
        content: 'initiate workflow',
        placement: 'bottom',
        animation: 'scale',
    
    },
    );
    tippy('#createChangeManagementWorkflowResetButton', {
        content: 'reset',
        placement: 'bottom',
        animation: 'scale',
    },
    );
    
    tippy('#show_comments_button', {
        content: 'Workflow Comments',
        placement: 'left',
        animation: 'scale',
    },
    );
    tippy('.close-change-management-workflow-modal', {
        content: 'Close request',
        placement: 'left',
        animation: 'scale',
    },
    );
    
    
    tippy('#show_comments_button', {
        content: 'Comments',
        placement: 'left',
        animation: 'scale',
    },
    );
    tippy('.reinitiate-button', {
        content: 'Reinitiate',
        placement: 'left',
        animation: 'scale',
    },
    );
    
    tippy('.close-workflow-class-modal', {
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
        content: 'Re initiate',
        placement: 'left',
        animation: 'perspective',
    });
    tippy('#reinitiateChangeManagementWorkflowButton', {
        content: 'Re initiate',
        placement: 'bottom',
        animation: 'perspective',
    });
    tippy('#reinitiateChangeManagementWorkflowResetButton', {
        content: 'Cancel',
        placement: 'bottom',
        animation: 'perspective',
    });
    tippy('.reject-workflow-class', {
        content: 'Reject',
        placement: 'left',
        animation: 'perspective',
    });
    tippy('#file_help_id', {
        content: ALLOWED_FILE_EXTENSION_ERROR_MESSAGE,
        placement: 'right',
        animation: 'perspective',
    });
    tippy('.accept-workflow-class', {
        content: 'Accept',
        placement: 'left',
        animation: 'perspective',
    });
    
    
    }
    
    tooltips()