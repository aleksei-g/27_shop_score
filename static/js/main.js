$(document).ready(function(){
    if (WaitTimeInSeconds < 420) $('.wait-time-text').css({color: 'forestgreen'});
    else if ((WaitTimeInSeconds > 420) && (WaitTimeInSeconds < 1800))
    $('.wait-time-text').css({color: 'darkorange'});
    else  $('.wait-time-text').css({color: 'firebrick'});
});