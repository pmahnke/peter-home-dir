use strict;
use Test::More tests => 9;

use XML::Atom::Feed;

my $feed = XML::Atom::Feed->new("t/samples/source.xml");
my $entry = ($feed->entries)[0];

ok $entry;
is $entry->title, "Example Entry";
ok $entry->source;
is $entry->source->title, "Frank's JiveBlog";

$entry->title("Altered Entry");
is $entry->title, "Altered Entry";

my $link = $entry->source->link;
is $link->rel, 'alternate';
is $link->type, 'text/html';
is $link->href, 'http://jiveblog.example.com/frank';

my $new_source = XML::Atom::Feed->new(Version => 1.0);

$new_source->title("Jank's FriveBlog");

$entry->source($new_source);

is $entry->source->title, "Jank's FriveBlog";



