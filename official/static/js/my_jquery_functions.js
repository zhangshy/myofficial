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
});