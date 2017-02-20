<script LANGUAGE="JavaScript">
function openSigninPopup(href) 
{
    var iMyLeft;
    var iMyTop;
    var sWinStr;
    //gets top and left positions based on user's resolution so hint window is centered.
    iMyLeft = (window.screen.width/2) - (140 + 10); //half the screen width minus half the new window width (plus 5 pixel borders).
    iMyTop = (window.screen.height/2) - (135 + 27); //half the screen height minus half the new window height (plus title and status bars).
    sWinStr="left=" + iMyLeft + ",top=" + iMyTop + ",screenX=" + iMyLeft + ",screenY=" + iMyTop;
    self.name = "europe_gartner_com_homepage";
    
    signinPopup = window.open(href,'LoginPopup', sWinStr + ',height=275,width=280,scrollbars=no,menubar=no');
       
    var killPopup = setTimeout("signinPopup.close()", 180000);
}
</script>
