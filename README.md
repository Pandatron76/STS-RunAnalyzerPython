# STS-RunAnalyzerPython

## Disclosure
This is my first 'proper' project written in Python. As such there might be some pythonic approaches that are missing from the code base. As time goes on, I hope to improve my overall skills in Python.

## Introductions
Ever curious about what cards you upgrade on floor 23 on the Defect or how often you pick them? Or how about what enemy you encounter most at floor 13 overall? "SlayTheSpire: Run Analyzer-Python" is a python tool used to analyze a single or multiple Slay the Spire playthroughs to learn more about player(s)'s choices. The tool reads the .run files and provides the user with details from the command line. 

## Getting Started
Make sure Python 3.6.5 is installed on the machine before running the script

## Usage Example
1. Locate the configuration file located in "..\sts_run_history_analyzer\config.ini"
2. Change the "TargetPath=" variable to the location where the character folders are stored
(Example: "..\Steam\steamapps\common\SlayTheSpire\runs\"
3. [Optional] Update the "CharactersToInclude=" to include characters you want to see information on
4. Set values (True or False) under the [PRINT_ALL_RUNS] or [PRINT_SINGLE_RUN] section that you wish to see information on

[PRINT_ALL_RUNS] will provide a compiled information for all playthroughs.

[PRINT_SINGLE_RUN] will print detailed information about each individual run. With this said, be careful with how many flags/options are turned on as the it will print detailed information for each file. Also if you play SlayTheSpire 'alot', please be patient while the script runs.

Navigate back to the root directory and run the "main.py" script

## F.A.Q
> Q: Why write this in Python? Wouldn't Rails or JavaScript provide a better visual representation?

> A: I wanted to try a language that was structural different than languages I worked with in the pass (Java and Ruby) and Python seemed to be a nice fit. There was a consideration of writing this in JavaScript (which I will still likely do) but once again I wanted to use something different than what I am normally familiar with. Django I think would also be an option if I wanted to present it visual as well.

> Q: Aren't there already sites and tools out there that perform what this script does?

> A: The short answer is yes and kind of... The long answer is I had trouble understanding how the information was derived on those sites or an individual(s) efforts when reviewing their reports. For myself the best way to understanding something is trying it on my own. By making this an open source project, it will hopefully give people a better idea of one possible way(s) of how all this information is being compiled. Equally there is some additional functionality I wish to incorporate that is a bit more in the weeds (for example: by adding card 'x' to your current deck, it impacts the overall damage of your starting hand by 'y')

> Q: Can I send you my ideas?

> A: Yes, ideas are appreicated. Submit an issue with the tag "Feature" and I will take a look at it.

> Q: How do I report on issues regarding incorrect calculations?

> A: Its possible something may not be present information correctly. Submit an issue with the 'Bug' tag and mention what keys(options) were enabled when the issue occured. 

> Q: Can I suggest a better name for what some of the configuration flags/options are actually doing?

> A: Sure! There's a old saying in coding that goes "There are only two hard things in Computer Science: cache invalidation and naming things" so its very likely something is named poorly. Submit an issue with the tag "Feature" and I will take a look at it.

> Q: Do you plan to add unit test?

> A: Yes, it is honestly something I should have done along the way but the additional features took priority. I realize that is a terrible excuse and plan to implement them now that the project is on GitHub. However I do understand that some considerable portions of the code will need to be rewritten to make it unit testable.

> Q: What if I encounter a run time error?

> A: Make sure your running Pythong 3.6.5 or higher. Next, I would make sure your configuration file is setup properly.
If there is still an issue, feel free to submit a issue with the tag 'Bug'. Most of the .run files I worked with is from my own playthroughs so its possible that older playthroughs (or playthroughs on beta branch) might generate issues.

> Q: Can I contribute?

> A: Sure! See the section '[Contributing]' for more information. This is my first Python project so I am more than open to suggestions on how the code base can be improved.

> Q: Can I provide feedback on your Read.me? I found it difficult to read.

> A: I have not written many of these so in general I am poor at writting them. Feel free to submit a pull request with the recommended changes.

## Contributing
1. Fork the project
2. Create a new feature brach on the fork project
3. Commit changes
4. Push the changes to the branch.
5. Create a new Pull Request back to the main project

## Acknowledgements
To my friends that were willing to listen to me ramble on about one player card games and Python.

The Doctor Who marathon that played in the background as I was writing this.

SlayTheSpire streamers in general. They are fun to have playing in the background (and watch) while I write this sort of stuff.  There's a couple that I follow and mostly lurk in the channels but specific shoutouts to the one(s) that spend a great deal of time thinking about the meta details and analzying the game in great detail

Spirelogs for providing some high level ideas of what to think about.


