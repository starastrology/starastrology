<?php
// Exit if accessed directly
if ( !defined( 'ABSPATH' ) ) exit;

// BEGIN ENQUEUE PARENT ACTION
// AUTO GENERATED - Do not modify or remove comment markers above or below:

if ( !function_exists( 'chld_thm_cfg_locale_css' ) ):
    function chld_thm_cfg_locale_css( $uri ){
        if ( empty( $uri ) && is_rtl() && file_exists( get_template_directory() . '/rtl.css' ) )
            $uri = get_template_directory_uri() . '/rtl.css';
        return $uri;
    }
endif;
add_filter( 'locale_stylesheet_uri', 'chld_thm_cfg_locale_css' );
         
if ( !function_exists( 'child_theme_configurator_css' ) ):
    function child_theme_configurator_css() {
        wp_enqueue_style( 'chld_thm_cfg_child', trailingslashit( get_stylesheet_directory_uri() ) . 'style.css', array( 'hello-elementor','hello-elementor','hello-elementor-theme-style','hello-elementor-header-footer' ) );
    }
endif;
add_action( 'wp_enqueue_scripts', 'child_theme_configurator_css', 10 );

// END ENQUEUE PARENT ACTION
/*function wpb_hook_javascript() {
    if (is_page ('2')) { 
      ?>
          <script type="text/javascript">

            window.onscroll = function(){
                if(pageYOffset >= 100){
                    //window.alert("hello");
                    document.getElementById('scroll-btn').style.visibility="visible";
                }
                else{
                    document.getElementById('scroll-btn').style.visibility="hidden";
                }
            }


            document.getElementById('home-viewproductsbutton').addEventListener('click', function() {
            document.getElementById('serviceheading').scrollIntoView({behavior: "smooth"});
            });

            document.getElementById('scroll-btn').addEventListener('click', function() {
            document.getElementById('scroll-btn').style.visibility="hidden";
            document.getElementById('top-scroll').scrollIntoView({behavior: "smooth"});
            });


          </script>
      <?php
    }
  }*/
  //add_action('wp_footer', 'wpb_hook_javascript');


// break












