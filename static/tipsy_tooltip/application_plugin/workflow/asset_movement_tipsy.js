function tooltips() {

    tippy('#initiateAssetMovementWorkflowButton', {
        content: 'Initiate',
        placement: 'bottom',
        animation: 'scale',
    
    },
    );
    tippy('#reinitiateAssetMovementWorkflowButton', {
        content: 'Reinitiate',
        placement: 'bottom',
        animation: 'scale',
    
    },
    );


    
    tippy('#file_help_id', {
        content: ALLOWED_FILE_EXTENSION_ERROR_MESSAGE,
        placement: 'right',
        animation: 'perspective',
    });

    tippy('#cancelReInitiateAssetMovementWorkflowButton', {
        content: 'Cancel',
        placement: 'bottom',
        animation: 'scale',
    
    },
    );
    tippy('.reinitiate-workflow-class', {
        content: 'Reinitiate',
        placement: 'left',
        animation: 'scale',
    
    },
    );
    tippy('#resetAssetMovementWorkflowButton', {
        content: 'reset',
        placement: 'bottom',
        animation: 'scale',
    },
    );
    tippy('.accept-workflow-class', {
        content: 'Accept',
        placement: 'left',
        animation: 'scale',
    },
    );
    tippy('.show-comment-workflow-class ', {
        content: 'History',
        placement: 'left',
        animation: 'perspective',
    });
    
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
    
    tippy('.delete-icon-class', {
        content: 'Reject',
        placement: 'left',
        animation: 'perspective',
    });
    
    
    // tippy('.bi-arrow-clockwise', {
    //     content: 'Reinitite',
    //     placement: 'left',
    //     animation: 'perspective',
    // });
    tippy('.close-workflow-class', {
        content: 'Close',
        placement: 'left',
        animation: 'perspective',
    });
    tippy('.show-asset-ids', {
        content: 'Asset Ids',
        placement: 'left',
        animation: 'perspective',
    });
    
    
    }
    
    tooltips()