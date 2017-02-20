<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
<title>Mint: A Fresh Look at Your Site</title>
<style type="text/css" title="text/css" media="screen">
/* <![CDATA[ */
body
{
	position: relative;
	background-color: #FFF;
	margin: 0;
	padding: 48px 0;
	font: 76%/1.6em "Lucida Grande", Verdana, Arial, sans-serif;
	color: #333;
	text-align: center;
}

div
{
	width: 400px;
	margin: 0 auto;
	text-align: left;
}

h1
{
	font-weight: normal;
}

ol
{
	margin: 0 0 1.0em;
	padding: 0;
	list-style: none;
}

li
{
	color: #C00;
	position: relative;
	height: 1%;
	padding-left: 20px;
}
li span
{
	position: absolute;
	top: 1px;
	left: 0;
	border: 1px solid #CCC;
	width: 14px;
	height: 14px;
	line-height: 12px;
	text-align: center;
	vertical-align: middle;
}

li.pass 
{
	color: #090;
}


/* ]]> */
</style>
</head>
<body>
<div>
	<!-- Crazy comments and formatting required to clean up output for those who don't have PHP -->
	<h1>A Simple Mint Compatibility Test</h1>
	<ol>
		<?php
			$ob = urldecode('%3C');
			$cb = urldecode('%3E');
			// <!--
			echo "{$ob}li class=\"pass\"{$cb}{$ob}span{$cb}&radic;{$ob}/span{$cb} This server is capable of parsing PHP.{$ob}/li{$cb}<!--";
			$compatible = '1';
			$report[] = 'PHP: Present';
			// -->
		?>
		<li><span>&times;</span> <h1>Your server is not capable of parsing PHP.</h1></li><?php
		// <!--
		echo "-->";
		
		// <!--
		// Version
		if (PHP_VERSION 
			> // <!--
			4)
		{
			echo "{$ob}li class=\"pass\"{$cb}{$ob}span{$cb}&radic;{$ob}/span{$cb} And this version of PHP (".PHP_VERSION.") is compatible with Mint!{$ob}/li{$cb}";
			$compatible .= '1';
			$report[] = 'PHP Version: '.PHP_VERSION;
			
			// Extensions
			$extensions = get_loaded_extensions();
			$required	= array('MySQL','CURL');
			foreach ($required as $ext)
			{
				if (in_array(strtolower($ext),$extensions))
				{
					echo "{$ob}li class=\"pass\"{$cb}{$ob}span{$cb}&radic;{$ob}/span{$cb} PHP has been compiled with ".$ext.".{$ob}/li{$cb}";
					$compatible .= '1';
					if ($ext=='MySQL')
					{
						if (mysql_get_client_info() 
							> // <!--
							2)
						{
							echo "{$ob}li class=\"pass\"{$cb}{$ob}span{$cb}&radic;{$ob}/span{$cb} And MySQL ".mysql_get_client_info()." is compatible with Mint!{$ob}/li{$cb}";
							$report[] = 'MySQL Version: '.mysql_get_client_info();
							$compatible .= '1';
						}
						else
						{
							echo "{$ob}li{$cb}{$ob}span{$cb}&times;{$ob}/span{$cb} But MySQL ".mysql_get_client_info()." is not compatible with Mint.{$ob}/li{$cb}";
							$compatible .= '0';
						}
					}
				}
				else
				{
					echo "{$ob}li{$cb}{$ob}span{$cb}&times;{$ob}/span{$cb} D'oh! Mint requires PHP be compiled with ".$ext.".{$ob}/li{$cb}";
					$compatible .= '0';
					$report[] = 'Missing: '.$ext;
				}
			}
		}
		else
		{
			echo "{$ob}li{$cb}{$ob}span{$cb}&times;{$ob}/span{$cb} But this version of PHP (".PHP_VERSION.") is not compatible with Mint.{$ob}/li{$cb}";
			$compatible .= '0';
			$report[] = 'PHP Version: '.PHP_VERSION;
		}
		
		// -->
		?>
	</ol>
	
	<p>
	<?php
	// <!--
	if (strpos($compatible, '0')===false)
	{
		echo "{$ob}strong{$cb}Green means go!{$ob}/strong{$cb} Mint is totally crushing on your server&mdash;be a pal and {$ob}a href=\"http://www.haveamint.com/purchase\"{$cb}hook them up!{$ob}/a{$cb}";
		
		if (true)
		{
		
		}
	}
	else
	{
		echo "{$ob}strong{$cb}Uh-oh. Unfortunately, this server is missing one or more features Mint requires to run.{$ob}/strong{$cb} Please contact your host about the deficiencies in red above if you are still interested in using Mint.";
	}
	
	echo '<!--'; 
	?>
	I'm sorry but Mint will not work with this server.
	<?php
	echo '-->'; 
	?>
	</p>
</div>
</body>
</html>
