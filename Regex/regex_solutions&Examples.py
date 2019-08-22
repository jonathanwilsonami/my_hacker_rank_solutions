###EXAMPLES###

#Pattern: xxXxxXxxxx where x is digit and X is a none digit. Ex: 06-11-2015
Regex_Pattern = r"\d\d\D\d\d\D(\d){4}"

#Matching specific chars [xs0] matches x or s or 0
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$' #The ^...$ ensures the length of the string is 6

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'

Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'

Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$'


Regex_Pattern = r'\b[1-9][0-9]{2,4}\b' #Matches -> 100 and 99999

#Group number
Regex_Pattern = r'(\w)(\w)(\w)(\w)y\4\3\2\1' #Matches -> takes first four letters and reverses them ex: malayalam

Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$'

#Backreferences To Failed Groups - Capturing group that match nothing
Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$" #Matches -> 12345678 and 12-34-56-87

#Positive Lookahead
$Regex_Pattern = '/o(?=oo)/'; #Matcfhes -> all occurrences of o followed immediately by oo ex: 

#Negative Lookahead
Regex_Pattern = r"(.)(?!\1)" #Matches -> all characters which are not immediately followed by that same character.

#Positive Lookbehind - The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2. 
#Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
Regex_Pattern = r"(?<=[13579])\d" #Matches -> all the occurences of digit which are immediately preceded by odd digit

#Negative Lookbehind - The negative lookbehind (?<!) asserts regex_1 not to be immediately preceded by regex_2. 
#Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
Regex_Pattern = r"(?<![aeiouAEIOU])." #Matches -> all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).
