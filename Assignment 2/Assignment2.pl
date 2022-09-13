#!/usr/bin/perl

#Defining filename and opening file to read the string from the file

#Note: I have taken pre-input text file whose text can be changed or filename can be modified here. 
#In case it has to be user input, the following commented line can uncommented and the pre-input line could be removed.

#my $filename= <STDIN>;
my $filename = "input_characters.txt";
open(char, $filename) or die $!;        #Opening file with file handle 'char'. If opening is unsuccessful, the error message is printed.
my $characters=<char>;      #<File_handle> reads line from the file.
chomp($characters);         #Removes newline character from the string

#Checking if the given file contains any input
if(length($characters)<1){
    print "Please enter alphabets in the input file '$filename'";
    exit 1;
}

print("-----------------------------------------------------------------------------------------\n");
print "Taking input from the file '$filename', containing the following alphabets: '$characters'\n\n";
print("-----------------------------------------------------------------------------------------\n");

#Taking values of count and length from the user.
print "Enter count: ";
my $count = <STDIN>;
print "\n";

print "Enter length: ";
my $max_length = <STDIN>;

print("-----------------------------------------------------------------------------------------\n");
print "\n";

#Initializing empty string with global access which is then modified inside the loop.
my $string = "";

#If count is less than or equal to 1, no character can be appended to the string, hence it is not possible to create such string.
if($count <= 1){
    print "String cannot be generated. Enter greater count value.\n";
    exit 1;
}

#Repeatedly applying random generating and concatenation operations until we get desired string length 
while(length($string) < $max_length){
    my $index = int(rand(length($characters)));         #Generating random index of less than the length of input alphabet. This includes zero and excludes upper bound.
    
    my $chosen_char = substr($characters, $index, 1 );  #Accessing character from the character string.

    my $choose_cnt = int(rand( $count ));               #Generating another random number less than count for repetition of character.

    #Checking if the last (Count - Generated repetition number) characters are same as the randomly chosen character so that the substring doesn't contain more than 'count' same characters.
    if(substr($string, length($string)-$count+$choose_cnt, $count-$choose_cnt) eq ($chosen_char x ($count - $choose_cnt))){
        next;
    }

    #Checking if adding the generated new string increases string length greater than allowed length.
    if( (length($string) + $choose_cnt) > $max_length){
        next;
    }

    #Creating the string by repetition of characters.
    my $add_string = $chosen_char x $choose_cnt;
    #Appending to string
    $string = $string.$add_string;
}
print "The generated string is: $string";

print "\n";
print("-----------------------------------------------------------------------------------------\n");

