<tm title=Gartner Europe Error>
<%@ page import="javax.servlet.jsp.JspException" %>
<%@ page language="java" isErrorPage="true" %>
<%@ page import="javax.servlet.http.HttpServletRequest"%>
<tm style=http://www4.gartner.com/css/win/newAdmin.css>
<tm jsInclude=stylesheet.incl>


<!--
Site Index
-->

<table border="0" cellspacing="0" cellpadding="0" width="100%">
    <tr>
        <td height="3"><img src="//img/trans_pixel.gif" alt="" border="0" height="3"></td>
    </tr>

    <tr class="contentCell">
        <td height="20"  vAlign="center" class="crumbBold" bgcolor="#cccc99">
   <a class=topNavText href="http://www4.gartner.com/6_help/help_overview.html"> Help </A>   >   Site Index
        </td>
    </tr>
    <tr>
        <td height="5" width="595"><img src="//img/trans_pixel.gif" alt="" border="0" height="5" width="595"></td>
    </tr>
    <tr>
        <td class="contentText">
error message is: <p />

<%=exception.getMessage()%>

<p/>
        </td>
    </tr>

    <tr>
        <td>
<tm src=06_site_index_detail.incl>
        </td>
    </tr>
</table>
