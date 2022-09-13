#!/usr/bin/perl

print "Enter file name: ";
my $filename = "input_characters.txt";
open(char, $filename) or die $!;
my $characters=<char>;
chomp($characters);

print "Enter count: ";
my $count = <STDIN>;
print "\n";

print "Enter length: ";
my $length = <STDIN>;
print "\n";

my $string = "";
if($count <= 1){
    print "String cannot be generated\n";
    exit 1;
}

while(length($string) < $length){
    my $index = int(rand(length($characters)));
    
    my $chosen_char = substr($characters, $index, 1 );
    my $choose_cnt = int(rand( $count ));
    if(substr($string, length($string)-$count+$choose_cnt, $count-$choose_cnt) eq ($chosen_char x ($count - $choose_cnt))){
        next;
    }
    if( (length($string) + $choose_cnt) > $length){
        next;
    }
    my $add_string = $chosen_char x $choose_cnt;
    $string = $string.$add_string;
}
print "The generated string is: $string";
print "\n";
