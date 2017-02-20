# ---------------------------------------------------------------------------
# MT-Textile Text Formatter
# A Plugin for Movable Type
#
# Release 1.1
# February 14, 2003
#
# From Brad Choate
# http://www.bradchoate.com/
# ---------------------------------------------------------------------------
# This software is provided as-is.
# You may use it for commercial or personal use.
# If you distribute it, please keep this notice intact.
#
# Copyright (c) 2003 Brad Choate
# ---------------------------------------------------------------------------

package plugins::textile;

use vars qw($VERSION);
$VERSION = 1.1;

use strict;

use MT;
use MT::Template::Context;

MT->add_text_filter('textile_1' => {
    label => 'Textile',
    on_format => sub {
        require bradchoate::textile;
        &bradchoate::textile::textile_1;
    },
    docs => 'http://www.bradchoate.com/mt/docs/mtmanual_textile.html'
});

MT::Template::Context->add_tag(TextileHeadOffset => sub {
    require bradchoate::textile;
    &bradchoate::textile::TextileHeadOffset;
});

MT::Template::Context->add_tag(TextileAutoEncode => sub {
    require bradchoate::textile;
    &bradchoate::textile::TextileAutoEncode;
});

1;
