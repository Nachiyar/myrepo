data College;

input RollNumber Name $ Dept $ Year;
   
datalines; 

2000 David ECE 2015

2001 Ravi EEE 2015

2002 Prabhu EIE 2015

2003 Ram ECE 2015

2004 Aishu ECE 2015

2005 Priya CSE 2015 .

;



proc print data=College;
   
title 'Students';

run;