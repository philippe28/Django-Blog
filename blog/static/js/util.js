$(document).ready(function () {

    $(".menu-responsivo").click(function () {
        console.log("click menu")
        if ($(this).find('ul').css('display') == 'none') {
            $(this).find('ul').css("display", "block");
        } else {
            $(this).find('ul').css("display", "none");
        }


    });
});