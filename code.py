import networkx as nx
import csv
import timeit

def getMean(values):
    mean=0
    numsum=0
    for index in range(len(values)):
        numsum=numsum+values[index]
    mean=float(numsum)/float(len(values))
    return mean

def HeadTailCommunityDetection(G,finaledgelist):
    H=nx.connected_component_subgraphs(G)
    for subgraph in H:
        result=nx.edge_betweenness(subgraph, False, None)
        edges=result.keys()
        values=result.values()
        mean = getMean(values)
        edgelist=[]
        edgetemp=subgraph.edges();
        if len(edgetemp)<=2:
            for edge in edgetemp:
                finaledgelist.append(edge)
        else:
            for index in range(len(values)):
                    if values[index] <= mean:
                        edgelist.append(edges[index])
            if  (float(len(edgelist))/float(len(edges)))<=0.6: #change the head/tail division rule here, here is for tail percentage, so if the rule is 40/60, the value should be assigned 0.6 as in the code.
                for edge in edgelist:
                    finaledgelist.append(edge)
            else:
                Gsub= nx.Graph()
                for edge in edgelist:
                    Gsub.add_edge(edge[0],edge[1])
                HeadTailCommunityDetection(Gsub,finaledgelist)

def HeadTailInitiator():
    G = nx.Graph()
    ins = open("sampleNetFile\\Protein\\edge.txt", "r")  #input file path
    for line in ins:
            words = line.split(' ')
            G.add_edge(int(words[0]), int(words[1]))
    ins.close()
    finaledgelist=[]
    start = timeit.default_timer()
    HeadTailCommunityDetection(G,finaledgelist)
    print "done!"
    stop = timeit.default_timer()
    print "Processing time(in second): "
    print stop - start
    text_file = open("OutputEdge.txt", "w")    #output file path
    for edge in finaledgelist:
        text_file.write(str(edge[0])+" "+str(edge[1])+"\n")
    text_file.close()

HeadTailInitiator()

