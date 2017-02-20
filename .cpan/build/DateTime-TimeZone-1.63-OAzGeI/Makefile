# This Makefile is for the DateTime::TimeZone extension to perl.
#
# It was generated automatically by MakeMaker version
# 6.84 (Revision: 68400) from the contents of
# Makefile.PL. Don't edit this file, edit Makefile.PL instead.
#
#       ANY CHANGES MADE HERE WILL BE LOST!
#
#   MakeMaker ARGV: (q[INSTALLDIRS=site])
#

#   MakeMaker Parameters:

#     ABSTRACT => q[Time zone object base class and factory]
#     AUTHOR => [q[Dave Rolsky <autarch@urth.org>]]
#     BUILD_REQUIRES => {  }
#     CONFIGURE_REQUIRES => { ExtUtils::MakeMaker=>q[6.30] }
#     DISTNAME => q[DateTime-TimeZone]
#     EXE_FILES => []
#     LICENSE => q[perl]
#     NAME => q[DateTime::TimeZone]
#     PREREQ_PM => { File::Spec=>q[0], Storable=>q[0], List::Util=>q[0], File::Compare=>q[0], File::Find=>q[0], lib=>q[0], Test::Output=>q[0], warnings=>q[0], base=>q[0], File::Copy=>q[0], parent=>q[0], Class::Load=>q[0], overload=>q[0], vars=>q[0], constant=>q[0], Test::More=>q[0.88], Class::Singleton=>q[1.03], strict=>q[0], Params::Validate=>q[0.72], File::Basename=>q[0], Sys::Hostname=>q[0], Cwd=>q[3] }
#     TEST_REQUIRES => { base=>q[0], File::Copy=>q[0], overload=>q[0], Storable=>q[0], Test::More=>q[0.88], lib=>q[0], Test::Output=>q[0], Sys::Hostname=>q[0] }
#     VERSION => q[1.63]
#     test => { TESTS=>q[t/*.t] }

# --- MakeMaker post_initialize section:


# --- MakeMaker const_config section:

# These definitions are from config.sh (via /usr/lib/perl/5.14/Config.pm).
# They may have been overridden via Makefile.PL or on the command line.
AR = ar
CC = cc
CCCDLFLAGS = -fPIC
CCDLFLAGS = -Wl,-E
DLEXT = so
DLSRC = dl_dlopen.xs
EXE_EXT = 
FULL_AR = /usr/bin/ar
LD = cc
LDDLFLAGS = -shared -L/usr/local/lib -fstack-protector
LDFLAGS =  -fstack-protector -L/usr/local/lib
LIBC = 
LIB_EXT = .a
OBJ_EXT = .o
OSNAME = linux
OSVERS = 3.2.0-37-generic
RANLIB = :
SITELIBEXP = /usr/local/share/perl/5.14.2
SITEARCHEXP = /usr/local/lib/perl/5.14.2
SO = so
VENDORARCHEXP = /usr/lib/perl5
VENDORLIBEXP = /usr/share/perl5


# --- MakeMaker constants section:
AR_STATIC_ARGS = cr
DIRFILESEP = /
DFSEP = $(DIRFILESEP)
NAME = DateTime::TimeZone
NAME_SYM = DateTime_TimeZone
VERSION = 1.63
VERSION_MACRO = VERSION
VERSION_SYM = 1_63
DEFINE_VERSION = -D$(VERSION_MACRO)=\"$(VERSION)\"
XS_VERSION = 1.63
XS_VERSION_MACRO = XS_VERSION
XS_DEFINE_VERSION = -D$(XS_VERSION_MACRO)=\"$(XS_VERSION)\"
INST_ARCHLIB = blib/arch
INST_SCRIPT = blib/script
INST_BIN = blib/bin
INST_LIB = blib/lib
INST_MAN1DIR = blib/man1
INST_MAN3DIR = blib/man3
MAN1EXT = 1p
MAN3EXT = 3pm
INSTALLDIRS = site
DESTDIR = 
PREFIX = $(SITEPREFIX)
PERLPREFIX = /usr
SITEPREFIX = /usr/local
VENDORPREFIX = /usr
INSTALLPRIVLIB = /usr/share/perl/5.14
DESTINSTALLPRIVLIB = $(DESTDIR)$(INSTALLPRIVLIB)
INSTALLSITELIB = /usr/local/share/perl/5.14.2
DESTINSTALLSITELIB = $(DESTDIR)$(INSTALLSITELIB)
INSTALLVENDORLIB = /usr/share/perl5
DESTINSTALLVENDORLIB = $(DESTDIR)$(INSTALLVENDORLIB)
INSTALLARCHLIB = /usr/lib/perl/5.14
DESTINSTALLARCHLIB = $(DESTDIR)$(INSTALLARCHLIB)
INSTALLSITEARCH = /usr/local/lib/perl/5.14.2
DESTINSTALLSITEARCH = $(DESTDIR)$(INSTALLSITEARCH)
INSTALLVENDORARCH = /usr/lib/perl5
DESTINSTALLVENDORARCH = $(DESTDIR)$(INSTALLVENDORARCH)
INSTALLBIN = /usr/bin
DESTINSTALLBIN = $(DESTDIR)$(INSTALLBIN)
INSTALLSITEBIN = /usr/local/bin
DESTINSTALLSITEBIN = $(DESTDIR)$(INSTALLSITEBIN)
INSTALLVENDORBIN = /usr/bin
DESTINSTALLVENDORBIN = $(DESTDIR)$(INSTALLVENDORBIN)
INSTALLSCRIPT = /usr/bin
DESTINSTALLSCRIPT = $(DESTDIR)$(INSTALLSCRIPT)
INSTALLSITESCRIPT = /usr/local/bin
DESTINSTALLSITESCRIPT = $(DESTDIR)$(INSTALLSITESCRIPT)
INSTALLVENDORSCRIPT = /usr/bin
DESTINSTALLVENDORSCRIPT = $(DESTDIR)$(INSTALLVENDORSCRIPT)
INSTALLMAN1DIR = /usr/share/man/man1
DESTINSTALLMAN1DIR = $(DESTDIR)$(INSTALLMAN1DIR)
INSTALLSITEMAN1DIR = /usr/local/man/man1
DESTINSTALLSITEMAN1DIR = $(DESTDIR)$(INSTALLSITEMAN1DIR)
INSTALLVENDORMAN1DIR = /usr/share/man/man1
DESTINSTALLVENDORMAN1DIR = $(DESTDIR)$(INSTALLVENDORMAN1DIR)
INSTALLMAN3DIR = /usr/share/man/man3
DESTINSTALLMAN3DIR = $(DESTDIR)$(INSTALLMAN3DIR)
INSTALLSITEMAN3DIR = /usr/local/man/man3
DESTINSTALLSITEMAN3DIR = $(DESTDIR)$(INSTALLSITEMAN3DIR)
INSTALLVENDORMAN3DIR = /usr/share/man/man3
DESTINSTALLVENDORMAN3DIR = $(DESTDIR)$(INSTALLVENDORMAN3DIR)
PERL_LIB = /usr/share/perl/5.14
PERL_ARCHLIB = /usr/lib/perl/5.14
LIBPERL_A = libperl.a
FIRST_MAKEFILE = Makefile
MAKEFILE_OLD = Makefile.old
MAKE_APERL_FILE = Makefile.aperl
PERLMAINCC = $(CC)
PERL_INC = /usr/lib/perl/5.14/CORE
PERL = /usr/bin/perl
FULLPERL = /usr/bin/perl
ABSPERL = $(PERL)
PERLRUN = $(PERL)
FULLPERLRUN = $(FULLPERL)
ABSPERLRUN = $(ABSPERL)
PERLRUNINST = $(PERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
FULLPERLRUNINST = $(FULLPERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
ABSPERLRUNINST = $(ABSPERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
PERL_CORE = 0
PERM_DIR = 755
PERM_RW = 644
PERM_RWX = 755

MAKEMAKER   = /usr/local/share/perl/5.14.2/ExtUtils/MakeMaker.pm
MM_VERSION  = 6.84
MM_REVISION = 68400

# FULLEXT = Pathname for extension directory (eg Foo/Bar/Oracle).
# BASEEXT = Basename part of FULLEXT. May be just equal FULLEXT. (eg Oracle)
# PARENT_NAME = NAME without BASEEXT and no trailing :: (eg Foo::Bar)
# DLBASE  = Basename part of dynamic library. May be just equal BASEEXT.
MAKE = make
FULLEXT = DateTime/TimeZone
BASEEXT = TimeZone
PARENT_NAME = DateTime
DLBASE = $(BASEEXT)
VERSION_FROM = 
OBJECT = 
LDFROM = $(OBJECT)
LINKTYPE = dynamic
BOOTDEP = 

# Handy lists of source code files:
XS_FILES = 
C_FILES  = 
O_FILES  = 
H_FILES  = 
MAN1PODS = 
MAN3PODS = lib/DateTime/TimeZone.pm \
	lib/DateTime/TimeZone/Catalog.pm \
	lib/DateTime/TimeZone/Floating.pm \
	lib/DateTime/TimeZone/Local.pm \
	lib/DateTime/TimeZone/Local/Unix.pm \
	lib/DateTime/TimeZone/Local/VMS.pm \
	lib/DateTime/TimeZone/Local/Win32.pm \
	lib/DateTime/TimeZone/OffsetOnly.pm \
	lib/DateTime/TimeZone/OlsonDB.pm \
	lib/DateTime/TimeZone/UTC.pm

# Where is the Config information that we are using/depend on
CONFIGDEP = $(PERL_ARCHLIB)$(DFSEP)Config.pm $(PERL_INC)$(DFSEP)config.h

# Where to build things
INST_LIBDIR      = $(INST_LIB)/DateTime
INST_ARCHLIBDIR  = $(INST_ARCHLIB)/DateTime

INST_AUTODIR     = $(INST_LIB)/auto/$(FULLEXT)
INST_ARCHAUTODIR = $(INST_ARCHLIB)/auto/$(FULLEXT)

INST_STATIC      = 
INST_DYNAMIC     = 
INST_BOOT        = 

# Extra linker info
EXPORT_LIST        = 
PERL_ARCHIVE       = 
PERL_ARCHIVE_AFTER = 


TO_INST_PM = lib/DateTime/TimeZone.pm \
	lib/DateTime/TimeZone/Africa/Abidjan.pm \
	lib/DateTime/TimeZone/Africa/Accra.pm \
	lib/DateTime/TimeZone/Africa/Addis_Ababa.pm \
	lib/DateTime/TimeZone/Africa/Algiers.pm \
	lib/DateTime/TimeZone/Africa/Asmara.pm \
	lib/DateTime/TimeZone/Africa/Bamako.pm \
	lib/DateTime/TimeZone/Africa/Bangui.pm \
	lib/DateTime/TimeZone/Africa/Banjul.pm \
	lib/DateTime/TimeZone/Africa/Bissau.pm \
	lib/DateTime/TimeZone/Africa/Blantyre.pm \
	lib/DateTime/TimeZone/Africa/Brazzaville.pm \
	lib/DateTime/TimeZone/Africa/Bujumbura.pm \
	lib/DateTime/TimeZone/Africa/Cairo.pm \
	lib/DateTime/TimeZone/Africa/Casablanca.pm \
	lib/DateTime/TimeZone/Africa/Ceuta.pm \
	lib/DateTime/TimeZone/Africa/Conakry.pm \
	lib/DateTime/TimeZone/Africa/Dakar.pm \
	lib/DateTime/TimeZone/Africa/Dar_es_Salaam.pm \
	lib/DateTime/TimeZone/Africa/Djibouti.pm \
	lib/DateTime/TimeZone/Africa/Douala.pm \
	lib/DateTime/TimeZone/Africa/El_Aaiun.pm \
	lib/DateTime/TimeZone/Africa/Freetown.pm \
	lib/DateTime/TimeZone/Africa/Gaborone.pm \
	lib/DateTime/TimeZone/Africa/Harare.pm \
	lib/DateTime/TimeZone/Africa/Johannesburg.pm \
	lib/DateTime/TimeZone/Africa/Kampala.pm \
	lib/DateTime/TimeZone/Africa/Khartoum.pm \
	lib/DateTime/TimeZone/Africa/Kigali.pm \
	lib/DateTime/TimeZone/Africa/Kinshasa.pm \
	lib/DateTime/TimeZone/Africa/Lagos.pm \
	lib/DateTime/TimeZone/Africa/Libreville.pm \
	lib/DateTime/TimeZone/Africa/Lome.pm \
	lib/DateTime/TimeZone/Africa/Luanda.pm \
	lib/DateTime/TimeZone/Africa/Lubumbashi.pm \
	lib/DateTime/TimeZone/Africa/Lusaka.pm \
	lib/DateTime/TimeZone/Africa/Malabo.pm \
	lib/DateTime/TimeZone/Africa/Maputo.pm \
	lib/DateTime/TimeZone/Africa/Maseru.pm \
	lib/DateTime/TimeZone/Africa/Mbabane.pm \
	lib/DateTime/TimeZone/Africa/Mogadishu.pm \
	lib/DateTime/TimeZone/Africa/Monrovia.pm \
	lib/DateTime/TimeZone/Africa/Nairobi.pm \
	lib/DateTime/TimeZone/Africa/Ndjamena.pm \
	lib/DateTime/TimeZone/Africa/Niamey.pm \
	lib/DateTime/TimeZone/Africa/Nouakchott.pm \
	lib/DateTime/TimeZone/Africa/Ouagadougou.pm \
	lib/DateTime/TimeZone/Africa/Porto_Novo.pm \
	lib/DateTime/TimeZone/Africa/Sao_Tome.pm \
	lib/DateTime/TimeZone/Africa/Tripoli.pm \
	lib/DateTime/TimeZone/Africa/Tunis.pm \
	lib/DateTime/TimeZone/Africa/Windhoek.pm \
	lib/DateTime/TimeZone/America/Adak.pm \
	lib/DateTime/TimeZone/America/Anchorage.pm \
	lib/DateTime/TimeZone/America/Antigua.pm \
	lib/DateTime/TimeZone/America/Araguaina.pm \
	lib/DateTime/TimeZone/America/Argentina/Buenos_Aires.pm \
	lib/DateTime/TimeZone/America/Argentina/Catamarca.pm \
	lib/DateTime/TimeZone/America/Argentina/Cordoba.pm \
	lib/DateTime/TimeZone/America/Argentina/Jujuy.pm \
	lib/DateTime/TimeZone/America/Argentina/La_Rioja.pm \
	lib/DateTime/TimeZone/America/Argentina/Mendoza.pm \
	lib/DateTime/TimeZone/America/Argentina/Rio_Gallegos.pm \
	lib/DateTime/TimeZone/America/Argentina/Salta.pm \
	lib/DateTime/TimeZone/America/Argentina/San_Juan.pm \
	lib/DateTime/TimeZone/America/Argentina/San_Luis.pm \
	lib/DateTime/TimeZone/America/Argentina/Tucuman.pm \
	lib/DateTime/TimeZone/America/Argentina/Ushuaia.pm \
	lib/DateTime/TimeZone/America/Asuncion.pm \
	lib/DateTime/TimeZone/America/Atikokan.pm \
	lib/DateTime/TimeZone/America/Bahia.pm \
	lib/DateTime/TimeZone/America/Bahia_Banderas.pm \
	lib/DateTime/TimeZone/America/Barbados.pm \
	lib/DateTime/TimeZone/America/Belem.pm \
	lib/DateTime/TimeZone/America/Belize.pm \
	lib/DateTime/TimeZone/America/Blanc_Sablon.pm \
	lib/DateTime/TimeZone/America/Boa_Vista.pm \
	lib/DateTime/TimeZone/America/Bogota.pm \
	lib/DateTime/TimeZone/America/Boise.pm \
	lib/DateTime/TimeZone/America/Cambridge_Bay.pm \
	lib/DateTime/TimeZone/America/Campo_Grande.pm \
	lib/DateTime/TimeZone/America/Cancun.pm \
	lib/DateTime/TimeZone/America/Caracas.pm \
	lib/DateTime/TimeZone/America/Cayenne.pm \
	lib/DateTime/TimeZone/America/Cayman.pm \
	lib/DateTime/TimeZone/America/Chicago.pm \
	lib/DateTime/TimeZone/America/Chihuahua.pm \
	lib/DateTime/TimeZone/America/Costa_Rica.pm \
	lib/DateTime/TimeZone/America/Creston.pm \
	lib/DateTime/TimeZone/America/Cuiaba.pm \
	lib/DateTime/TimeZone/America/Curacao.pm \
	lib/DateTime/TimeZone/America/Danmarkshavn.pm \
	lib/DateTime/TimeZone/America/Dawson.pm \
	lib/DateTime/TimeZone/America/Dawson_Creek.pm \
	lib/DateTime/TimeZone/America/Denver.pm \
	lib/DateTime/TimeZone/America/Detroit.pm \
	lib/DateTime/TimeZone/America/Edmonton.pm \
	lib/DateTime/TimeZone/America/Eirunepe.pm \
	lib/DateTime/TimeZone/America/El_Salvador.pm \
	lib/DateTime/TimeZone/America/Fortaleza.pm \
	lib/DateTime/TimeZone/America/Glace_Bay.pm \
	lib/DateTime/TimeZone/America/Godthab.pm \
	lib/DateTime/TimeZone/America/Goose_Bay.pm \
	lib/DateTime/TimeZone/America/Grand_Turk.pm \
	lib/DateTime/TimeZone/America/Guatemala.pm \
	lib/DateTime/TimeZone/America/Guayaquil.pm \
	lib/DateTime/TimeZone/America/Guyana.pm \
	lib/DateTime/TimeZone/America/Halifax.pm \
	lib/DateTime/TimeZone/America/Havana.pm \
	lib/DateTime/TimeZone/America/Hermosillo.pm \
	lib/DateTime/TimeZone/America/Indiana/Indianapolis.pm \
	lib/DateTime/TimeZone/America/Indiana/Knox.pm \
	lib/DateTime/TimeZone/America/Indiana/Marengo.pm \
	lib/DateTime/TimeZone/America/Indiana/Petersburg.pm \
	lib/DateTime/TimeZone/America/Indiana/Tell_City.pm \
	lib/DateTime/TimeZone/America/Indiana/Vevay.pm \
	lib/DateTime/TimeZone/America/Indiana/Vincennes.pm \
	lib/DateTime/TimeZone/America/Indiana/Winamac.pm \
	lib/DateTime/TimeZone/America/Inuvik.pm \
	lib/DateTime/TimeZone/America/Iqaluit.pm \
	lib/DateTime/TimeZone/America/Jamaica.pm \
	lib/DateTime/TimeZone/America/Juneau.pm \
	lib/DateTime/TimeZone/America/Kentucky/Louisville.pm \
	lib/DateTime/TimeZone/America/Kentucky/Monticello.pm \
	lib/DateTime/TimeZone/America/La_Paz.pm \
	lib/DateTime/TimeZone/America/Lima.pm \
	lib/DateTime/TimeZone/America/Los_Angeles.pm \
	lib/DateTime/TimeZone/America/Maceio.pm \
	lib/DateTime/TimeZone/America/Managua.pm \
	lib/DateTime/TimeZone/America/Manaus.pm \
	lib/DateTime/TimeZone/America/Martinique.pm \
	lib/DateTime/TimeZone/America/Matamoros.pm \
	lib/DateTime/TimeZone/America/Mazatlan.pm \
	lib/DateTime/TimeZone/America/Menominee.pm \
	lib/DateTime/TimeZone/America/Merida.pm \
	lib/DateTime/TimeZone/America/Metlakatla.pm \
	lib/DateTime/TimeZone/America/Mexico_City.pm \
	lib/DateTime/TimeZone/America/Miquelon.pm \
	lib/DateTime/TimeZone/America/Moncton.pm \
	lib/DateTime/TimeZone/America/Monterrey.pm \
	lib/DateTime/TimeZone/America/Montevideo.pm \
	lib/DateTime/TimeZone/America/Montreal.pm \
	lib/DateTime/TimeZone/America/Nassau.pm \
	lib/DateTime/TimeZone/America/New_York.pm \
	lib/DateTime/TimeZone/America/Nipigon.pm \
	lib/DateTime/TimeZone/America/Nome.pm \
	lib/DateTime/TimeZone/America/Noronha.pm \
	lib/DateTime/TimeZone/America/North_Dakota/Beulah.pm \
	lib/DateTime/TimeZone/America/North_Dakota/Center.pm \
	lib/DateTime/TimeZone/America/North_Dakota/New_Salem.pm \
	lib/DateTime/TimeZone/America/Ojinaga.pm \
	lib/DateTime/TimeZone/America/Panama.pm \
	lib/DateTime/TimeZone/America/Pangnirtung.pm \
	lib/DateTime/TimeZone/America/Paramaribo.pm \
	lib/DateTime/TimeZone/America/Phoenix.pm \
	lib/DateTime/TimeZone/America/Port_au_Prince.pm \
	lib/DateTime/TimeZone/America/Port_of_Spain.pm \
	lib/DateTime/TimeZone/America/Porto_Velho.pm \
	lib/DateTime/TimeZone/America/Puerto_Rico.pm \
	lib/DateTime/TimeZone/America/Rainy_River.pm \
	lib/DateTime/TimeZone/America/Rankin_Inlet.pm \
	lib/DateTime/TimeZone/America/Recife.pm \
	lib/DateTime/TimeZone/America/Regina.pm \
	lib/DateTime/TimeZone/America/Resolute.pm \
	lib/DateTime/TimeZone/America/Rio_Branco.pm \
	lib/DateTime/TimeZone/America/Santa_Isabel.pm \
	lib/DateTime/TimeZone/America/Santarem.pm \
	lib/DateTime/TimeZone/America/Santiago.pm \
	lib/DateTime/TimeZone/America/Santo_Domingo.pm \
	lib/DateTime/TimeZone/America/Sao_Paulo.pm \
	lib/DateTime/TimeZone/America/Scoresbysund.pm \
	lib/DateTime/TimeZone/America/Sitka.pm \
	lib/DateTime/TimeZone/America/St_Johns.pm \
	lib/DateTime/TimeZone/America/Swift_Current.pm \
	lib/DateTime/TimeZone/America/Tegucigalpa.pm \
	lib/DateTime/TimeZone/America/Thule.pm \
	lib/DateTime/TimeZone/America/Thunder_Bay.pm \
	lib/DateTime/TimeZone/America/Tijuana.pm \
	lib/DateTime/TimeZone/America/Toronto.pm \
	lib/DateTime/TimeZone/America/Vancouver.pm \
	lib/DateTime/TimeZone/America/Whitehorse.pm \
	lib/DateTime/TimeZone/America/Winnipeg.pm \
	lib/DateTime/TimeZone/America/Yakutat.pm \
	lib/DateTime/TimeZone/America/Yellowknife.pm \
	lib/DateTime/TimeZone/Antarctica/Casey.pm \
	lib/DateTime/TimeZone/Antarctica/Davis.pm \
	lib/DateTime/TimeZone/Antarctica/DumontDUrville.pm \
	lib/DateTime/TimeZone/Antarctica/Macquarie.pm \
	lib/DateTime/TimeZone/Antarctica/Mawson.pm \
	lib/DateTime/TimeZone/Antarctica/Palmer.pm \
	lib/DateTime/TimeZone/Antarctica/Rothera.pm \
	lib/DateTime/TimeZone/Antarctica/Syowa.pm \
	lib/DateTime/TimeZone/Antarctica/Vostok.pm \
	lib/DateTime/TimeZone/Asia/Aden.pm \
	lib/DateTime/TimeZone/Asia/Almaty.pm \
	lib/DateTime/TimeZone/Asia/Amman.pm \
	lib/DateTime/TimeZone/Asia/Anadyr.pm \
	lib/DateTime/TimeZone/Asia/Aqtau.pm \
	lib/DateTime/TimeZone/Asia/Aqtobe.pm \
	lib/DateTime/TimeZone/Asia/Ashgabat.pm \
	lib/DateTime/TimeZone/Asia/Baghdad.pm \
	lib/DateTime/TimeZone/Asia/Bahrain.pm \
	lib/DateTime/TimeZone/Asia/Baku.pm \
	lib/DateTime/TimeZone/Asia/Bangkok.pm \
	lib/DateTime/TimeZone/Asia/Beirut.pm \
	lib/DateTime/TimeZone/Asia/Bishkek.pm \
	lib/DateTime/TimeZone/Asia/Brunei.pm \
	lib/DateTime/TimeZone/Asia/Choibalsan.pm \
	lib/DateTime/TimeZone/Asia/Chongqing.pm \
	lib/DateTime/TimeZone/Asia/Colombo.pm \
	lib/DateTime/TimeZone/Asia/Damascus.pm \
	lib/DateTime/TimeZone/Asia/Dhaka.pm \
	lib/DateTime/TimeZone/Asia/Dili.pm \
	lib/DateTime/TimeZone/Asia/Dubai.pm \
	lib/DateTime/TimeZone/Asia/Dushanbe.pm \
	lib/DateTime/TimeZone/Asia/Gaza.pm \
	lib/DateTime/TimeZone/Asia/Harbin.pm \
	lib/DateTime/TimeZone/Asia/Hebron.pm \
	lib/DateTime/TimeZone/Asia/Ho_Chi_Minh.pm \
	lib/DateTime/TimeZone/Asia/Hong_Kong.pm \
	lib/DateTime/TimeZone/Asia/Hovd.pm \
	lib/DateTime/TimeZone/Asia/Irkutsk.pm \
	lib/DateTime/TimeZone/Asia/Jakarta.pm \
	lib/DateTime/TimeZone/Asia/Jayapura.pm \
	lib/DateTime/TimeZone/Asia/Jerusalem.pm \
	lib/DateTime/TimeZone/Asia/Kabul.pm \
	lib/DateTime/TimeZone/Asia/Kamchatka.pm \
	lib/DateTime/TimeZone/Asia/Karachi.pm \
	lib/DateTime/TimeZone/Asia/Kashgar.pm \
	lib/DateTime/TimeZone/Asia/Kathmandu.pm \
	lib/DateTime/TimeZone/Asia/Khandyga.pm \
	lib/DateTime/TimeZone/Asia/Kolkata.pm \
	lib/DateTime/TimeZone/Asia/Krasnoyarsk.pm \
	lib/DateTime/TimeZone/Asia/Kuala_Lumpur.pm \
	lib/DateTime/TimeZone/Asia/Kuching.pm \
	lib/DateTime/TimeZone/Asia/Kuwait.pm \
	lib/DateTime/TimeZone/Asia/Macau.pm \
	lib/DateTime/TimeZone/Asia/Magadan.pm \
	lib/DateTime/TimeZone/Asia/Makassar.pm \
	lib/DateTime/TimeZone/Asia/Manila.pm \
	lib/DateTime/TimeZone/Asia/Muscat.pm \
	lib/DateTime/TimeZone/Asia/Nicosia.pm \
	lib/DateTime/TimeZone/Asia/Novokuznetsk.pm \
	lib/DateTime/TimeZone/Asia/Novosibirsk.pm \
	lib/DateTime/TimeZone/Asia/Omsk.pm \
	lib/DateTime/TimeZone/Asia/Oral.pm \
	lib/DateTime/TimeZone/Asia/Phnom_Penh.pm \
	lib/DateTime/TimeZone/Asia/Pontianak.pm \
	lib/DateTime/TimeZone/Asia/Pyongyang.pm \
	lib/DateTime/TimeZone/Asia/Qatar.pm \
	lib/DateTime/TimeZone/Asia/Qyzylorda.pm \
	lib/DateTime/TimeZone/Asia/Rangoon.pm \
	lib/DateTime/TimeZone/Asia/Riyadh.pm \
	lib/DateTime/TimeZone/Asia/Sakhalin.pm \
	lib/DateTime/TimeZone/Asia/Samarkand.pm \
	lib/DateTime/TimeZone/Asia/Seoul.pm \
	lib/DateTime/TimeZone/Asia/Shanghai.pm \
	lib/DateTime/TimeZone/Asia/Singapore.pm \
	lib/DateTime/TimeZone/Asia/Taipei.pm \
	lib/DateTime/TimeZone/Asia/Tashkent.pm \
	lib/DateTime/TimeZone/Asia/Tbilisi.pm \
	lib/DateTime/TimeZone/Asia/Tehran.pm \
	lib/DateTime/TimeZone/Asia/Thimphu.pm \
	lib/DateTime/TimeZone/Asia/Tokyo.pm \
	lib/DateTime/TimeZone/Asia/Ulaanbaatar.pm \
	lib/DateTime/TimeZone/Asia/Urumqi.pm \
	lib/DateTime/TimeZone/Asia/Ust_Nera.pm \
	lib/DateTime/TimeZone/Asia/Vientiane.pm \
	lib/DateTime/TimeZone/Asia/Vladivostok.pm \
	lib/DateTime/TimeZone/Asia/Yakutsk.pm \
	lib/DateTime/TimeZone/Asia/Yekaterinburg.pm \
	lib/DateTime/TimeZone/Asia/Yerevan.pm \
	lib/DateTime/TimeZone/Atlantic/Azores.pm \
	lib/DateTime/TimeZone/Atlantic/Bermuda.pm \
	lib/DateTime/TimeZone/Atlantic/Canary.pm \
	lib/DateTime/TimeZone/Atlantic/Cape_Verde.pm \
	lib/DateTime/TimeZone/Atlantic/Faroe.pm \
	lib/DateTime/TimeZone/Atlantic/Madeira.pm \
	lib/DateTime/TimeZone/Atlantic/Reykjavik.pm \
	lib/DateTime/TimeZone/Atlantic/South_Georgia.pm \
	lib/DateTime/TimeZone/Atlantic/St_Helena.pm \
	lib/DateTime/TimeZone/Atlantic/Stanley.pm \
	lib/DateTime/TimeZone/Australia/Adelaide.pm \
	lib/DateTime/TimeZone/Australia/Brisbane.pm \
	lib/DateTime/TimeZone/Australia/Broken_Hill.pm \
	lib/DateTime/TimeZone/Australia/Currie.pm \
	lib/DateTime/TimeZone/Australia/Darwin.pm \
	lib/DateTime/TimeZone/Australia/Eucla.pm \
	lib/DateTime/TimeZone/Australia/Hobart.pm \
	lib/DateTime/TimeZone/Australia/Lindeman.pm \
	lib/DateTime/TimeZone/Australia/Lord_Howe.pm \
	lib/DateTime/TimeZone/Australia/Melbourne.pm \
	lib/DateTime/TimeZone/Australia/Perth.pm \
	lib/DateTime/TimeZone/Australia/Sydney.pm \
	lib/DateTime/TimeZone/CET.pm \
	lib/DateTime/TimeZone/CST6CDT.pm \
	lib/DateTime/TimeZone/Catalog.pm \
	lib/DateTime/TimeZone/EET.pm \
	lib/DateTime/TimeZone/EST.pm \
	lib/DateTime/TimeZone/EST5EDT.pm \
	lib/DateTime/TimeZone/Europe/Amsterdam.pm \
	lib/DateTime/TimeZone/Europe/Andorra.pm \
	lib/DateTime/TimeZone/Europe/Athens.pm \
	lib/DateTime/TimeZone/Europe/Belgrade.pm \
	lib/DateTime/TimeZone/Europe/Berlin.pm \
	lib/DateTime/TimeZone/Europe/Brussels.pm \
	lib/DateTime/TimeZone/Europe/Bucharest.pm \
	lib/DateTime/TimeZone/Europe/Budapest.pm \
	lib/DateTime/TimeZone/Europe/Chisinau.pm \
	lib/DateTime/TimeZone/Europe/Copenhagen.pm \
	lib/DateTime/TimeZone/Europe/Dublin.pm \
	lib/DateTime/TimeZone/Europe/Gibraltar.pm \
	lib/DateTime/TimeZone/Europe/Helsinki.pm \
	lib/DateTime/TimeZone/Europe/Istanbul.pm \
	lib/DateTime/TimeZone/Europe/Kaliningrad.pm \
	lib/DateTime/TimeZone/Europe/Kiev.pm \
	lib/DateTime/TimeZone/Europe/Lisbon.pm \
	lib/DateTime/TimeZone/Europe/London.pm \
	lib/DateTime/TimeZone/Europe/Luxembourg.pm \
	lib/DateTime/TimeZone/Europe/Madrid.pm \
	lib/DateTime/TimeZone/Europe/Malta.pm \
	lib/DateTime/TimeZone/Europe/Minsk.pm \
	lib/DateTime/TimeZone/Europe/Monaco.pm \
	lib/DateTime/TimeZone/Europe/Moscow.pm \
	lib/DateTime/TimeZone/Europe/Oslo.pm \
	lib/DateTime/TimeZone/Europe/Paris.pm \
	lib/DateTime/TimeZone/Europe/Prague.pm \
	lib/DateTime/TimeZone/Europe/Riga.pm \
	lib/DateTime/TimeZone/Europe/Rome.pm \
	lib/DateTime/TimeZone/Europe/Samara.pm \
	lib/DateTime/TimeZone/Europe/Simferopol.pm \
	lib/DateTime/TimeZone/Europe/Sofia.pm \
	lib/DateTime/TimeZone/Europe/Stockholm.pm \
	lib/DateTime/TimeZone/Europe/Tallinn.pm \
	lib/DateTime/TimeZone/Europe/Tirane.pm \
	lib/DateTime/TimeZone/Europe/Uzhgorod.pm \
	lib/DateTime/TimeZone/Europe/Vienna.pm \
	lib/DateTime/TimeZone/Europe/Vilnius.pm \
	lib/DateTime/TimeZone/Europe/Volgograd.pm \
	lib/DateTime/TimeZone/Europe/Warsaw.pm \
	lib/DateTime/TimeZone/Europe/Zaporozhye.pm \
	lib/DateTime/TimeZone/Europe/Zurich.pm \
	lib/DateTime/TimeZone/Floating.pm \
	lib/DateTime/TimeZone/HST.pm \
	lib/DateTime/TimeZone/Indian/Antananarivo.pm \
	lib/DateTime/TimeZone/Indian/Chagos.pm \
	lib/DateTime/TimeZone/Indian/Christmas.pm \
	lib/DateTime/TimeZone/Indian/Cocos.pm \
	lib/DateTime/TimeZone/Indian/Comoro.pm \
	lib/DateTime/TimeZone/Indian/Kerguelen.pm \
	lib/DateTime/TimeZone/Indian/Mahe.pm \
	lib/DateTime/TimeZone/Indian/Maldives.pm \
	lib/DateTime/TimeZone/Indian/Mauritius.pm \
	lib/DateTime/TimeZone/Indian/Mayotte.pm \
	lib/DateTime/TimeZone/Indian/Reunion.pm \
	lib/DateTime/TimeZone/Local.pm \
	lib/DateTime/TimeZone/Local/Unix.pm \
	lib/DateTime/TimeZone/Local/VMS.pm \
	lib/DateTime/TimeZone/Local/Win32.pm \
	lib/DateTime/TimeZone/MET.pm \
	lib/DateTime/TimeZone/MST.pm \
	lib/DateTime/TimeZone/MST7MDT.pm \
	lib/DateTime/TimeZone/OffsetOnly.pm \
	lib/DateTime/TimeZone/OlsonDB.pm \
	lib/DateTime/TimeZone/OlsonDB/Change.pm \
	lib/DateTime/TimeZone/OlsonDB/Observance.pm \
	lib/DateTime/TimeZone/OlsonDB/Rule.pm \
	lib/DateTime/TimeZone/OlsonDB/Zone.pm \
	lib/DateTime/TimeZone/PST8PDT.pm \
	lib/DateTime/TimeZone/Pacific/Apia.pm \
	lib/DateTime/TimeZone/Pacific/Auckland.pm \
	lib/DateTime/TimeZone/Pacific/Chatham.pm \
	lib/DateTime/TimeZone/Pacific/Chuuk.pm \
	lib/DateTime/TimeZone/Pacific/Easter.pm \
	lib/DateTime/TimeZone/Pacific/Efate.pm \
	lib/DateTime/TimeZone/Pacific/Enderbury.pm \
	lib/DateTime/TimeZone/Pacific/Fakaofo.pm \
	lib/DateTime/TimeZone/Pacific/Fiji.pm \
	lib/DateTime/TimeZone/Pacific/Funafuti.pm \
	lib/DateTime/TimeZone/Pacific/Galapagos.pm \
	lib/DateTime/TimeZone/Pacific/Gambier.pm \
	lib/DateTime/TimeZone/Pacific/Guadalcanal.pm \
	lib/DateTime/TimeZone/Pacific/Guam.pm \
	lib/DateTime/TimeZone/Pacific/Honolulu.pm \
	lib/DateTime/TimeZone/Pacific/Kiritimati.pm \
	lib/DateTime/TimeZone/Pacific/Kosrae.pm \
	lib/DateTime/TimeZone/Pacific/Kwajalein.pm \
	lib/DateTime/TimeZone/Pacific/Majuro.pm \
	lib/DateTime/TimeZone/Pacific/Marquesas.pm \
	lib/DateTime/TimeZone/Pacific/Midway.pm \
	lib/DateTime/TimeZone/Pacific/Nauru.pm \
	lib/DateTime/TimeZone/Pacific/Niue.pm \
	lib/DateTime/TimeZone/Pacific/Norfolk.pm \
	lib/DateTime/TimeZone/Pacific/Noumea.pm \
	lib/DateTime/TimeZone/Pacific/Pago_Pago.pm \
	lib/DateTime/TimeZone/Pacific/Palau.pm \
	lib/DateTime/TimeZone/Pacific/Pitcairn.pm \
	lib/DateTime/TimeZone/Pacific/Pohnpei.pm \
	lib/DateTime/TimeZone/Pacific/Port_Moresby.pm \
	lib/DateTime/TimeZone/Pacific/Rarotonga.pm \
	lib/DateTime/TimeZone/Pacific/Saipan.pm \
	lib/DateTime/TimeZone/Pacific/Tahiti.pm \
	lib/DateTime/TimeZone/Pacific/Tarawa.pm \
	lib/DateTime/TimeZone/Pacific/Tongatapu.pm \
	lib/DateTime/TimeZone/Pacific/Wake.pm \
	lib/DateTime/TimeZone/Pacific/Wallis.pm \
	lib/DateTime/TimeZone/UTC.pm \
	lib/DateTime/TimeZone/WET.pm

PM_TO_BLIB = lib/DateTime/TimeZone.pm \
	blib/lib/DateTime/TimeZone.pm \
	lib/DateTime/TimeZone/Africa/Abidjan.pm \
	blib/lib/DateTime/TimeZone/Africa/Abidjan.pm \
	lib/DateTime/TimeZone/Africa/Accra.pm \
	blib/lib/DateTime/TimeZone/Africa/Accra.pm \
	lib/DateTime/TimeZone/Africa/Addis_Ababa.pm \
	blib/lib/DateTime/TimeZone/Africa/Addis_Ababa.pm \
	lib/DateTime/TimeZone/Africa/Algiers.pm \
	blib/lib/DateTime/TimeZone/Africa/Algiers.pm \
	lib/DateTime/TimeZone/Africa/Asmara.pm \
	blib/lib/DateTime/TimeZone/Africa/Asmara.pm \
	lib/DateTime/TimeZone/Africa/Bamako.pm \
	blib/lib/DateTime/TimeZone/Africa/Bamako.pm \
	lib/DateTime/TimeZone/Africa/Bangui.pm \
	blib/lib/DateTime/TimeZone/Africa/Bangui.pm \
	lib/DateTime/TimeZone/Africa/Banjul.pm \
	blib/lib/DateTime/TimeZone/Africa/Banjul.pm \
	lib/DateTime/TimeZone/Africa/Bissau.pm \
	blib/lib/DateTime/TimeZone/Africa/Bissau.pm \
	lib/DateTime/TimeZone/Africa/Blantyre.pm \
	blib/lib/DateTime/TimeZone/Africa/Blantyre.pm \
	lib/DateTime/TimeZone/Africa/Brazzaville.pm \
	blib/lib/DateTime/TimeZone/Africa/Brazzaville.pm \
	lib/DateTime/TimeZone/Africa/Bujumbura.pm \
	blib/lib/DateTime/TimeZone/Africa/Bujumbura.pm \
	lib/DateTime/TimeZone/Africa/Cairo.pm \
	blib/lib/DateTime/TimeZone/Africa/Cairo.pm \
	lib/DateTime/TimeZone/Africa/Casablanca.pm \
	blib/lib/DateTime/TimeZone/Africa/Casablanca.pm \
	lib/DateTime/TimeZone/Africa/Ceuta.pm \
	blib/lib/DateTime/TimeZone/Africa/Ceuta.pm \
	lib/DateTime/TimeZone/Africa/Conakry.pm \
	blib/lib/DateTime/TimeZone/Africa/Conakry.pm \
	lib/DateTime/TimeZone/Africa/Dakar.pm \
	blib/lib/DateTime/TimeZone/Africa/Dakar.pm \
	lib/DateTime/TimeZone/Africa/Dar_es_Salaam.pm \
	blib/lib/DateTime/TimeZone/Africa/Dar_es_Salaam.pm \
	lib/DateTime/TimeZone/Africa/Djibouti.pm \
	blib/lib/DateTime/TimeZone/Africa/Djibouti.pm \
	lib/DateTime/TimeZone/Africa/Douala.pm \
	blib/lib/DateTime/TimeZone/Africa/Douala.pm \
	lib/DateTime/TimeZone/Africa/El_Aaiun.pm \
	blib/lib/DateTime/TimeZone/Africa/El_Aaiun.pm \
	lib/DateTime/TimeZone/Africa/Freetown.pm \
	blib/lib/DateTime/TimeZone/Africa/Freetown.pm \
	lib/DateTime/TimeZone/Africa/Gaborone.pm \
	blib/lib/DateTime/TimeZone/Africa/Gaborone.pm \
	lib/DateTime/TimeZone/Africa/Harare.pm \
	blib/lib/DateTime/TimeZone/Africa/Harare.pm \
	lib/DateTime/TimeZone/Africa/Johannesburg.pm \
	blib/lib/DateTime/TimeZone/Africa/Johannesburg.pm \
	lib/DateTime/TimeZone/Africa/Kampala.pm \
	blib/lib/DateTime/TimeZone/Africa/Kampala.pm \
	lib/DateTime/TimeZone/Africa/Khartoum.pm \
	blib/lib/DateTime/TimeZone/Africa/Khartoum.pm \
	lib/DateTime/TimeZone/Africa/Kigali.pm \
	blib/lib/DateTime/TimeZone/Africa/Kigali.pm \
	lib/DateTime/TimeZone/Africa/Kinshasa.pm \
	blib/lib/DateTime/TimeZone/Africa/Kinshasa.pm \
	lib/DateTime/TimeZone/Africa/Lagos.pm \
	blib/lib/DateTime/TimeZone/Africa/Lagos.pm \
	lib/DateTime/TimeZone/Africa/Libreville.pm \
	blib/lib/DateTime/TimeZone/Africa/Libreville.pm \
	lib/DateTime/TimeZone/Africa/Lome.pm \
	blib/lib/DateTime/TimeZone/Africa/Lome.pm \
	lib/DateTime/TimeZone/Africa/Luanda.pm \
	blib/lib/DateTime/TimeZone/Africa/Luanda.pm \
	lib/DateTime/TimeZone/Africa/Lubumbashi.pm \
	blib/lib/DateTime/TimeZone/Africa/Lubumbashi.pm \
	lib/DateTime/TimeZone/Africa/Lusaka.pm \
	blib/lib/DateTime/TimeZone/Africa/Lusaka.pm \
	lib/DateTime/TimeZone/Africa/Malabo.pm \
	blib/lib/DateTime/TimeZone/Africa/Malabo.pm \
	lib/DateTime/TimeZone/Africa/Maputo.pm \
	blib/lib/DateTime/TimeZone/Africa/Maputo.pm \
	lib/DateTime/TimeZone/Africa/Maseru.pm \
	blib/lib/DateTime/TimeZone/Africa/Maseru.pm \
	lib/DateTime/TimeZone/Africa/Mbabane.pm \
	blib/lib/DateTime/TimeZone/Africa/Mbabane.pm \
	lib/DateTime/TimeZone/Africa/Mogadishu.pm \
	blib/lib/DateTime/TimeZone/Africa/Mogadishu.pm \
	lib/DateTime/TimeZone/Africa/Monrovia.pm \
	blib/lib/DateTime/TimeZone/Africa/Monrovia.pm \
	lib/DateTime/TimeZone/Africa/Nairobi.pm \
	blib/lib/DateTime/TimeZone/Africa/Nairobi.pm \
	lib/DateTime/TimeZone/Africa/Ndjamena.pm \
	blib/lib/DateTime/TimeZone/Africa/Ndjamena.pm \
	lib/DateTime/TimeZone/Africa/Niamey.pm \
	blib/lib/DateTime/TimeZone/Africa/Niamey.pm \
	lib/DateTime/TimeZone/Africa/Nouakchott.pm \
	blib/lib/DateTime/TimeZone/Africa/Nouakchott.pm \
	lib/DateTime/TimeZone/Africa/Ouagadougou.pm \
	blib/lib/DateTime/TimeZone/Africa/Ouagadougou.pm \
	lib/DateTime/TimeZone/Africa/Porto_Novo.pm \
	blib/lib/DateTime/TimeZone/Africa/Porto_Novo.pm \
	lib/DateTime/TimeZone/Africa/Sao_Tome.pm \
	blib/lib/DateTime/TimeZone/Africa/Sao_Tome.pm \
	lib/DateTime/TimeZone/Africa/Tripoli.pm \
	blib/lib/DateTime/TimeZone/Africa/Tripoli.pm \
	lib/DateTime/TimeZone/Africa/Tunis.pm \
	blib/lib/DateTime/TimeZone/Africa/Tunis.pm \
	lib/DateTime/TimeZone/Africa/Windhoek.pm \
	blib/lib/DateTime/TimeZone/Africa/Windhoek.pm \
	lib/DateTime/TimeZone/America/Adak.pm \
	blib/lib/DateTime/TimeZone/America/Adak.pm \
	lib/DateTime/TimeZone/America/Anchorage.pm \
	blib/lib/DateTime/TimeZone/America/Anchorage.pm \
	lib/DateTime/TimeZone/America/Antigua.pm \
	blib/lib/DateTime/TimeZone/America/Antigua.pm \
	lib/DateTime/TimeZone/America/Araguaina.pm \
	blib/lib/DateTime/TimeZone/America/Araguaina.pm \
	lib/DateTime/TimeZone/America/Argentina/Buenos_Aires.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Buenos_Aires.pm \
	lib/DateTime/TimeZone/America/Argentina/Catamarca.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Catamarca.pm \
	lib/DateTime/TimeZone/America/Argentina/Cordoba.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Cordoba.pm \
	lib/DateTime/TimeZone/America/Argentina/Jujuy.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Jujuy.pm \
	lib/DateTime/TimeZone/America/Argentina/La_Rioja.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/La_Rioja.pm \
	lib/DateTime/TimeZone/America/Argentina/Mendoza.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Mendoza.pm \
	lib/DateTime/TimeZone/America/Argentina/Rio_Gallegos.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Rio_Gallegos.pm \
	lib/DateTime/TimeZone/America/Argentina/Salta.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Salta.pm \
	lib/DateTime/TimeZone/America/Argentina/San_Juan.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/San_Juan.pm \
	lib/DateTime/TimeZone/America/Argentina/San_Luis.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/San_Luis.pm \
	lib/DateTime/TimeZone/America/Argentina/Tucuman.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Tucuman.pm \
	lib/DateTime/TimeZone/America/Argentina/Ushuaia.pm \
	blib/lib/DateTime/TimeZone/America/Argentina/Ushuaia.pm \
	lib/DateTime/TimeZone/America/Asuncion.pm \
	blib/lib/DateTime/TimeZone/America/Asuncion.pm \
	lib/DateTime/TimeZone/America/Atikokan.pm \
	blib/lib/DateTime/TimeZone/America/Atikokan.pm \
	lib/DateTime/TimeZone/America/Bahia.pm \
	blib/lib/DateTime/TimeZone/America/Bahia.pm \
	lib/DateTime/TimeZone/America/Bahia_Banderas.pm \
	blib/lib/DateTime/TimeZone/America/Bahia_Banderas.pm \
	lib/DateTime/TimeZone/America/Barbados.pm \
	blib/lib/DateTime/TimeZone/America/Barbados.pm \
	lib/DateTime/TimeZone/America/Belem.pm \
	blib/lib/DateTime/TimeZone/America/Belem.pm \
	lib/DateTime/TimeZone/America/Belize.pm \
	blib/lib/DateTime/TimeZone/America/Belize.pm \
	lib/DateTime/TimeZone/America/Blanc_Sablon.pm \
	blib/lib/DateTime/TimeZone/America/Blanc_Sablon.pm \
	lib/DateTime/TimeZone/America/Boa_Vista.pm \
	blib/lib/DateTime/TimeZone/America/Boa_Vista.pm \
	lib/DateTime/TimeZone/America/Bogota.pm \
	blib/lib/DateTime/TimeZone/America/Bogota.pm \
	lib/DateTime/TimeZone/America/Boise.pm \
	blib/lib/DateTime/TimeZone/America/Boise.pm \
	lib/DateTime/TimeZone/America/Cambridge_Bay.pm \
	blib/lib/DateTime/TimeZone/America/Cambridge_Bay.pm \
	lib/DateTime/TimeZone/America/Campo_Grande.pm \
	blib/lib/DateTime/TimeZone/America/Campo_Grande.pm \
	lib/DateTime/TimeZone/America/Cancun.pm \
	blib/lib/DateTime/TimeZone/America/Cancun.pm \
	lib/DateTime/TimeZone/America/Caracas.pm \
	blib/lib/DateTime/TimeZone/America/Caracas.pm \
	lib/DateTime/TimeZone/America/Cayenne.pm \
	blib/lib/DateTime/TimeZone/America/Cayenne.pm \
	lib/DateTime/TimeZone/America/Cayman.pm \
	blib/lib/DateTime/TimeZone/America/Cayman.pm \
	lib/DateTime/TimeZone/America/Chicago.pm \
	blib/lib/DateTime/TimeZone/America/Chicago.pm \
	lib/DateTime/TimeZone/America/Chihuahua.pm \
	blib/lib/DateTime/TimeZone/America/Chihuahua.pm \
	lib/DateTime/TimeZone/America/Costa_Rica.pm \
	blib/lib/DateTime/TimeZone/America/Costa_Rica.pm \
	lib/DateTime/TimeZone/America/Creston.pm \
	blib/lib/DateTime/TimeZone/America/Creston.pm \
	lib/DateTime/TimeZone/America/Cuiaba.pm \
	blib/lib/DateTime/TimeZone/America/Cuiaba.pm \
	lib/DateTime/TimeZone/America/Curacao.pm \
	blib/lib/DateTime/TimeZone/America/Curacao.pm \
	lib/DateTime/TimeZone/America/Danmarkshavn.pm \
	blib/lib/DateTime/TimeZone/America/Danmarkshavn.pm \
	lib/DateTime/TimeZone/America/Dawson.pm \
	blib/lib/DateTime/TimeZone/America/Dawson.pm \
	lib/DateTime/TimeZone/America/Dawson_Creek.pm \
	blib/lib/DateTime/TimeZone/America/Dawson_Creek.pm \
	lib/DateTime/TimeZone/America/Denver.pm \
	blib/lib/DateTime/TimeZone/America/Denver.pm \
	lib/DateTime/TimeZone/America/Detroit.pm \
	blib/lib/DateTime/TimeZone/America/Detroit.pm \
	lib/DateTime/TimeZone/America/Edmonton.pm \
	blib/lib/DateTime/TimeZone/America/Edmonton.pm \
	lib/DateTime/TimeZone/America/Eirunepe.pm \
	blib/lib/DateTime/TimeZone/America/Eirunepe.pm \
	lib/DateTime/TimeZone/America/El_Salvador.pm \
	blib/lib/DateTime/TimeZone/America/El_Salvador.pm \
	lib/DateTime/TimeZone/America/Fortaleza.pm \
	blib/lib/DateTime/TimeZone/America/Fortaleza.pm \
	lib/DateTime/TimeZone/America/Glace_Bay.pm \
	blib/lib/DateTime/TimeZone/America/Glace_Bay.pm \
	lib/DateTime/TimeZone/America/Godthab.pm \
	blib/lib/DateTime/TimeZone/America/Godthab.pm \
	lib/DateTime/TimeZone/America/Goose_Bay.pm \
	blib/lib/DateTime/TimeZone/America/Goose_Bay.pm \
	lib/DateTime/TimeZone/America/Grand_Turk.pm \
	blib/lib/DateTime/TimeZone/America/Grand_Turk.pm \
	lib/DateTime/TimeZone/America/Guatemala.pm \
	blib/lib/DateTime/TimeZone/America/Guatemala.pm \
	lib/DateTime/TimeZone/America/Guayaquil.pm \
	blib/lib/DateTime/TimeZone/America/Guayaquil.pm \
	lib/DateTime/TimeZone/America/Guyana.pm \
	blib/lib/DateTime/TimeZone/America/Guyana.pm \
	lib/DateTime/TimeZone/America/Halifax.pm \
	blib/lib/DateTime/TimeZone/America/Halifax.pm \
	lib/DateTime/TimeZone/America/Havana.pm \
	blib/lib/DateTime/TimeZone/America/Havana.pm \
	lib/DateTime/TimeZone/America/Hermosillo.pm \
	blib/lib/DateTime/TimeZone/America/Hermosillo.pm \
	lib/DateTime/TimeZone/America/Indiana/Indianapolis.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Indianapolis.pm \
	lib/DateTime/TimeZone/America/Indiana/Knox.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Knox.pm \
	lib/DateTime/TimeZone/America/Indiana/Marengo.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Marengo.pm \
	lib/DateTime/TimeZone/America/Indiana/Petersburg.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Petersburg.pm \
	lib/DateTime/TimeZone/America/Indiana/Tell_City.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Tell_City.pm \
	lib/DateTime/TimeZone/America/Indiana/Vevay.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Vevay.pm \
	lib/DateTime/TimeZone/America/Indiana/Vincennes.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Vincennes.pm \
	lib/DateTime/TimeZone/America/Indiana/Winamac.pm \
	blib/lib/DateTime/TimeZone/America/Indiana/Winamac.pm \
	lib/DateTime/TimeZone/America/Inuvik.pm \
	blib/lib/DateTime/TimeZone/America/Inuvik.pm \
	lib/DateTime/TimeZone/America/Iqaluit.pm \
	blib/lib/DateTime/TimeZone/America/Iqaluit.pm \
	lib/DateTime/TimeZone/America/Jamaica.pm \
	blib/lib/DateTime/TimeZone/America/Jamaica.pm \
	lib/DateTime/TimeZone/America/Juneau.pm \
	blib/lib/DateTime/TimeZone/America/Juneau.pm \
	lib/DateTime/TimeZone/America/Kentucky/Louisville.pm \
	blib/lib/DateTime/TimeZone/America/Kentucky/Louisville.pm \
	lib/DateTime/TimeZone/America/Kentucky/Monticello.pm \
	blib/lib/DateTime/TimeZone/America/Kentucky/Monticello.pm \
	lib/DateTime/TimeZone/America/La_Paz.pm \
	blib/lib/DateTime/TimeZone/America/La_Paz.pm \
	lib/DateTime/TimeZone/America/Lima.pm \
	blib/lib/DateTime/TimeZone/America/Lima.pm \
	lib/DateTime/TimeZone/America/Los_Angeles.pm \
	blib/lib/DateTime/TimeZone/America/Los_Angeles.pm \
	lib/DateTime/TimeZone/America/Maceio.pm \
	blib/lib/DateTime/TimeZone/America/Maceio.pm \
	lib/DateTime/TimeZone/America/Managua.pm \
	blib/lib/DateTime/TimeZone/America/Managua.pm \
	lib/DateTime/TimeZone/America/Manaus.pm \
	blib/lib/DateTime/TimeZone/America/Manaus.pm \
	lib/DateTime/TimeZone/America/Martinique.pm \
	blib/lib/DateTime/TimeZone/America/Martinique.pm \
	lib/DateTime/TimeZone/America/Matamoros.pm \
	blib/lib/DateTime/TimeZone/America/Matamoros.pm \
	lib/DateTime/TimeZone/America/Mazatlan.pm \
	blib/lib/DateTime/TimeZone/America/Mazatlan.pm \
	lib/DateTime/TimeZone/America/Menominee.pm \
	blib/lib/DateTime/TimeZone/America/Menominee.pm \
	lib/DateTime/TimeZone/America/Merida.pm \
	blib/lib/DateTime/TimeZone/America/Merida.pm \
	lib/DateTime/TimeZone/America/Metlakatla.pm \
	blib/lib/DateTime/TimeZone/America/Metlakatla.pm \
	lib/DateTime/TimeZone/America/Mexico_City.pm \
	blib/lib/DateTime/TimeZone/America/Mexico_City.pm \
	lib/DateTime/TimeZone/America/Miquelon.pm \
	blib/lib/DateTime/TimeZone/America/Miquelon.pm \
	lib/DateTime/TimeZone/America/Moncton.pm \
	blib/lib/DateTime/TimeZone/America/Moncton.pm \
	lib/DateTime/TimeZone/America/Monterrey.pm \
	blib/lib/DateTime/TimeZone/America/Monterrey.pm \
	lib/DateTime/TimeZone/America/Montevideo.pm \
	blib/lib/DateTime/TimeZone/America/Montevideo.pm \
	lib/DateTime/TimeZone/America/Montreal.pm \
	blib/lib/DateTime/TimeZone/America/Montreal.pm \
	lib/DateTime/TimeZone/America/Nassau.pm \
	blib/lib/DateTime/TimeZone/America/Nassau.pm \
	lib/DateTime/TimeZone/America/New_York.pm \
	blib/lib/DateTime/TimeZone/America/New_York.pm \
	lib/DateTime/TimeZone/America/Nipigon.pm \
	blib/lib/DateTime/TimeZone/America/Nipigon.pm \
	lib/DateTime/TimeZone/America/Nome.pm \
	blib/lib/DateTime/TimeZone/America/Nome.pm \
	lib/DateTime/TimeZone/America/Noronha.pm \
	blib/lib/DateTime/TimeZone/America/Noronha.pm \
	lib/DateTime/TimeZone/America/North_Dakota/Beulah.pm \
	blib/lib/DateTime/TimeZone/America/North_Dakota/Beulah.pm \
	lib/DateTime/TimeZone/America/North_Dakota/Center.pm \
	blib/lib/DateTime/TimeZone/America/North_Dakota/Center.pm \
	lib/DateTime/TimeZone/America/North_Dakota/New_Salem.pm \
	blib/lib/DateTime/TimeZone/America/North_Dakota/New_Salem.pm \
	lib/DateTime/TimeZone/America/Ojinaga.pm \
	blib/lib/DateTime/TimeZone/America/Ojinaga.pm \
	lib/DateTime/TimeZone/America/Panama.pm \
	blib/lib/DateTime/TimeZone/America/Panama.pm \
	lib/DateTime/TimeZone/America/Pangnirtung.pm \
	blib/lib/DateTime/TimeZone/America/Pangnirtung.pm \
	lib/DateTime/TimeZone/America/Paramaribo.pm \
	blib/lib/DateTime/TimeZone/America/Paramaribo.pm \
	lib/DateTime/TimeZone/America/Phoenix.pm \
	blib/lib/DateTime/TimeZone/America/Phoenix.pm \
	lib/DateTime/TimeZone/America/Port_au_Prince.pm \
	blib/lib/DateTime/TimeZone/America/Port_au_Prince.pm \
	lib/DateTime/TimeZone/America/Port_of_Spain.pm \
	blib/lib/DateTime/TimeZone/America/Port_of_Spain.pm \
	lib/DateTime/TimeZone/America/Porto_Velho.pm \
	blib/lib/DateTime/TimeZone/America/Porto_Velho.pm \
	lib/DateTime/TimeZone/America/Puerto_Rico.pm \
	blib/lib/DateTime/TimeZone/America/Puerto_Rico.pm \
	lib/DateTime/TimeZone/America/Rainy_River.pm \
	blib/lib/DateTime/TimeZone/America/Rainy_River.pm \
	lib/DateTime/TimeZone/America/Rankin_Inlet.pm \
	blib/lib/DateTime/TimeZone/America/Rankin_Inlet.pm \
	lib/DateTime/TimeZone/America/Recife.pm \
	blib/lib/DateTime/TimeZone/America/Recife.pm \
	lib/DateTime/TimeZone/America/Regina.pm \
	blib/lib/DateTime/TimeZone/America/Regina.pm \
	lib/DateTime/TimeZone/America/Resolute.pm \
	blib/lib/DateTime/TimeZone/America/Resolute.pm \
	lib/DateTime/TimeZone/America/Rio_Branco.pm \
	blib/lib/DateTime/TimeZone/America/Rio_Branco.pm \
	lib/DateTime/TimeZone/America/Santa_Isabel.pm \
	blib/lib/DateTime/TimeZone/America/Santa_Isabel.pm \
	lib/DateTime/TimeZone/America/Santarem.pm \
	blib/lib/DateTime/TimeZone/America/Santarem.pm \
	lib/DateTime/TimeZone/America/Santiago.pm \
	blib/lib/DateTime/TimeZone/America/Santiago.pm \
	lib/DateTime/TimeZone/America/Santo_Domingo.pm \
	blib/lib/DateTime/TimeZone/America/Santo_Domingo.pm \
	lib/DateTime/TimeZone/America/Sao_Paulo.pm \
	blib/lib/DateTime/TimeZone/America/Sao_Paulo.pm \
	lib/DateTime/TimeZone/America/Scoresbysund.pm \
	blib/lib/DateTime/TimeZone/America/Scoresbysund.pm \
	lib/DateTime/TimeZone/America/Sitka.pm \
	blib/lib/DateTime/TimeZone/America/Sitka.pm \
	lib/DateTime/TimeZone/America/St_Johns.pm \
	blib/lib/DateTime/TimeZone/America/St_Johns.pm \
	lib/DateTime/TimeZone/America/Swift_Current.pm \
	blib/lib/DateTime/TimeZone/America/Swift_Current.pm \
	lib/DateTime/TimeZone/America/Tegucigalpa.pm \
	blib/lib/DateTime/TimeZone/America/Tegucigalpa.pm \
	lib/DateTime/TimeZone/America/Thule.pm \
	blib/lib/DateTime/TimeZone/America/Thule.pm \
	lib/DateTime/TimeZone/America/Thunder_Bay.pm \
	blib/lib/DateTime/TimeZone/America/Thunder_Bay.pm \
	lib/DateTime/TimeZone/America/Tijuana.pm \
	blib/lib/DateTime/TimeZone/America/Tijuana.pm \
	lib/DateTime/TimeZone/America/Toronto.pm \
	blib/lib/DateTime/TimeZone/America/Toronto.pm \
	lib/DateTime/TimeZone/America/Vancouver.pm \
	blib/lib/DateTime/TimeZone/America/Vancouver.pm \
	lib/DateTime/TimeZone/America/Whitehorse.pm \
	blib/lib/DateTime/TimeZone/America/Whitehorse.pm \
	lib/DateTime/TimeZone/America/Winnipeg.pm \
	blib/lib/DateTime/TimeZone/America/Winnipeg.pm \
	lib/DateTime/TimeZone/America/Yakutat.pm \
	blib/lib/DateTime/TimeZone/America/Yakutat.pm \
	lib/DateTime/TimeZone/America/Yellowknife.pm \
	blib/lib/DateTime/TimeZone/America/Yellowknife.pm \
	lib/DateTime/TimeZone/Antarctica/Casey.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Casey.pm \
	lib/DateTime/TimeZone/Antarctica/Davis.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Davis.pm \
	lib/DateTime/TimeZone/Antarctica/DumontDUrville.pm \
	blib/lib/DateTime/TimeZone/Antarctica/DumontDUrville.pm \
	lib/DateTime/TimeZone/Antarctica/Macquarie.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Macquarie.pm \
	lib/DateTime/TimeZone/Antarctica/Mawson.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Mawson.pm \
	lib/DateTime/TimeZone/Antarctica/Palmer.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Palmer.pm \
	lib/DateTime/TimeZone/Antarctica/Rothera.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Rothera.pm \
	lib/DateTime/TimeZone/Antarctica/Syowa.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Syowa.pm \
	lib/DateTime/TimeZone/Antarctica/Vostok.pm \
	blib/lib/DateTime/TimeZone/Antarctica/Vostok.pm \
	lib/DateTime/TimeZone/Asia/Aden.pm \
	blib/lib/DateTime/TimeZone/Asia/Aden.pm \
	lib/DateTime/TimeZone/Asia/Almaty.pm \
	blib/lib/DateTime/TimeZone/Asia/Almaty.pm \
	lib/DateTime/TimeZone/Asia/Amman.pm \
	blib/lib/DateTime/TimeZone/Asia/Amman.pm \
	lib/DateTime/TimeZone/Asia/Anadyr.pm \
	blib/lib/DateTime/TimeZone/Asia/Anadyr.pm \
	lib/DateTime/TimeZone/Asia/Aqtau.pm \
	blib/lib/DateTime/TimeZone/Asia/Aqtau.pm \
	lib/DateTime/TimeZone/Asia/Aqtobe.pm \
	blib/lib/DateTime/TimeZone/Asia/Aqtobe.pm \
	lib/DateTime/TimeZone/Asia/Ashgabat.pm \
	blib/lib/DateTime/TimeZone/Asia/Ashgabat.pm \
	lib/DateTime/TimeZone/Asia/Baghdad.pm \
	blib/lib/DateTime/TimeZone/Asia/Baghdad.pm \
	lib/DateTime/TimeZone/Asia/Bahrain.pm \
	blib/lib/DateTime/TimeZone/Asia/Bahrain.pm \
	lib/DateTime/TimeZone/Asia/Baku.pm \
	blib/lib/DateTime/TimeZone/Asia/Baku.pm \
	lib/DateTime/TimeZone/Asia/Bangkok.pm \
	blib/lib/DateTime/TimeZone/Asia/Bangkok.pm \
	lib/DateTime/TimeZone/Asia/Beirut.pm \
	blib/lib/DateTime/TimeZone/Asia/Beirut.pm \
	lib/DateTime/TimeZone/Asia/Bishkek.pm \
	blib/lib/DateTime/TimeZone/Asia/Bishkek.pm \
	lib/DateTime/TimeZone/Asia/Brunei.pm \
	blib/lib/DateTime/TimeZone/Asia/Brunei.pm \
	lib/DateTime/TimeZone/Asia/Choibalsan.pm \
	blib/lib/DateTime/TimeZone/Asia/Choibalsan.pm \
	lib/DateTime/TimeZone/Asia/Chongqing.pm \
	blib/lib/DateTime/TimeZone/Asia/Chongqing.pm \
	lib/DateTime/TimeZone/Asia/Colombo.pm \
	blib/lib/DateTime/TimeZone/Asia/Colombo.pm \
	lib/DateTime/TimeZone/Asia/Damascus.pm \
	blib/lib/DateTime/TimeZone/Asia/Damascus.pm \
	lib/DateTime/TimeZone/Asia/Dhaka.pm \
	blib/lib/DateTime/TimeZone/Asia/Dhaka.pm \
	lib/DateTime/TimeZone/Asia/Dili.pm \
	blib/lib/DateTime/TimeZone/Asia/Dili.pm \
	lib/DateTime/TimeZone/Asia/Dubai.pm \
	blib/lib/DateTime/TimeZone/Asia/Dubai.pm \
	lib/DateTime/TimeZone/Asia/Dushanbe.pm \
	blib/lib/DateTime/TimeZone/Asia/Dushanbe.pm \
	lib/DateTime/TimeZone/Asia/Gaza.pm \
	blib/lib/DateTime/TimeZone/Asia/Gaza.pm \
	lib/DateTime/TimeZone/Asia/Harbin.pm \
	blib/lib/DateTime/TimeZone/Asia/Harbin.pm \
	lib/DateTime/TimeZone/Asia/Hebron.pm \
	blib/lib/DateTime/TimeZone/Asia/Hebron.pm \
	lib/DateTime/TimeZone/Asia/Ho_Chi_Minh.pm \
	blib/lib/DateTime/TimeZone/Asia/Ho_Chi_Minh.pm \
	lib/DateTime/TimeZone/Asia/Hong_Kong.pm \
	blib/lib/DateTime/TimeZone/Asia/Hong_Kong.pm \
	lib/DateTime/TimeZone/Asia/Hovd.pm \
	blib/lib/DateTime/TimeZone/Asia/Hovd.pm \
	lib/DateTime/TimeZone/Asia/Irkutsk.pm \
	blib/lib/DateTime/TimeZone/Asia/Irkutsk.pm \
	lib/DateTime/TimeZone/Asia/Jakarta.pm \
	blib/lib/DateTime/TimeZone/Asia/Jakarta.pm \
	lib/DateTime/TimeZone/Asia/Jayapura.pm \
	blib/lib/DateTime/TimeZone/Asia/Jayapura.pm \
	lib/DateTime/TimeZone/Asia/Jerusalem.pm \
	blib/lib/DateTime/TimeZone/Asia/Jerusalem.pm \
	lib/DateTime/TimeZone/Asia/Kabul.pm \
	blib/lib/DateTime/TimeZone/Asia/Kabul.pm \
	lib/DateTime/TimeZone/Asia/Kamchatka.pm \
	blib/lib/DateTime/TimeZone/Asia/Kamchatka.pm \
	lib/DateTime/TimeZone/Asia/Karachi.pm \
	blib/lib/DateTime/TimeZone/Asia/Karachi.pm \
	lib/DateTime/TimeZone/Asia/Kashgar.pm \
	blib/lib/DateTime/TimeZone/Asia/Kashgar.pm \
	lib/DateTime/TimeZone/Asia/Kathmandu.pm \
	blib/lib/DateTime/TimeZone/Asia/Kathmandu.pm \
	lib/DateTime/TimeZone/Asia/Khandyga.pm \
	blib/lib/DateTime/TimeZone/Asia/Khandyga.pm \
	lib/DateTime/TimeZone/Asia/Kolkata.pm \
	blib/lib/DateTime/TimeZone/Asia/Kolkata.pm \
	lib/DateTime/TimeZone/Asia/Krasnoyarsk.pm \
	blib/lib/DateTime/TimeZone/Asia/Krasnoyarsk.pm \
	lib/DateTime/TimeZone/Asia/Kuala_Lumpur.pm \
	blib/lib/DateTime/TimeZone/Asia/Kuala_Lumpur.pm \
	lib/DateTime/TimeZone/Asia/Kuching.pm \
	blib/lib/DateTime/TimeZone/Asia/Kuching.pm \
	lib/DateTime/TimeZone/Asia/Kuwait.pm \
	blib/lib/DateTime/TimeZone/Asia/Kuwait.pm \
	lib/DateTime/TimeZone/Asia/Macau.pm \
	blib/lib/DateTime/TimeZone/Asia/Macau.pm \
	lib/DateTime/TimeZone/Asia/Magadan.pm \
	blib/lib/DateTime/TimeZone/Asia/Magadan.pm \
	lib/DateTime/TimeZone/Asia/Makassar.pm \
	blib/lib/DateTime/TimeZone/Asia/Makassar.pm \
	lib/DateTime/TimeZone/Asia/Manila.pm \
	blib/lib/DateTime/TimeZone/Asia/Manila.pm \
	lib/DateTime/TimeZone/Asia/Muscat.pm \
	blib/lib/DateTime/TimeZone/Asia/Muscat.pm \
	lib/DateTime/TimeZone/Asia/Nicosia.pm \
	blib/lib/DateTime/TimeZone/Asia/Nicosia.pm \
	lib/DateTime/TimeZone/Asia/Novokuznetsk.pm \
	blib/lib/DateTime/TimeZone/Asia/Novokuznetsk.pm \
	lib/DateTime/TimeZone/Asia/Novosibirsk.pm \
	blib/lib/DateTime/TimeZone/Asia/Novosibirsk.pm \
	lib/DateTime/TimeZone/Asia/Omsk.pm \
	blib/lib/DateTime/TimeZone/Asia/Omsk.pm \
	lib/DateTime/TimeZone/Asia/Oral.pm \
	blib/lib/DateTime/TimeZone/Asia/Oral.pm \
	lib/DateTime/TimeZone/Asia/Phnom_Penh.pm \
	blib/lib/DateTime/TimeZone/Asia/Phnom_Penh.pm \
	lib/DateTime/TimeZone/Asia/Pontianak.pm \
	blib/lib/DateTime/TimeZone/Asia/Pontianak.pm \
	lib/DateTime/TimeZone/Asia/Pyongyang.pm \
	blib/lib/DateTime/TimeZone/Asia/Pyongyang.pm \
	lib/DateTime/TimeZone/Asia/Qatar.pm \
	blib/lib/DateTime/TimeZone/Asia/Qatar.pm \
	lib/DateTime/TimeZone/Asia/Qyzylorda.pm \
	blib/lib/DateTime/TimeZone/Asia/Qyzylorda.pm \
	lib/DateTime/TimeZone/Asia/Rangoon.pm \
	blib/lib/DateTime/TimeZone/Asia/Rangoon.pm \
	lib/DateTime/TimeZone/Asia/Riyadh.pm \
	blib/lib/DateTime/TimeZone/Asia/Riyadh.pm \
	lib/DateTime/TimeZone/Asia/Sakhalin.pm \
	blib/lib/DateTime/TimeZone/Asia/Sakhalin.pm \
	lib/DateTime/TimeZone/Asia/Samarkand.pm \
	blib/lib/DateTime/TimeZone/Asia/Samarkand.pm \
	lib/DateTime/TimeZone/Asia/Seoul.pm \
	blib/lib/DateTime/TimeZone/Asia/Seoul.pm \
	lib/DateTime/TimeZone/Asia/Shanghai.pm \
	blib/lib/DateTime/TimeZone/Asia/Shanghai.pm \
	lib/DateTime/TimeZone/Asia/Singapore.pm \
	blib/lib/DateTime/TimeZone/Asia/Singapore.pm \
	lib/DateTime/TimeZone/Asia/Taipei.pm \
	blib/lib/DateTime/TimeZone/Asia/Taipei.pm \
	lib/DateTime/TimeZone/Asia/Tashkent.pm \
	blib/lib/DateTime/TimeZone/Asia/Tashkent.pm \
	lib/DateTime/TimeZone/Asia/Tbilisi.pm \
	blib/lib/DateTime/TimeZone/Asia/Tbilisi.pm \
	lib/DateTime/TimeZone/Asia/Tehran.pm \
	blib/lib/DateTime/TimeZone/Asia/Tehran.pm \
	lib/DateTime/TimeZone/Asia/Thimphu.pm \
	blib/lib/DateTime/TimeZone/Asia/Thimphu.pm \
	lib/DateTime/TimeZone/Asia/Tokyo.pm \
	blib/lib/DateTime/TimeZone/Asia/Tokyo.pm \
	lib/DateTime/TimeZone/Asia/Ulaanbaatar.pm \
	blib/lib/DateTime/TimeZone/Asia/Ulaanbaatar.pm \
	lib/DateTime/TimeZone/Asia/Urumqi.pm \
	blib/lib/DateTime/TimeZone/Asia/Urumqi.pm \
	lib/DateTime/TimeZone/Asia/Ust_Nera.pm \
	blib/lib/DateTime/TimeZone/Asia/Ust_Nera.pm \
	lib/DateTime/TimeZone/Asia/Vientiane.pm \
	blib/lib/DateTime/TimeZone/Asia/Vientiane.pm \
	lib/DateTime/TimeZone/Asia/Vladivostok.pm \
	blib/lib/DateTime/TimeZone/Asia/Vladivostok.pm \
	lib/DateTime/TimeZone/Asia/Yakutsk.pm \
	blib/lib/DateTime/TimeZone/Asia/Yakutsk.pm \
	lib/DateTime/TimeZone/Asia/Yekaterinburg.pm \
	blib/lib/DateTime/TimeZone/Asia/Yekaterinburg.pm \
	lib/DateTime/TimeZone/Asia/Yerevan.pm \
	blib/lib/DateTime/TimeZone/Asia/Yerevan.pm \
	lib/DateTime/TimeZone/Atlantic/Azores.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Azores.pm \
	lib/DateTime/TimeZone/Atlantic/Bermuda.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Bermuda.pm \
	lib/DateTime/TimeZone/Atlantic/Canary.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Canary.pm \
	lib/DateTime/TimeZone/Atlantic/Cape_Verde.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Cape_Verde.pm \
	lib/DateTime/TimeZone/Atlantic/Faroe.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Faroe.pm \
	lib/DateTime/TimeZone/Atlantic/Madeira.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Madeira.pm \
	lib/DateTime/TimeZone/Atlantic/Reykjavik.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Reykjavik.pm \
	lib/DateTime/TimeZone/Atlantic/South_Georgia.pm \
	blib/lib/DateTime/TimeZone/Atlantic/South_Georgia.pm \
	lib/DateTime/TimeZone/Atlantic/St_Helena.pm \
	blib/lib/DateTime/TimeZone/Atlantic/St_Helena.pm \
	lib/DateTime/TimeZone/Atlantic/Stanley.pm \
	blib/lib/DateTime/TimeZone/Atlantic/Stanley.pm \
	lib/DateTime/TimeZone/Australia/Adelaide.pm \
	blib/lib/DateTime/TimeZone/Australia/Adelaide.pm \
	lib/DateTime/TimeZone/Australia/Brisbane.pm \
	blib/lib/DateTime/TimeZone/Australia/Brisbane.pm \
	lib/DateTime/TimeZone/Australia/Broken_Hill.pm \
	blib/lib/DateTime/TimeZone/Australia/Broken_Hill.pm \
	lib/DateTime/TimeZone/Australia/Currie.pm \
	blib/lib/DateTime/TimeZone/Australia/Currie.pm \
	lib/DateTime/TimeZone/Australia/Darwin.pm \
	blib/lib/DateTime/TimeZone/Australia/Darwin.pm \
	lib/DateTime/TimeZone/Australia/Eucla.pm \
	blib/lib/DateTime/TimeZone/Australia/Eucla.pm \
	lib/DateTime/TimeZone/Australia/Hobart.pm \
	blib/lib/DateTime/TimeZone/Australia/Hobart.pm \
	lib/DateTime/TimeZone/Australia/Lindeman.pm \
	blib/lib/DateTime/TimeZone/Australia/Lindeman.pm \
	lib/DateTime/TimeZone/Australia/Lord_Howe.pm \
	blib/lib/DateTime/TimeZone/Australia/Lord_Howe.pm \
	lib/DateTime/TimeZone/Australia/Melbourne.pm \
	blib/lib/DateTime/TimeZone/Australia/Melbourne.pm \
	lib/DateTime/TimeZone/Australia/Perth.pm \
	blib/lib/DateTime/TimeZone/Australia/Perth.pm \
	lib/DateTime/TimeZone/Australia/Sydney.pm \
	blib/lib/DateTime/TimeZone/Australia/Sydney.pm \
	lib/DateTime/TimeZone/CET.pm \
	blib/lib/DateTime/TimeZone/CET.pm \
	lib/DateTime/TimeZone/CST6CDT.pm \
	blib/lib/DateTime/TimeZone/CST6CDT.pm \
	lib/DateTime/TimeZone/Catalog.pm \
	blib/lib/DateTime/TimeZone/Catalog.pm \
	lib/DateTime/TimeZone/EET.pm \
	blib/lib/DateTime/TimeZone/EET.pm \
	lib/DateTime/TimeZone/EST.pm \
	blib/lib/DateTime/TimeZone/EST.pm \
	lib/DateTime/TimeZone/EST5EDT.pm \
	blib/lib/DateTime/TimeZone/EST5EDT.pm \
	lib/DateTime/TimeZone/Europe/Amsterdam.pm \
	blib/lib/DateTime/TimeZone/Europe/Amsterdam.pm \
	lib/DateTime/TimeZone/Europe/Andorra.pm \
	blib/lib/DateTime/TimeZone/Europe/Andorra.pm \
	lib/DateTime/TimeZone/Europe/Athens.pm \
	blib/lib/DateTime/TimeZone/Europe/Athens.pm \
	lib/DateTime/TimeZone/Europe/Belgrade.pm \
	blib/lib/DateTime/TimeZone/Europe/Belgrade.pm \
	lib/DateTime/TimeZone/Europe/Berlin.pm \
	blib/lib/DateTime/TimeZone/Europe/Berlin.pm \
	lib/DateTime/TimeZone/Europe/Brussels.pm \
	blib/lib/DateTime/TimeZone/Europe/Brussels.pm \
	lib/DateTime/TimeZone/Europe/Bucharest.pm \
	blib/lib/DateTime/TimeZone/Europe/Bucharest.pm \
	lib/DateTime/TimeZone/Europe/Budapest.pm \
	blib/lib/DateTime/TimeZone/Europe/Budapest.pm \
	lib/DateTime/TimeZone/Europe/Chisinau.pm \
	blib/lib/DateTime/TimeZone/Europe/Chisinau.pm \
	lib/DateTime/TimeZone/Europe/Copenhagen.pm \
	blib/lib/DateTime/TimeZone/Europe/Copenhagen.pm \
	lib/DateTime/TimeZone/Europe/Dublin.pm \
	blib/lib/DateTime/TimeZone/Europe/Dublin.pm \
	lib/DateTime/TimeZone/Europe/Gibraltar.pm \
	blib/lib/DateTime/TimeZone/Europe/Gibraltar.pm \
	lib/DateTime/TimeZone/Europe/Helsinki.pm \
	blib/lib/DateTime/TimeZone/Europe/Helsinki.pm \
	lib/DateTime/TimeZone/Europe/Istanbul.pm \
	blib/lib/DateTime/TimeZone/Europe/Istanbul.pm \
	lib/DateTime/TimeZone/Europe/Kaliningrad.pm \
	blib/lib/DateTime/TimeZone/Europe/Kaliningrad.pm \
	lib/DateTime/TimeZone/Europe/Kiev.pm \
	blib/lib/DateTime/TimeZone/Europe/Kiev.pm \
	lib/DateTime/TimeZone/Europe/Lisbon.pm \
	blib/lib/DateTime/TimeZone/Europe/Lisbon.pm \
	lib/DateTime/TimeZone/Europe/London.pm \
	blib/lib/DateTime/TimeZone/Europe/London.pm \
	lib/DateTime/TimeZone/Europe/Luxembourg.pm \
	blib/lib/DateTime/TimeZone/Europe/Luxembourg.pm \
	lib/DateTime/TimeZone/Europe/Madrid.pm \
	blib/lib/DateTime/TimeZone/Europe/Madrid.pm \
	lib/DateTime/TimeZone/Europe/Malta.pm \
	blib/lib/DateTime/TimeZone/Europe/Malta.pm \
	lib/DateTime/TimeZone/Europe/Minsk.pm \
	blib/lib/DateTime/TimeZone/Europe/Minsk.pm \
	lib/DateTime/TimeZone/Europe/Monaco.pm \
	blib/lib/DateTime/TimeZone/Europe/Monaco.pm \
	lib/DateTime/TimeZone/Europe/Moscow.pm \
	blib/lib/DateTime/TimeZone/Europe/Moscow.pm \
	lib/DateTime/TimeZone/Europe/Oslo.pm \
	blib/lib/DateTime/TimeZone/Europe/Oslo.pm \
	lib/DateTime/TimeZone/Europe/Paris.pm \
	blib/lib/DateTime/TimeZone/Europe/Paris.pm \
	lib/DateTime/TimeZone/Europe/Prague.pm \
	blib/lib/DateTime/TimeZone/Europe/Prague.pm \
	lib/DateTime/TimeZone/Europe/Riga.pm \
	blib/lib/DateTime/TimeZone/Europe/Riga.pm \
	lib/DateTime/TimeZone/Europe/Rome.pm \
	blib/lib/DateTime/TimeZone/Europe/Rome.pm \
	lib/DateTime/TimeZone/Europe/Samara.pm \
	blib/lib/DateTime/TimeZone/Europe/Samara.pm \
	lib/DateTime/TimeZone/Europe/Simferopol.pm \
	blib/lib/DateTime/TimeZone/Europe/Simferopol.pm \
	lib/DateTime/TimeZone/Europe/Sofia.pm \
	blib/lib/DateTime/TimeZone/Europe/Sofia.pm \
	lib/DateTime/TimeZone/Europe/Stockholm.pm \
	blib/lib/DateTime/TimeZone/Europe/Stockholm.pm \
	lib/DateTime/TimeZone/Europe/Tallinn.pm \
	blib/lib/DateTime/TimeZone/Europe/Tallinn.pm \
	lib/DateTime/TimeZone/Europe/Tirane.pm \
	blib/lib/DateTime/TimeZone/Europe/Tirane.pm \
	lib/DateTime/TimeZone/Europe/Uzhgorod.pm \
	blib/lib/DateTime/TimeZone/Europe/Uzhgorod.pm \
	lib/DateTime/TimeZone/Europe/Vienna.pm \
	blib/lib/DateTime/TimeZone/Europe/Vienna.pm \
	lib/DateTime/TimeZone/Europe/Vilnius.pm \
	blib/lib/DateTime/TimeZone/Europe/Vilnius.pm \
	lib/DateTime/TimeZone/Europe/Volgograd.pm \
	blib/lib/DateTime/TimeZone/Europe/Volgograd.pm \
	lib/DateTime/TimeZone/Europe/Warsaw.pm \
	blib/lib/DateTime/TimeZone/Europe/Warsaw.pm \
	lib/DateTime/TimeZone/Europe/Zaporozhye.pm \
	blib/lib/DateTime/TimeZone/Europe/Zaporozhye.pm \
	lib/DateTime/TimeZone/Europe/Zurich.pm \
	blib/lib/DateTime/TimeZone/Europe/Zurich.pm \
	lib/DateTime/TimeZone/Floating.pm \
	blib/lib/DateTime/TimeZone/Floating.pm \
	lib/DateTime/TimeZone/HST.pm \
	blib/lib/DateTime/TimeZone/HST.pm \
	lib/DateTime/TimeZone/Indian/Antananarivo.pm \
	blib/lib/DateTime/TimeZone/Indian/Antananarivo.pm \
	lib/DateTime/TimeZone/Indian/Chagos.pm \
	blib/lib/DateTime/TimeZone/Indian/Chagos.pm \
	lib/DateTime/TimeZone/Indian/Christmas.pm \
	blib/lib/DateTime/TimeZone/Indian/Christmas.pm \
	lib/DateTime/TimeZone/Indian/Cocos.pm \
	blib/lib/DateTime/TimeZone/Indian/Cocos.pm \
	lib/DateTime/TimeZone/Indian/Comoro.pm \
	blib/lib/DateTime/TimeZone/Indian/Comoro.pm \
	lib/DateTime/TimeZone/Indian/Kerguelen.pm \
	blib/lib/DateTime/TimeZone/Indian/Kerguelen.pm \
	lib/DateTime/TimeZone/Indian/Mahe.pm \
	blib/lib/DateTime/TimeZone/Indian/Mahe.pm \
	lib/DateTime/TimeZone/Indian/Maldives.pm \
	blib/lib/DateTime/TimeZone/Indian/Maldives.pm \
	lib/DateTime/TimeZone/Indian/Mauritius.pm \
	blib/lib/DateTime/TimeZone/Indian/Mauritius.pm \
	lib/DateTime/TimeZone/Indian/Mayotte.pm \
	blib/lib/DateTime/TimeZone/Indian/Mayotte.pm \
	lib/DateTime/TimeZone/Indian/Reunion.pm \
	blib/lib/DateTime/TimeZone/Indian/Reunion.pm \
	lib/DateTime/TimeZone/Local.pm \
	blib/lib/DateTime/TimeZone/Local.pm \
	lib/DateTime/TimeZone/Local/Unix.pm \
	blib/lib/DateTime/TimeZone/Local/Unix.pm \
	lib/DateTime/TimeZone/Local/VMS.pm \
	blib/lib/DateTime/TimeZone/Local/VMS.pm \
	lib/DateTime/TimeZone/Local/Win32.pm \
	blib/lib/DateTime/TimeZone/Local/Win32.pm \
	lib/DateTime/TimeZone/MET.pm \
	blib/lib/DateTime/TimeZone/MET.pm \
	lib/DateTime/TimeZone/MST.pm \
	blib/lib/DateTime/TimeZone/MST.pm \
	lib/DateTime/TimeZone/MST7MDT.pm \
	blib/lib/DateTime/TimeZone/MST7MDT.pm \
	lib/DateTime/TimeZone/OffsetOnly.pm \
	blib/lib/DateTime/TimeZone/OffsetOnly.pm \
	lib/DateTime/TimeZone/OlsonDB.pm \
	blib/lib/DateTime/TimeZone/OlsonDB.pm \
	lib/DateTime/TimeZone/OlsonDB/Change.pm \
	blib/lib/DateTime/TimeZone/OlsonDB/Change.pm \
	lib/DateTime/TimeZone/OlsonDB/Observance.pm \
	blib/lib/DateTime/TimeZone/OlsonDB/Observance.pm \
	lib/DateTime/TimeZone/OlsonDB/Rule.pm \
	blib/lib/DateTime/TimeZone/OlsonDB/Rule.pm \
	lib/DateTime/TimeZone/OlsonDB/Zone.pm \
	blib/lib/DateTime/TimeZone/OlsonDB/Zone.pm \
	lib/DateTime/TimeZone/PST8PDT.pm \
	blib/lib/DateTime/TimeZone/PST8PDT.pm \
	lib/DateTime/TimeZone/Pacific/Apia.pm \
	blib/lib/DateTime/TimeZone/Pacific/Apia.pm \
	lib/DateTime/TimeZone/Pacific/Auckland.pm \
	blib/lib/DateTime/TimeZone/Pacific/Auckland.pm \
	lib/DateTime/TimeZone/Pacific/Chatham.pm \
	blib/lib/DateTime/TimeZone/Pacific/Chatham.pm \
	lib/DateTime/TimeZone/Pacific/Chuuk.pm \
	blib/lib/DateTime/TimeZone/Pacific/Chuuk.pm \
	lib/DateTime/TimeZone/Pacific/Easter.pm \
	blib/lib/DateTime/TimeZone/Pacific/Easter.pm \
	lib/DateTime/TimeZone/Pacific/Efate.pm \
	blib/lib/DateTime/TimeZone/Pacific/Efate.pm \
	lib/DateTime/TimeZone/Pacific/Enderbury.pm \
	blib/lib/DateTime/TimeZone/Pacific/Enderbury.pm \
	lib/DateTime/TimeZone/Pacific/Fakaofo.pm \
	blib/lib/DateTime/TimeZone/Pacific/Fakaofo.pm \
	lib/DateTime/TimeZone/Pacific/Fiji.pm \
	blib/lib/DateTime/TimeZone/Pacific/Fiji.pm \
	lib/DateTime/TimeZone/Pacific/Funafuti.pm \
	blib/lib/DateTime/TimeZone/Pacific/Funafuti.pm \
	lib/DateTime/TimeZone/Pacific/Galapagos.pm \
	blib/lib/DateTime/TimeZone/Pacific/Galapagos.pm \
	lib/DateTime/TimeZone/Pacific/Gambier.pm \
	blib/lib/DateTime/TimeZone/Pacific/Gambier.pm \
	lib/DateTime/TimeZone/Pacific/Guadalcanal.pm \
	blib/lib/DateTime/TimeZone/Pacific/Guadalcanal.pm \
	lib/DateTime/TimeZone/Pacific/Guam.pm \
	blib/lib/DateTime/TimeZone/Pacific/Guam.pm \
	lib/DateTime/TimeZone/Pacific/Honolulu.pm \
	blib/lib/DateTime/TimeZone/Pacific/Honolulu.pm \
	lib/DateTime/TimeZone/Pacific/Kiritimati.pm \
	blib/lib/DateTime/TimeZone/Pacific/Kiritimati.pm \
	lib/DateTime/TimeZone/Pacific/Kosrae.pm \
	blib/lib/DateTime/TimeZone/Pacific/Kosrae.pm \
	lib/DateTime/TimeZone/Pacific/Kwajalein.pm \
	blib/lib/DateTime/TimeZone/Pacific/Kwajalein.pm \
	lib/DateTime/TimeZone/Pacific/Majuro.pm \
	blib/lib/DateTime/TimeZone/Pacific/Majuro.pm \
	lib/DateTime/TimeZone/Pacific/Marquesas.pm \
	blib/lib/DateTime/TimeZone/Pacific/Marquesas.pm \
	lib/DateTime/TimeZone/Pacific/Midway.pm \
	blib/lib/DateTime/TimeZone/Pacific/Midway.pm \
	lib/DateTime/TimeZone/Pacific/Nauru.pm \
	blib/lib/DateTime/TimeZone/Pacific/Nauru.pm \
	lib/DateTime/TimeZone/Pacific/Niue.pm \
	blib/lib/DateTime/TimeZone/Pacific/Niue.pm \
	lib/DateTime/TimeZone/Pacific/Norfolk.pm \
	blib/lib/DateTime/TimeZone/Pacific/Norfolk.pm \
	lib/DateTime/TimeZone/Pacific/Noumea.pm \
	blib/lib/DateTime/TimeZone/Pacific/Noumea.pm \
	lib/DateTime/TimeZone/Pacific/Pago_Pago.pm \
	blib/lib/DateTime/TimeZone/Pacific/Pago_Pago.pm \
	lib/DateTime/TimeZone/Pacific/Palau.pm \
	blib/lib/DateTime/TimeZone/Pacific/Palau.pm \
	lib/DateTime/TimeZone/Pacific/Pitcairn.pm \
	blib/lib/DateTime/TimeZone/Pacific/Pitcairn.pm \
	lib/DateTime/TimeZone/Pacific/Pohnpei.pm \
	blib/lib/DateTime/TimeZone/Pacific/Pohnpei.pm \
	lib/DateTime/TimeZone/Pacific/Port_Moresby.pm \
	blib/lib/DateTime/TimeZone/Pacific/Port_Moresby.pm \
	lib/DateTime/TimeZone/Pacific/Rarotonga.pm \
	blib/lib/DateTime/TimeZone/Pacific/Rarotonga.pm \
	lib/DateTime/TimeZone/Pacific/Saipan.pm \
	blib/lib/DateTime/TimeZone/Pacific/Saipan.pm \
	lib/DateTime/TimeZone/Pacific/Tahiti.pm \
	blib/lib/DateTime/TimeZone/Pacific/Tahiti.pm \
	lib/DateTime/TimeZone/Pacific/Tarawa.pm \
	blib/lib/DateTime/TimeZone/Pacific/Tarawa.pm \
	lib/DateTime/TimeZone/Pacific/Tongatapu.pm \
	blib/lib/DateTime/TimeZone/Pacific/Tongatapu.pm \
	lib/DateTime/TimeZone/Pacific/Wake.pm \
	blib/lib/DateTime/TimeZone/Pacific/Wake.pm \
	lib/DateTime/TimeZone/Pacific/Wallis.pm \
	blib/lib/DateTime/TimeZone/Pacific/Wallis.pm \
	lib/DateTime/TimeZone/UTC.pm \
	blib/lib/DateTime/TimeZone/UTC.pm \
	lib/DateTime/TimeZone/WET.pm \
	blib/lib/DateTime/TimeZone/WET.pm


# --- MakeMaker platform_constants section:
MM_Unix_VERSION = 6.84
PERL_MALLOC_DEF = -DPERL_EXTMALLOC_DEF -Dmalloc=Perl_malloc -Dfree=Perl_mfree -Drealloc=Perl_realloc -Dcalloc=Perl_calloc


# --- MakeMaker tool_autosplit section:
# Usage: $(AUTOSPLITFILE) FileToSplit AutoDirToSplitInto
AUTOSPLITFILE = $(ABSPERLRUN)  -e 'use AutoSplit;  autosplit($$$$ARGV[0], $$$$ARGV[1], 0, 1, 1)' --



# --- MakeMaker tool_xsubpp section:


# --- MakeMaker tools_other section:
SHELL = /bin/sh
CHMOD = chmod
CP = cp
MV = mv
NOOP = $(TRUE)
NOECHO = @
RM_F = rm -f
RM_RF = rm -rf
TEST_F = test -f
TOUCH = touch
UMASK_NULL = umask 0
DEV_NULL = > /dev/null 2>&1
MKPATH = $(ABSPERLRUN) -MExtUtils::Command -e 'mkpath' --
EQUALIZE_TIMESTAMP = $(ABSPERLRUN) -MExtUtils::Command -e 'eqtime' --
FALSE = false
TRUE = true
ECHO = echo
ECHO_N = echo -n
UNINST = 0
VERBINST = 0
MOD_INSTALL = $(ABSPERLRUN) -MExtUtils::Install -e 'install([ from_to => {@ARGV}, verbose => '\''$(VERBINST)'\'', uninstall_shadows => '\''$(UNINST)'\'', dir_mode => '\''$(PERM_DIR)'\'' ]);' --
DOC_INSTALL = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'perllocal_install' --
UNINSTALL = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'uninstall' --
WARN_IF_OLD_PACKLIST = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'warn_if_old_packlist' --
MACROSTART = 
MACROEND = 
USEMAKEFILE = -f
FIXIN = $(ABSPERLRUN) -MExtUtils::MY -e 'MY->fixin(shift)' --
CP_NONEMPTY = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'cp_nonempty' --


# --- MakeMaker makemakerdflt section:
makemakerdflt : all
	$(NOECHO) $(NOOP)


# --- MakeMaker dist section:
TAR = tar
TARFLAGS = cvf
ZIP = zip
ZIPFLAGS = -r
COMPRESS = gzip --best
SUFFIX = .gz
SHAR = shar
PREOP = $(NOECHO) $(NOOP)
POSTOP = $(NOECHO) $(NOOP)
TO_UNIX = $(NOECHO) $(NOOP)
CI = ci -u
RCS_LABEL = rcs -Nv$(VERSION_SYM): -q
DIST_CP = best
DIST_DEFAULT = tardist
DISTNAME = DateTime-TimeZone
DISTVNAME = DateTime-TimeZone-1.63


# --- MakeMaker macro section:


# --- MakeMaker depend section:


# --- MakeMaker cflags section:


# --- MakeMaker const_loadlibs section:


# --- MakeMaker const_cccmd section:


# --- MakeMaker post_constants section:


# --- MakeMaker pasthru section:

PASTHRU = LIBPERL_A="$(LIBPERL_A)"\
	LINKTYPE="$(LINKTYPE)"\
	PREFIX="$(PREFIX)"


# --- MakeMaker special_targets section:
.SUFFIXES : .xs .c .C .cpp .i .s .cxx .cc $(OBJ_EXT)

.PHONY: all config static dynamic test linkext manifest blibdirs clean realclean disttest distdir



# --- MakeMaker c_o section:


# --- MakeMaker xs_c section:


# --- MakeMaker xs_o section:


# --- MakeMaker top_targets section:
all :: pure_all manifypods
	$(NOECHO) $(NOOP)


pure_all :: config pm_to_blib subdirs linkext
	$(NOECHO) $(NOOP)

subdirs :: $(MYEXTLIB)
	$(NOECHO) $(NOOP)

config :: $(FIRST_MAKEFILE) blibdirs
	$(NOECHO) $(NOOP)

help :
	perldoc ExtUtils::MakeMaker


# --- MakeMaker blibdirs section:
blibdirs : $(INST_LIBDIR)$(DFSEP).exists $(INST_ARCHLIB)$(DFSEP).exists $(INST_AUTODIR)$(DFSEP).exists $(INST_ARCHAUTODIR)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists $(INST_SCRIPT)$(DFSEP).exists $(INST_MAN1DIR)$(DFSEP).exists $(INST_MAN3DIR)$(DFSEP).exists
	$(NOECHO) $(NOOP)

# Backwards compat with 6.18 through 6.25
blibdirs.ts : blibdirs
	$(NOECHO) $(NOOP)

$(INST_LIBDIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_LIBDIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_LIBDIR)
	$(NOECHO) $(TOUCH) $(INST_LIBDIR)$(DFSEP).exists

$(INST_ARCHLIB)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_ARCHLIB)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_ARCHLIB)
	$(NOECHO) $(TOUCH) $(INST_ARCHLIB)$(DFSEP).exists

$(INST_AUTODIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_AUTODIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_AUTODIR)
	$(NOECHO) $(TOUCH) $(INST_AUTODIR)$(DFSEP).exists

$(INST_ARCHAUTODIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_ARCHAUTODIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_ARCHAUTODIR)
	$(NOECHO) $(TOUCH) $(INST_ARCHAUTODIR)$(DFSEP).exists

$(INST_BIN)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_BIN)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_BIN)
	$(NOECHO) $(TOUCH) $(INST_BIN)$(DFSEP).exists

$(INST_SCRIPT)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_SCRIPT)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_SCRIPT)
	$(NOECHO) $(TOUCH) $(INST_SCRIPT)$(DFSEP).exists

$(INST_MAN1DIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_MAN1DIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_MAN1DIR)
	$(NOECHO) $(TOUCH) $(INST_MAN1DIR)$(DFSEP).exists

$(INST_MAN3DIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_MAN3DIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_MAN3DIR)
	$(NOECHO) $(TOUCH) $(INST_MAN3DIR)$(DFSEP).exists



# --- MakeMaker linkext section:

linkext :: $(LINKTYPE)
	$(NOECHO) $(NOOP)


# --- MakeMaker dlsyms section:


# --- MakeMaker dynamic_bs section:

BOOTSTRAP =


# --- MakeMaker dynamic section:

dynamic :: $(FIRST_MAKEFILE) $(BOOTSTRAP) $(INST_DYNAMIC)
	$(NOECHO) $(NOOP)


# --- MakeMaker dynamic_lib section:


# --- MakeMaker static section:

## $(INST_PM) has been moved to the all: target.
## It remains here for awhile to allow for old usage: "make static"
static :: $(FIRST_MAKEFILE) $(INST_STATIC)
	$(NOECHO) $(NOOP)


# --- MakeMaker static_lib section:


# --- MakeMaker manifypods section:

POD2MAN_EXE = $(PERLRUN) "-MExtUtils::Command::MM" -e pod2man "--"
POD2MAN = $(POD2MAN_EXE)


manifypods : pure_all  \
	lib/DateTime/TimeZone.pm \
	lib/DateTime/TimeZone/Catalog.pm \
	lib/DateTime/TimeZone/Floating.pm \
	lib/DateTime/TimeZone/Local.pm \
	lib/DateTime/TimeZone/Local/Unix.pm \
	lib/DateTime/TimeZone/Local/VMS.pm \
	lib/DateTime/TimeZone/Local/Win32.pm \
	lib/DateTime/TimeZone/OffsetOnly.pm \
	lib/DateTime/TimeZone/OlsonDB.pm \
	lib/DateTime/TimeZone/UTC.pm
	$(NOECHO) $(POD2MAN) --section=3 --perm_rw=$(PERM_RW) \
	  lib/DateTime/TimeZone.pm $(INST_MAN3DIR)/DateTime::TimeZone.$(MAN3EXT) \
	  lib/DateTime/TimeZone/Catalog.pm $(INST_MAN3DIR)/DateTime::TimeZone::Catalog.$(MAN3EXT) \
	  lib/DateTime/TimeZone/Floating.pm $(INST_MAN3DIR)/DateTime::TimeZone::Floating.$(MAN3EXT) \
	  lib/DateTime/TimeZone/Local.pm $(INST_MAN3DIR)/DateTime::TimeZone::Local.$(MAN3EXT) \
	  lib/DateTime/TimeZone/Local/Unix.pm $(INST_MAN3DIR)/DateTime::TimeZone::Local::Unix.$(MAN3EXT) \
	  lib/DateTime/TimeZone/Local/VMS.pm $(INST_MAN3DIR)/DateTime::TimeZone::Local::VMS.$(MAN3EXT) \
	  lib/DateTime/TimeZone/Local/Win32.pm $(INST_MAN3DIR)/DateTime::TimeZone::Local::Win32.$(MAN3EXT) \
	  lib/DateTime/TimeZone/OffsetOnly.pm $(INST_MAN3DIR)/DateTime::TimeZone::OffsetOnly.$(MAN3EXT) \
	  lib/DateTime/TimeZone/OlsonDB.pm $(INST_MAN3DIR)/DateTime::TimeZone::OlsonDB.$(MAN3EXT) \
	  lib/DateTime/TimeZone/UTC.pm $(INST_MAN3DIR)/DateTime::TimeZone::UTC.$(MAN3EXT) 




# --- MakeMaker processPL section:


# --- MakeMaker installbin section:


# --- MakeMaker subdirs section:

# none

# --- MakeMaker clean_subdirs section:
clean_subdirs :
	$(NOECHO) $(NOOP)


# --- MakeMaker clean section:

# Delete temporary files but do not touch installed files. We don't delete
# the Makefile here so a later make realclean still has a makefile to use.

clean :: clean_subdirs
	- $(RM_F) \
	  $(BASEEXT).bso $(BASEEXT).def \
	  $(BASEEXT).exp $(BASEEXT).x \
	  $(BOOTSTRAP) $(INST_ARCHAUTODIR)/extralibs.all \
	  $(INST_ARCHAUTODIR)/extralibs.ld $(MAKE_APERL_FILE) \
	  *$(LIB_EXT) *$(OBJ_EXT) \
	  *perl.core MYMETA.json \
	  MYMETA.yml blibdirs.ts \
	  core core.*perl.*.? \
	  core.[0-9] core.[0-9][0-9] \
	  core.[0-9][0-9][0-9] core.[0-9][0-9][0-9][0-9] \
	  core.[0-9][0-9][0-9][0-9][0-9] lib$(BASEEXT).def \
	  mon.out perl \
	  perl$(EXE_EXT) perl.exe \
	  perlmain.c pm_to_blib \
	  pm_to_blib.ts so_locations \
	  tmon.out 
	- $(RM_RF) \
	  blib 
	  $(NOECHO) $(RM_F) $(MAKEFILE_OLD)
	- $(MV) $(FIRST_MAKEFILE) $(MAKEFILE_OLD) $(DEV_NULL)


# --- MakeMaker realclean_subdirs section:
realclean_subdirs :
	$(NOECHO) $(NOOP)


# --- MakeMaker realclean section:
# Delete temporary files (via clean) and also delete dist files
realclean purge ::  clean realclean_subdirs
	- $(RM_F) \
	  $(MAKEFILE_OLD) $(FIRST_MAKEFILE) 
	- $(RM_RF) \
	  $(DISTVNAME) 


# --- MakeMaker metafile section:
metafile : create_distdir
	$(NOECHO) $(ECHO) Generating META.yml
	$(NOECHO) $(ECHO) '---' > META_new.yml
	$(NOECHO) $(ECHO) 'abstract: '\''Time zone object base class and factory'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'author:' >> META_new.yml
	$(NOECHO) $(ECHO) '  - '\''Dave Rolsky <autarch@urth.org>'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'build_requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Copy: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  Storable: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  Sys::Hostname: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  Test::More: 0.88' >> META_new.yml
	$(NOECHO) $(ECHO) '  Test::Output: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  base: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  lib: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  overload: 0' >> META_new.yml
	$(NOECHO) $(ECHO) 'configure_requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::MakeMaker: 6.30' >> META_new.yml
	$(NOECHO) $(ECHO) 'dynamic_config: 1' >> META_new.yml
	$(NOECHO) $(ECHO) 'generated_by: '\''ExtUtils::MakeMaker version 6.84, CPAN::Meta::Converter version 2.120351'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'license: perl' >> META_new.yml
	$(NOECHO) $(ECHO) 'meta-spec:' >> META_new.yml
	$(NOECHO) $(ECHO) '  url: http://module-build.sourceforge.net/META-spec-v1.4.html' >> META_new.yml
	$(NOECHO) $(ECHO) '  version: 1.4' >> META_new.yml
	$(NOECHO) $(ECHO) 'name: DateTime-TimeZone' >> META_new.yml
	$(NOECHO) $(ECHO) 'no_index:' >> META_new.yml
	$(NOECHO) $(ECHO) '  directory:' >> META_new.yml
	$(NOECHO) $(ECHO) '    - t' >> META_new.yml
	$(NOECHO) $(ECHO) '    - inc' >> META_new.yml
	$(NOECHO) $(ECHO) 'requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  Class::Load: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  Class::Singleton: 1.03' >> META_new.yml
	$(NOECHO) $(ECHO) '  Cwd: 3' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Basename: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Compare: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Find: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Spec: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  List::Util: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  Params::Validate: 0.72' >> META_new.yml
	$(NOECHO) $(ECHO) '  constant: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  parent: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  strict: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  vars: 0' >> META_new.yml
	$(NOECHO) $(ECHO) '  warnings: 0' >> META_new.yml
	$(NOECHO) $(ECHO) 'version: 1.63' >> META_new.yml
	-$(NOECHO) $(MV) META_new.yml $(DISTVNAME)/META.yml
	$(NOECHO) $(ECHO) Generating META.json
	$(NOECHO) $(ECHO) '{' > META_new.json
	$(NOECHO) $(ECHO) '   "abstract" : "Time zone object base class and factory",' >> META_new.json
	$(NOECHO) $(ECHO) '   "author" : [' >> META_new.json
	$(NOECHO) $(ECHO) '      "Dave Rolsky <autarch@urth.org>"' >> META_new.json
	$(NOECHO) $(ECHO) '   ],' >> META_new.json
	$(NOECHO) $(ECHO) '   "dynamic_config" : 1,' >> META_new.json
	$(NOECHO) $(ECHO) '   "generated_by" : "ExtUtils::MakeMaker version 6.84, CPAN::Meta::Converter version 2.120351",' >> META_new.json
	$(NOECHO) $(ECHO) '   "license" : [' >> META_new.json
	$(NOECHO) $(ECHO) '      "perl_5"' >> META_new.json
	$(NOECHO) $(ECHO) '   ],' >> META_new.json
	$(NOECHO) $(ECHO) '   "meta-spec" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "url" : "http://search.cpan.org/perldoc?CPAN::Meta::Spec",' >> META_new.json
	$(NOECHO) $(ECHO) '      "version" : "2"' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "name" : "DateTime-TimeZone",' >> META_new.json
	$(NOECHO) $(ECHO) '   "no_index" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "directory" : [' >> META_new.json
	$(NOECHO) $(ECHO) '         "t",' >> META_new.json
	$(NOECHO) $(ECHO) '         "inc"' >> META_new.json
	$(NOECHO) $(ECHO) '      ]' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "prereqs" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "build" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Copy" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Storable" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Sys::Hostname" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Test::More" : "0.88",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Test::Output" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "base" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "lib" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "overload" : "0"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "configure" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::MakeMaker" : "6.30"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "runtime" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "Class::Load" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Class::Singleton" : "1.03",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Cwd" : "3",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Basename" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Compare" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Find" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Spec" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "List::Util" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Params::Validate" : "0.72",' >> META_new.json
	$(NOECHO) $(ECHO) '            "constant" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "parent" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "strict" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "vars" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "warnings" : "0"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      }' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "release_status" : "stable",' >> META_new.json
	$(NOECHO) $(ECHO) '   "version" : "1.63"' >> META_new.json
	$(NOECHO) $(ECHO) '}' >> META_new.json
	-$(NOECHO) $(MV) META_new.json $(DISTVNAME)/META.json


# --- MakeMaker signature section:
signature :
	cpansign -s


# --- MakeMaker dist_basics section:
distclean :: realclean distcheck
	$(NOECHO) $(NOOP)

distcheck :
	$(PERLRUN) "-MExtUtils::Manifest=fullcheck" -e fullcheck

skipcheck :
	$(PERLRUN) "-MExtUtils::Manifest=skipcheck" -e skipcheck

manifest :
	$(PERLRUN) "-MExtUtils::Manifest=mkmanifest" -e mkmanifest

veryclean : realclean
	$(RM_F) *~ */*~ *.orig */*.orig *.bak */*.bak *.old */*.old



# --- MakeMaker dist_core section:

dist : $(DIST_DEFAULT) $(FIRST_MAKEFILE)
	$(NOECHO) $(ABSPERLRUN) -l -e 'print '\''Warning: Makefile possibly out of date with $(VERSION_FROM)'\''' \
	  -e '    if -e '\''$(VERSION_FROM)'\'' and -M '\''$(VERSION_FROM)'\'' < -M '\''$(FIRST_MAKEFILE)'\'';' --

tardist : $(DISTVNAME).tar$(SUFFIX)
	$(NOECHO) $(NOOP)

uutardist : $(DISTVNAME).tar$(SUFFIX)
	uuencode $(DISTVNAME).tar$(SUFFIX) $(DISTVNAME).tar$(SUFFIX) > $(DISTVNAME).tar$(SUFFIX)_uu
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).tar$(SUFFIX)_uu'

$(DISTVNAME).tar$(SUFFIX) : distdir
	$(PREOP)
	$(TO_UNIX)
	$(TAR) $(TARFLAGS) $(DISTVNAME).tar $(DISTVNAME)
	$(RM_RF) $(DISTVNAME)
	$(COMPRESS) $(DISTVNAME).tar
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).tar$(SUFFIX)'
	$(POSTOP)

zipdist : $(DISTVNAME).zip
	$(NOECHO) $(NOOP)

$(DISTVNAME).zip : distdir
	$(PREOP)
	$(ZIP) $(ZIPFLAGS) $(DISTVNAME).zip $(DISTVNAME)
	$(RM_RF) $(DISTVNAME)
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).zip'
	$(POSTOP)

shdist : distdir
	$(PREOP)
	$(SHAR) $(DISTVNAME) > $(DISTVNAME).shar
	$(RM_RF) $(DISTVNAME)
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).shar'
	$(POSTOP)


# --- MakeMaker distdir section:
create_distdir :
	$(RM_RF) $(DISTVNAME)
	$(PERLRUN) "-MExtUtils::Manifest=manicopy,maniread" \
		-e "manicopy(maniread(),'$(DISTVNAME)', '$(DIST_CP)');"

distdir : create_distdir distmeta 
	$(NOECHO) $(NOOP)



# --- MakeMaker dist_test section:
disttest : distdir
	cd $(DISTVNAME) && $(ABSPERLRUN) Makefile.PL "INSTALLDIRS=site"
	cd $(DISTVNAME) && $(MAKE) $(PASTHRU)
	cd $(DISTVNAME) && $(MAKE) test $(PASTHRU)



# --- MakeMaker dist_ci section:

ci :
	$(PERLRUN) "-MExtUtils::Manifest=maniread" \
	  -e "@all = keys %{ maniread() };" \
	  -e "print(qq{Executing $(CI) @all\n}); system(qq{$(CI) @all});" \
	  -e "print(qq{Executing $(RCS_LABEL) ...\n}); system(qq{$(RCS_LABEL) @all});"


# --- MakeMaker distmeta section:
distmeta : create_distdir metafile
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'exit unless -e q{META.yml};' \
	  -e 'eval { maniadd({q{META.yml} => q{Module YAML meta-data (added by MakeMaker)}}) }' \
	  -e '    or print "Could not add META.yml to MANIFEST: $$$${'\''@'\''}\n"' --
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'exit unless -f q{META.json};' \
	  -e 'eval { maniadd({q{META.json} => q{Module JSON meta-data (added by MakeMaker)}}) }' \
	  -e '    or print "Could not add META.json to MANIFEST: $$$${'\''@'\''}\n"' --



# --- MakeMaker distsignature section:
distsignature : create_distdir
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'eval { maniadd({q{SIGNATURE} => q{Public-key signature (added by MakeMaker)}}) }' \
	  -e '    or print "Could not add SIGNATURE to MANIFEST: $$$${'\''@'\''}\n"' --
	$(NOECHO) cd $(DISTVNAME) && $(TOUCH) SIGNATURE
	cd $(DISTVNAME) && cpansign -s



# --- MakeMaker install section:

install :: pure_install doc_install
	$(NOECHO) $(NOOP)

install_perl :: pure_perl_install doc_perl_install
	$(NOECHO) $(NOOP)

install_site :: pure_site_install doc_site_install
	$(NOECHO) $(NOOP)

install_vendor :: pure_vendor_install doc_vendor_install
	$(NOECHO) $(NOOP)

pure_install :: pure_$(INSTALLDIRS)_install
	$(NOECHO) $(NOOP)

doc_install :: doc_$(INSTALLDIRS)_install
	$(NOECHO) $(NOOP)

pure__install : pure_site_install
	$(NOECHO) $(ECHO) INSTALLDIRS not defined, defaulting to INSTALLDIRS=site

doc__install : doc_site_install
	$(NOECHO) $(ECHO) INSTALLDIRS not defined, defaulting to INSTALLDIRS=site

pure_perl_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read $(PERL_ARCHLIB)/auto/$(FULLEXT)/.packlist \
		write $(DESTINSTALLARCHLIB)/auto/$(FULLEXT)/.packlist \
		$(INST_LIB) $(DESTINSTALLPRIVLIB) \
		$(INST_ARCHLIB) $(DESTINSTALLARCHLIB) \
		$(INST_BIN) $(DESTINSTALLBIN) \
		$(INST_SCRIPT) $(DESTINSTALLSCRIPT) \
		$(INST_MAN1DIR) $(DESTINSTALLMAN1DIR) \
		$(INST_MAN3DIR) $(DESTINSTALLMAN3DIR)
	$(NOECHO) $(WARN_IF_OLD_PACKLIST) \
		$(SITEARCHEXP)/auto/$(FULLEXT)


pure_site_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read $(SITEARCHEXP)/auto/$(FULLEXT)/.packlist \
		write $(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist \
		$(INST_LIB) $(DESTINSTALLSITELIB) \
		$(INST_ARCHLIB) $(DESTINSTALLSITEARCH) \
		$(INST_BIN) $(DESTINSTALLSITEBIN) \
		$(INST_SCRIPT) $(DESTINSTALLSITESCRIPT) \
		$(INST_MAN1DIR) $(DESTINSTALLSITEMAN1DIR) \
		$(INST_MAN3DIR) $(DESTINSTALLSITEMAN3DIR)
	$(NOECHO) $(WARN_IF_OLD_PACKLIST) \
		$(PERL_ARCHLIB)/auto/$(FULLEXT)

pure_vendor_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read $(VENDORARCHEXP)/auto/$(FULLEXT)/.packlist \
		write $(DESTINSTALLVENDORARCH)/auto/$(FULLEXT)/.packlist \
		$(INST_LIB) $(DESTINSTALLVENDORLIB) \
		$(INST_ARCHLIB) $(DESTINSTALLVENDORARCH) \
		$(INST_BIN) $(DESTINSTALLVENDORBIN) \
		$(INST_SCRIPT) $(DESTINSTALLVENDORSCRIPT) \
		$(INST_MAN1DIR) $(DESTINSTALLVENDORMAN1DIR) \
		$(INST_MAN3DIR) $(DESTINSTALLVENDORMAN3DIR)


doc_perl_install :: all
	$(NOECHO) $(ECHO) Appending installation info to $(DESTINSTALLARCHLIB)/perllocal.pod
	-$(NOECHO) $(MKPATH) $(DESTINSTALLARCHLIB)
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLPRIVLIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> $(DESTINSTALLARCHLIB)/perllocal.pod

doc_site_install :: all
	$(NOECHO) $(ECHO) Appending installation info to $(DESTINSTALLARCHLIB)/perllocal.pod
	-$(NOECHO) $(MKPATH) $(DESTINSTALLARCHLIB)
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLSITELIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> $(DESTINSTALLARCHLIB)/perllocal.pod

doc_vendor_install :: all
	$(NOECHO) $(ECHO) Appending installation info to $(DESTINSTALLARCHLIB)/perllocal.pod
	-$(NOECHO) $(MKPATH) $(DESTINSTALLARCHLIB)
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLVENDORLIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> $(DESTINSTALLARCHLIB)/perllocal.pod


uninstall :: uninstall_from_$(INSTALLDIRS)dirs
	$(NOECHO) $(NOOP)

uninstall_from_perldirs ::
	$(NOECHO) $(UNINSTALL) $(PERL_ARCHLIB)/auto/$(FULLEXT)/.packlist

uninstall_from_sitedirs ::
	$(NOECHO) $(UNINSTALL) $(SITEARCHEXP)/auto/$(FULLEXT)/.packlist

uninstall_from_vendordirs ::
	$(NOECHO) $(UNINSTALL) $(VENDORARCHEXP)/auto/$(FULLEXT)/.packlist


# --- MakeMaker force section:
# Phony target to force checking subdirectories.
FORCE :
	$(NOECHO) $(NOOP)


# --- MakeMaker perldepend section:


# --- MakeMaker makefile section:
# We take a very conservative approach here, but it's worth it.
# We move Makefile to Makefile.old here to avoid gnu make looping.
$(FIRST_MAKEFILE) : Makefile.PL $(CONFIGDEP)
	$(NOECHO) $(ECHO) "Makefile out-of-date with respect to $?"
	$(NOECHO) $(ECHO) "Cleaning current config before rebuilding Makefile..."
	-$(NOECHO) $(RM_F) $(MAKEFILE_OLD)
	-$(NOECHO) $(MV)   $(FIRST_MAKEFILE) $(MAKEFILE_OLD)
	- $(MAKE) $(USEMAKEFILE) $(MAKEFILE_OLD) clean $(DEV_NULL)
	$(PERLRUN) Makefile.PL "INSTALLDIRS=site"
	$(NOECHO) $(ECHO) "==> Your Makefile has been rebuilt. <=="
	$(NOECHO) $(ECHO) "==> Please rerun the $(MAKE) command.  <=="
	$(FALSE)



# --- MakeMaker staticmake section:

# --- MakeMaker makeaperl section ---
MAP_TARGET    = perl
FULLPERL      = /usr/bin/perl

$(MAP_TARGET) :: static $(MAKE_APERL_FILE)
	$(MAKE) $(USEMAKEFILE) $(MAKE_APERL_FILE) $@

$(MAKE_APERL_FILE) : $(FIRST_MAKEFILE) pm_to_blib
	$(NOECHO) $(ECHO) Writing \"$(MAKE_APERL_FILE)\" for this $(MAP_TARGET)
	$(NOECHO) $(PERLRUNINST) \
		Makefile.PL DIR= \
		MAKEFILE=$(MAKE_APERL_FILE) LINKTYPE=static \
		MAKEAPERL=1 NORECURS=1 CCCDLFLAGS= \
		INSTALLDIRS=site


# --- MakeMaker test section:

TEST_VERBOSE=0
TEST_TYPE=test_$(LINKTYPE)
TEST_FILE = test.pl
TEST_FILES = t/*.t
TESTDB_SW = -d

testdb :: testdb_$(LINKTYPE)

test :: $(TEST_TYPE) subdirs-test

subdirs-test ::
	$(NOECHO) $(NOOP)


test_dynamic :: pure_all
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) "-MExtUtils::Command::MM" "-MTest::Harness" "-e" "undef *Test::Harness::Switches; test_harness($(TEST_VERBOSE), '$(INST_LIB)', '$(INST_ARCHLIB)')" $(TEST_FILES)

testdb_dynamic :: pure_all
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) $(TESTDB_SW) "-I$(INST_LIB)" "-I$(INST_ARCHLIB)" $(TEST_FILE)

test_ : test_dynamic

test_static :: test_dynamic
testdb_static :: testdb_dynamic


# --- MakeMaker ppd section:
# Creates a PPD (Perl Package Description) for a binary distribution.
ppd :
	$(NOECHO) $(ECHO) '<SOFTPKG NAME="$(DISTNAME)" VERSION="$(VERSION)">' > $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '    <ABSTRACT>Time zone object base class and factory</ABSTRACT>' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '    <AUTHOR>Dave Rolsky &lt;autarch@urth.org&gt;</AUTHOR>' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '    <IMPLEMENTATION>' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Class::Load" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Class::Singleton" VERSION="1.03" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Cwd::" VERSION="3" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="File::Basename" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="File::Compare" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="File::Find" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="File::Spec" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="List::Util" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Params::Validate" VERSION="0.72" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="constant::" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="parent::" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="strict::" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="vars::" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="warnings::" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <ARCHITECTURE NAME="i686-linux-gnu-thread-multi-64int-5.14" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '        <CODEBASE HREF="" />' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '    </IMPLEMENTATION>' >> $(DISTNAME).ppd
	$(NOECHO) $(ECHO) '</SOFTPKG>' >> $(DISTNAME).ppd


# --- MakeMaker pm_to_blib section:

pm_to_blib : $(FIRST_MAKEFILE) $(TO_INST_PM)
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone.pm blib/lib/DateTime/TimeZone.pm \
	  lib/DateTime/TimeZone/Africa/Abidjan.pm blib/lib/DateTime/TimeZone/Africa/Abidjan.pm \
	  lib/DateTime/TimeZone/Africa/Accra.pm blib/lib/DateTime/TimeZone/Africa/Accra.pm \
	  lib/DateTime/TimeZone/Africa/Addis_Ababa.pm blib/lib/DateTime/TimeZone/Africa/Addis_Ababa.pm \
	  lib/DateTime/TimeZone/Africa/Algiers.pm blib/lib/DateTime/TimeZone/Africa/Algiers.pm \
	  lib/DateTime/TimeZone/Africa/Asmara.pm blib/lib/DateTime/TimeZone/Africa/Asmara.pm \
	  lib/DateTime/TimeZone/Africa/Bamako.pm blib/lib/DateTime/TimeZone/Africa/Bamako.pm \
	  lib/DateTime/TimeZone/Africa/Bangui.pm blib/lib/DateTime/TimeZone/Africa/Bangui.pm \
	  lib/DateTime/TimeZone/Africa/Banjul.pm blib/lib/DateTime/TimeZone/Africa/Banjul.pm \
	  lib/DateTime/TimeZone/Africa/Bissau.pm blib/lib/DateTime/TimeZone/Africa/Bissau.pm \
	  lib/DateTime/TimeZone/Africa/Blantyre.pm blib/lib/DateTime/TimeZone/Africa/Blantyre.pm \
	  lib/DateTime/TimeZone/Africa/Brazzaville.pm blib/lib/DateTime/TimeZone/Africa/Brazzaville.pm \
	  lib/DateTime/TimeZone/Africa/Bujumbura.pm blib/lib/DateTime/TimeZone/Africa/Bujumbura.pm \
	  lib/DateTime/TimeZone/Africa/Cairo.pm blib/lib/DateTime/TimeZone/Africa/Cairo.pm \
	  lib/DateTime/TimeZone/Africa/Casablanca.pm blib/lib/DateTime/TimeZone/Africa/Casablanca.pm \
	  lib/DateTime/TimeZone/Africa/Ceuta.pm blib/lib/DateTime/TimeZone/Africa/Ceuta.pm \
	  lib/DateTime/TimeZone/Africa/Conakry.pm blib/lib/DateTime/TimeZone/Africa/Conakry.pm \
	  lib/DateTime/TimeZone/Africa/Dakar.pm blib/lib/DateTime/TimeZone/Africa/Dakar.pm \
	  lib/DateTime/TimeZone/Africa/Dar_es_Salaam.pm blib/lib/DateTime/TimeZone/Africa/Dar_es_Salaam.pm \
	  lib/DateTime/TimeZone/Africa/Djibouti.pm blib/lib/DateTime/TimeZone/Africa/Djibouti.pm \
	  lib/DateTime/TimeZone/Africa/Douala.pm blib/lib/DateTime/TimeZone/Africa/Douala.pm \
	  lib/DateTime/TimeZone/Africa/El_Aaiun.pm blib/lib/DateTime/TimeZone/Africa/El_Aaiun.pm \
	  lib/DateTime/TimeZone/Africa/Freetown.pm blib/lib/DateTime/TimeZone/Africa/Freetown.pm \
	  lib/DateTime/TimeZone/Africa/Gaborone.pm blib/lib/DateTime/TimeZone/Africa/Gaborone.pm \
	  lib/DateTime/TimeZone/Africa/Harare.pm blib/lib/DateTime/TimeZone/Africa/Harare.pm \
	  lib/DateTime/TimeZone/Africa/Johannesburg.pm blib/lib/DateTime/TimeZone/Africa/Johannesburg.pm \
	  lib/DateTime/TimeZone/Africa/Kampala.pm blib/lib/DateTime/TimeZone/Africa/Kampala.pm \
	  lib/DateTime/TimeZone/Africa/Khartoum.pm blib/lib/DateTime/TimeZone/Africa/Khartoum.pm \
	  lib/DateTime/TimeZone/Africa/Kigali.pm blib/lib/DateTime/TimeZone/Africa/Kigali.pm \
	  lib/DateTime/TimeZone/Africa/Kinshasa.pm blib/lib/DateTime/TimeZone/Africa/Kinshasa.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Africa/Lagos.pm blib/lib/DateTime/TimeZone/Africa/Lagos.pm \
	  lib/DateTime/TimeZone/Africa/Libreville.pm blib/lib/DateTime/TimeZone/Africa/Libreville.pm \
	  lib/DateTime/TimeZone/Africa/Lome.pm blib/lib/DateTime/TimeZone/Africa/Lome.pm \
	  lib/DateTime/TimeZone/Africa/Luanda.pm blib/lib/DateTime/TimeZone/Africa/Luanda.pm \
	  lib/DateTime/TimeZone/Africa/Lubumbashi.pm blib/lib/DateTime/TimeZone/Africa/Lubumbashi.pm \
	  lib/DateTime/TimeZone/Africa/Lusaka.pm blib/lib/DateTime/TimeZone/Africa/Lusaka.pm \
	  lib/DateTime/TimeZone/Africa/Malabo.pm blib/lib/DateTime/TimeZone/Africa/Malabo.pm \
	  lib/DateTime/TimeZone/Africa/Maputo.pm blib/lib/DateTime/TimeZone/Africa/Maputo.pm \
	  lib/DateTime/TimeZone/Africa/Maseru.pm blib/lib/DateTime/TimeZone/Africa/Maseru.pm \
	  lib/DateTime/TimeZone/Africa/Mbabane.pm blib/lib/DateTime/TimeZone/Africa/Mbabane.pm \
	  lib/DateTime/TimeZone/Africa/Mogadishu.pm blib/lib/DateTime/TimeZone/Africa/Mogadishu.pm \
	  lib/DateTime/TimeZone/Africa/Monrovia.pm blib/lib/DateTime/TimeZone/Africa/Monrovia.pm \
	  lib/DateTime/TimeZone/Africa/Nairobi.pm blib/lib/DateTime/TimeZone/Africa/Nairobi.pm \
	  lib/DateTime/TimeZone/Africa/Ndjamena.pm blib/lib/DateTime/TimeZone/Africa/Ndjamena.pm \
	  lib/DateTime/TimeZone/Africa/Niamey.pm blib/lib/DateTime/TimeZone/Africa/Niamey.pm \
	  lib/DateTime/TimeZone/Africa/Nouakchott.pm blib/lib/DateTime/TimeZone/Africa/Nouakchott.pm \
	  lib/DateTime/TimeZone/Africa/Ouagadougou.pm blib/lib/DateTime/TimeZone/Africa/Ouagadougou.pm \
	  lib/DateTime/TimeZone/Africa/Porto_Novo.pm blib/lib/DateTime/TimeZone/Africa/Porto_Novo.pm \
	  lib/DateTime/TimeZone/Africa/Sao_Tome.pm blib/lib/DateTime/TimeZone/Africa/Sao_Tome.pm \
	  lib/DateTime/TimeZone/Africa/Tripoli.pm blib/lib/DateTime/TimeZone/Africa/Tripoli.pm \
	  lib/DateTime/TimeZone/Africa/Tunis.pm blib/lib/DateTime/TimeZone/Africa/Tunis.pm \
	  lib/DateTime/TimeZone/Africa/Windhoek.pm blib/lib/DateTime/TimeZone/Africa/Windhoek.pm \
	  lib/DateTime/TimeZone/America/Adak.pm blib/lib/DateTime/TimeZone/America/Adak.pm \
	  lib/DateTime/TimeZone/America/Anchorage.pm blib/lib/DateTime/TimeZone/America/Anchorage.pm \
	  lib/DateTime/TimeZone/America/Antigua.pm blib/lib/DateTime/TimeZone/America/Antigua.pm \
	  lib/DateTime/TimeZone/America/Araguaina.pm blib/lib/DateTime/TimeZone/America/Araguaina.pm \
	  lib/DateTime/TimeZone/America/Argentina/Buenos_Aires.pm blib/lib/DateTime/TimeZone/America/Argentina/Buenos_Aires.pm \
	  lib/DateTime/TimeZone/America/Argentina/Catamarca.pm blib/lib/DateTime/TimeZone/America/Argentina/Catamarca.pm \
	  lib/DateTime/TimeZone/America/Argentina/Cordoba.pm blib/lib/DateTime/TimeZone/America/Argentina/Cordoba.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/America/Argentina/Jujuy.pm blib/lib/DateTime/TimeZone/America/Argentina/Jujuy.pm \
	  lib/DateTime/TimeZone/America/Argentina/La_Rioja.pm blib/lib/DateTime/TimeZone/America/Argentina/La_Rioja.pm \
	  lib/DateTime/TimeZone/America/Argentina/Mendoza.pm blib/lib/DateTime/TimeZone/America/Argentina/Mendoza.pm \
	  lib/DateTime/TimeZone/America/Argentina/Rio_Gallegos.pm blib/lib/DateTime/TimeZone/America/Argentina/Rio_Gallegos.pm \
	  lib/DateTime/TimeZone/America/Argentina/Salta.pm blib/lib/DateTime/TimeZone/America/Argentina/Salta.pm \
	  lib/DateTime/TimeZone/America/Argentina/San_Juan.pm blib/lib/DateTime/TimeZone/America/Argentina/San_Juan.pm \
	  lib/DateTime/TimeZone/America/Argentina/San_Luis.pm blib/lib/DateTime/TimeZone/America/Argentina/San_Luis.pm \
	  lib/DateTime/TimeZone/America/Argentina/Tucuman.pm blib/lib/DateTime/TimeZone/America/Argentina/Tucuman.pm \
	  lib/DateTime/TimeZone/America/Argentina/Ushuaia.pm blib/lib/DateTime/TimeZone/America/Argentina/Ushuaia.pm \
	  lib/DateTime/TimeZone/America/Asuncion.pm blib/lib/DateTime/TimeZone/America/Asuncion.pm \
	  lib/DateTime/TimeZone/America/Atikokan.pm blib/lib/DateTime/TimeZone/America/Atikokan.pm \
	  lib/DateTime/TimeZone/America/Bahia.pm blib/lib/DateTime/TimeZone/America/Bahia.pm \
	  lib/DateTime/TimeZone/America/Bahia_Banderas.pm blib/lib/DateTime/TimeZone/America/Bahia_Banderas.pm \
	  lib/DateTime/TimeZone/America/Barbados.pm blib/lib/DateTime/TimeZone/America/Barbados.pm \
	  lib/DateTime/TimeZone/America/Belem.pm blib/lib/DateTime/TimeZone/America/Belem.pm \
	  lib/DateTime/TimeZone/America/Belize.pm blib/lib/DateTime/TimeZone/America/Belize.pm \
	  lib/DateTime/TimeZone/America/Blanc_Sablon.pm blib/lib/DateTime/TimeZone/America/Blanc_Sablon.pm \
	  lib/DateTime/TimeZone/America/Boa_Vista.pm blib/lib/DateTime/TimeZone/America/Boa_Vista.pm \
	  lib/DateTime/TimeZone/America/Bogota.pm blib/lib/DateTime/TimeZone/America/Bogota.pm \
	  lib/DateTime/TimeZone/America/Boise.pm blib/lib/DateTime/TimeZone/America/Boise.pm \
	  lib/DateTime/TimeZone/America/Cambridge_Bay.pm blib/lib/DateTime/TimeZone/America/Cambridge_Bay.pm \
	  lib/DateTime/TimeZone/America/Campo_Grande.pm blib/lib/DateTime/TimeZone/America/Campo_Grande.pm \
	  lib/DateTime/TimeZone/America/Cancun.pm blib/lib/DateTime/TimeZone/America/Cancun.pm \
	  lib/DateTime/TimeZone/America/Caracas.pm blib/lib/DateTime/TimeZone/America/Caracas.pm \
	  lib/DateTime/TimeZone/America/Cayenne.pm blib/lib/DateTime/TimeZone/America/Cayenne.pm \
	  lib/DateTime/TimeZone/America/Cayman.pm blib/lib/DateTime/TimeZone/America/Cayman.pm \
	  lib/DateTime/TimeZone/America/Chicago.pm blib/lib/DateTime/TimeZone/America/Chicago.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/America/Chihuahua.pm blib/lib/DateTime/TimeZone/America/Chihuahua.pm \
	  lib/DateTime/TimeZone/America/Costa_Rica.pm blib/lib/DateTime/TimeZone/America/Costa_Rica.pm \
	  lib/DateTime/TimeZone/America/Creston.pm blib/lib/DateTime/TimeZone/America/Creston.pm \
	  lib/DateTime/TimeZone/America/Cuiaba.pm blib/lib/DateTime/TimeZone/America/Cuiaba.pm \
	  lib/DateTime/TimeZone/America/Curacao.pm blib/lib/DateTime/TimeZone/America/Curacao.pm \
	  lib/DateTime/TimeZone/America/Danmarkshavn.pm blib/lib/DateTime/TimeZone/America/Danmarkshavn.pm \
	  lib/DateTime/TimeZone/America/Dawson.pm blib/lib/DateTime/TimeZone/America/Dawson.pm \
	  lib/DateTime/TimeZone/America/Dawson_Creek.pm blib/lib/DateTime/TimeZone/America/Dawson_Creek.pm \
	  lib/DateTime/TimeZone/America/Denver.pm blib/lib/DateTime/TimeZone/America/Denver.pm \
	  lib/DateTime/TimeZone/America/Detroit.pm blib/lib/DateTime/TimeZone/America/Detroit.pm \
	  lib/DateTime/TimeZone/America/Edmonton.pm blib/lib/DateTime/TimeZone/America/Edmonton.pm \
	  lib/DateTime/TimeZone/America/Eirunepe.pm blib/lib/DateTime/TimeZone/America/Eirunepe.pm \
	  lib/DateTime/TimeZone/America/El_Salvador.pm blib/lib/DateTime/TimeZone/America/El_Salvador.pm \
	  lib/DateTime/TimeZone/America/Fortaleza.pm blib/lib/DateTime/TimeZone/America/Fortaleza.pm \
	  lib/DateTime/TimeZone/America/Glace_Bay.pm blib/lib/DateTime/TimeZone/America/Glace_Bay.pm \
	  lib/DateTime/TimeZone/America/Godthab.pm blib/lib/DateTime/TimeZone/America/Godthab.pm \
	  lib/DateTime/TimeZone/America/Goose_Bay.pm blib/lib/DateTime/TimeZone/America/Goose_Bay.pm \
	  lib/DateTime/TimeZone/America/Grand_Turk.pm blib/lib/DateTime/TimeZone/America/Grand_Turk.pm \
	  lib/DateTime/TimeZone/America/Guatemala.pm blib/lib/DateTime/TimeZone/America/Guatemala.pm \
	  lib/DateTime/TimeZone/America/Guayaquil.pm blib/lib/DateTime/TimeZone/America/Guayaquil.pm \
	  lib/DateTime/TimeZone/America/Guyana.pm blib/lib/DateTime/TimeZone/America/Guyana.pm \
	  lib/DateTime/TimeZone/America/Halifax.pm blib/lib/DateTime/TimeZone/America/Halifax.pm \
	  lib/DateTime/TimeZone/America/Havana.pm blib/lib/DateTime/TimeZone/America/Havana.pm \
	  lib/DateTime/TimeZone/America/Hermosillo.pm blib/lib/DateTime/TimeZone/America/Hermosillo.pm \
	  lib/DateTime/TimeZone/America/Indiana/Indianapolis.pm blib/lib/DateTime/TimeZone/America/Indiana/Indianapolis.pm \
	  lib/DateTime/TimeZone/America/Indiana/Knox.pm blib/lib/DateTime/TimeZone/America/Indiana/Knox.pm \
	  lib/DateTime/TimeZone/America/Indiana/Marengo.pm blib/lib/DateTime/TimeZone/America/Indiana/Marengo.pm \
	  lib/DateTime/TimeZone/America/Indiana/Petersburg.pm blib/lib/DateTime/TimeZone/America/Indiana/Petersburg.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/America/Indiana/Tell_City.pm blib/lib/DateTime/TimeZone/America/Indiana/Tell_City.pm \
	  lib/DateTime/TimeZone/America/Indiana/Vevay.pm blib/lib/DateTime/TimeZone/America/Indiana/Vevay.pm \
	  lib/DateTime/TimeZone/America/Indiana/Vincennes.pm blib/lib/DateTime/TimeZone/America/Indiana/Vincennes.pm \
	  lib/DateTime/TimeZone/America/Indiana/Winamac.pm blib/lib/DateTime/TimeZone/America/Indiana/Winamac.pm \
	  lib/DateTime/TimeZone/America/Inuvik.pm blib/lib/DateTime/TimeZone/America/Inuvik.pm \
	  lib/DateTime/TimeZone/America/Iqaluit.pm blib/lib/DateTime/TimeZone/America/Iqaluit.pm \
	  lib/DateTime/TimeZone/America/Jamaica.pm blib/lib/DateTime/TimeZone/America/Jamaica.pm \
	  lib/DateTime/TimeZone/America/Juneau.pm blib/lib/DateTime/TimeZone/America/Juneau.pm \
	  lib/DateTime/TimeZone/America/Kentucky/Louisville.pm blib/lib/DateTime/TimeZone/America/Kentucky/Louisville.pm \
	  lib/DateTime/TimeZone/America/Kentucky/Monticello.pm blib/lib/DateTime/TimeZone/America/Kentucky/Monticello.pm \
	  lib/DateTime/TimeZone/America/La_Paz.pm blib/lib/DateTime/TimeZone/America/La_Paz.pm \
	  lib/DateTime/TimeZone/America/Lima.pm blib/lib/DateTime/TimeZone/America/Lima.pm \
	  lib/DateTime/TimeZone/America/Los_Angeles.pm blib/lib/DateTime/TimeZone/America/Los_Angeles.pm \
	  lib/DateTime/TimeZone/America/Maceio.pm blib/lib/DateTime/TimeZone/America/Maceio.pm \
	  lib/DateTime/TimeZone/America/Managua.pm blib/lib/DateTime/TimeZone/America/Managua.pm \
	  lib/DateTime/TimeZone/America/Manaus.pm blib/lib/DateTime/TimeZone/America/Manaus.pm \
	  lib/DateTime/TimeZone/America/Martinique.pm blib/lib/DateTime/TimeZone/America/Martinique.pm \
	  lib/DateTime/TimeZone/America/Matamoros.pm blib/lib/DateTime/TimeZone/America/Matamoros.pm \
	  lib/DateTime/TimeZone/America/Mazatlan.pm blib/lib/DateTime/TimeZone/America/Mazatlan.pm \
	  lib/DateTime/TimeZone/America/Menominee.pm blib/lib/DateTime/TimeZone/America/Menominee.pm \
	  lib/DateTime/TimeZone/America/Merida.pm blib/lib/DateTime/TimeZone/America/Merida.pm \
	  lib/DateTime/TimeZone/America/Metlakatla.pm blib/lib/DateTime/TimeZone/America/Metlakatla.pm \
	  lib/DateTime/TimeZone/America/Mexico_City.pm blib/lib/DateTime/TimeZone/America/Mexico_City.pm \
	  lib/DateTime/TimeZone/America/Miquelon.pm blib/lib/DateTime/TimeZone/America/Miquelon.pm \
	  lib/DateTime/TimeZone/America/Moncton.pm blib/lib/DateTime/TimeZone/America/Moncton.pm \
	  lib/DateTime/TimeZone/America/Monterrey.pm blib/lib/DateTime/TimeZone/America/Monterrey.pm \
	  lib/DateTime/TimeZone/America/Montevideo.pm blib/lib/DateTime/TimeZone/America/Montevideo.pm \
	  lib/DateTime/TimeZone/America/Montreal.pm blib/lib/DateTime/TimeZone/America/Montreal.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/America/Nassau.pm blib/lib/DateTime/TimeZone/America/Nassau.pm \
	  lib/DateTime/TimeZone/America/New_York.pm blib/lib/DateTime/TimeZone/America/New_York.pm \
	  lib/DateTime/TimeZone/America/Nipigon.pm blib/lib/DateTime/TimeZone/America/Nipigon.pm \
	  lib/DateTime/TimeZone/America/Nome.pm blib/lib/DateTime/TimeZone/America/Nome.pm \
	  lib/DateTime/TimeZone/America/Noronha.pm blib/lib/DateTime/TimeZone/America/Noronha.pm \
	  lib/DateTime/TimeZone/America/North_Dakota/Beulah.pm blib/lib/DateTime/TimeZone/America/North_Dakota/Beulah.pm \
	  lib/DateTime/TimeZone/America/North_Dakota/Center.pm blib/lib/DateTime/TimeZone/America/North_Dakota/Center.pm \
	  lib/DateTime/TimeZone/America/North_Dakota/New_Salem.pm blib/lib/DateTime/TimeZone/America/North_Dakota/New_Salem.pm \
	  lib/DateTime/TimeZone/America/Ojinaga.pm blib/lib/DateTime/TimeZone/America/Ojinaga.pm \
	  lib/DateTime/TimeZone/America/Panama.pm blib/lib/DateTime/TimeZone/America/Panama.pm \
	  lib/DateTime/TimeZone/America/Pangnirtung.pm blib/lib/DateTime/TimeZone/America/Pangnirtung.pm \
	  lib/DateTime/TimeZone/America/Paramaribo.pm blib/lib/DateTime/TimeZone/America/Paramaribo.pm \
	  lib/DateTime/TimeZone/America/Phoenix.pm blib/lib/DateTime/TimeZone/America/Phoenix.pm \
	  lib/DateTime/TimeZone/America/Port_au_Prince.pm blib/lib/DateTime/TimeZone/America/Port_au_Prince.pm \
	  lib/DateTime/TimeZone/America/Port_of_Spain.pm blib/lib/DateTime/TimeZone/America/Port_of_Spain.pm \
	  lib/DateTime/TimeZone/America/Porto_Velho.pm blib/lib/DateTime/TimeZone/America/Porto_Velho.pm \
	  lib/DateTime/TimeZone/America/Puerto_Rico.pm blib/lib/DateTime/TimeZone/America/Puerto_Rico.pm \
	  lib/DateTime/TimeZone/America/Rainy_River.pm blib/lib/DateTime/TimeZone/America/Rainy_River.pm \
	  lib/DateTime/TimeZone/America/Rankin_Inlet.pm blib/lib/DateTime/TimeZone/America/Rankin_Inlet.pm \
	  lib/DateTime/TimeZone/America/Recife.pm blib/lib/DateTime/TimeZone/America/Recife.pm \
	  lib/DateTime/TimeZone/America/Regina.pm blib/lib/DateTime/TimeZone/America/Regina.pm \
	  lib/DateTime/TimeZone/America/Resolute.pm blib/lib/DateTime/TimeZone/America/Resolute.pm \
	  lib/DateTime/TimeZone/America/Rio_Branco.pm blib/lib/DateTime/TimeZone/America/Rio_Branco.pm \
	  lib/DateTime/TimeZone/America/Santa_Isabel.pm blib/lib/DateTime/TimeZone/America/Santa_Isabel.pm \
	  lib/DateTime/TimeZone/America/Santarem.pm blib/lib/DateTime/TimeZone/America/Santarem.pm \
	  lib/DateTime/TimeZone/America/Santiago.pm blib/lib/DateTime/TimeZone/America/Santiago.pm \
	  lib/DateTime/TimeZone/America/Santo_Domingo.pm blib/lib/DateTime/TimeZone/America/Santo_Domingo.pm \
	  lib/DateTime/TimeZone/America/Sao_Paulo.pm blib/lib/DateTime/TimeZone/America/Sao_Paulo.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/America/Scoresbysund.pm blib/lib/DateTime/TimeZone/America/Scoresbysund.pm \
	  lib/DateTime/TimeZone/America/Sitka.pm blib/lib/DateTime/TimeZone/America/Sitka.pm \
	  lib/DateTime/TimeZone/America/St_Johns.pm blib/lib/DateTime/TimeZone/America/St_Johns.pm \
	  lib/DateTime/TimeZone/America/Swift_Current.pm blib/lib/DateTime/TimeZone/America/Swift_Current.pm \
	  lib/DateTime/TimeZone/America/Tegucigalpa.pm blib/lib/DateTime/TimeZone/America/Tegucigalpa.pm \
	  lib/DateTime/TimeZone/America/Thule.pm blib/lib/DateTime/TimeZone/America/Thule.pm \
	  lib/DateTime/TimeZone/America/Thunder_Bay.pm blib/lib/DateTime/TimeZone/America/Thunder_Bay.pm \
	  lib/DateTime/TimeZone/America/Tijuana.pm blib/lib/DateTime/TimeZone/America/Tijuana.pm \
	  lib/DateTime/TimeZone/America/Toronto.pm blib/lib/DateTime/TimeZone/America/Toronto.pm \
	  lib/DateTime/TimeZone/America/Vancouver.pm blib/lib/DateTime/TimeZone/America/Vancouver.pm \
	  lib/DateTime/TimeZone/America/Whitehorse.pm blib/lib/DateTime/TimeZone/America/Whitehorse.pm \
	  lib/DateTime/TimeZone/America/Winnipeg.pm blib/lib/DateTime/TimeZone/America/Winnipeg.pm \
	  lib/DateTime/TimeZone/America/Yakutat.pm blib/lib/DateTime/TimeZone/America/Yakutat.pm \
	  lib/DateTime/TimeZone/America/Yellowknife.pm blib/lib/DateTime/TimeZone/America/Yellowknife.pm \
	  lib/DateTime/TimeZone/Antarctica/Casey.pm blib/lib/DateTime/TimeZone/Antarctica/Casey.pm \
	  lib/DateTime/TimeZone/Antarctica/Davis.pm blib/lib/DateTime/TimeZone/Antarctica/Davis.pm \
	  lib/DateTime/TimeZone/Antarctica/DumontDUrville.pm blib/lib/DateTime/TimeZone/Antarctica/DumontDUrville.pm \
	  lib/DateTime/TimeZone/Antarctica/Macquarie.pm blib/lib/DateTime/TimeZone/Antarctica/Macquarie.pm \
	  lib/DateTime/TimeZone/Antarctica/Mawson.pm blib/lib/DateTime/TimeZone/Antarctica/Mawson.pm \
	  lib/DateTime/TimeZone/Antarctica/Palmer.pm blib/lib/DateTime/TimeZone/Antarctica/Palmer.pm \
	  lib/DateTime/TimeZone/Antarctica/Rothera.pm blib/lib/DateTime/TimeZone/Antarctica/Rothera.pm \
	  lib/DateTime/TimeZone/Antarctica/Syowa.pm blib/lib/DateTime/TimeZone/Antarctica/Syowa.pm \
	  lib/DateTime/TimeZone/Antarctica/Vostok.pm blib/lib/DateTime/TimeZone/Antarctica/Vostok.pm \
	  lib/DateTime/TimeZone/Asia/Aden.pm blib/lib/DateTime/TimeZone/Asia/Aden.pm \
	  lib/DateTime/TimeZone/Asia/Almaty.pm blib/lib/DateTime/TimeZone/Asia/Almaty.pm \
	  lib/DateTime/TimeZone/Asia/Amman.pm blib/lib/DateTime/TimeZone/Asia/Amman.pm \
	  lib/DateTime/TimeZone/Asia/Anadyr.pm blib/lib/DateTime/TimeZone/Asia/Anadyr.pm \
	  lib/DateTime/TimeZone/Asia/Aqtau.pm blib/lib/DateTime/TimeZone/Asia/Aqtau.pm \
	  lib/DateTime/TimeZone/Asia/Aqtobe.pm blib/lib/DateTime/TimeZone/Asia/Aqtobe.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Asia/Ashgabat.pm blib/lib/DateTime/TimeZone/Asia/Ashgabat.pm \
	  lib/DateTime/TimeZone/Asia/Baghdad.pm blib/lib/DateTime/TimeZone/Asia/Baghdad.pm \
	  lib/DateTime/TimeZone/Asia/Bahrain.pm blib/lib/DateTime/TimeZone/Asia/Bahrain.pm \
	  lib/DateTime/TimeZone/Asia/Baku.pm blib/lib/DateTime/TimeZone/Asia/Baku.pm \
	  lib/DateTime/TimeZone/Asia/Bangkok.pm blib/lib/DateTime/TimeZone/Asia/Bangkok.pm \
	  lib/DateTime/TimeZone/Asia/Beirut.pm blib/lib/DateTime/TimeZone/Asia/Beirut.pm \
	  lib/DateTime/TimeZone/Asia/Bishkek.pm blib/lib/DateTime/TimeZone/Asia/Bishkek.pm \
	  lib/DateTime/TimeZone/Asia/Brunei.pm blib/lib/DateTime/TimeZone/Asia/Brunei.pm \
	  lib/DateTime/TimeZone/Asia/Choibalsan.pm blib/lib/DateTime/TimeZone/Asia/Choibalsan.pm \
	  lib/DateTime/TimeZone/Asia/Chongqing.pm blib/lib/DateTime/TimeZone/Asia/Chongqing.pm \
	  lib/DateTime/TimeZone/Asia/Colombo.pm blib/lib/DateTime/TimeZone/Asia/Colombo.pm \
	  lib/DateTime/TimeZone/Asia/Damascus.pm blib/lib/DateTime/TimeZone/Asia/Damascus.pm \
	  lib/DateTime/TimeZone/Asia/Dhaka.pm blib/lib/DateTime/TimeZone/Asia/Dhaka.pm \
	  lib/DateTime/TimeZone/Asia/Dili.pm blib/lib/DateTime/TimeZone/Asia/Dili.pm \
	  lib/DateTime/TimeZone/Asia/Dubai.pm blib/lib/DateTime/TimeZone/Asia/Dubai.pm \
	  lib/DateTime/TimeZone/Asia/Dushanbe.pm blib/lib/DateTime/TimeZone/Asia/Dushanbe.pm \
	  lib/DateTime/TimeZone/Asia/Gaza.pm blib/lib/DateTime/TimeZone/Asia/Gaza.pm \
	  lib/DateTime/TimeZone/Asia/Harbin.pm blib/lib/DateTime/TimeZone/Asia/Harbin.pm \
	  lib/DateTime/TimeZone/Asia/Hebron.pm blib/lib/DateTime/TimeZone/Asia/Hebron.pm \
	  lib/DateTime/TimeZone/Asia/Ho_Chi_Minh.pm blib/lib/DateTime/TimeZone/Asia/Ho_Chi_Minh.pm \
	  lib/DateTime/TimeZone/Asia/Hong_Kong.pm blib/lib/DateTime/TimeZone/Asia/Hong_Kong.pm \
	  lib/DateTime/TimeZone/Asia/Hovd.pm blib/lib/DateTime/TimeZone/Asia/Hovd.pm \
	  lib/DateTime/TimeZone/Asia/Irkutsk.pm blib/lib/DateTime/TimeZone/Asia/Irkutsk.pm \
	  lib/DateTime/TimeZone/Asia/Jakarta.pm blib/lib/DateTime/TimeZone/Asia/Jakarta.pm \
	  lib/DateTime/TimeZone/Asia/Jayapura.pm blib/lib/DateTime/TimeZone/Asia/Jayapura.pm \
	  lib/DateTime/TimeZone/Asia/Jerusalem.pm blib/lib/DateTime/TimeZone/Asia/Jerusalem.pm \
	  lib/DateTime/TimeZone/Asia/Kabul.pm blib/lib/DateTime/TimeZone/Asia/Kabul.pm \
	  lib/DateTime/TimeZone/Asia/Kamchatka.pm blib/lib/DateTime/TimeZone/Asia/Kamchatka.pm \
	  lib/DateTime/TimeZone/Asia/Karachi.pm blib/lib/DateTime/TimeZone/Asia/Karachi.pm \
	  lib/DateTime/TimeZone/Asia/Kashgar.pm blib/lib/DateTime/TimeZone/Asia/Kashgar.pm \
	  lib/DateTime/TimeZone/Asia/Kathmandu.pm blib/lib/DateTime/TimeZone/Asia/Kathmandu.pm \
	  lib/DateTime/TimeZone/Asia/Khandyga.pm blib/lib/DateTime/TimeZone/Asia/Khandyga.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Asia/Kolkata.pm blib/lib/DateTime/TimeZone/Asia/Kolkata.pm \
	  lib/DateTime/TimeZone/Asia/Krasnoyarsk.pm blib/lib/DateTime/TimeZone/Asia/Krasnoyarsk.pm \
	  lib/DateTime/TimeZone/Asia/Kuala_Lumpur.pm blib/lib/DateTime/TimeZone/Asia/Kuala_Lumpur.pm \
	  lib/DateTime/TimeZone/Asia/Kuching.pm blib/lib/DateTime/TimeZone/Asia/Kuching.pm \
	  lib/DateTime/TimeZone/Asia/Kuwait.pm blib/lib/DateTime/TimeZone/Asia/Kuwait.pm \
	  lib/DateTime/TimeZone/Asia/Macau.pm blib/lib/DateTime/TimeZone/Asia/Macau.pm \
	  lib/DateTime/TimeZone/Asia/Magadan.pm blib/lib/DateTime/TimeZone/Asia/Magadan.pm \
	  lib/DateTime/TimeZone/Asia/Makassar.pm blib/lib/DateTime/TimeZone/Asia/Makassar.pm \
	  lib/DateTime/TimeZone/Asia/Manila.pm blib/lib/DateTime/TimeZone/Asia/Manila.pm \
	  lib/DateTime/TimeZone/Asia/Muscat.pm blib/lib/DateTime/TimeZone/Asia/Muscat.pm \
	  lib/DateTime/TimeZone/Asia/Nicosia.pm blib/lib/DateTime/TimeZone/Asia/Nicosia.pm \
	  lib/DateTime/TimeZone/Asia/Novokuznetsk.pm blib/lib/DateTime/TimeZone/Asia/Novokuznetsk.pm \
	  lib/DateTime/TimeZone/Asia/Novosibirsk.pm blib/lib/DateTime/TimeZone/Asia/Novosibirsk.pm \
	  lib/DateTime/TimeZone/Asia/Omsk.pm blib/lib/DateTime/TimeZone/Asia/Omsk.pm \
	  lib/DateTime/TimeZone/Asia/Oral.pm blib/lib/DateTime/TimeZone/Asia/Oral.pm \
	  lib/DateTime/TimeZone/Asia/Phnom_Penh.pm blib/lib/DateTime/TimeZone/Asia/Phnom_Penh.pm \
	  lib/DateTime/TimeZone/Asia/Pontianak.pm blib/lib/DateTime/TimeZone/Asia/Pontianak.pm \
	  lib/DateTime/TimeZone/Asia/Pyongyang.pm blib/lib/DateTime/TimeZone/Asia/Pyongyang.pm \
	  lib/DateTime/TimeZone/Asia/Qatar.pm blib/lib/DateTime/TimeZone/Asia/Qatar.pm \
	  lib/DateTime/TimeZone/Asia/Qyzylorda.pm blib/lib/DateTime/TimeZone/Asia/Qyzylorda.pm \
	  lib/DateTime/TimeZone/Asia/Rangoon.pm blib/lib/DateTime/TimeZone/Asia/Rangoon.pm \
	  lib/DateTime/TimeZone/Asia/Riyadh.pm blib/lib/DateTime/TimeZone/Asia/Riyadh.pm \
	  lib/DateTime/TimeZone/Asia/Sakhalin.pm blib/lib/DateTime/TimeZone/Asia/Sakhalin.pm \
	  lib/DateTime/TimeZone/Asia/Samarkand.pm blib/lib/DateTime/TimeZone/Asia/Samarkand.pm \
	  lib/DateTime/TimeZone/Asia/Seoul.pm blib/lib/DateTime/TimeZone/Asia/Seoul.pm \
	  lib/DateTime/TimeZone/Asia/Shanghai.pm blib/lib/DateTime/TimeZone/Asia/Shanghai.pm \
	  lib/DateTime/TimeZone/Asia/Singapore.pm blib/lib/DateTime/TimeZone/Asia/Singapore.pm \
	  lib/DateTime/TimeZone/Asia/Taipei.pm blib/lib/DateTime/TimeZone/Asia/Taipei.pm \
	  lib/DateTime/TimeZone/Asia/Tashkent.pm blib/lib/DateTime/TimeZone/Asia/Tashkent.pm \
	  lib/DateTime/TimeZone/Asia/Tbilisi.pm blib/lib/DateTime/TimeZone/Asia/Tbilisi.pm \
	  lib/DateTime/TimeZone/Asia/Tehran.pm blib/lib/DateTime/TimeZone/Asia/Tehran.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Asia/Thimphu.pm blib/lib/DateTime/TimeZone/Asia/Thimphu.pm \
	  lib/DateTime/TimeZone/Asia/Tokyo.pm blib/lib/DateTime/TimeZone/Asia/Tokyo.pm \
	  lib/DateTime/TimeZone/Asia/Ulaanbaatar.pm blib/lib/DateTime/TimeZone/Asia/Ulaanbaatar.pm \
	  lib/DateTime/TimeZone/Asia/Urumqi.pm blib/lib/DateTime/TimeZone/Asia/Urumqi.pm \
	  lib/DateTime/TimeZone/Asia/Ust_Nera.pm blib/lib/DateTime/TimeZone/Asia/Ust_Nera.pm \
	  lib/DateTime/TimeZone/Asia/Vientiane.pm blib/lib/DateTime/TimeZone/Asia/Vientiane.pm \
	  lib/DateTime/TimeZone/Asia/Vladivostok.pm blib/lib/DateTime/TimeZone/Asia/Vladivostok.pm \
	  lib/DateTime/TimeZone/Asia/Yakutsk.pm blib/lib/DateTime/TimeZone/Asia/Yakutsk.pm \
	  lib/DateTime/TimeZone/Asia/Yekaterinburg.pm blib/lib/DateTime/TimeZone/Asia/Yekaterinburg.pm \
	  lib/DateTime/TimeZone/Asia/Yerevan.pm blib/lib/DateTime/TimeZone/Asia/Yerevan.pm \
	  lib/DateTime/TimeZone/Atlantic/Azores.pm blib/lib/DateTime/TimeZone/Atlantic/Azores.pm \
	  lib/DateTime/TimeZone/Atlantic/Bermuda.pm blib/lib/DateTime/TimeZone/Atlantic/Bermuda.pm \
	  lib/DateTime/TimeZone/Atlantic/Canary.pm blib/lib/DateTime/TimeZone/Atlantic/Canary.pm \
	  lib/DateTime/TimeZone/Atlantic/Cape_Verde.pm blib/lib/DateTime/TimeZone/Atlantic/Cape_Verde.pm \
	  lib/DateTime/TimeZone/Atlantic/Faroe.pm blib/lib/DateTime/TimeZone/Atlantic/Faroe.pm \
	  lib/DateTime/TimeZone/Atlantic/Madeira.pm blib/lib/DateTime/TimeZone/Atlantic/Madeira.pm \
	  lib/DateTime/TimeZone/Atlantic/Reykjavik.pm blib/lib/DateTime/TimeZone/Atlantic/Reykjavik.pm \
	  lib/DateTime/TimeZone/Atlantic/South_Georgia.pm blib/lib/DateTime/TimeZone/Atlantic/South_Georgia.pm \
	  lib/DateTime/TimeZone/Atlantic/St_Helena.pm blib/lib/DateTime/TimeZone/Atlantic/St_Helena.pm \
	  lib/DateTime/TimeZone/Atlantic/Stanley.pm blib/lib/DateTime/TimeZone/Atlantic/Stanley.pm \
	  lib/DateTime/TimeZone/Australia/Adelaide.pm blib/lib/DateTime/TimeZone/Australia/Adelaide.pm \
	  lib/DateTime/TimeZone/Australia/Brisbane.pm blib/lib/DateTime/TimeZone/Australia/Brisbane.pm \
	  lib/DateTime/TimeZone/Australia/Broken_Hill.pm blib/lib/DateTime/TimeZone/Australia/Broken_Hill.pm \
	  lib/DateTime/TimeZone/Australia/Currie.pm blib/lib/DateTime/TimeZone/Australia/Currie.pm \
	  lib/DateTime/TimeZone/Australia/Darwin.pm blib/lib/DateTime/TimeZone/Australia/Darwin.pm \
	  lib/DateTime/TimeZone/Australia/Eucla.pm blib/lib/DateTime/TimeZone/Australia/Eucla.pm \
	  lib/DateTime/TimeZone/Australia/Hobart.pm blib/lib/DateTime/TimeZone/Australia/Hobart.pm \
	  lib/DateTime/TimeZone/Australia/Lindeman.pm blib/lib/DateTime/TimeZone/Australia/Lindeman.pm \
	  lib/DateTime/TimeZone/Australia/Lord_Howe.pm blib/lib/DateTime/TimeZone/Australia/Lord_Howe.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Australia/Melbourne.pm blib/lib/DateTime/TimeZone/Australia/Melbourne.pm \
	  lib/DateTime/TimeZone/Australia/Perth.pm blib/lib/DateTime/TimeZone/Australia/Perth.pm \
	  lib/DateTime/TimeZone/Australia/Sydney.pm blib/lib/DateTime/TimeZone/Australia/Sydney.pm \
	  lib/DateTime/TimeZone/CET.pm blib/lib/DateTime/TimeZone/CET.pm \
	  lib/DateTime/TimeZone/CST6CDT.pm blib/lib/DateTime/TimeZone/CST6CDT.pm \
	  lib/DateTime/TimeZone/Catalog.pm blib/lib/DateTime/TimeZone/Catalog.pm \
	  lib/DateTime/TimeZone/EET.pm blib/lib/DateTime/TimeZone/EET.pm \
	  lib/DateTime/TimeZone/EST.pm blib/lib/DateTime/TimeZone/EST.pm \
	  lib/DateTime/TimeZone/EST5EDT.pm blib/lib/DateTime/TimeZone/EST5EDT.pm \
	  lib/DateTime/TimeZone/Europe/Amsterdam.pm blib/lib/DateTime/TimeZone/Europe/Amsterdam.pm \
	  lib/DateTime/TimeZone/Europe/Andorra.pm blib/lib/DateTime/TimeZone/Europe/Andorra.pm \
	  lib/DateTime/TimeZone/Europe/Athens.pm blib/lib/DateTime/TimeZone/Europe/Athens.pm \
	  lib/DateTime/TimeZone/Europe/Belgrade.pm blib/lib/DateTime/TimeZone/Europe/Belgrade.pm \
	  lib/DateTime/TimeZone/Europe/Berlin.pm blib/lib/DateTime/TimeZone/Europe/Berlin.pm \
	  lib/DateTime/TimeZone/Europe/Brussels.pm blib/lib/DateTime/TimeZone/Europe/Brussels.pm \
	  lib/DateTime/TimeZone/Europe/Bucharest.pm blib/lib/DateTime/TimeZone/Europe/Bucharest.pm \
	  lib/DateTime/TimeZone/Europe/Budapest.pm blib/lib/DateTime/TimeZone/Europe/Budapest.pm \
	  lib/DateTime/TimeZone/Europe/Chisinau.pm blib/lib/DateTime/TimeZone/Europe/Chisinau.pm \
	  lib/DateTime/TimeZone/Europe/Copenhagen.pm blib/lib/DateTime/TimeZone/Europe/Copenhagen.pm \
	  lib/DateTime/TimeZone/Europe/Dublin.pm blib/lib/DateTime/TimeZone/Europe/Dublin.pm \
	  lib/DateTime/TimeZone/Europe/Gibraltar.pm blib/lib/DateTime/TimeZone/Europe/Gibraltar.pm \
	  lib/DateTime/TimeZone/Europe/Helsinki.pm blib/lib/DateTime/TimeZone/Europe/Helsinki.pm \
	  lib/DateTime/TimeZone/Europe/Istanbul.pm blib/lib/DateTime/TimeZone/Europe/Istanbul.pm \
	  lib/DateTime/TimeZone/Europe/Kaliningrad.pm blib/lib/DateTime/TimeZone/Europe/Kaliningrad.pm \
	  lib/DateTime/TimeZone/Europe/Kiev.pm blib/lib/DateTime/TimeZone/Europe/Kiev.pm \
	  lib/DateTime/TimeZone/Europe/Lisbon.pm blib/lib/DateTime/TimeZone/Europe/Lisbon.pm \
	  lib/DateTime/TimeZone/Europe/London.pm blib/lib/DateTime/TimeZone/Europe/London.pm \
	  lib/DateTime/TimeZone/Europe/Luxembourg.pm blib/lib/DateTime/TimeZone/Europe/Luxembourg.pm \
	  lib/DateTime/TimeZone/Europe/Madrid.pm blib/lib/DateTime/TimeZone/Europe/Madrid.pm \
	  lib/DateTime/TimeZone/Europe/Malta.pm blib/lib/DateTime/TimeZone/Europe/Malta.pm \
	  lib/DateTime/TimeZone/Europe/Minsk.pm blib/lib/DateTime/TimeZone/Europe/Minsk.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Europe/Monaco.pm blib/lib/DateTime/TimeZone/Europe/Monaco.pm \
	  lib/DateTime/TimeZone/Europe/Moscow.pm blib/lib/DateTime/TimeZone/Europe/Moscow.pm \
	  lib/DateTime/TimeZone/Europe/Oslo.pm blib/lib/DateTime/TimeZone/Europe/Oslo.pm \
	  lib/DateTime/TimeZone/Europe/Paris.pm blib/lib/DateTime/TimeZone/Europe/Paris.pm \
	  lib/DateTime/TimeZone/Europe/Prague.pm blib/lib/DateTime/TimeZone/Europe/Prague.pm \
	  lib/DateTime/TimeZone/Europe/Riga.pm blib/lib/DateTime/TimeZone/Europe/Riga.pm \
	  lib/DateTime/TimeZone/Europe/Rome.pm blib/lib/DateTime/TimeZone/Europe/Rome.pm \
	  lib/DateTime/TimeZone/Europe/Samara.pm blib/lib/DateTime/TimeZone/Europe/Samara.pm \
	  lib/DateTime/TimeZone/Europe/Simferopol.pm blib/lib/DateTime/TimeZone/Europe/Simferopol.pm \
	  lib/DateTime/TimeZone/Europe/Sofia.pm blib/lib/DateTime/TimeZone/Europe/Sofia.pm \
	  lib/DateTime/TimeZone/Europe/Stockholm.pm blib/lib/DateTime/TimeZone/Europe/Stockholm.pm \
	  lib/DateTime/TimeZone/Europe/Tallinn.pm blib/lib/DateTime/TimeZone/Europe/Tallinn.pm \
	  lib/DateTime/TimeZone/Europe/Tirane.pm blib/lib/DateTime/TimeZone/Europe/Tirane.pm \
	  lib/DateTime/TimeZone/Europe/Uzhgorod.pm blib/lib/DateTime/TimeZone/Europe/Uzhgorod.pm \
	  lib/DateTime/TimeZone/Europe/Vienna.pm blib/lib/DateTime/TimeZone/Europe/Vienna.pm \
	  lib/DateTime/TimeZone/Europe/Vilnius.pm blib/lib/DateTime/TimeZone/Europe/Vilnius.pm \
	  lib/DateTime/TimeZone/Europe/Volgograd.pm blib/lib/DateTime/TimeZone/Europe/Volgograd.pm \
	  lib/DateTime/TimeZone/Europe/Warsaw.pm blib/lib/DateTime/TimeZone/Europe/Warsaw.pm \
	  lib/DateTime/TimeZone/Europe/Zaporozhye.pm blib/lib/DateTime/TimeZone/Europe/Zaporozhye.pm \
	  lib/DateTime/TimeZone/Europe/Zurich.pm blib/lib/DateTime/TimeZone/Europe/Zurich.pm \
	  lib/DateTime/TimeZone/Floating.pm blib/lib/DateTime/TimeZone/Floating.pm \
	  lib/DateTime/TimeZone/HST.pm blib/lib/DateTime/TimeZone/HST.pm \
	  lib/DateTime/TimeZone/Indian/Antananarivo.pm blib/lib/DateTime/TimeZone/Indian/Antananarivo.pm \
	  lib/DateTime/TimeZone/Indian/Chagos.pm blib/lib/DateTime/TimeZone/Indian/Chagos.pm \
	  lib/DateTime/TimeZone/Indian/Christmas.pm blib/lib/DateTime/TimeZone/Indian/Christmas.pm \
	  lib/DateTime/TimeZone/Indian/Cocos.pm blib/lib/DateTime/TimeZone/Indian/Cocos.pm \
	  lib/DateTime/TimeZone/Indian/Comoro.pm blib/lib/DateTime/TimeZone/Indian/Comoro.pm \
	  lib/DateTime/TimeZone/Indian/Kerguelen.pm blib/lib/DateTime/TimeZone/Indian/Kerguelen.pm \
	  lib/DateTime/TimeZone/Indian/Mahe.pm blib/lib/DateTime/TimeZone/Indian/Mahe.pm \
	  lib/DateTime/TimeZone/Indian/Maldives.pm blib/lib/DateTime/TimeZone/Indian/Maldives.pm \
	  lib/DateTime/TimeZone/Indian/Mauritius.pm blib/lib/DateTime/TimeZone/Indian/Mauritius.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Indian/Mayotte.pm blib/lib/DateTime/TimeZone/Indian/Mayotte.pm \
	  lib/DateTime/TimeZone/Indian/Reunion.pm blib/lib/DateTime/TimeZone/Indian/Reunion.pm \
	  lib/DateTime/TimeZone/Local.pm blib/lib/DateTime/TimeZone/Local.pm \
	  lib/DateTime/TimeZone/Local/Unix.pm blib/lib/DateTime/TimeZone/Local/Unix.pm \
	  lib/DateTime/TimeZone/Local/VMS.pm blib/lib/DateTime/TimeZone/Local/VMS.pm \
	  lib/DateTime/TimeZone/Local/Win32.pm blib/lib/DateTime/TimeZone/Local/Win32.pm \
	  lib/DateTime/TimeZone/MET.pm blib/lib/DateTime/TimeZone/MET.pm \
	  lib/DateTime/TimeZone/MST.pm blib/lib/DateTime/TimeZone/MST.pm \
	  lib/DateTime/TimeZone/MST7MDT.pm blib/lib/DateTime/TimeZone/MST7MDT.pm \
	  lib/DateTime/TimeZone/OffsetOnly.pm blib/lib/DateTime/TimeZone/OffsetOnly.pm \
	  lib/DateTime/TimeZone/OlsonDB.pm blib/lib/DateTime/TimeZone/OlsonDB.pm \
	  lib/DateTime/TimeZone/OlsonDB/Change.pm blib/lib/DateTime/TimeZone/OlsonDB/Change.pm \
	  lib/DateTime/TimeZone/OlsonDB/Observance.pm blib/lib/DateTime/TimeZone/OlsonDB/Observance.pm \
	  lib/DateTime/TimeZone/OlsonDB/Rule.pm blib/lib/DateTime/TimeZone/OlsonDB/Rule.pm \
	  lib/DateTime/TimeZone/OlsonDB/Zone.pm blib/lib/DateTime/TimeZone/OlsonDB/Zone.pm \
	  lib/DateTime/TimeZone/PST8PDT.pm blib/lib/DateTime/TimeZone/PST8PDT.pm \
	  lib/DateTime/TimeZone/Pacific/Apia.pm blib/lib/DateTime/TimeZone/Pacific/Apia.pm \
	  lib/DateTime/TimeZone/Pacific/Auckland.pm blib/lib/DateTime/TimeZone/Pacific/Auckland.pm \
	  lib/DateTime/TimeZone/Pacific/Chatham.pm blib/lib/DateTime/TimeZone/Pacific/Chatham.pm \
	  lib/DateTime/TimeZone/Pacific/Chuuk.pm blib/lib/DateTime/TimeZone/Pacific/Chuuk.pm \
	  lib/DateTime/TimeZone/Pacific/Easter.pm blib/lib/DateTime/TimeZone/Pacific/Easter.pm \
	  lib/DateTime/TimeZone/Pacific/Efate.pm blib/lib/DateTime/TimeZone/Pacific/Efate.pm \
	  lib/DateTime/TimeZone/Pacific/Enderbury.pm blib/lib/DateTime/TimeZone/Pacific/Enderbury.pm \
	  lib/DateTime/TimeZone/Pacific/Fakaofo.pm blib/lib/DateTime/TimeZone/Pacific/Fakaofo.pm \
	  lib/DateTime/TimeZone/Pacific/Fiji.pm blib/lib/DateTime/TimeZone/Pacific/Fiji.pm \
	  lib/DateTime/TimeZone/Pacific/Funafuti.pm blib/lib/DateTime/TimeZone/Pacific/Funafuti.pm \
	  lib/DateTime/TimeZone/Pacific/Galapagos.pm blib/lib/DateTime/TimeZone/Pacific/Galapagos.pm \
	  lib/DateTime/TimeZone/Pacific/Gambier.pm blib/lib/DateTime/TimeZone/Pacific/Gambier.pm \
	  lib/DateTime/TimeZone/Pacific/Guadalcanal.pm blib/lib/DateTime/TimeZone/Pacific/Guadalcanal.pm \
	  lib/DateTime/TimeZone/Pacific/Guam.pm blib/lib/DateTime/TimeZone/Pacific/Guam.pm \
	  lib/DateTime/TimeZone/Pacific/Honolulu.pm blib/lib/DateTime/TimeZone/Pacific/Honolulu.pm \
	  lib/DateTime/TimeZone/Pacific/Kiritimati.pm blib/lib/DateTime/TimeZone/Pacific/Kiritimati.pm 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  lib/DateTime/TimeZone/Pacific/Kosrae.pm blib/lib/DateTime/TimeZone/Pacific/Kosrae.pm \
	  lib/DateTime/TimeZone/Pacific/Kwajalein.pm blib/lib/DateTime/TimeZone/Pacific/Kwajalein.pm \
	  lib/DateTime/TimeZone/Pacific/Majuro.pm blib/lib/DateTime/TimeZone/Pacific/Majuro.pm \
	  lib/DateTime/TimeZone/Pacific/Marquesas.pm blib/lib/DateTime/TimeZone/Pacific/Marquesas.pm \
	  lib/DateTime/TimeZone/Pacific/Midway.pm blib/lib/DateTime/TimeZone/Pacific/Midway.pm \
	  lib/DateTime/TimeZone/Pacific/Nauru.pm blib/lib/DateTime/TimeZone/Pacific/Nauru.pm \
	  lib/DateTime/TimeZone/Pacific/Niue.pm blib/lib/DateTime/TimeZone/Pacific/Niue.pm \
	  lib/DateTime/TimeZone/Pacific/Norfolk.pm blib/lib/DateTime/TimeZone/Pacific/Norfolk.pm \
	  lib/DateTime/TimeZone/Pacific/Noumea.pm blib/lib/DateTime/TimeZone/Pacific/Noumea.pm \
	  lib/DateTime/TimeZone/Pacific/Pago_Pago.pm blib/lib/DateTime/TimeZone/Pacific/Pago_Pago.pm \
	  lib/DateTime/TimeZone/Pacific/Palau.pm blib/lib/DateTime/TimeZone/Pacific/Palau.pm \
	  lib/DateTime/TimeZone/Pacific/Pitcairn.pm blib/lib/DateTime/TimeZone/Pacific/Pitcairn.pm \
	  lib/DateTime/TimeZone/Pacific/Pohnpei.pm blib/lib/DateTime/TimeZone/Pacific/Pohnpei.pm \
	  lib/DateTime/TimeZone/Pacific/Port_Moresby.pm blib/lib/DateTime/TimeZone/Pacific/Port_Moresby.pm \
	  lib/DateTime/TimeZone/Pacific/Rarotonga.pm blib/lib/DateTime/TimeZone/Pacific/Rarotonga.pm \
	  lib/DateTime/TimeZone/Pacific/Saipan.pm blib/lib/DateTime/TimeZone/Pacific/Saipan.pm \
	  lib/DateTime/TimeZone/Pacific/Tahiti.pm blib/lib/DateTime/TimeZone/Pacific/Tahiti.pm \
	  lib/DateTime/TimeZone/Pacific/Tarawa.pm blib/lib/DateTime/TimeZone/Pacific/Tarawa.pm \
	  lib/DateTime/TimeZone/Pacific/Tongatapu.pm blib/lib/DateTime/TimeZone/Pacific/Tongatapu.pm \
	  lib/DateTime/TimeZone/Pacific/Wake.pm blib/lib/DateTime/TimeZone/Pacific/Wake.pm \
	  lib/DateTime/TimeZone/Pacific/Wallis.pm blib/lib/DateTime/TimeZone/Pacific/Wallis.pm \
	  lib/DateTime/TimeZone/UTC.pm blib/lib/DateTime/TimeZone/UTC.pm \
	  lib/DateTime/TimeZone/WET.pm blib/lib/DateTime/TimeZone/WET.pm 
	$(NOECHO) $(TOUCH) pm_to_blib


# --- MakeMaker selfdocument section:


# --- MakeMaker postamble section:


# End.
