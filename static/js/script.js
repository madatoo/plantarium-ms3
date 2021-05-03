$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});//sidenavbar inititialization
    $(document).ready(function(){//carousel
      $('#carousel-auto').carousel({fullWidth: true});
  setInterval(function() {
    $('#carousel-auto').carousel('next');
  }, 1800);   
  })});
