var S = KISSY;
S.config({
    packages:[{
        name:"kg",path:"http://g.tbcdn.cn/kg/",charset:"utf-8",ignorePackageNameInUri:true
    }]});
if (S.Config.debug){
    var srcPath = "../";
    S.config({packages:[{name:"kg/countdown/2.0.1",path:srcPath,charset:"utf-8",ignorePackageNameInUri:true}]});}

KISSY.use('kg/countdown/2.0.1/', function (S, Countdown) {
    S.all('#countdown .cd, #demo2 .cd').each(function(node) {
        Countdown({
            el: node
        });
    });
})