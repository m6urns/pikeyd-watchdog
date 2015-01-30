Python script to monitor GPIO and keep pikeyd incheck.

I was havinf issues with pikeyd repeatedly returning a
key press long after I had stopped pressing. This script 
monitors GPIO 18 for keypress and kills the runaway 
process, starting pikeyd again. Wonderfully hacky isn't it?
