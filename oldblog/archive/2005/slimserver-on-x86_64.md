Title: Slimserver on x86_64
Date: 2005-11-20 23:38
Author: slacy
Category: Linux Stuff, Music
Status: published

So, I installed the slimserver version 6.2.1 on my new Fedora Core 4
x86\_64 Athlon machine and had some trouble starting up. For google's
search sake, I'll list the problem here:

` # service slimserver start Starting SlimServer: Had to create DBI::_dbistate unexpectedly at /usr/lib64/perl5/5.8.6/x86_64-linux-thread-multi/DynaLoader.pm line 253.`  
And then, in slimserver.log, it said:  
` Can't locate auto/DBI/connect.al in @INC (@INC contains: /usr/local/slimserver/Plugins /usr/local/slimserver /usr/local/slimserver/CPAN /usr/local/slimserver/CPAN/arch/5.8.6/x86_64-linux-thread-multi /usr/local/slimserver/CPAN/arch/5.8.6/x86_64-linux-thread-multi/auto /usr/local/slimserver/CPAN/arch/5.8/x86_64-linux-thread-multi /usr/local/slimserver/CPAN/arch/5.8/x86_64-linux-thread-multi/auto /usr/local/slimserver/CPAN/arch/x86_64-linux-thread-multi /usr/lib64/perl5/site_perl/5.8.6/x86_64-linux-thread-multi /usr/lib64/perl5/site_perl/5.8.5/x86_64-linux-thread-multi /usr/lib64/perl5/site_perl/5.8.4/x86_64-linux-thread-multi /usr/lib64/perl5/site_perl/5.8.3/x86_64-linux-thread-multi /usr/lib/perl5/site_perl/5.8.6 /usr/lib/perl5/site_perl/5.8.5 /usr/lib/perl5/site_perl/5.8.4 /usr/lib/perl5/site_perl/5.8.3 /usr/lib/perl5/site_perl /usr/lib64/perl5/vendor_perl/5.8.6/x86_64-linux-thread-multi /usr/lib64/perl5/vendor_perl/5.8.5/x86_64-linux-thread-multi /usr/lib64/perl5/vendor_perl/5.8.4/x86_64-linux-thread-multi /usr/lib64/perl5/vendor_perl/5.8.3/x86_64-linux-thread-multi /usr/lib/perl5/vendor_perl/5.8.6 /usr/lib/perl5/vendor_perl/5.8.5 /usr/lib/perl5/vendor_perl/5.8.4 /usr/lib/perl5/vendor_perl/5.8.3 /usr/lib/perl5/vendor_perl /usr/lib64/perl5/5.8.6/x86_64-linux-thread-multi /usr/lib/perl5/5.8.6 .) at /usr/local/slimserver/Slim/DataStores/DBI/DataModel.pm line 147`  
The solution was to rename the "included" version of the Perl DBI module
from the slimserver distribution. In other words:  
` # mv /usr/local/slimserver/CPAN/DBI.pm /usr/local/slimserver/CPAN/DBI.crap`

I blame the Slimserver software developers for this one -- they
shouldn't be including versions of standard Perl libraries in their
RPMs. They should just make the RPMs have dependencies on the versions
of the libraries that they need. That way, they could always use the
right system libraries and not have to re-distribute a bunch of crap.

I think that their methodology about this has to do with the portability
of the slimserver software -- they haev it running on Windows, which is
a real accomplishment, and there isn't something like RPM for Windows,
so they just have to include everything (on that platform).
