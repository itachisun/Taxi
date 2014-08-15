#! /usr/bin/env perl
#################################################################################
#     File Name           :     TAXI_1.pl
#     Created By          :     xd
#     Creation Date       :     [2014-08-15 16:41]
#     Last Modified       :     [2014-08-15 18:11]
#     Description         :     pick out GPS points of same vehicle 
#################################################################################

use warnings;

if (scalar (@ARGV) != 1) { die "please specify <file>\n" };
print "$ARGV[0]\n";
my $file = $ARGV[0];
open my $info, $file or die "Could not open $file: $!";

# frequent open and close file make it very slow. also read / write on same disk
# so use some help from tmpfs
# for 1.6G (7727 files) r: 174.719, u: 124.824, s: 47.719
while( my $line = <$info> )  {   
     my @values = split(',', $line);
     # this will append newline to write
     open(my $fh, '>>', "/run/shm/ByCars/$values[2]") or die "Could not open file '$filename' $!";
     say $fh $line;
     close $fh;
}

close $info;

