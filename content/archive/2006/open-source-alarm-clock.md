Title: Open source alarm clock.
Date: 2006-03-06 23:06
Author: slacy
Category: General
Status: published

I'm building an Open Source alarm clock, and I'll document some of the
possible features here, edits as they come.

-   Varying alarm sounds. Random, "alarm-tones", differing volumes,
    severities, etc.
-   "Sleep 8 hours" button
-   Day of week indicator, so alarm is automatically off on weekends.
    Possible day-of-year mode for extra-special behaviors.
-   Automatic DST adjustment (based on date, if available)
-   Non-linear time display and/or "unpredictable" alarm advance (for
    people who tend to set their clocks ahead by 5-10 minutes so they're
    not late).
-   Special tests to turn alarm off in the morning (math puzzle,
    reaction time tester, etc.)
-   12-hour mode (no concept of AM/PM or at least not for setting
    alarm times)
-   Funky displays (rolling numbers, fades, blinky, etc.)
-   "Approximate" time display (round to 15 minutes, etc.)
-   Clock display off or "symbolic" while alarm is set to prevent seeing
    what time it is while you're sleeping.
-   Sleep/Wake cycle logging (when do you go to sleep, when do you
    wake up)
-   subtle pre-waking sounds that don't actually wake you up if you're
    sound asleep.
-   truly random "snooze" durations
-   "I really have to wake up" mode that prevents snoozing altogether
-   Jet Lag helper modes (clock gradually shifts from time zone 1 to
    zone 2 over N days, either pre or post trip)
-   Mars time, possibly other extra-solar times for use at NASA
-   Easy to use multi-user modes. (multiple predefined alarms, easy to
    choose between them)
-   Funky or easier semantics for setting the time.
-   Scrolling text (how feasible with 7-segment display?)
-   Enhanced dot-matrix display for text and extra functions.
    (more buttons!)

Here are the characters you can easily display on a 7-segment display:  
AbcdEFghiJLnoPSuyZ

Things that are coming some day:

-   PCB schematic.
-   Intstructions & photos for modifying/gutting an existing clock
-   Source code (C for AVR)

