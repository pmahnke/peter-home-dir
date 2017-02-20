#!/usr/bin/perl

$dir = "/var/log/qmail";


$buffer = $ENV{'QUERY_STRING'};

if ($buffer) {	# assumes that form has been filled out
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$FORM{$name} = $value;
    }				# End of foreach $pair
}
 
if ($FORM{'app'}) {
    &printResults;
} else {
    &printQuery;
}
   
exit;




sub printResults {

    $results = `/usr/local/qmailanalog/bin/matchup  <"$FORM{'log'}" | $FORM{'app'}`;

    print <<EOF;
Content-type: text/html


<html>
<head><title>QMAIL LOG ANALYZER</title></head>
<body>
<form method=GET>
<h1> Qmail Log Analyzer Results</h1>
<pre>
$results
</pre>
<p>
</body>
</html>

EOF


}


sub printQuery {

    opendir (LOGS, "$dir");
    @fileList = readdir LOGS;
    foreach $file (@fileList) { $fileList = "\<option\> $file\n" }
    closedir (LOGS);

    print <<EOF;
Content-type: text/html


<html>
<head><title>QMAIL LOG ANALYZER</title></head>
<body>
<form method=GET>

<h1> Qmail Log Analyzer</h1>

Log file:<br>
<select name=app>
$fileList
</select>
<p>

Application:<br> 
<select name=app>
 <option> xqp
 <option> xrecipient
 <option> xsender
 <option> zdeferrals
 <option> zrhosts
 <option> zsuccesses
 <option> zfailures
 <option> zrxdelay
 <option> zsuids
 <option> zoverall
 <option> zsenders
 <option> zddist
 <option> zrecipients
 <option> zsendmail
</select><p>

<input type=submit name=submit value=run>
</form>
<p>
</body>
</html>

EOF

}
