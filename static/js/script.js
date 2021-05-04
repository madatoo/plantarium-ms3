$(document).ready(function(){
    //sidenavbar inititialization
    $('.sidenav').sidenav({edge:"right"});
    //carousel
    $('#carousel-auto').carousel({fullWidth: true});
      setInterval(function() {
      $('#carousel-auto').carousel('next');
    }, 1800);
    //add plant form
    $('select').formSelect();
    $('input#plant_name, textarea#plant_description,textarea#plant_tips, texarea#plant_more_info, texarea#plant_notes').characterCounter();
    $('#plant_description').val('');
      M.textareaAutoResize($('#plant_description'));   



});
