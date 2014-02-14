jQuery(document).ready(function() {

    $(".postTitle, .postTitleWithImage").hover(function() {
      $(this).stop().animate({opacity: "0.8"}, 300);
     
    },
    function() {
       $(this).stop().animate({opacity: "1"}, 300);
  
    });

                        
  	//Hide the tooglebox when page load
jQuery(".togglebox").hide();
//slide up and down when click over heading 2
jQuery(".toggle_anchor").click(function(){
// slide toggle effect set to slow you can set it to fast too.
jQuery(this).next(".togglebox").slideToggle("medium");
return true;
});

    jQuery('.toggle_anchor_active').click();
jQuery(".toggle_anchor").click(function(){
// slide toggle effect set to slow you can set it to fast too.
jQuery(this).toggleClass('anchor_active');

});
               jQuery('#s').attr('placeholder', 'Search ...');
      jQuery('#s').on('click', function() {
         
         jQuery(this).attr('placeholder', '');
         
         
      });
      
  jQuery('.search a').on('click', function(e) {
         
      
       e.preventDefault();

      
      });
               
      jQuery('.search').on('click', function() {
         
      
         jQuery(this).find('.icon-search').fadeToggle(0);
           jQuery(this).find('.icon-cancel').fadeToggle(0);
           jQuery(this).toggleClass('searchActive')
           jQuery('.topBarSearch').slideToggle(200);

      
      });
  
    
    $(".dd_causes_widget li, .causeTitle").hover(function() {
      $(this).find('img').stop().animate({opacity: "0.6"}, 300);
       $(this).find('ul').stop().animate({bottom: "25%"}, 200);
    },
    function() {
       $(this).find('img').stop().animate({opacity: "1"}, 300);
        $(this).find('ul').stop().animate({bottom: "20%"}, 200);
    });

function logo() {
    
    
 var offset = jQuery('.mainNav').offset().left - 10;
        jQuery('.sliderLogo').css('left', offset);

}

function prettyPhoto() {
    
    jQuery("area[rel^='prettyPhoto']").prettyPhoto();
				
				jQuery(".gallery:first a[rel^='prettyPhoto']").prettyPhoto({animation_speed:'normal',theme:'light_square',slideshow:3000, autoplay_slideshow: false});
				jQuery(".gallery:gt(0) a[rel^='prettyPhoto']").prettyPhoto({animation_speed:'fast',slideshow:10000, hideflash: true});
		
				jQuery("#custom_content a[rel^='prettyPhoto']:first").prettyPhoto({
					custom_markup: '<div id="map_canvas" style="width:260px; height:265px"></div>',
					changepicturecallback: function(){initialize();}
				});

				jQuery("#custom_content a[rel^='prettyPhoto']:last").prettyPhoto({
					custom_markup: '<div id="bsap_1259344" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6"></div><div id="bsap_1237859" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6" style="height:260px"></div><div id="bsap_1251710" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6"></div>',
					changepicturecallback: function(){_bsap.exec();}
				});
    
}



 function mobileMenu() {
            
        // Create the dropdown base
        jQuery("<select />").appendTo("nav .container .sixteen");
        jQuery("nav select").hide();
        
        // Create default option "Go to..."
        jQuery("<option />", {
            "selected": "selected",
            "value"   : "",
            "text"    : "Go"
        }).appendTo("nav select");

        // Populate dropdown with menu items
        jQuery(".mainNav a").each(function() {
            var el = jQuery(this);
            $("<option />", {
                "value"   : el.attr("href"),
                "text"    : el.text()
            }).appendTo("nav select");
        });

        jQuery("nav select").change(function() {
            window.location = jQuery(this).find("option:selected").val();
        });
            
        }
        
          
        function select() {
            
        
              // FOR EACH SELECT
    jQuery('nav select').each(function() {
        
        // LET'S PUT OUR MARKUP BEFORE IT
        jQuery(this).before('<div class="select-wrapper">');
        
        // LETS PUR OUR MARKUP AFTER IT
        jQuery(this).after('<span class="select-container"></span></div>');
        
        // UPDATES THE INITIAL SELECTED VALUE
        var initialVal = jQuery(this).children('option:selected').text();
        jQuery(this).siblings('span.select-container').text(initialVal);
        
        // HIDES SELECT BUT LET THE USER STILL CLICK IT
        jQuery(this).css({opacity: 0});  
        
        // WHEN USER CHANGES THE SELECT, WE UPDATE THE SPAN BOX
        jQuery(this).change(function() {
            
            // GETS NEW SELECTED VALUE
            var newSelVal = jQuery(this).children('option:selected').text();
            
            // UPDATES BOX
            jQuery(this).siblings('span.select-container').text(newSelVal);
            
        });
        
    }); 
            
        }
        
        function slider() {
      
            $('#carousel').flexslider({
        animation: "slide",
        controlNav: false,
        animationLoop: false,
        slideshow: false,
        itemWidth: 215,
        itemMargin: 20,
        asNavFor: '#slider'
      });
      
      $('#slider').flexslider({
        animation: "slide",
        controlNav: false,
        animationLoop: false,
        slideshow: false,
        sync: "#carousel",
        start: function(slider){
          $('body').removeClass('loading');
        }
      });
      
          jQuery('.sliderWrapper').fadeToggle();
          
          jQuery('#carousel img').css('opacity', 0.35);
          jQuery('#carousel .flex-active-slide img').css('opacity', 1);
          
          jQuery('#carousel li, .flex-next, .flex-prev').on('click', function() {
             
             jQuery('#carousel img').css('opacity', 0.35);
          jQuery('#carousel .flex-active-slide img').css('opacity', 1);
              
          });
		 
            
        }
        
   function megafolio() {
            
            jQuery('.filters a').on('click',function(e){
                
                e.preventDefault();
                
            });
            	var api=jQuery('.megafolio-container').megafoliopro(
						{
							filterChangeAnimation:"rotatescale",			// fade, rotate, scale, scalerotate, pagetop, pagebottom,pagemiddle
							filterChangeSpeed:600,					// Speed of Transition
							filterChangeRotate:99,					// If you ue scalerotate or rotate you can set the rotation (99 = random !!)
							filterChangeScale:0.6,					// Scale Animation Endparameter
							delay:20,
							defaultWidth:980,
							paddingHorizontal:5,
							paddingVertical:5,
							lazyLoadStartEntry:0,
							layoutarray:[7]		// Defines the Layout Types which can be used in the Gallery. 2-9 or "random". You can define more than one, like {5,2,6,4} where the first items will be orderd in layout 5, the next comming items in layout 2, the next comming items in layout 6 etc... You can use also simple {9} then all item ordered in Layout 9 type.

						});

					jQuery('.order').click(function()  { api.megaremix(jQuery(this).data('order')); });
					jQuery('.filter').click(function() { api.megafilter(jQuery(this).data('category')); });


					jQuery(".pad").change(function() {
						var mc = jQuery('.megafolio-container');
						mc.data('paddingh',jQuery("#ph").val());
						mc.data('paddingv',jQuery("#pv").val());
						api.megaremix(api.megagetcurrentorder());
					});
	jQuery(".fancybox").fancybox();

        }
       
    logo(); 
    mobileMenu();
    select();
      slider();
      megafolio();



});

 
jQuery(window).load(function() {       
  

    jQuery('ul.sf-menu').superfish(); 

     jQuery('.flex-active-slide img').addClass('test');
    


});
    
jQuery(window).resize(function() {

    jQuery('.flex-caption div').css('left', 0);
    var offset = jQuery('.mainNav').offset().left;
    jQuery('.sliderLogo').css('left', offset);
 

});