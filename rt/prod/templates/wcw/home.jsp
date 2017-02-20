<tm jsInclude=00_set_home_tab.incl>
<tm src=home_prehtml.incl>
<tm src=00_set_locale.incl>
<tm title=Gartner Europe>

   <style>
   .bgimg4 {
      background-color: #cccccc ;
      font-family:verdana,arial,helvetica; 
      font-size:11px; 
      color:#333333; 
      font-weight:bold; 
      TEXT-DECORATION: none;
      }
       .contentCell {background-color:#000000;}
   </style>

<%
System.out.println("About to render Table 0");
%>

<!-- Table 0 everything below the header -->
<table border="0" cellpadding="0" cellspacing="0"  bgcolor="black" width="100%" >
<tr>
   <td class="blackBack" bgcolor="black" width="2"><img width="2" src="//img/trans_pixel.gif"></td>
   <td align="center">
<!-- Login.incl start -->
   <tm src=login.incl>
<!-- Login.incl end -->
   </td>
   <td width="2" class="blackBack" bgcolor="black"><img width="2" src="//img/trans_pixel.gif"></td>
</tr>
</table>
<!-- close Table 0--->
<!-- Table I--->
<table border="0" cellpadding="0" cellspacing="0"  bgcolor="white" width="100%">
<tr>
   <td width="2" alt=left border bgcolor="white" rowspan="2"><img width="2" src="//img/trans_pixel.gif"></td>
   <td valign="top" align="left"><!-- Table IA body research area news area events area-->
   <!-- Table IA--->
   <table width="100%" cellpadding="0" cellspacing="0" border="0"  bgcolor="white">
   <tr>
      <td width="15"><img src="//img/trans_pixel.gif" width="15"></td>
      <td valign="top">
      <!-- Table IA-1 research area news area events area-->
      <table width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr>
         <td valign="top" width="270">
         <!-- Table IA-1b-->
         <table width="100%" cellspacing="0" cellpadding="0" border="0">
         <tr>
            <td align="left" valign="top">
<!-- PROMOS worldwide marketing start -->
            <tm src=ww_mkt_camp_left_01.incl>
<!-- PROMOS worldwide marketing end -->
<!-- RESEARCH PROMO regional spotlighted research start -->
            <tm src=reg_spot_research_left_02.incl>
<!-- RESEARCH PROMO regional spotlighted research end -->
<!-- RESEARCH PROMO worldwide spotlighted research start -->
            <tm src=ww_spot_research_left_03.incl>
<!-- RESEARCH PROMO worldwide spotlighted research end -->
            </td>
         </tr>


<!-- Focus Area start -->
         <tr>
            <td align="left" valign="top">
            <tm src=ww_focus_area_center_01.incl>
            </td>
         </tr>
<!-- Focus Area end -->


         </table>
         <!-- close Table IA-1b-->
         </td>
         <td width="16"><img src="//img/trans_pixel.gif" width="16" border="0" alt=""></td>
         <td valign="top">
         <!-- Table IA-1c -->
         <table width="100%" cellspacing="0" cellpadding="0" border="0">
        
          
<!-- News Analysis start-->
         <tr>
            <td>
<hr size=1 color=#CCCCCC noshade>
<!-- NEW ANALYSIS TITLE start -->
<tm src=UI_new_analysis_title.incl>
<!-- NEW ANALYSIS TITLE end -->
<!-- Regional News Analysis start -->
            <tm src=reg_news_analysis_center_02.incl>
<!-- Regional News Analysis end -->
            </td>
         </tr>
         <tr>
            <td align="left" valign="top">


            <div class="textBlackBold" style="position: relative; top: 8px">Worldwide News</div><br>

<!-- WW News Analysis start -->
            <tm src=ww_news_analysis_center_03.incl>
<!-- WW News Analysis end -->
            </td>
         </tr>

         <tr>
            <td align="left" valign="top">
<tm src=UI_more_news_analysis.incl>
            </td>
         </tr>
<!-- News Analysis end-->

<!-- Featured Research start -->
             <tr>
              <td align="left" valign="top">
               <tm src=UI_featured_research_title.incl>
               <tm src=reg_featured_research_left_04.incl>
              </td>
             </tr>
<!-- Featured Research end -->


         </table>
         <!-- close Table IA-1c -->
         </td>
      </tr>

<%
  System.out.println("About to render Announcements");
%>

<!-- Announcements start-->
      <tr>
         <td colspan=3 valign="top">
<!-- WW PRESS RELEASES start -->
         <tm src=UI_press_releases_title.incl>
         <tm src=ww_press_releases_bottom_01.incl>
<!-- WW PRESS RELEASES end -->
         <!-- tm src=bottom_02.incl -->
         </td>
      </tr>
      </table>
      <!-- close Table IA-1 -->
      </td>
      <td width="16"><img src="//img/trans_pixel.gif" width="16" border="0" alt=""></td>
      <td valign="top" width="192" align="right">
      <!-- Table IA-2 -->
      <table width="192" cellpadding="0" cellspacing="0" border="0">
      <tr>
         <td width="192">
<!-- PROMOS right_01.incl - currently regional version of 4 ways start -->
    
<tm src=right_01.incl>


<!-- PROMOS right_01.incl end -->
<!-- PROMOS right_02.incl start-->
<tm src=right_02.incl>
<!-- PROMOS right_02.incl end-->
         </td>
      </tr>
      <tr>
        <td align="left" valign="top">

              <!-- Featured Events start -->
<table width="100%" cellspacing="0" cellpadding="0" border="0">
<tr>
 <td><img src="//img/trans_pixel.gif" height="1" width="1" vspace="0" border="0" alt=""></td>
</tr>
<tr>
 <td> 
   <tm src=reg_symposium_promo.incl>
 </td>
</tr>
<tr>
  <td>
   <tm src=UI_featured_events_title.incl>
 </td>
</tr>
<tr>
  <td>
    <tm src=reg_featured_events_right_03.incl>
  </td>
 </tr>
</table>
<!-- Featured Events end -->
<!-- PROMOS right_04.incl - currently security mini-site and G2 start -->
         <tm src=right_04.incl>
<!-- PROMOS right_04.incl end -->
<!-- PROMOS right_05.incl - Gartner Vendor Ratings start -->
         <tm src=right_05.incl>
<!-- PROMOS right_05.incl end -->
<!-- Gartner Press start -->
<table width="100%" cellspacing="0" cellpadding="0" border="0">
<tr>
 <td>
   <tm src=UI_gartner_press_title.incl>
 </td>
</tr>
         <tm src=right_gpress.incl>
<!-- Gartner Press end -->
<!-- Corrections start -->
         <tm src=corrections_right_06.incl>
<!-- Corrections end -->
         </td>
      </tr>
      </table>
      <!-- close Table IA-2 -->
      </td>
      <td width="10"><img src="//img/trans_pixel.gif" width="10" border="0" alt=""></td>
      
      </tr>
      </table>
      <!--close Table IA-->
      </td>
      <!-- <td width="3" class="blackBack" bgcolor="black" rowspan="2"><img width="3" src="//img/trans_pixel.gif"></td> -->
   </tr>
   <tr>
   <td colspan="2">
   <!-- Table IB -->
   <table width="100%" cellpadding="0" cellspacing="0" border="0">
   <tr>
   <td width="15"><img src="//img/trans_pixel.gif" width="15"></td> 
      <td valign="top">
<!-- Gartner Accessibility and Vendor Relations sites start -->
      <tm src=bottom_03.incl>
<!-- Gartner Accessibility and Vendor Relations sites end -->
      </td>
      <td width="10"><img src="//img/trans_pixel.gif" width="10"></td>
   </tr>
   </table>
   <!-- close Table IB -->
   </td>

</tr>
</table>
<!-- close Table I -->
