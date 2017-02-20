#!/usr/bin/perl

use Image::Magick;   

my($image);    

$image = Image::Magick->new;
$image->Set(size=>'100x100');    
$image->ReadImage('xc:black');

$text = 'Works like magick!';    
$image->Annotate(font=>'Courier', pointsize=>40, fill=>'green', text=>$text);

$filename = "/home/gartner/html/image.jpg";
open(IMAGE, ">$filename");
$image->Write(file=>\*IMAGE, filename=>$filename);
close(IMAGE);
