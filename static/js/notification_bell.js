$(document).on('click','#my_notification_bell_icon',function(e){
    e.preventDefault();
    window.location.href = $(this).attr('data-href')
})