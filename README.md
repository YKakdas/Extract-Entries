# Extract-Entries

This script is to distinguish real entries from fake ones.

 A real entry:
- Starts with a ‘yyyy-mm-dd’ formatted date,
- Continues with a valid user name,
- Ends with an IPv4 address that does not start with ‘10’.

A valid user name meets the following conditions:
- Starts with ‘_’ (underscore) or ‘.’ (dot) character,
- First character is followed by exactly three letters,
- After these letters, there must be one or more digits,
- Optionally ends with ‘/’ (forward slash) character

IPv4 address:
- IPv4 address is a series of numbers and dots, the string of
 numbers is separated by the dots into four sections.
- Each number can be in the range of [0,255].
