$(function(){
    $(document).ready(function(){

        
        //Responsive Menu

        $('.toggle-class').on('click', function(){
            $('.main-menu').toggleClass('show');
        });

        $('.toggle-social').on('click', function(){
            $('.social-menu').toggleClass('slide')
        })

        //Typed jquery

        var typed = new Typed('.typ', {
            strings: ['null'],
            typeSpeed: 50,
            backSpeed: 200,
            loop: false,
            shuffle: false,
        });

        // Team Slider

        $('.team-slide').slick({
            centerMode: true,
            centerPadding: '00px',
            slidesToShow: 5,
            dots: false,
            arrows: false,
            //autoplay: 3000,
            responsive: [
                {
                  breakpoint: 1199,
                  settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: false
                  }
                },
                {
                    breakpoint: 992,
                    settings: {
                      slidesToShow: 3,
                      slidesToScroll: 1
                    }
                  },
                {
                  breakpoint: 768,
                  settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                  }
                },
                {
                  breakpoint: 576,
                  settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                  }
                }
                
              ]
        });

    });
});