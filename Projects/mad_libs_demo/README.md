# Mad Libs
Prompt the user for a series of words (i.e. - noun, adjective, verb, etc). Insert the word in the appropriate places in a given text, to create a [humorous?] story.
<br/>
<br/>
<strong>Example:</strong>
<br/>
<em>My ANIMAL's name is PROPER NOUN and PRONOUN lives on the NOUN.</em>
<br/>
<br/>
Prompt the user for an ANIMAL, a PROPER NOUN, a PRONOUN and a NOUN and replace the appropriate text with the user's input.
<br/>
So if the user inputs 
<br/>
- <em>cat</em> for ANIMAL
- <em>Trixy</em> for  PROPER NOUN
- <em>she</em> for PRONOUN
- <em>tree</em> for NOUN

<br/>
The subsequent text should read:
<br/>
<em>My <strong>cat's</strong> name is <strong>Trixy</strong> and <strong>she</strong> lives on the <strong>tree</strong>.</em>
<br/>
<br/>
<hr/>

## Solution

For this solution I used a dictionary of lists. Each list contains two strings:
- The first string element gives the word-type to prompt the user for.
- The second string element is the actual Mad Lib text with a replacement text in the place where the given word-type should be placed


Once the user enters the requested word-type the application displays the Mad Lib with the given replacement text. The replacement text is uppercase for clarity.

