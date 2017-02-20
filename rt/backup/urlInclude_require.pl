#!/usr/local/bin/perl



sub urlIncl {

    # pass it 2 arg, <file to get from gartner.com> <locale - optional>
    
    require ("/home/gartner/cgi-bin/glogin_regionals.pl");

    $locale = $_[1];

    $website = ""; # "\/";# "http\:\/\/www4.gartner.com\/";


    undef $newDocument; # variable where return data is stored.

    &parseUrlInclPage;
    &getUrlInclDocument;

    # print command line version of output
    return ($newDocument);


}


#################################################################
sub parseUrlInclPage {



	$clVersionFlag = 1;
	$FORM{'url'} = $_[0];
	$f = index ($_[0], "/", 0);
	$l = rindex ($_[0], "/");
	$length = $l - $f + 1;
	$relPath = substr ($_[0], $f, $length);
    
}



##########################################################
sub getUrlInclDocument {

    $URL = "$website\/$FORM{url}";
    $URL = "http:\/\/regionals4.gartner.com"."$FORM{url}";
    #$URL = "http:\/\/intl.gartner.com\/"."$FORM{url}";
    $msg .=  "\nurlIncl: GETTING URL $URL\n";

    if ($FORM{'intl'}) {
	$URL = "http:\/\/intl.gartner.com\/rt\/content\/emea\/focus_areas.inc" if ($FORM{'url'} =~ /focus_areas/);
	$URL = "http:\/\/intl.gartner.com\/rt\/content\/emea\/mq_vr.inc" if ($FORM{'url'} =~ /mq_vr/);
    }

    undef local $document;
    undef local @doc;
    undef local $prevprevLine;
    undef local $prevLine;

    $document = &getGARTNERpage($URL, $ARGV[1]);

    
    #process document
    @doc = split (/\n/, $document); # split on newlines
       
    foreach (@doc) {
    
	@tag = split (/\>/, $line);

	$inBodyFlag = 1 if ($FORM{'url'} =~ /\.inc/);
	$inBodyFlag = 1 if (/document.write\(headString\)/);
	$inBodyFlag = 1 if (/<\!\-\- PAGE CONTENT \-\-\>/i); # <!-- PAGE CONTENT -->
	$inBodyFlag++ if ($inBodyFlag);
	# $inBodyFlag = 0 if (/<table border\=\"0\" cellpadding\=\"0\" cellspacing\=\"0\"\>/);

	next if ($inBodyFlag < 2);


	if (/remove rt nav layer/ ) {
	    last;
	} 




	##########################################
	# mq_vr.inc for italia
	if ($FORM{'url'} =~ /\/mq_vr.inc/) {

	    s/dottedline/dottedLine/g;
	    if ($locale eq "it") {

		# hype cycles
		s/Gartner Hype Cycles clearly explain the difference between hype and the future of technology./Gartner Hype Cycles illustra con chiarezza la differenza tra le aspettative non realistiche e il futuro della tecnologia./;
		s/View All Hype Cycles/Altri Hype Cycles/;
		s/Latest Hype Cycle/Ultimo Hype Cycle/;

		# magic quadrants
		s/Find out which vendors are leaders, visionaries, challengers or niche players./Scopri quali fornitori sono leader, \"visionari\", \"sfidanti\", <br \/\>di nicchia/;
		s/Latest Magic Quadrants/Ultimi Magic Quadrants/;
		s/Latest Magic Quadrant/Ultimo Magic Quadrant/;

		# s/Latest Magic Quadrant:/Visualizza tutti i Magic Quadrant pi\&ugrave\; recenti:/;
		s/View All Magic Quadrants/Altri Magic Quadrants/;
		
		# vendor ratings
		s/Gartner\'s latest ratings of leading vendors/Le ultime valutazioni Gartner sui principali fornitori/;
		s/Latest Ratings/Ultime valutazioni/;
		s/View All Vendor Ratings/Altri Vendor Ratings/;
		s/width\=\"100/width\=\"130/;
		s/width\=\"236/width\=\"206/;

		# weblogs
		s/Find out what Gartner analysts are thinking about current business & technology issues/Scoprite il parere degli analisti Gartner su temi attuali di business e tecnologie/;
		s/View All Gartner Weblogs/Visualizza tutti i Gartner Weblog/;

		# research collections
		s/Research Collections/Raccolte di ricerche/;
		s/Get research articles, tools and other resources./Consulta gli articoli di ricerca, i tool e le altre risorse./;
		s/View All Raccolte di ricerche/Altre Ricerche recenti/;
		

	    } elsif ($locale eq "de") {

		# hype cycles
		s/Gartner Hype Cycles clearly explain the difference between hype and the future of technology./Gartner Hype Cycles machen den Unterschied zwischen Medien-Rummel und den Technologien der Zukunft deutlich./;
		s/View All Hype Cycles/Alle Hype Cycles/;
		s/Latest Hype Cycle:\&nbsp\;<\/b\>/Aktuellster Hype Cycle:\&nbsp\;<\/b\><br \/\>\n/;

		# magic quadrants
		s/Find out which vendors are leaders, visionaries, challengers or niche players./Finden Sie heraus, welche Anbieter f\&uuml\;hrend, vision\&auml\;r, Herausforderer oder Nischenplayer sind/;
		s/View All Magic Quadrants/Alle Magic Quadrants/;
		s/Latest Magic Quadrant:\&nbsp\;\&nbsp\;<\/b\><\/span\>/Aktuellster Magic Quadrant:\&nbsp\;\&nbsp\;<\/b\><\/span\><br \/\>/;
		s/<img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"12\" alt\=\"\" border\=\"0\"\>//; # added 28 Nov 2003 for dumb spacer
	      
		s/<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"20\" height\=\"12\" alt\=\"\" border\=\"0\"\>/ /;# added 28 Nov 2003 for dumb spacer
		
		# vendor ratings
		s/Gartner\'s latest ratings of leading vendors/Gartners neueste Bewertungen der f\&uuml\;hrenden Anbieter/;
		s/View All Vendor Ratings/Alle Vendor Ratings/; # was Anbieter-Bewertungen/;
		
		s/Latest Ratings/Aktuellste Vendor Ratings/; # was Anbieter-Bewertung/;

                 # wider left column for german translation
		 s/width\=\"100/width\=\"190/;
		 s/width\=\"236/width\=\"146/;

		# weblogs
		s/Find out what Gartner analysts are thinking about current business & technology issues/Finden Sie heraus, was Gartner-Analysten zu aktuellen Business- und Technologie-Themen zu sagen haben/;
		s/View All Gartner Weblogs/Alle Gartner Weblogs/;
		s/Latest Topic/Aktuellstes Thema/;

 		# research collection
		s/Research Collections/Unser Research/;
		s/Get research articles, tools and other resources./Research, Tools und andere Ressourcen./;
		s/View All Unser Research/Weiterer Research/; # phrase "research collection already changed

	    }
	}

	##########################################
	# focus_area.inc for italia
	if ($FORM{'url'} =~ /\/focus_areas.inc/) {

	    if ($locale eq "it") {
		if (/\/pages\/section.php.id.2126.s.8.jsp/) {
		
		    # http://regionals4.gartner.com/regionalization/content/emea/it/mp_architects.html
		    
		    $msg .= "urlIncl: found mp architects for italia\n\n";
		    s/\/pages\/section.php.id.2126.s.8.jsp/\/regionalization\/content\/emea\/it\/mp_architects.html/i;
		    
		} elsif (/\/pages\/section.php.id.2123.s.8.jsp/) {
		    
		    # http://regionals4.gartner.com/regionalization/content/emea/it/mp_investment.html
		    
		    $msg .= "urlIncl: found mp investment for italia\n\n";
		    s/\/pages\/section.php.id.2123.s.8.jsp/\/regionalization\/content\/emea\/it\/mp_investment.html/i;
		    
		} elsif (/\/pages\/section.php.id.2125.s.8.jsp/) {
		    
		    # http://regionals4.gartner.com/regionalization/content/emea/it/mp_network.html
		    
		    $msg .= "urlIncl: found mp network for italia\n\n";
		    s/\/pages\/section.php.id.2125.s.8.jsp/\/regionalization\/content\/emea\/it\/mp_network.html/i;
		    
		}
		
		# change the descriptive text to italian
		s/Get the insight, services and<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>tools you need to succeed in<\/div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>your job<div\>/Le conoscenze, i servizi e<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>gli strumenti per raggiungere<\/div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>il successo<div\>/;
		
		# add in the italian membership program
		$ssmiIE = <<EndofList;
		document.write('<option value="/regionalization/content/emea/it/ssmi_unrec_home.jsp"> SSMI - Outsourcing Professionals in Italy</option>');
		
EndofList
		    
		    
		    
                s/(Telecom Managers<\/option\>\'\)\;)/\1\n$ssmiIE/;
		
		
		# add in the italian membership program for netscape
		
		$ssmiNSCP = <<EndofList;
		document.write('<div><img src="./img/trans_pixel.gif" width="196" height="1" alt="" border="0"></div><img src="/images/homepage/trans_arrow.gif" width="8" height="8" alt="" hspace="3" border="0"><a href="/regionalization/content/emea/it/ssmi_unrec_home.jsp" class="membershipProgramLink">Outsourcing Professionals in Italy</a>');
		
EndofList
		    
		    s/(Telecom Managers<\/a\>\'\)\;)/\1\n$ssmiNSCP/;
		
		
		# text NOSCRIPT version
		
		$ssmiNOSCRIPT = <<EndofList;
		<div><img src="/images/trans_pixel.gif" width="196" height="1" alt="" border="0"></div>           
		    <img src="/images/homepage/trans_arrow.gif" width="8" height="8" alt="" hspace="3" border="0"><a href="/regionalization/content/emea/it/ssmi_unrec_home.jsp" class="membershipProgramLink">Outsourcing Professionals in Italy</a>
			
EndofList
			    
                s/(Telecom Managers<\/a\>)$/\1\n$ssmiNOSCRIPT/;
		
		
		s/Choose Your Job Role/Scegli il tuo ruolo/;

	    } elsif ($locale eq "de") {

		# change the descriptive text to italian
		s/Get the insight, services and<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>tools you need to succeed in<\/div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>your job<div\>/Wissen, Services und<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>Tools, die Ihren beruflichen<\/div\><div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>Erfolg sichern<div\>/;
		
		s/Choose Your Job Role/W\&auml\;hlen Sie Ihre Job-Funktion aus/;


	    }
	    
	}

    





	##########################################
	# too many contentText classes in 05_z_about
	if ($FORM{'url'} =~ /\/5_about\/company_information\/41a.html/) {

	    if (/CLASS\=\"contentText\"/i) {

		$msg .= "urlIncl: found CLASS/5_about/ BIG TD class=contentText found\n\n";
		s/CLASS\=\"contentText\"//i;
	    }

	}


	##########################################
	# start point for WEBLOGS
	if ($FORM{'url'} =~ /\/featured_research.inc/) {
	    if ($_ =~ /\-\- Gartner Weblogs/  || $_ =~ /\-\- Oracle promo/) {
		# START
		$msg .= "urlIncl: found start weblogs\n\n";
		undef $newDocument;
		undef $prevprevLine;
		undef $prevLine;
	    }
	    if (/End Gartner Weblogs/ || /end Oracle promo/){
		# END
		$msg .= "urlIncl: found end weblogs\n\n";
		last;
	    }
	}

	##########################################
	# funny start for 03 consulting multi client studies
	if ($FORM{'url'} =~ /3_consulting_services\/multiclient_studies.html/
	    && $_ =~ /cellpadding\=\"6\"/ ) {
	    $msg .= "urlIncl: 02 consulting multi client studies start found\n\n ";
	    undef $newDocument;
	    undef $prevprevLine;
	    undef $prevLine;
	    
	}	    


	##########################################
	# end point for 03 consulting
	if ($FORM{'url'} =~ /3_consulting/ &&  $_ =~ /For more information/ ) {
	    $msg .= "urlIncl: 02 consulting contact info found, ending\n\n ";
	    $newDocument .= " <!-- contact info handler -->\n\n <p\> \n$prevprevline \n\n  $prevline \n\n <!-- contact line -->  $_  \n\n <p\>\n\n\n";
	    last;
	} 


	##########################################
	# end point for 04 measurement
	if ($FORM{'url'} =~ /4_decision_tools/ &&  $_ =~ /Contact Information/ ) {
	    $msg .= "urlIncl: 03 measurement contact info found, ending\n\n ";
	    $newDocument .= "  <\/td\>\t <\/tr\>\n<\/table\>\n\n\n";
	    $newDocument =~ s/<hr\/>//i; # remove any hr
	    last;
	} 



	# deal with overview pages
	if ($_ =~ /<\!\-\- Page Content \-\-\>/i ||
	    $_ =~ /<\!\-\- Page Body \-\-\>/i )

	{
	    $msg .= "urlIncl: found Page Content\/Body\n";
	    undef $newDocument;
	    undef $prevprevLine;
	    undef $prevLine;
	    next;

	}

	# deal with more news page     /5_about/news/more_news.html
	if ($_ =~ /<\!\-\-THIS WEEK \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\>/) 

	{
	    
	    $newDocument = "<table border\=\"0\" cellspacing\=\"0\" cellpadding\=\"0\" width\=\"100\%\"\>";
	    undef $prevprevLine;
	    undef $prevLine;

	    next;
	    
	}

	# fix images
	if (/src\=\"\/images\/trans_pixel.gif/i) {

	    # trans_pixel.gif
	    # s/\/images\/trans_pixel.gif/\.\/img\/trans_pixel.gif/g;
	    # $msg .= "trans_pixel fixed: $_\n\n";

	} elsif (/src\=\"images/) {

	    s/src\=\"images/src\=\"\/images/g;
	    # $msg .= "src\=\"images fixed: $_\n\n";

	} elsif (/src\=\"\//i) {
	    # absolute refs
	    # $msg .= "\n\nimg abs refs: $_\n";
	    # leave alone 31/5 - s/(src\=\")\/(.[^\"]*)\"/$1$website$2\"/gi;
	    # $msg .= "\t$_\n\n";

	} elsif (/src\=\"/i) {
	    # relative refs
	    #$msg .= "\n\nimg rel refs: $_\n";
	    # s/(src\=\")(.[^\"]*)\"/$1$website$relPath$2\"/gi;
	    s/src\=\"/src\=\"$relPath\//gi;
	    # $msg .= "\t$_\n\n";
	}

	# remove script that write breadcrum at least on the core research methodologies page
	s/<td colspan\=\"3\" class\=\"contentCell\"\><script\>document.write\(buildTopNav\(\)\)\<\/script\>\<\/td\>//gi; 

	# remove script that writes sub nav 
	s/document.write\(buildSubNav\(\)\)//gi; 

	# remove widths of 99%
	s/width\=\"99\%\"//g; # remove?
      
	
	# html
	if ($_ =~ /href\=\"(.[^\"]*)\"(.[^\>]*)\>/i) {
	    
	    $filename     = $1;
	    $rest = $2;
	    
	    if ($filename =~ /javascript/i || 
		$filename =~ /http:\/\//i) {
		
		$msg .= "urlIncl: ignoring js or http link: $filename\n";
		
		if ($filename !~ /javascript\:void\(null\)/ ) {
		    
		    $_ =~ s/\\'\//\\'$website\//;
		    $_ =~ s/(href\=\")/$1$website/g if ($_ !~ /http:\/\//);
		    
		    $_ =~ s/imgdvweb01/www/g; # perhaps not required
		}

	    } elsif ($filename =~ /\#/) {
		
		# index reference to point to same page
		# I think the baseurl on the page screws it up
		$_ =~ s/$filename/javascript\:void\(null\)/;
		$_ =~ s/$rest/ onClick\=\"javascript\:document.location\=\'$filename\'\" $rest/;
		

	    } else {

		$msg .=  "urlIncl: FOUND link $filename\n";
		# $_ =~ s/$filename/$website\/$filename/; # removed with 31 May release
	    }
	    
	} 

	if ($_ =~ /open(.[^\(]*)\('(.[^']*)'/i) {
	    
	    $filename     = $2;

	    $msg .= "urlIncl: looking at js src issue with Open$1: $filename\n";
		
	    
	    $_ =~ s/'\//'$website/;
	    $_ =~ s/imgdvweb01/www/g; # perhaps not required
	
	}


        $_ =~ s/(this.src\=\')\//$1http:\/\/www.gartner.com\//gi; # for mouse overs in strat sourcing page

        $_ =~ s/.com\/\/\//.com\//g; # get rid of triple /// for a single /
        $_ =~ s/.com\/\//.com\//g; # get rid of double // for a single /


	$newDocument .= "$prevprevLine\n";
	$prevprevLine = $prevLine;
	$prevLine = "$_";
	
    }

    # only add last line if it isn't a random table tag
    $newDocument .= "<!-- pp line --> $prevprevLine <!-- end pp line -->\n"; # added 28 Aug
    $newDocument .= "<!-- p line  --> $prevLine <!-- end p line-->\n" if ($prevLine !~ /<\/td\>/);
    
    
}

1;
