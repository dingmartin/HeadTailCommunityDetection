This program (download <a rel="nofollow" target="_blank" href="http://fromto.hig.se/~bjg/HeadTailBreaksCode/HeadTailCommunityDetectionCode.rar"> <i>here</i></a></font></font>) is developed out of the following paper:

<i>Jiang B. and Ding M. (2015), Defining least community as a homogeneous group in complex networks, Physica A, 428, 154-160.</i>

Simply put, it is for obtaining homogeneous communities in complex networks by applying head/tail breaks on edge betweenness given its heavy-tailed distribution. The program is based on NetworkX 1.8, and its input and output files follow with Pajek file format (.net). 


<b>How to do:</b>

1. Open .net file in txt and copy all edges under line "*edges" and then paste them into a new txt file. 
2. Replace the related lines of the code with the input file location, the division rule, and output file location as the comment indicated. 
3. Run the program and then replace the edges from the original .net with the edges from the output file (It is better to make a copy of original net file for later comparison). 
4. Load the changed .net file in Pajek, click <i> draw network </i> button, then press "ctrl + k", all the homogeneous groups will show up. In case you want to know further info of detected homo-groups, in Pajek click <i> Network > Create Partition > Components > Weak </i>, set minimum size = 1, then the number of homo-groups and their node members etc. will be obtained. 

Note that the computing capacity of this program is limited to around 30,000 edges, and it may take couple of minutes or longer for a bigger graph (say > 10,000 edges). 

Please note that do NOT make space as the last row in the input file. 


