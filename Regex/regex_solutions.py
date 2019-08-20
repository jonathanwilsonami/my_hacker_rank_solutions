####NOTES###

#\d digit
#\D non-digit
#\s [\r\n\t\f] any white space char
#\S any non-white sapce char
#\w any alpha numeric char (a-z, A-Z and 0-9) as well as underscores
#\W anything that is not alhpa numeric such as % or $
#^ matches pos at start of string ^123
#$ matches pos at end of string 123$
#. matches anything except for newline
# [] The character class [ ] matches only one out of several characters placed inside the square brackets.
#[^] The negated character class [^] matches any character that is not in the square brackets.
#[a-z] Range 
#{5} repetitions
#{x,y} The {x,y} tool will match between  and  (both inclusive) repetitions of character/character class/group.
    #EX: w{3,5} : It will match the character w 3, 4 or 5 times. 
    #EX: [xyz]{5,} : It will match the character x, y or z 5 or more times. 
    #EX: \d{1, 4} : It will match any digits 1, 2, 3 or 4 times.


###EXAMPLES###

#Pattern: xxXxxXxxxx where x is digit and X is a none digit. Ex: 06-11-2015
Regex_Pattern = r"\d\d\D\d\d\D(\d){4}"

#Matching specific chars [xs0] matches x or s or 0
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$' #The ^...$ ensures the length of the string is 6

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'

Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
