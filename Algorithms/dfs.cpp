/*
Author : Pushkar Godbole
Roll no. : 09D01005
Course : CS 213 (Minor)
Course name : Datastructures and Algorithms

*** Assignment 2 ***

This code finds all paths between any two nodes in a directed graph.

It uses DFS to find all the paths. It remembers the nodes with splits using a stack (last in-first out) structure. Therefore the algorithm does not have to start from the start-node in every traversal. It instead starts from the last unfinished split-node (the path to which from start-node is known). Thus every node uptil the split is effectively traversed only once. The code reads the graph data from a text file provided to it as argument.

USAGE :

./a.out dfs_graphdata.txt

INPUT :

Ex)

0:1
1:2 3
3:5 7
2:4
5:6
4:6
7:5

(The ordering of numbers need not be sorted)

Node 0 connected to 1, node 1 connected to 2 and 3, and so on...
Do not leave extraneous spaces between digits.

OUTPUT

Ex)

Start node : 0
End node : 6
Paths between 0 and 6 :
1 : 0 1 3 7 5 6 
2 : 0 1 3 5 6 
3 : 0 1 2 4 6 
*/

#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;
//***************************************************************** arc data structure *************************************************************
struct arc
{
	public:
		int node1;
		int node2;
};

//*************************************************************** DFS function *******************************************************************
vector<vector<arc> > getallpaths(int start, int end, vector<vector<arc> > connects)
{
	vector<vector<arc> > allpaths;
	vector<vector<arc> > splitpaths;
	vector<int> splitnodes;
	vector<arc> open;
	vector<arc> path;
	int curr_node;
	do
	{
		if(open.size()!=0)
		{
			path.clear();
			start = open[open.size()-1].node2;
			while(open[open.size()-1].node1 != splitnodes[splitnodes.size()-1])
			{
				splitnodes.pop_back();
				splitpaths.pop_back();
			}
			path = splitpaths[splitpaths.size()-1];
			path.push_back(open[open.size()-1]);
			open.pop_back();
		}
		curr_node = start;
		while(connects[curr_node].size()!=0 && curr_node!=end)
		{
			for(int i=0;i<connects[curr_node].size();i++) open.push_back(connects[curr_node][i]);
			if(connects[curr_node].size()>1)
			{
				splitnodes.push_back(curr_node);
				splitpaths.push_back(path);
			}
			curr_node = open[open.size()-1].node2;
			path.push_back(open[open.size()-1]);
			open.pop_back();
		}
		if(path.size()!=0)
		{
			if(path[path.size()-1].node2 == end)
			{
				allpaths.push_back(path);
			}
		}
	}while(open.size()!=0);
	return allpaths;
}

//************************************************** Function to read graph data from input file ****************************************************
vector<vector<arc> > getdata(char* filename)
{
	ifstream myfile;
	myfile.open(filename);
	string line;
	string str;
	size_t split;
	vector<vector<arc> > temp_connects;
	vector<int> parents;
	vector<vector<arc> > connects;
	int count = 0;
	vector<arc> temparcs;
	int max_parent = 0;
	while(getline(myfile, line))
	{
		split = line.find_first_of(":");
		int parent, child;
		if(split!=string::npos)
		{
			str = line.substr(0,split);
			stringstream(str) >> parent;
			parents.push_back(parent);
			if(parent > max_parent) max_parent = parent;
			line.erase(0,split+1);
			temp_connects.push_back(temparcs);
			arc temp;
			temp.node1 = parent;
			while(line.length()!=0)
			{
				split = line.find_first_of(" ");
				if(split!=string::npos)
				{
					str = line.substr(0,split);
					stringstream(str) >> child;
					temp.node2 = child;
					temp_connects[count].push_back(temp);
					line.erase(0,split+1);
				}
				else break;
			}
			stringstream(line) >> child;
			temp.node2 = child;
			temp_connects[count].push_back(temp);
		}
		else break;
		count++;
	}
	max_parent++;
	for(int i=0;i<max_parent;i++) connects.push_back(temparcs);
	for(int i=0;i<parents.size();i++) connects[parents[i]]=temp_connects[i];
	return connects;
}	
//*************************************************************** main *******************************************************************
int main(int noarg, char* args[])
{
	string str;
	vector<vector<arc> > connects;
	connects = getdata(args[1]);
	vector<vector<arc> > allpaths;
	int start, end;
	cout << "Start node : ";
	cin >> str;
	stringstream(str) >> start;
	cout << "End node : ";
	cin >> str;
	stringstream(str) >> end;
	int max_parent = connects.size();
	if(start >= 0 && start < max_parent && end >= 0 && end < max_parent)
	{
		allpaths = getallpaths(start, end, connects);
		if(allpaths.size()!=0)
		{
			cout << "Paths between " << start << " and " << end << " :" << endl;
			for(int i=0;i<allpaths.size();i++)
			{
				cout << i+1 << " : ";
				cout << allpaths[i][0].node1 << " ";
				for(int j=0;j<allpaths[i].size();j++) cout << allpaths[i][j].node2 << " ";
				cout << endl;
			}
		}
		else cout << "No paths found between " << start << " and " << end << endl;
	}
	else cout << "Invalid start or end node" << endl;
	return 0;
}
