###EXAMPLES###

#Pattern: xxXxxXxxxx where x is digit and X is a none digit. Ex: 06-11-2015
Regex_Pattern = r"\d\d\D\d\d\D(\d){4}"

#Matching specific chars [xs0] matches x or s or 0
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$' #The ^...$ ensures the length of the string is 6

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'

Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'

Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$'
