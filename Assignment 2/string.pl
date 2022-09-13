#!/usr/bin/perl
use strict;
use warnings;
# sub choose_index 
# {
#     my $index = int(rand(length($_[0]));
#     return($index);
# }
# sub sub_length
# {
#     my $length_substring= int(rand(length($_[0])));
#     return($length_substring);
# }
# opendir (my $dh, $dir) or die $!;
my $filename = <STDIN>;
chomp($filename);
print $filename;
open(FH,$filename) or die("Error");
my $characters=<FH>;

my $max_length = <STDIN>;
my $max_count = <STDIN>;

my $chosen_char= substr($characters, choose_index($characters), 1);

my $substring= $chosen_char x sub_length($max_count);

print "$substring";
print "$max_length";