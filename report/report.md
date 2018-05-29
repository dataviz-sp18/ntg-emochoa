Text Visualization Write-up
================
Erin M. Ochoa
2018/05/29

Overview
========

<p align="justify">
The <a href=http://people.cs.uchicago.edu/~emo/hp>visualization</a> I created for this assignment shows seven individual word clouds, one for each book in the <i>Harry Potter</i> series. It is best viewed full-screen and requires a few minutes to fully render.
</p>
<p align="justify">
Each word cloud is constructed with a bias toward the character names that appear most frequently in the underlying novel. This showcases the characters most important in a given novel. Thus, even though Dumbledore makes only a series of brief appearances in <i>Deathly Hallows</i>, he is nevertheless a crucial character in that installment of the series (and, if you're lucky, you can see his name in the seventh word cloud!).
</p>
The Word Cloud as a Medium
==========================

<p align="justify">
At first glance, the word cloud appears to be an aesthetically pleasing way to explore the words most commonly used in a given corpus. It seems to be a good choice for the <i>Harry Potter</i> series because each of the seven books explores different scenarios and themes with an evolving cast of characters; thus, it can be used to emphasize the motifs, characters, and plot points prominent in each novel. In the end, though word clouds—or at least those created with <u>wordcloud2</u>—are easily manipulated and readers should be skeptical of them.
</p>
The Implementation
==================

<p align="justify">
To clean the text of a given novel (each as represented in the <u>harrypotter</u> library), I first converted all characters to lowercase, then removed all instances of <i>'s</i> and digits. I split each novel into a vector of individual words (sans punctuation) and filtered out words using the <u>stopwords</u> library (augmented with the eponymous character's given name, the word <i>said</i>, and the letter <i>c</i>, which appeared notably often in the seventh novel in what seemed to be a character-encoding mishap). Next, I used a dictionary to count the occurrence of each remaining word in the novel, then saved the dictionary entries to a dataframe. I sorted the dataframe by descending order of frequency, then pulled all the character names (including surnames, as listed on <a href=https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters>Wikipedia</a> and cleaned in <u>Python</u>) to the top of the dataframe, and finally placed Hermione's given name at the very top.
</p>
<p align="justify">
I assigned each novel a color that contrasts well with the black background. Next, I chose a sans-serif, normal-weight font over the default (boldface serif) so that each word would take up a little less space. Finally, I set the layout to reflect the relative lengths of the novels (the first four together are shorter than the last three combined, so each of the earlier novels gets a little less space) and also to allow the plotting algorithm to place longer words (which were rare in the original single-row layout).
</p>
Challenges
==========

<p align="justify">
I encountered a series of challenges in creating the word clouds. It turns out that <u>flexdashboard</u>'s storyboard format will not render word clouds on slides beyond the first; because I wanted to implement the visualization in a single file, this ruled out the possibility of creating seven full-sized clouds. I then placed all seven word clouds in a single row on a single page, which I liked (as the seven long, narrow clouds fittingly resembled book spines on a shelf), but longer words like <i>hermione</i> and <i>dumbledore</i> almost never appeared in these clouds.
</p>
<p align="justify">
Even in the final layout, the word <i>hermione</i> only sometimes shows up, despite being among the top five most common words in each book. This appears to be related to what I hope is a bug (and not a feature) in <u>wordcloud2</u> that places words in the order they appear in the dataframe, but only if they appear to fit into the current cloud layout (and even then, not reliably so). I attempted to take advantage of this by sorting by frequency, then moving all the character names to the top, and then moving <i>hermione</i> to the very top of the dataframe; the name now appears in word clouds more frequently but still rarely.
</p>
