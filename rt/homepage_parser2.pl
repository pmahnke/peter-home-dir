#!/usr/local/bin/perl

########################################################################
#
#	homepage_parser2.pl
#
#	   writen:	09 Dec 2003 by Peter Mahnke
#	   modified:
#				7 Jul 2005 by Peter Mahnke
#				- completed updated based on gartner.com 6.5
#				  updates
#				26 Apr 2005 by Peter Mahnke
#				- changed Altri precedenti to Altri webcast
#				  on request of Mimma
#				13 Apr 2005 by Peter Mahnke
#				- commented out the write and ftp of news and research
#				  on request of Jim Carolan
#				14 Mar 2005 by Peter Mahnke
#				- added sections for In the News and Featured Research
#				  so Europe mirrors WCW
#				07 Jan 2004 by Peter Mahnke
#				- added <br /> to push MQ headlines to second line
#				- added <br /> to push HC headlines to second line
#				- added <br /> to push VR headlines to second line
#				18 Jan 2004 by Peter Mahnke
#				- added FTP to campsqa
#			16 Aug 2004 by Ian Smith
#				- updated DE Hype Cycle intro text
#				09 Sept 2004 by Ian Smith
#				- disabled ftp of announcement headlines
#				12 Nov 2004 by Ian Smith
#				- added extra string translation to DE webcasts
#				14 Jan 2005 by Ian Smith
#				- added strings for translation to DE Webcasts
#			18 Jan 2005 by Ian Smith
#				- added strings for translation to IT Webcasts
#
#	   run from command line, or cron
#
#	   script gets the unrecognised homepage of gartner.com and
#	   parses out all the sections used by the regional sites
#	   then translates the required sections for the local
#	   language sites
#
#	   this script is required as of 8 Dec 2003 the gartner.com
#	   homepages are created by CAMPS and only product a flattened
#	   jsp page
#
#	   the gartner.com team left comment tags for us to parse
#	   sections out
#
#	   if an alternate selection is picked via the pickMQHCVR.cgi,
#	   it writes a new include (.incl) file and puts a lock on that
#	   file that homepage_parser.pl respects
#
#	   if homepage_parser.pl sees the lock, via the script
#	   commonLock.pl it saves the translated default gartner.com
#	   include as <filename>.incl.latest
#
#
#	   TODO
#		-  add logic to try other servers if regionals4 is down
#		-  deal with spacing on long MQ, HC and VR latest listings
#		-  create require version
#
########################################################################

require ('/home/gartner/cgi-bin/glogin_regionals.pl');
require ('/home/gartner/html/rt/commonLock.pl');
require ('/home/gartner/html/rt/replaceChars.pl');
require ('/home/gartner/html/rt/SmartyPants.pl');

########################################################################
# variables
my $URL = "http:\/\/www.gartner.com\/UnrecognizedUserHomePage.jsp";
$URL = "http:\/\/vaqa.gartner.com\/UnrecognizedUserHomePage.jsp" if ($ARGV[0] =~ /qa/i);
undef my $document;
undef my @doc;



########################################################################
# get contents of the $URL page
$document = &getGARTNERpage($URL, 'www');

# change DOS newlines to UNIX
$document =~ s//\n/g;

########################################################################
#process document
@doc = split (/\n/, $document); # split on newlines

foreach (@doc) {


	$inBodyFlag = 1 if (/BEGIN BODY/);
	$inBodyFlag++ if ($inBodyFlag);

	next if ($inBodyFlag < 2);

	if (/END BODY/ ) {
		last;
	}


	#####################################################################
	# Parse out these sections from flatted gartner.com homepage

	#####################################################################
	# BLURB : CONSULTING

	# end OF BLURB : CONSULTING
	if (/end blurb consulting/) {
		$flagBlurbConsulting = 0;
		&write('emea/home_blurb_consulting.incl', $line);
		&FTPfile('home_blurb_consulting.incl');
		&transBlurbConsulting($line,'home_blurb_consulting.incl');
	}

	# IN BLURB : CONSULTING
	if ($flagBlurbConsulting) {
		$line .= $_;
	}

	# START OF BLURB : CONSULTING
	if (/start blurb consulting/) {
		$flagBlurbConsulting = 1;
		undef $line;
	}



	#####################################################################
	# BLURB : EXP

	# end OF BLURB : EXP
	if (/end blurb exp/) {
		$flagBlurbEXP = 0;
		&write('emea/home_blurb_exp.incl', $line);
		&FTPfile('home_blurb_exp.incl');
		&transBlurbEXP($line,'home_blurb_exp.incl');
	}

	# IN BLURB : EXP
	if ($flagBlurbEXP) {
		$line .= $_;
	}

	# START OF BLURB : EXP
	if (/start blurb exp/) {
		$flagBlurbEXP = 1;
		undef $line;
	}



	#####################################################################
	# BLURB : INVEST

	# end OF BLURB : Invest
	if (/end blurb invest/) {
		$flagBlurbInvest = 0;
		&write('emea/home_blurb_invest.incl', $line);
		&FTPfile('home_blurb_invest.incl');
		&transBlurbInvest($line, 'home_blurb_invest.incl');
	}

	# IN BLURB : INVEST
	if ($flagBlurbInvest) {
		$line .= $_;
	}

	# START OF BLURB : INVEST
	if (/start blurb invest/) {
		$flagBlurbInvest = 1;
		undef $line;
	}



	#####################################################################
	# MAIN PROMO

	# end OF MAIN PROMO
	if (/end main pr.mo/) {
		$flagMainPromo = 0;
		&write('emea/home_main_promo.incl', $line);
		&FTPfile('home_main_promo.incl');
		#&transMainPromo($line, 'home_main_promo.incl'); # currently there are none
	}

	# IN MAIN PROMO
	if ($flagMainPromo) {
		$line .= $_;
	}

	# START OF MAIN PROMO
	if (/start main pr.mo/) {
		$flagMainPromo = 1;
		undef $line;
	}



	#####################################################################
	# RESEARCH HEADLINES

	# end OF RESEARCH HEADLINES
	if (/end research headlines/) {
		$flagResearchHeadlines = 0;
		#&write('emea/home_featured_research.incl', $line);
		#&FTPfile('home_featured_research.incl');
		#&transResearchHeadlines($line); # currently there are none
	}

	# IN RESEARCH HEADLINES
	if ($flagResearchHeadlines) {
		$line .= $_;
	}

   # START OF RESEARCH HEADLINES
	if (/start research headlines/) {
		$flagResearchHeadlines = 1;
		undef $line;
	}



	#####################################################################
	# BLOG HEADLINES

	# end OF BLOG HEADLINES
	if (/end blog headlines/) {
		$flagBlogHeadlines = 0;
		&write('emea/home_blog_headlines.incl', $line);
		&FTPfile('home_blog_headlines.incl');
		&transBlogHeadlines($line,'home_blog_headlines.incl');
	}

	# IN BLOG HEADLINES
	if ($flagBlogHeadlines) {
		$line .= $_;
	}

	# START OF BLOG HEADLINES
	if (/start blog headlines/) {
		$flagBlogHeadlines = 1;
		undef $line;
	}



	#####################################################################
	# TOP RIGHT PROMO

	#	# end OF TOP PROMOS
	#	if (/end bottom right pr0mo/) {
	#	$flagRightPromo = 0;
	#	&write('emea/home_prm.incl', $line);
	#	&FTPfile('home_prm.incl');
	#	#&transRightPromo($line);
	#	}
    #
	#	# IN TOP PROMO
	#	if ($flagRightPromo) {
	#		$line .= $_;
	#	}

	# START OF TOP PROMO
	if (/start bottom left pr0mo/) {
		# $flagRightPromo = 1;
		undef $line;
		$line = $_;
		&write('emea/home_prm.incl', $line);
		&FTPfile('home_prm.incl');
		#&transRightPromo($line);
	}




	#####################################################################
	# COLUMN MARKETS

	# end OF COLUMN MARKETS TEXT
	if (/end column markets text/) {
		$flagColumnMarketsText = 0;
		&write('emea/home_ff_col_markets_text.incl', $line);
		&FTPfile('home_ff_col_markets_text.incl');
		&transColumnMarketsText($line,'home_ff_col_markets_text.incl');
	}

	# IN COLUMN MARKETS TEXT
	if ($flagColumnMarketsText) {
		$line .= $_;
	}

	# START OF COLUMN MARKETS TEXT
	if (/start column markets text/) {
		$flagColumnMarketsText = 1;
		undef $line;
	}

	##############################
	# end OF COLUMN MARKETS LIST
	if (/end column markets list/) {
		$flagColumnMarketsList = 0;
		$line =~ s/\&amp /&amp\; /g;
		&write('emea/home_ff_col_markets.incl', $line);
		&FTPfile('home_ff_col_markets.incl');
		&transColumnMarketsList($line,'home_ff_col_markets.incl');
	}

	# IN COLUMN MARKETS LIST
	if ($flagColumnMarketsList) {
		$line .= "$_";
	}

	# START OF COLUMN MARKETS LIST
	if (/start column markets list/) {
		$flagColumnMarketsList = 1;
		undef $line;
	}



	#####################################################################
	# COLUMN TOPICS

	# end OF COLUMN TOPICS TEXT
	if (/end column topics text/) {
		$flagColumnTopicsText = 0;
		&write('emea/home_ff_col_topics_text.incl', $line);
		&FTPfile('home_ff_col_topics_text.incl');
		&transColumnTopicsText($line,'home_ff_col_topics_text.incl');
	}

	# IN COLUMN TOPICS TEXT
	if ($flagColumnTopicsText) {
		$line .= "$_";
	}

	# START OF COLUMN TOPICS TEXT
	if (/start column topics text/) {
		$flagColumnTopicsText = 1;
		undef $line;
	}

	##############################
	# end OF COLUMN TOPICS LIST
	if (/end column topics list/) {
		$flagColumnTopicsList = 0;
		&write('emea/home_ff_col_topics.incl', $line);
		&FTPfile('home_ff_col_topics.incl');
		&transColumnTopicsList($line,'home_ff_col_topics.incl');
	}

	# IN COLUMN TOPICS LIST
	if ($flagColumnTopicsList) {
		$line .= "$_";
	}

	# START OF COLUMN TOPICS LIST
	if (/start column topics list/) {
		$flagColumnTopicsList = 1;
		undef $line;
	}



	#####################################################################
	# COLUMN INDUSTRIES

	# end OF COLUMN INDUSTRIES TEXT
	if (/end column industries text/) {
		$flagColumnIndustriesText = 0;
		&write('emea/home_ff_col_industries_text.incl', $line);
		&FTPfile('home_ff_col_industries_text.incl');
		&transColumnIndustriesText($line,'home_ff_col_industries_text.incl');
	}

	# IN COLUMN INDUSTRIES TEXT
	if ($flagColumnIndustriesText) {
		$line .= "$_";
	}

	# START OF COLUMN INDUSTRIES TEXT
	if (/start column industries text/) {
		$flagColumnIndustriesText = 1;
		undef $line;
	}

	##############################
	# end OF COLUMN INDUSTRIES LIST
	if (/end column industries list/) {
		$flagColumnIndustriesList = 0;
		&write('emea/home_ff_col_industries.incl', $line);
		&FTPfile('home_ff_col_industries.incl');
		&transColumnIndustriesList($line,'home_ff_col_industries.incl');
	}

	# IN COLUMN INDUSTRIES LIST
	if ($flagColumnIndustriesList) {
		$line .= "$_";
	}

	# START OF COLUMN INDUSTRIES LIST
	if (/start column industries list/) {
		$flagColumnIndustriesList = 1;
		undef $line;
	}



	#####################################################################
	# SIXPACK MQ

	# end OF SIXPACK MQ TEXT
	if (/end sixpack mq text/) {
	$flagSixpackMQText = 0;
	$line =~ s/Latest: //;

	&write('emea/home_sixpack_magicquadrants_text.incl', $line);
	&FTPfile('home_sixpack_magicquadrants_text.incl');
	&transSixpackMQText($line,'home_sixpack_magicquadrants_text.incl');
	}

	# IN TOP SIXPACK MQ TEXT
	if ($flagSixpackMQText) {
		$line .= $_;
	}

	# START OF SIXPACK MQ TEXT
	if (/start sixpack mq text/) {
		$flagSixpackMQText = 1;
		undef $line;
	}

	##############################
	# end OF SIXPACK MQ LIST
	if (/end sixpack mq headlines/) {
		$flagSixpackMQList = 0;

		if (!&testLock('MQ', 'emea')) {

			# no lock
			&write('emea/home_sixpack_magicquadrants_headlines.incl', $line);
			&FTPfile('home_sixpack_magicquadrants_headlines.incl');

		} else {

			# lock, so just write the current file locally
			&write('emea/home_sixpack_magicquadrants_headlines.incl.latest', $line);
		}

		&transSixpackMQHeadlines($line,'home_sixpack_magicquadrants_headlines.incl');
	}

	# IN SIXPACK MQ LIST
	if ($flagSixpackMQList) {
		$line .= $_;
	}

	# START OF SIXPACK MQ
	if (/start sixpack mq headlines/) {
		$flagSixpackMQList = 1;
		undef $line;
	}



	#####################################################################
	# SIXPACK HC

	# end OF SIXPACK HC TEXT
	if (/end sixpack hc text/) {
		$flagSixpackHCText = 0;
		&write('emea/home_sixpack_hypecycles_text.incl', $line);
		&FTPfile('home_sixpack_hypecycles_text.incl');
		&transSixpackHCText($line,'home_sixpack_hypecycles_text.incl');
	}

	# IN TOP SIXPACK HC TEXT
	if ($flagSixpackHCText) {
		$line .= $_;
	}

	# START OF SIXPACK HC TEXT
	if (/start sixpack hc text/) {
		$flagSixpackHCText = 1;
		undef $line;
	}

	##############################
	# end OF SIXPACK HC LIST
	if (/end sixpack hc headlines/) {
		$flagSixpackHCList = 0;
		$line =~ s/Hype Cycle for //g;

		if (!&testLock('HC', 'emea')) {

			# no lock
			&write('emea/home_sixpack_hypecycles_headlines.incl', $line);
			&FTPfile('home_sixpack_hypecycles_headlines.incl');

		} else {

			# lock, so just write the current file locally
			&write('emea/home_sixpack_hypecycles_headlines.incl.latest', $line);
		}

		&transSixpackHCHeadlines($line,'home_sixpack_hypecycles_headlines.incl');
	}

	# IN SIXPACK HC LIST
	if ($flagSixpackHCList) {
		$line .= $_;
	}

	# START OF SIXPACK HC
	if (/start sixpack hc headlines/) {
		$flagSixpackHCList = 1;
		undef $line;
	}



	#####################################################################
	# SIXPACK VR

	# end OF SIXPACK VR TEXT
	if (/end sixpack vr text/) {
		$flagSixpackVRText = 0;
		&write('emea/home_sixpack_vendorratings_text.incl', $line);
		&FTPfile('home_sixpack_vendorratings_text.incl');
		&transSixpackVRText($line,'home_sixpack_vendorratings_text.incl');
	}

	# IN TOP SIXPACK VR TEXT
	if ($flagSixpackVRText) {
		$line .= $_;
	}

	# START OF SIXPACK VR TEXT
	if (/start sixpack vr text/) {
		$flagSixpackVRText = 1;
		undef $line;
	}

	##############################
	# end OF SIXPACK VR LIST
	if (/end sixpack vr headlines/) {
		$flagSixpackVRList = 0;

		if (!&testLock('VR', 'emea')) {

			# no lock
			&write('emea/home_sixpack_vendorratings_headlines.incl', $line);
			&FTPfile('home_sixpack_vendorratings_headlines.incl');

		} else {

			# lock, so just write the current file locally
			&write('emea/home_sixpack_vendorratings_headlines.incl.latest', $line);
		}

		&transSixpackVRHeadlines($line,'home_sixpack_vendorratings_headlines.incl');
	}

	# IN SIXPACK VR LIST
	if ($flagSixpackVRList) {
		$line .= $_;
	}

	# START OF SIXPACK VR
	if (/start sixpack vr headlines/) {
		$flagSixpackVRList = 1;
		undef $line;
	}



	#####################################################################
	# SIXPACK META

	# end OF SIXPACK META TEXT
	if (/end sixpack meta text/) {
		$flagSixpackMETAText = 0;
		#&write('emea/home_sixpack_meta_text.incl', $line);
		#&FTPfile('home_sixpack_meta_text.incl');
		#&transSixpackMETAText($line);
	}

	# IN TOP SIXPACK META TEXT
	if ($flagSixpackMETAText) {
		$line .= $_;
	}

	# START OF SIXPACK META TEXT
	if (/start sixpack meta text/) {
		$flagSixpackMETAText = 1;
		undef $line;
	}

	##############################
	# end OF SIXPACK META LIST
	if (/end sixpack meta headlines/) {
		$flagSixpackMETAList = 0;
		#&write('emea/home_sixpack_meta_headlines.incl', $line);
		#&FTPfile('home_sixpack_meta_headlines.incl');
		#&transSixpackMETAHeadlines($line);
	}

	# IN SIXPACK META LIST
	if ($flagSixpackMETAList) {
		$line .= $_;
	}

   # START OF SIXPACK META
	if (/start sixpack meta headlines/) {
		$flagSixpackMETAList = 1;
		undef $line;
	}



	#####################################################################
	# SIXPACK CV

	# end OF SIXPACK CV TEXT
	if (/end sixpack cv text/) {
		$flagSixpackCVText = 0;
		&write('emea/home_sixpack_coolvendors_text.incl', $line);
		&FTPfile('home_sixpack_coolvendors_text.incl');
		&transSixpackCVText($line,'home_sixpack_coolvendors_text.incl');
	}

	# IN TOP SIXPACK CV TEXT
	if ($flagSixpackCVText) {
		$line .= $_;
	}

	# START OF SIXPACK CV TEXT
	if (/start sixpack cv text/) {
		$flagSixpackCVText = 1;
		undef $line;
	}

	##############################
	# end OF SIXPACK CV LIST
	if (/end sixpack cv headlines/) {
		$flagSixpackCVList = 0;

		if (!&testLock('VR', 'emea')) {

			# no lock
			&write('emea/home_sixpack_coolvendors_headlines.incl', $line);
			&FTPfile('home_sixpack_coolvendors_headlines.incl');

		} else {

			# lock, so just write the current file locally
			&write('emea/home_sixpack_coolvendors_headlines.incl.latest', $line);
		}

		&transSixpackCVHeadlines($line,'home_sixpack_coolvendors_headlines.incl');
	}

	# IN SIXPACK CV LIST
	if ($flagSixpackCVList) {
		$line .= $_;
	}

	# START OF SIXPACK CV
	if (/start sixpack cv headlines/) {
		$flagSixpackCVList = 1;
		undef $line;
	}



	#####################################################################
	# SIXPACK FELLOWS

	# end OF SIXPACK FELLOWS TEXT
	if (/end sixpack fellows text/) {
		$flagSixpackFELLOWSText = 0;
		&write('emea/home_sixpack_fellows_text.incl', $line);
		&FTPfile('home_sixpack_fellows_text.incl');
		&transSixpackFELLOWSText($line,'home_sixpack_fellows_text.incl');
	}

	# IN TOP SIXPACK FELLOWS TEXT
	if ($flagSixpackFELLOWSText) {
		$line .= $_;
	}

	# START OF SIXPACK FELLOWS TEXT
	if (/start sixpack fellows text/) {
		$flagSixpackFELLOWSText = 1;
		undef $line;
	}

	##############################
	# end OF SIXPACK FELLOWS LIST
	if (/end sixpack fellows headlines/) {
		$flagSixpackFELLOWSList = 0;
		&transSixpackFELLOWSHeadlines($line,'home_sixpack_fellows_headlines.incl');
		$line =~ s/The Gartner Fellows: //;
		$line =~ s/View All</View All Interviews</;
		&write('emea/home_sixpack_fellows_headlines.incl', $line);
		&FTPfile('home_sixpack_fellows_headlines.incl');
	}

	# IN SIXPACK FELLOWS LIST
	if ($flagSixpackFELLOWSList) {
		$line .= $_;
	}

	# START OF SIXPACK FELLOWS
	if (/start sixpack fellows headlines/) {
		$flagSixpackFELLOWSList = 1;
		undef $line;
	}

	#####################################################################
	# TOP BOTTOM PROMO

	# end OF TOP RIGHT PROMO
	if (/end bottom pr.mo/) {
		$flagBottomPromo = 0;
		&write('emea/home_prm_bottom.incl', $line);
		&FTPfile('home_prm_bottom.incl');
		#&transBottomPromo($line);
	}

	# IN TOP RIGHT PROMO
	if ($flagBottomPromo) {
		$line .= $_;
	}

	# START OF TOP RIGHT PROMO
	if (/start bottom pr0mo/) {
		$flagBottomPromo = 1;
		undef $line;
	}

}











########################################################################
########################################################################
sub write {

	# writes files

	# take 2 inputs
	#  $_[0]  -  name of file with extra path information
	#  $_[1]  -  content of file

	# replace characters with html entities for accents, etc
	my $output = &SmartyPants ($_[1], 1);
	   $output = &replaceCharacters($output);


	$file = "/home/gartner/html/rt/content/"."$_[0]";
	open (FILE, ">$file") || die "Can't open file for writing: $file \n\n";
	#print FILE "<!-- created by homepage_parser.pl -->\n\n";
	print FILE $output;
	close (FILE);

	print "\nwrote $file\n";

	return();

}
########################################################################
########################################################################









########################################################################
#
# Following sections are to translate
#  links, text and html of various sections
#




########################################################################
sub transBlurbConsulting  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Put Gartner's expertise to work on your organization's unique challenges. Our consultants can help you achieve high returns on your IT investments./Avvaletevi dell’esperienza Gartner per le esigenze specifiche della vostra organizzazione. I nostri consulenti possono aiutarvi a ottimizzare i vostri investimenti IT./;
		s/read more/Ulteriori informazioni./i;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Put Gartner's expertise to work on your organization's unique challenges. Our consultants can help you achieve high returns on your IT investments./Setzen Sie unsere Experten auf Ihre Problemstellungen an. Gartner Consultants holen das Optimum aus Ihren IT-Investitionen heraus./;
		s/read more/Lesen Sie mehr/i;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();

}




########################################################################
sub transBlurbEXP  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Access exclusive research, share best practices with other IT executives, and get personalized support from a dedicated team of Gartner analysts./Per accedere a ricerche esclusive, condividere best practice con altri IT executive e ricevere un supporto personalizzato da parte di un team dedicato di analisti Gartner./;
		s/read more/Ulteriori informazioni./i;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Access exclusive research, share best practices with other IT executives, and get personalized support from a dedicated team of Gartner analysts./Lesen Sie exklusiven Research, teilen Sie Best Practices mit anderen CIOs und erhalten Sie individuelle Unterstützung von einem speziellen EXP-Team./;
		s/read more/Lesen Sie mehr/i;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();

}




########################################################################
sub transBlurbInvest  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transMainPromo  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transResearchHeadlines  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}



########################################################################
sub transBlogHeadlines  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Featured Blog/Il blog/;
		s/All Blogs/Visualizza tutti i blog/;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Featured Blog/Aktueller Blog/;
		s/All Blogs/Weitere Blogs/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transRightPromo  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transColumnMarketsText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Statistics, forecasts and market analysis you can trust./Statistiche, analisi e tendenze sugli aspetti principali dell’IT/;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Statistics, forecasts and market analysis you can trust./Fundierte Statistiken, Prognosen und Analysen/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transColumnMarketsList  {

	undef my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Computing Hardware/Piattaforme di computing/;
		s/Print Markets \&amp\; Management/Documenti digitali e imaging/;
		s/Security Solutions/Sicurezza delle informazioni/;
		s/Applications/Applicazioni/;
		s/Infrastructure/Infrastruttura/;
		s/IT Services/Servizi IT/g;
		s/Consulting \&amp\; Integration/Consulenza e integrazione/;
		s/Infrastructure Support/Supporto all’infrastruttura/;
		s/Network \&amp\; Storage/Network e storage/;
		s/Mobile Communications/Comunicazioni mobili/;
		s/Communications/Comunicazioni/g;
		s/Enterprise Networks/Network aziendali/;
		s/Equipment/Apparati/;
		s/Public Networks/Network Pubblici/;
		s/Semiconductor/Semiconduttori/g;
		s/Applications/Applicazioni/;
		s/Design \&amp\; Manufacturing/Progettazione e produzione/;
		s/Industry \&amp\; Devices/Industry e device/;
		s/Cross Market/Cross market/;
		s/Business Strategies/Strategie di business/;
		s/Industry Strategies/Strategie di settore/;
		s/Small \&amp\; Midsized Business/Piccole e medie imprese/;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/IT Services/IT\-Services/;
		s/Computing Hardware/Computing Plattformen/;
		s/Print Markets \&amp\; Management/Digitale Dokumente und Imaging/;
		s/Security Solutions/Informationssicherheit/;
		s/Storage/Speicher /;
		s/Applications/Applikationen/;
		s/Infrastructure/Infrastruktur/;
		s/Consulting \&amp\; Integration/Consulting \&amp\; Integration/;
		s/Infrastructure Support/Infrastruktur-Support/;
		s/Network \&amp\; Storage/Netzwerk \&amp\; Speicher/;
		s/Communications/Kommunikation/g;
		s/Enterprise Networks/Unternehmens-Netzwerke/;
		s/Equipment/Ausrüstung/;
		s/Mobile Communications/Mobile Kommunikation/;
		s/Public Networks/Öffentliche Netze /;
		s/Semiconductor/Halbleiter/g;
		s/Applications/Applikationen/g;
		s/Design \&amp\; Manufacturing/Design und Fertigung/;
		s/Industry \&amp\; Devices/Industrie und Geräte/;
		s/Cross Market/Marktübergreifend/;
		s/Business Strategies/Business-Strategien/;
		s/Industry Strategies/Branchen-Strategien/;
		s/Small \&amp\; Midsized Business/Kleine und mittlere Unternehmen/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transColumnTopicsText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/More than research - insight into your most critical issues./La ricerca si concentra sulle vostre problematiche principali./;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/More than research - insight into your most critical issues./Mehr als Research – Einblicke in Ihre wichtigsten Fragestellungen./;


		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transColumnTopicsList  {

	my @lines;
	push @lines, split(/<br \/\>/, $_[0]);

	# ITALY LOOP
	undef my $output;
	undef my %output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Application Development/Sviluppo applicativo/;
		s/Application Integration \&amp\; Middleware/Application Integration e Middleware/;
		s/Business Intelligence \&amp\; Data Integration/Business Intelligence e Data Warehousing/;
		s/Business Process Management/Gestione dei processi aziendali/;
		s/Consumer Technologies/Tecnologie consumer/;
		s/Customer Relationship Management/Customer relationship management/;
		s/Emerging Trends \&amp\; Technologies/Tendenze e tecnologie emergenti/;
		# s/Enterprise Architecture//;
		s/Enterprise Systems Management/Enterprise Systems Management/;
		s/ERP \&amp\; Supply Chain Management/ERP e gestione della supply chain/;
		s/High Performance Workplace/High Performance Workplace/;
		s/IT Asset Management/Gestione degli asset IT/;
		s/IT Management/Gestione dell’IT/;
		s/IT Services/Servizi IT/;
		s/Mobile \&amp\; Wireless/Mobile e wireless/;
		s/Network Equipment/Network Equipment/;
		s/Network Services/Servizi di rete/;
		s/Open Source/Open source/;
		s/PCs, Laptops, \&amp\; Handheld Devices/PC, laptop e palmari/;
		s/Regulatory Compliance/Conformità/;
		s/Security \&amp\; Privacy/Sicurezza e privacy/;
		s/Servers \&amp\; Storage/Server e storage/;
		s/Web Services/Web services/;

		my $key = $1 if (/\>(.[^<]*)</);
		$output{$key} = "$_<br \/\>\n";

	}

	foreach (sort { $a cmp $b } keys %output) {
		$output .= "$output{$_}\n";
	}
	$output .= "<br \/\><br \/\>\n";

	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');



	# GERMANY LOOP
	undef @lines;
	push @lines, split(/<br \/\>/, $_[0]);
	undef my $output;
	my %output;
	foreach (@lines) {

		# add text translations here
		#s///;


		s/IT Management/IT\-Management/;
		s/IT Services/IT\-Services/;
		s/Application Development/Anwendungsentwicklung/;
		s/Application Integration \&amp\; Middleware/Anwendungsintegration \&amp\; Middleware/;
		s/Business Intelligence \&amp\; Data Integration/Business Intelligence und Datenintegration/;
		s/Business Process Management/Business Process Management \(BPM\)/;
		s/Consumer Technologies/Endverbraucher-Technologien/;
		s/Customer Relationship Management/Customer Relationship Management/;
		s/Emerging Trends \&amp\; Technologies/Zukünftige Trends und Technologien/;
		s/Enterprise Architecture/Architekturen/;
		s/Enterprise Systems Management/System-Management/;
		s/ERP \&amp\; Supply Chain Management/ERP \&amp\; Supply Chain Management/;
		s/Mobile \&amp\; Wireless/Mobile \&amp\; Wireless/;
		s/Network Equipment/Netzwerkausrüstung/;
		s/Network Services/Netzwerk-Services/;
		s/Open Source/Open Source Software/;
		s/PCs, Laptops, \&amp\; Handheld Devices/PCs, Laptops \&amp\; Handhelds/;
		s/Regulatory Compliance/Compliance-Bestimmungen/;
		s/Security \&amp\; Privacy/Sicherheit \&amp\; Datenschutz/;
		s/Servers \&amp\; Storage/Server \&amp\; Speicher/;

		my $key = $1 if (/\>(.[^<]*)</);
		$output{$key} = "$_<br \/\>\n";

	}

	foreach (sort { $a cmp $b } keys %output) {
		$output .= $output{$_};
	}
	$output .= "<br \/\><br \/\>\n";

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transColumnIndustriesText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Understanding technologies and services that deliver business value./Analisi esaustiva sull’interazione tra business e IT./;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Understanding technologies and services that deliver business value./Technologien und Services, die für Ihr Geschäft von Bedeutung sind./;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transColumnIndustriesList  {

	my @lines;
	push @lines, split(/<br \/\>/, $_[0]);

	# ITALY LOOP
	undef my $output;
	undef my %output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Banking/Bancario/;
		s/Education/Istruzione/;
		s/Energy \&amp\; Utilities/Energia e utility/;
		s/Government/Pubblica Amministrazione/;
		s/Healthcare Providers/Sanità/;
		s/Insurance/Assicurativo/;
		s/Investment Services/Servizi per gli investimenti/;
		s/Manufacturing/Manifatturiero/;
		# s/Retail/Vendita al dettaglio/;

		my $key = $1 if (/\>(.[^<]*)</);
		$output{$key} = "$_<br \/\>\n";

	}

	foreach (sort { $a cmp $b } keys %output) {
		$output .= $output{$_};
	}
	$output .= "<br \/\><br \/\>\n";

	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	undef %output;
	push @lines, split(/<br \/\>/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Education/Hochschulen &amp; Ausbildung/;
		s/Energy \&amp\; Utilities/Energie\- und Versorgungsunternehmen/;
		s/Government/Öffentlicher Sektor/;
		s/Healthcare Providers/Gesundheitswesen/;
		s/Insurance/Versicherungen/;
		# s/Investment Services/Kapitalanlagen \&amp\; Wertpapiere/;
		s/Manufacturing/Verarbeitende Industrie/;
		s/Media/Medien/;
		s/Retail/Handel/;

		my $key = $1 if (/\>(.[^<]*)</);
		$key =~ s/Ö/O/;
		$output{$key} = "$_<br \/\>\n";

	}

	foreach (sort { $a cmp $b } keys %output) {
		$output .= $output{$_};
	}
	$output .= "<br \/\><br \/\>\n";

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transSixpackMQText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Find out which vendors are leaders, visionaries, challengers or niche players./Scopri quali fornitori sono leader, "visionari", "sfidanti" e "di nicchia"./;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Find out which vendors are leaders, visionaries, challengers or niche players./Finden Sie heraus, welche Anbieter führend, visionär, Herausforderer oder Nischenplayer sind./;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transSixpackMQHeadlines  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View All/Visualizza tutti i/;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];

	if (!&testLock('MQ', 'it')) {

	    # no lock
	    &write($file, $output);
	    &FTPfile($_[1], 'it');

	} else {

	    # lock, so just write the current file locally
	    &write($file.'.latest', $output);

	}


	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View All/Alle/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];

	if (!&testLock('MQ', 'de')) {

		# no lock
		&write($file, $output);
		&FTPfile($_[1], 'de');

	} else {

		# lock, so just write the current file locally
		&write($file.'.latest', $output);
	}

	return();


}




########################################################################
sub transSixpackHCText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/The wave of the future\? Or just hype\? Gartner Hype Cycles show the difference./I Gartner Hype Cycles illustrano con chiarezza la differenza tra le aspettative non realistiche e il futuro della tecnologia./;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/The wave of the future\? Or just hype\? Gartner Hype Cycles show the difference./Machen den Unterschied zwischen Erwartungen und der tatsächlichen Entwicklung von Technologien deutlich./;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transSixpackHCHeadlines  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View All/Visualizza tutti gli/;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	if (!&testLock('HC', 'it')) {

		# no lock
		&write($file, $output);
		&FTPfile($_[1], 'it');

	} else {

		# lock, so just write the current file locally
		&write($file.'.latest', $output);
	}

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View All/Alle/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	if (!&testLock('HC', 'de')) {

		# no lock
		&write($file, $output);
		&FTPfile($_[1], 'de');

	} else {

		# lock, so just write the current file locally
		&write($file.'.latest', $output);
	}

	return();


}




########################################################################
sub transSixpackVRText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Gartner's latest ratings of vendors and technology providers./Le ultime valutazioni Gartner sui principali fornitori./;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Gartner's latest ratings of vendors and technology providers./Gartners aktuelle Bewertungen der führenden Anbieter/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transSixpackVRHeadlines  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View All/Visualizza tutti i/;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	if (!&testLock('VR', 'it')) {

		# no lock
		&write($file, $output);
		&FTPfile($_[1], 'it');

	} else {

		# lock, so just write the current file locally
		&write($file.'.latest', $output);
	}

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View All/Alle/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	if (!&testLock('VR', 'de')) {

		# no lock
		&write($file, $output);
		&FTPfile($_[1], 'de');

	} else {

		# lock, so just write the current file locally
		&write($file.'.latest', $output);
	}

	return();


}




########################################################################
sub transSixpackMETAText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}

	&write('emea/it/home_focus_areas.incl', $output);
	&FTPfile('home_focus_areas.incl', 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}
	&write('emea/de/home_focus_areas.incl', $output);
	&FTPfile('home_focus_areas.incl', 'de');

	return();


}




########################################################################
sub transSixpackMETAList  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}

	&write('emea/it/home_focus_areas.incl', $output);
	&FTPfile('home_focus_areas.incl', 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}
	&write('emea/de/home_focus_areas.incl', $output);
	&FTPfile('home_focus_areas.incl', 'de');

	return();


}




########################################################################
sub transSixpackCVText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Introducing the newest, most innovative and intriguing vendor./Gartner vi presenta i fornitori più innovativi e influenti in 17 categorie/;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/Introducing the newest, most innovative and intriguing vendor./Gartner stellt die innovativsten und vielversprechendsten Anbieter aus 17 Bereichen vor./;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transSixpackCVHeadlines  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View the Special Report/Visualizza lo Special Report/;
		s/View All Special Reports/Visualizza tutti gli Special Report/g;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	if (!&testLock('CV', 'it')) {

		# no lock
		&write($file, $output);
		&FTPfile($_[1], 'it');

	} else {

		# lock, so just write the current file locally
		&write($file.'.latest', $output);
	}

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/View the Special Report/Zum Special Report/;
		s/View All Special Reports/Alle Special Reports/g;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	if (!&testLock('CV', 'de')) {

		# no lock
		&write($file, $output);
		&FTPfile($_[1], 'de');

	} else {

		# lock, so just write the current file locally
		&write($file.'.latest', $output);
	}

	return();


}




########################################################################
sub transSixpackFELLOWSText  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/The Gartner Fellows Interviews pair the best and the brightest Gartner analysts with the bright lights of the industry./Nelle Gartner Fellows Interviews i migliori analisti gartner intervistano esponenti di spicco del settore./;

		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		s/The Gartner Fellows Interviews pair the best and the brightest Gartner analysts with the bright lights of the industry./Renommierte Gartner-Analysten kommen mit den besten und schillerndsten IT-Größen zusammen./;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transSixpackFELLOWSHeadlines  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		if (/blueLink55pctBold\"\>(.*)\'s Interview/) {
			$_ = "$`blueLink55pctBold\"\>Intervista con $1$'";
		}

		s/View All/Visualizza tutte le interviste/;
		# s/Interview with/Intervista con/;
		$output .= "$_\n";

	}
	my $file = "emea/it/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		if (/blueLink55pctBold\"\>(.*)\'s Interview/) {
			$_ = "$`blueLink55pctBold\"\>Interview mit $1$'";
		}

		s/View All/Alle Interviews/;
		# s/Interview with/Interview mit/;

		$output .= "$_\n";

	}

	my $file = "emea/de/".$_[1];
	&write($file, $output);
	&FTPfile($_[1], 'de');

	return();


}




########################################################################
sub transBottomPromo  {

	my @lines;
	push @lines, split(/\n/, $_[0]);

	# ITALY LOOP
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}

	&write('emea/it/home_prm_bottom.incl', $output);
	&FTPfile('home_prm_bottom.incl', 'it');

	# GERMANY LOOP
	undef @lines;
	push @lines, split(/\n/, $_[0]);
	undef my $output;
	foreach (@lines) {

		# add text translations here
		#s///;

		$output .= "$_\n";

	}
	&write('emea/de/home_prm_bottom.incl', $output);
	&FTPfile('home_prm_bottom.incl', 'de');

	return();


}






########################################################################
sub FTPfile {

	# ftp files to remote servers
	# take 2 args
	# 1. filename
	# 2. relative path from emea/

	use Net::FTP;

	chdir("/home/gartner/html/rt/content/emea/$_[1]/");

	$remoteFullPath  = "regionalization/templates/emea/$_[1]/";

	$saveFile = "$_[0]"."\.old";

	if ($ARGV[0] =~ /qa/i) {

		$ftp = Net::FTP->new("campsqa.gartner.com") or $ftpmsg .= "FTPfile: Can't start FTP session<br>\n";
		$ftp->login("pmahnke","hi11top")		  or $ftpmsg .= "FTPfile: Can't login into FTP session<br>\n";
		$ftp->cwd($remoteFullPath)			   or $ftpmsg .= "FTPfile: Can't change directory on remove server: $remoteFullPath<br>\n";
		$ftp->type('I')						or $ftpmsg .= "FTPfile: Can't change to ascii mode<br>\n";
		$ftp->rename($_[0], $saveFile)			or $ftpmsg .= "FTPfile: Can't rename file: $_[1]/$_[0]<br>\n";
		$ftp->put($_[0],$_[0])				  or $ftpmsg .= "FTPfile: Can't PUT file on campsqa: $_[1]/$_[0]<br>\n";
		$ftp->quit();
	} else {
		$pftp = Net::FTP->new("hibachi.gartner.com") or $ftpmsg .= "FTPfile: Can't start FTP session<br>\n";
		$pftp->login("pmahnke","hi11top")		  or $ftpmsg .= "FTPfile: Can't login into FTP session<br>\n";
		$pftp->cwd($remoteFullPath)			   or $ftpmsg .= "FTPfile: Can't change directory on remove server: $remoteFullPath<br>\n";
		$pftp->type('I')						or $ftpmsg .= "FTPfile: Can't change to ascii mode<br>\n";
		$pftp->rename($_[0], $saveFile)			or $ftpmsg .= "FTPfile: Can't rename file: $_[1]/$_[0]<br>\n";
		$pftp->put($_[0],$_[0])				  or $ftpmsg .= "FTPfile: Can't PUT file on hibachi: $_[1]/$_[0]<br>\n";
		$pftp->quit();
	}
	print $ftpmsg;


}


########################################################################

1;
