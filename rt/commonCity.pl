#!/usr/local/bin/perl

################################################################################
#
# commonCity.pl
#
#   written:  01 Dec 2003 by Peter Mahnke
#   modified: 01 Feb 2004 by Peter Mahnke
#
#   require script, called from event include scripts:
#   getConf.pl & getLocalBriefings.pl
#
#   DESCRIPTION OF SUBROUTINES
#
#     localiseLocation
#       cleans-up and translates English city name to correct one for the locale
#        takes 3 arguments
#        1. location
#        2. locale
#        3. type of filter - optional  (strict for locale only,
#           loose -default for all europe)
#
#        returns 0 if not in locale and strict filter on
#        otherwise returns name
#
#
################################################################################


sub localiseLocation {

    # takes 3 args
    # 1. location
    # 2. locale
    # 3. type of filter - optional  (strict for locale only, loose -default for all europe)

    # returns 0 if not in locale and strict filter on
    # otherwise returns name

    my $location = $_[0];
    my $locale   = $_[1];
    my $strict   = 1 if ($_[2]);

    # location clean up#
    $location =  $1 if ($location =~ /(.[^\,]*)\,/); # dump comma country
    $location =~ s/[0-9]//g;                         # dump numbers
    $location =~ s/CH\-//;                           # some strange Swiss thing
    $location =~ s/, M90 3RA//;                       # some strange UK Postcode

    # fix some bad spellings
    $location = "Rome"       if ($location eq "Roma");
    $location = "Dusseldorf" if ($location eq "Duesseldorf"
				 || $location =~ /Neuss \- Duesseldorf/);
    $location = "Geneva"     if ($location eq "Geneve");
    $location = "Vienna"     if ($location =~ /Wien/);
    $location = "Lisbon"     if ($location eq "Lisboa");


    # bigger city that event is near
    $location = "Zurich"     if ($location =~ /Glattbrugg/);
    $location = "Stockholm"  if ($location =~ /Solna/);
    $location = "Madrid"     if ($location =~ /Las Rozas/);
    $location = "Helsinki"   if ($location =~ /Helskinki/);
    $location = "Copenhagen" if ($location =~ /Klampenborg/);
    $location = "Amsterdam"  if ($location =~ /Hoofddorp/);



    # skip non-european cities
    return (0) if (

		   $location =~ /Riyadh/    ||
		   $location =~ /Dubai/     ||
		   $location =~ /Ankara/    ||
		   $location =~ /Istanbul/

   );



    # locale localisation

   # ITALIA
    if ($locale eq "it") {

		if ($location =~ /(Rome|Roma|Milan|Geneva|Zurich)/) { #    ||
		    $location = "Roma"    if ($location eq "Rome");
		    $location = "Milano"  if ($location eq "Milan");
		    $location = "Zurigo"  if ($location eq "Zurich");
		    $location = "Ginevra" if ($location eq "Geneva");

		} elsif ($strict) {

		    # return 0 - skip cities not in italia locale
		    return(0);

		} else {

		    # italian translations for european cities, if not strict
		    $location = "Londra"     if ($location eq "London");
		    $location = "Bruxelles"  if ($location eq "Brussels");
		    $location = "Barcellona" if ($location eq "Barcelona");
		    $location = "Stoccolma"  if ($location eq "Stockholm");
		    $location = "Parigi"     if ($location eq "Paris");
		    $location = "Lisbona"    if ($location eq "Lisbon");
		    $location = "Dublino"    if ($location eq "Dublin");
		    $location = "Varsavia"   if ($location eq "Warsaw");
		    $location = "Zagabria"   if ($location eq "Zagreb");
		    $location = "Lubiana"    if ($location eq "Ljubliana");
		    $location = "Atene"      if ($location eq "Athens");
		    $location = "Monaco di Baviera"   if ($location eq "Munich");
		    # $location = ""   if ($location eq "");
		    
		}
    }


    # DEUTCHLAND
    # add german city logic here... when we get some briefings
    if ($locale eq "de") {

		if ($location =~ /(Hamburg|Munich|Berlin|Frankfurt|Vienna|Hanover|Copenhagen|Geneva|Duesseldorf|Dusseldorf)/) {
		    $location  = "M\&uuml\;nchen"  if ($location eq "Munich");
		    $location  = "Wien"            if ($location eq "Vienna");
		    #$location  = "Zurigo"        if ($location eq "Zurich");
		    #$location  = "Ginevra"       if ($location eq "Geneva");
		    $location  = "D&uuml;sseldorf" if ($location eq "Duesseldorf" || $location eq "Dusseldorf");

		} elsif ($strict) {

		   # return 0 - skip cities not in german locale
		    return(0);

		} else {

		    # german translations for european cities, if not strict
		    $location = "Br\&uuml\;ssel" if ($location eq "Brussels");
		}

    }

    return ($location);

}


1;
