use inc::Module::Install::DSL 0.91;

all_from      lib/Test/Script.pm
requires      blib                  0
requires      File::Spec            0.80
requires      IPC::Run3             0.034
requires      Probe::Perl           0.01
requires      Test::More            0.62
test_requires Test::Builder         0.32
test_requires Test::Builder::Tester 1.02
