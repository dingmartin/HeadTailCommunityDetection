The program (download <a rel="nofollow" target="_blank" href="http://fromto.hig.se/~bjg/HeadTailBreaksCode/HeadTailCommunityDetectionCode.rar"> <i>here</i></a></font></font>) is for obtaining homogeneous communities in complex networks by applying head/tail breaks on edge betweenness given its heavy-tailed distribution. The program is developed based on NetworkX 1.8 and its input and output files follow with Pajek file format (.net). 

<b>How to do:</b>

Both the input and output files of the program are related to edges in graph. To generate input file, open .net file in txt and copy all edge data under line "*edges" and then paste them into a new txt file. Then change the code with the input file location, you can also change the division rule and output file location as the comment indicated. Run the program and then copy the edge data from output file and replace the edges in original net with the copied edges (It is better to make a copy of original net file for later comparison purpose). Finally, load the changed .net file in Pajek, click draw network button, then press "ctrl + k", all the homogeneous groups will be shown.

And in case you want to know further info of detected homo-groups, click Network > Create Partition > Components > Weak, set minimum size = 1, then the number of homo-groups and their node members etc. will be obtained. 

Note that the computing capacity of this program is limited to around 30,000 edges, and it may take couple of minutes or longer for a bigger graph (say > 10,000 edges). 

And please make sure to keep the "networkx" folder and the code file in the same folder and do NOT make space as the last row for input file. 


