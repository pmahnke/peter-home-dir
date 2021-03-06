
use strict;
use warnings;

use Module::Build 0.3601;


my %module_build_args = (
  "build_requires" => {
    "Module::Build" => "0.3601"
  },
  "c_source" => "c",
  "configure_requires" => {
    "Module::Build" => "0.3601"
  },
  "dist_abstract" => "Validate method/function parameters",
  "dist_author" => [
    "Dave Rolsky, <autarch\@urth.org> and Ilya Martynov <ilya\@martynov.org>"
  ],
  "dist_name" => "Params-Validate",
  "dist_version" => "1.08",
  "license" => "artistic_2",
  "module_name" => "Params::Validate",
  "recommends" => {},
  "recursive_test_files" => 1,
  "requires" => {
    "Attribute::Handlers" => "0.79",
    "Carp" => 0,
    "Exporter" => 0,
    "Module::Implementation" => 0,
    "Scalar::Util" => "1.10",
    "XSLoader" => 0,
    "attributes" => 0,
    "perl" => "5.008001",
    "strict" => 0,
    "vars" => 0,
    "warnings" => 0
  },
  "script_files" => [],
  "test_requires" => {
    "Devel::Peek" => 0,
    "File::Spec" => 0,
    "File::Temp" => 0,
    "Test::Fatal" => 0,
    "Test::More" => "0.88",
    "Tie::Array" => 0,
    "Tie::Hash" => 0,
    "base" => 0,
    "overload" => 0
  }
);


unless ( eval { Module::Build->VERSION(0.4004) } ) {
  my $tr = delete $module_build_args{test_requires};
  my $br = $module_build_args{build_requires};
  for my $mod ( keys %$tr ) {
    if ( exists $br->{$mod} ) {
      $br->{$mod} = $tr->{$mod} if $tr->{$mod} > $br->{$mod};
    }
    else {
      $br->{$mod} = $tr->{$mod};
    }
  }
}

my $build = Module::Build->new(%module_build_args);

my $skip_xs;
if ( grep { $_ eq '--pp' } @ARGV ) {
    $skip_xs = 1;
}
elsif ( ! $build->have_c_compiler() ) {
    $skip_xs = 1;
}

if ($skip_xs) {
    $build->build_elements(
        [ grep { $_ ne 'xs' } @{ $build->build_elements() } ] );
}
$build->create_build_script;
