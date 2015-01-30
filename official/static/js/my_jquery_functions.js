$(document).ready(function() {
    $("p.disappear").click(function(){
        $(this).hide();
    });
    $(".ex .hide").click(function() {
        $(this).parent(".ex").hide("slow");
    });
    $(".toggle .btn_toggle").click(function() {
        $(this).parent(".toggle").children(".ex").toggle("slow");
    });
    $(".flip").click(function() {
        $(".panel").slideToggle(1000);//1s
    });
    $("button.btn_animate").click(function() {
        var div = $("div.div_animate");
        div.animate({left:'100px', opacity:'0.4'}, "slow", function() {
            div.css("color","red");
        });
        div.animate({fontSize:'3em'}, "slow", function() {
            div.css("color","blue");
        });
        div.animate({fontSize:'1em'}, "slow");
        div.animate({left:'0px', opacity:'1'}, "slow");
    });
});