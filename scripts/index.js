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
});

//返回顶部的函数
function retunTop(){
    $('body,html').animate({scrollTop:0},1000);
    return false;
}