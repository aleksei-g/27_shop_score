$(document).ready(function(){
    if (WaitTimeInSeconds < 420) $('.dynamic_color').css({color: 'forestgreen'});
    else if ((WaitTimeInSeconds > 420) && (WaitTimeInSeconds < 1800))
    $('.dynamic_color').css({color: 'darkorange'});
    else  $('.dynamic_color').css({color: 'firebrick'});
});