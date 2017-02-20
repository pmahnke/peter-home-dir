#!/usr/local/bin/perl



sub localiseLocation {

    # takes 3 args
    # 1. location
    # 2. locale
    # 3. type of filter - optional  (strict for locale only, loose -default for all europe)

    # returns 0 if not in locale and strict filter on
    # otherwise returns name

    local $location = $_[0];
    local $locale   = $_[1];
    local $strict   = 1 if ($_[2] =~ /strict/i);

    # location clean up#
    $location =  $1 if ($location =~ /(.[^\,]*)\,/); # dump comma contry
    $location =~ s/[0-9]//g; # dump numbers
    $location =~ s/CH\-//; # some strange Swiss thing
    $location =~ s/, M90 3RA//; # some strange UK Postcode
    
    # fix some bad spellings
    $location = "Rome" if ($location eq "Roma");
    $location = "Dusseldorf" if ($location eq "Duesseldorf"
				 || $location =~ /Neuss \- Duesseldorf/);
    $location = "Geneva" if ($location eq "Geneve");
    $location = "Vienna" if ($location =~ /Wien/);
    $location = "Lisbon" if ($location eq "Lisboa");
    



    # bigger city that event is near
    $location = "Zurich" if ($location =~ /Glattbrugg/);
    $location = "Stockholm" if ($location =~ /Solna/);
    $location = "Madrid" if ($location =~ /Las Rozas/);
    $location = "Helsinki" if ($location =~ /Helskinki/);
    $location = "Copenhagen" if ($location =~ /Klampenborg/);
    $location = "Amsterdam" if ($location =~ /Hoofddorp/);
    


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
	    $location = "Roma" if ($location eq "Rome");
	    $location = "Milano" if ($location eq "Milan");
	    $location = "Zurigo" if ($location eq "Zurich");
	    $location = "Ginevra" if ($location eq "Geneva");

	} elsif ($strict) {
	    
	    # return 0 - skip cities not in italia locale
	    return(0);

	} else {

	    # italian translations for european cities, if not strict
	    $location = "Londra"    if ($location eq "London");
	    $location = "Bruxelles" if ($location eq "Brussels");
	    
	}
    }
    
    
    # DEUTCHLAND
    # add german city logic here... when we get some briefings
    if ($locale eq "de") {
	if ($location =~ /(Hamburg|Munich|Berlin|Frankfurt|Vienna|Duesseldorf)/) {
	    $location = "M\&uuml\;nchen" if ($location eq "Munich");
	    $location = "Wein" if ($location eq "Vienna");
	    #$location = "Zurigo" if ($location eq "Zurich");
	    #$location = "Ginevra" if ($location eq "Geneva");
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
