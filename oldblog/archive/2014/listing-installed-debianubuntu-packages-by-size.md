Title: Listing installed debian/Ubuntu packages by size.
Date: 2014-11-10 14:50
Author: slacy
Category: General
Status: published

Here's a command to list all installed Debian/Ubuntu packages, sorted by
size:  
`dpkg-query -W -f='${db:Status-Abbrev} ${Installed-Size}\t${binary:Package} ${Version}\t${Maintainer}\n' | egrep "^ii" | sort -k2n`
