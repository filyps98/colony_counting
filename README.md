# Colony Counting
This program processes images of Petri dishes to count the number of colonies present inside.
The following Petri dish agars are used:
1. CHOC
2. CLED: this particular agar presents a writing at the bottom of the petri dish that complicates the image processing
3. CNA
4. CPSE
5. MCK
6. MRSA: transform the image to HSV and extract the saturation component, invert white with black, blur the image, and apply a binary and otsu threshold to further highlight the colonies.

For each of these agars, a different strategy is employed
