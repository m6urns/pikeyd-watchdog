Python script to monitor GPIO and keep pikeyd in check.

I was having issues with pikeyd repeatedly returning a
key press long after I had stopped pressing. This script 
monitors GPIO 18 for keypress and kills the runaway 
process, starting pikeyd again. Wonderfully hacky isn't it?

Note: Turns out it was totally a hardware issue. Pikeyd works 
perfectly. The watchdog script also works great, maybe someone
else has a use for it?
