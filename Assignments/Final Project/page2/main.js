

var swiper = new Swiper(".home",{
    effect:'fade',
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay : 5000,
        disableOnInteraction: false,
    },

    navigation:{
        nextE1:'.swiper-button-next',
        prevE1:'.swiper-button-prev',
    },
    pagination:{
        el:".swiper-pagination",
        clickable: true,
    },
    
});




let navText = ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"]
$('#must-slide').owlCarousel({
    margin:10,
    items: 5,
    dots: false,
    loop: false,
    autoplay: false,
    nav:true,
    navText: navText,
    slideBy:5,
    
    autoplayHoverPause: true,
    responsive: {
        500: {
            items:5
        },
        1280: {
            items:6.5
        },
        1600: {
            items:8.5
        }
    }
   


});

$('#ing-slide').owlCarousel({
    items:5,
    margin:10,
    dots: false,
    loop: false,
    autoplay: false,

    autoplayHoverPause: true,

    responsive: {
        500: {
            items:5
        },
        1280: {
            items:6.5
        },
        1600: {
            items:8.5
        }
    
    }
});

$('#like-slide').owlCarousel({
    items:5,
    margin:10,
    dots: false,
    loop: false,
    autoplay: false,
    nav:true,
    navText:navText,
    slideBy:5,
    

    autoplayHoverPause: true,
    responsive: {
        500: {
            items:5
        },
        1280: {
            items:6.5
        },
        1600: {
            items:8.5
        }
    }
});

$(document).ready(function(){ 
   
    $(window).scroll(function(){
       if ($(this).scrollTop() <150) {
          $('.menuBar').css('opacity', 0.9);
       }
       else  {
          $('.menuBar').css('opacity',0.4);
       }
    });
 })





