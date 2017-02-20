#!/usr/local/bin/perl

# FTP UTIL
#  takes 3 args 
#   Source rel dir (dev/tempates/emea/, qa/, prod/)
#   Server (dev, qa, prod) and the 
#   Filename with the rel path (templates/01_research.html)
#   &put($FORM{'source'}, $FORM{'server'}, $FORM{'file'}, $FORM{'dir'});

sub put {
 
    # VARIABLES
    $rootDir    = "/home/gartner/html/mirror/";
    $localFile  = $rootDir.$_[0].$_[3]."/".$_[2];
    $localDest  = $rootDir.$_[1].$_[3]."/".$_[2];

    # copy mirrored local files
    $msg .= "cp $localFile $localDest<p\>";
    `cp $localFile $localDest`;

    
    if ($_[1] eq "dev") 
    {
	$passwd     = "ftpuser:rgn252";
	$server     = "10.36.1.96/";
	$remoteFile = "regionalization/$_[3]/$_[2]";
    } 
    elsif ($_[1] eq "qa") 
    {
	$passwd     = "pmahnke:hi11top";
	$server     = "kitkat.gartner.com/";
	$remoteFile = "regionalizationqa/$_[3]/$_[2]";
    } 
    elsif ($_[1] eq "prod") 
    {
	$passwd     = "pmahnke:hi11top";
	$server     = "twix.gartner.com/";
	$remoteFile = "regionalization/$_[3]/$_[2]";
    } 
    else
    {
	return(0);
    }

    # include the necessary libraries
    use LWP::UserAgent;
    use HTTP::Request;
    
    # define the URL of the file to put ($u)
    $u = "ftp://".$passwd."\@".$server.$remoteFile;
    
    # create the user agent ($a)
    $a = new LWP::UserAgent;
    
    # create the request ($r)
    $r = new HTTP::Request 'PUT', "$u";
    $r->content(scalar `cat $localFile`);  # for instance

    # PUT it and save the output ($o)
    $o = $a->request($r);
    
    return($u);
    exit;
}

return(1);
