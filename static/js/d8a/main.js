$(document).ready(function(){

    /* NAVIGATION */
    $('#main-nav li:first').addClass('last');
    $('#nav-projects li:first').addClass('last');
	$('#nav-product li:first').addClass('last');
    $('#nav-solutions li:first').addClass('last');
    $('#pre-header-social-links li:last').addClass('last');


    /* HOME PAGE */
    $('#home-carousel').carousel({ interval:5000 });
    $('#home-process .process-step img')
        .mouseenter(function(){
            $('#home-process-details > div').hide();
            $('#home-process-details > div#home-process-details-' + $(this).data('target')).show();
        })
        .mouseleave(function(){
            $('#home-process-details > div').hide();
            $('#home-process-details > div#home-process-details-none').show();
        });

    /* PROJECTS */
    $('.project-thumbnail')
        .click(function(){
            var target = $(this).data('target');
            $(window).scrollTop($('.project-details-container').offset().top - 120);
            $('.project-details-container > div:visible').fadeOut(function(){
                $('.project.' + target).fadeIn();
            })
        })
        .mouseenter(function(){
            $(this).find('img').animate({opacity: 1}, 200);
        })
        .mouseleave(function(){
            $(this).find('img').animate({opacity: 0.6}, 200);
        });

    /* product */
    $('.product-thumbnail')
        .click(function(){
            var target = $(this).data('target');
            $(window).scrollTop($('.product-details-container').offset().top - 120);
            $('.product-details-container > div:visible').fadeOut(function(){
                $('.product.' + target).fadeIn();
            })
        })
        .mouseenter(function(){
            $(this).find('img').animate({opacity: 1}, 200);
        })
        .mouseleave(function(){
            $(this).find('img').animate({opacity: 0.6}, 200);
        });


    /* CAPABILITIES */
    $('.capability-thumbnail')
        .click(function(){
            var target = $(this).data('target');
            $(window).scrollTop($('.capability-details-container').offset().top - 120);
            $('.capability-details-container > div:visible').fadeOut(function(){
                $('.capability.' + target).fadeIn();
            })
        })
        .mouseenter(function(){
            $(this).find('img').animate({opacity: 1}, 200);
        })
        .mouseleave(function(){
            $(this).find('img').animate({opacity: 0.6}, 200);
        });


    /* clients */
    $('.client-thumbnail')
        .click(function(){
            var target = $(this).data('target');
            $(window).scrollTop($('.client-details-container').offset().top - 120);
            $('.client-details-container > div:visible').fadeOut(function(){
                $('.client.' + target).fadeIn();
            })
        })
        .mouseenter(function(){
            $(this).find('img').animate({opacity: 1}, 200);
        })
        .mouseleave(function(){
            $(this).find('img').animate({opacity: 0.6}, 200);
        });
});
