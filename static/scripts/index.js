/**
 * Created by Jonny on 2015/3/29.
 */
$(function() {

    //caches a jQuery object containing the header element
    var toTop = $(".btnTop");

    //自动返回顶端
    toTop.click(function(){
        retunTop();
    });
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        if (scroll <= 300) {
            toTop.removeClass('scrolled');
        } else {
            toTop.addClass("scrolled animated fadeInDown");
        }
    });

    $('a[href^="#"]').bind('click.smoothscroll',function (e) {
        e.preventDefault();

        var target = this.hash,
            $target = $(target);

        $('html, body').stop().animate({
            'scrollTop': $target.offset().top-50
        }, 300, 'swing', function () {
            window.location.hash = target;
        });
    });
    overlayOn = function()
    {
        $( '<div id="imagelightbox-overlay"></div>' ).appendTo( 'body' );
    },
    overlayOff = function()
    {
        $( '#imagelightbox-overlay' ).remove();
    },
    activityIndicatorOn = function()
    {
        $( '<div id="imagelightbox-loading"><div></div></div>' ).appendTo( 'body' );
    },
    activityIndicatorOff = function()
    {
        $( '#imagelightbox-loading' ).remove();
    },

    $( 'a[data-imagelightbox="b"]' ).imageLightbox(
        {
            onStart:     function() { overlayOn(); },
            onEnd:       function() { overlayOff(); activityIndicatorOff(); },
            onLoadStart: function() { activityIndicatorOn(); },
            onLoadEnd:   function() { activityIndicatorOff(); }
        });
});

//返回顶部的函数
function retunTop(){
    $('body,html').animate({scrollTop:0},1000);
    return false;
}