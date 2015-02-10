function changyan(){
    var appid = 'cyrCnFEuY',
    conf = 'prod_5ab7e5e5771bb2b8b11c9edf3923c384';
    var doc = document,
    s = doc.createElement('script'),
    h = doc.getElementsByTagName('head')[0] || doc.head || doc.documentElement;
    s.type = 'text/javascript';
    s.charset = 'utf-8';
    s.src =  'http://assets.changyan.sohu.com/upload/changyan.js?conf='+ conf +'&appid=' + appid;
    h.insertBefore(s,h.firstChild);
    window.SCS_NO_IFRAME = true;
  }

function vote_img(image_id) {
    var xmlhttp;
    var txt,x,i;
    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    }
    else {// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4 && xmlhttp.status==200) {
          document.getElementById("vote_image_"+image_id).innerHTML =xmlhttp.responseText;
        }
      }
    xmlhttp.open("GET","/vote/img?id="+image_id,true);
    xmlhttp.send();
}