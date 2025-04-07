---
title: ReDrUm Java
date: 2020-01-19
tags: 
 - math
 - java
 - forfun
---
One of my favorite horror movies of all time is Stanley Kubrick's _"The Shining"_. It has minimum deaths and killing but still conveys the same kind of fear and anticipation every horror movie has. So, after finding myself absolutely bored in the middle of November 2019, I gave the movie a spin again. It was the scene when Wendy finds out that Jack had abandoned his play to write the sentence "All work no play makes Jack a dull boy" in different variations that had inspired me to write up some code. Something about the variation was particularly spooky, and I wanted to copy it.

So, I sat down and pulled up eclipse. It had been a while since I last practiced my Java-- I hadn't touched it since the AP Comp Sci A Exam. This would be a fun little string challenge to warm up my skills.

You can find the code [here](https://github.com/maryeversley/redrum) on GitHub. My GitHub is still somewhat empty but I'm sure I'll add more of my projects as time passes.

I named my Java Project "REDRuM" for obvious reasons (if not so obvious, it's the phrase Danny, Jack's son, writes on the bathroom door in Wendy's red lipstick). I figure I would only have one class as I was just printing strings. To make things even more spooky, I wanted all the sentence variations to be somewhat randomized so that each printed line is vastly different than the previous. Thus, let us import java.util.random!

SideNote: I must say, my java and computer science lingo is quite limited as our AP Comp Sci teacher didn't quite integrate them into our heads-- my most "sincere" apologies if I start to use general words like "that" or "that thingy".

I didn't know if I wanted to have multiple methods yet to make all the changes to the original sentence yet. It seems like it could be down with just the main method but I figured I would lay down the foundation before adding any variations. After toying around with the while loop and for loop, I opted for the for loop, since I could be sure of the number of lines I was running (237, a direct reference to room 237).

I listed out some of the "formats" I wanted to use for each line on a scrap piece of paper. It's always been a habit of mine to write down my thoughts with a Pilot G-07 black pen and a white sheet of 8.5'' by 11'' copy paper. Visually, I have all this empty space to literally map out the ideas I have in mind.

So, what sort of "formats" did I want to have?

- Print the plain line "All work and no play makes Jack a dull boy"
- In all UPPERCASE
- In all lowercase
- To change "Jack" to a character in the movie
- To randomly replace a letter with a random letter
- To repeat a certain letter a certain amount of times each time the letter appeared
- To alternate between upper and lower cases
- To alternate between lower and upper cases (very different from the previous one)
- To have random letters be in uppercase
- Mix and match "formats"!

With all these formats in mind, I decided to make all of them into methods so I could work on each component. Here, I present to you my thoughts on each of these methods:  

**1. THE FORMAT CHOOSER.** I needed to find out some way I could have any of the formats chosen at random. My first thought was to do this in the main class but I soon found this to be a problem- see (temp), the name changer. So, I decided to move everything to a method. Besides, the main class would look so much neater! I set randEvent as the random number generator and used a series of if-else statements to call each format changer. Looking back, I think that switch-case might have been less to type up, yet here we are. So, listed are the "formats" I have in this method:

- The line itself without any alterations
- The line in all lowercase (just add the .toLowerCase() to the printed out line- no additional methods needed)
- The line in all uppercase (just add the .toUpperCase() to the printed out line- no additional methods needed)
- The line with one letter replaced with another each time the first letter appears
- The line alternating between uppercase and lowercase
- The line alternating between lowercase and uppercase
- The line with a random number of a certain letter being repeated each time the letter appears
- And 6 formats that are a combination of the ones above

**2. PICKING A RANDOM LETTER.** Okay, this is the one method that I'm not very fond of. I literally mapped out each variation of characters to a switch case. Now that I think about it, it seems like doing a loop in an array could have been a better go at this method.

I set each letter as a case in a switch. A random number generator would then pick a number from 1-19, that number would then be the case picked. Not exactly a very interesting method.  

**3. ALTERNATING UPPER&LOWER CASE and LOWER&UPPER CASE.** These two methods didn't take very long. I would first set the whole line to lowercase, and in a for loop, I would change it to upper case depending on if the index number was even or odd (used i % 2 ==0) and add it to a new string.

**4. Random UPPERCASE.** This was very similar to the alternating UL and LU methods. In this case, only one method was needed as you could say that the letters that are in lowercase are randomly generated too. Instead of having 2 as a mod to check if the index number was odd or even, I used a random generated number as the "moder" to determine its case. The mod numbers ranged from 1 to 4, and if the index number was divisible by moder, then it would be changed into uppercase- otherwise stay in lowercase. You could say it was "calculated randomness".

**5. REPEATING A LETTER EVERY TIME IT APPEARS.** This method was also quite simple. I had an int multiple that would repeat the process for different letters. Most of this section was done so that I won't spam the line too much so the multiple variable was limited to a random integer from 1 to 2. I know, a great deal and a variety of options. I had called my random letter method for the letter I was going to repeat in the line. int numTimes allowed me to repeat the letter 1-4 times and I added those letters to the new string.

**6. REPLACING A LETTER WITH A RANDOM LETTER.** I thought it would be a good idea to have a single letter to be replaced with another random letter. It would be somewhat spooky as if the typewriter just refused to type the correct letter and replaced it with another character. Quite simple as well. I used a random generator for char characters and converted that char to a string. The string method .replace was pretty helpful for this method.

_AND FINALLY..._

**7. REPLACE JACK WITH A CHARACTER FROM THE MOVIE.** Oh goshers. I'll admit, this simple task had my mind confused for the longest time. Nevertheless, let's dive into this mess.

Originally, I wanted to have a random person generator in the main class. But this proved to be a problem as all the lines now contained that character's name when I wanted the majority of the lines to have Jack but one or two with a character. It frustrated me to no end, so I decided to take a break and knit for a while.

Then it hit me-- I could just write up another method for it and have a small if-else in the loop in the main class. The method would only be called if the random number was divisible by the random moder. I choose numbers from the range 10-17 as I wanted some lines to have the character change but the majority of them to have "Jack". This range has a couple of "odd" (pun intended) primes and a good amount of composite numbers as well (10, 12, 16).

The line with the new name would then to into the format chooser and go through the whole process much like the original line.

Well, that's pretty much it! I'm glad you've made it this far reading my thought process through these methods.

Leave any thoughts you may have on this small String practice I did. I'm eager to hear any sort of feedback!