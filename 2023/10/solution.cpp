#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>

typedef std::pair<int,int> position;

std::vector<position> deltas = {{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0}};
std::map<char,std::map<position,position>> pipeElements;


position addPos(position a, position b){
	return {a.first+b.first,a.second+b.second};
}

template<typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1,T2>& p){
	os<<"("<<p.first<<","<<p.second<<")";
	return os;
}

template<typename T1, typename T2>
std::pair<T1,T2> operator+(std::pair<T1,T2> p1, std::pair<T1,T2> p2){
	return {p1.first+p2.first, p1.second+p2.second};
}


position findStartingPoint(std::map<position,char> plan){
	for(auto [pos,c] : plan){
		if(c=='S')
			return pos;
	}
	return {-1,-1};
}
std::map<position,char> areaPlan;

bool checkNextPipeElement(position pos, position delta){
	auto node = areaPlan[pos];
	if(!pipeElements.contains(node)){
			return false; //not a pipe element!
	}
	if(!pipeElements[node].contains(delta)){
		return false; //pipe element not correctly oriented!
	}
	return true;
}

std::pair<bool,int> traverseLoop(position pos, position delta, std::vector<std::pair<float,float>>& vertices){
	int nSteps=1;
	while(true){
		auto node = areaPlan[pos];
		vertices.push_back({pos.first,pos.second});
		delta = pipeElements[node][delta];
		pos = pos+delta;
		if(areaPlan[pos]=='S'){
			return {true, nSteps};
		}
		if(!checkNextPipeElement(pos,delta))
			return {false,nSteps};
		nSteps++;
	}

}

bool isIn( std::vector<std::pair<float,float>> vertices, std::pair<float,float> testPoint) {
  int i, j, c = 0;
  for (i = 0, j = vertices.size()-1; i < vertices.size(); j = i++) {
    if ( ((vertices[i].second>testPoint.second) != (vertices[j].second>testPoint.second)) &&
	 (testPoint.first < (vertices[j].first-vertices[i].first) * (testPoint.second-vertices[i].second) / (vertices[j].second-vertices[i].second) + vertices[i].first) )
       c = !c;
  }
  return c;
}

int main(){
	pipeElements['|'] = {
		{{ 0,-1},{ 0,-1}},
		{{ 0, 1},{ 0, 1}}
	};
	pipeElements['-'] = {
		{{-1, 0},{-1, 0}},
		{{ 1, 0},{ 1, 0}}
	};
	pipeElements['L'] = {
		{{ 0, 1},{ 1, 0}},
		{{-1, 0},{ 0,-1}}
	};
	pipeElements['J'] = {
		{{ 1, 0},{ 0,-1}},
		{{ 0, 1},{-1, 0}}
	};
	pipeElements['7'] = {
		{{ 1, 0},{ 0, 1}},
		{{ 0,-1},{-1, 0}}
	};
	pipeElements['F'] = {
		{{ 0,-1},{ 1, 0}},
		{{-1, 0},{ 0, 1}}
	};
	std::ifstream f{"in.txt"};
	std::string line;
	int lineId=0;
	int nLines=0;
	int nRows=0;
	while(std::getline(f,line)){
		for(unsigned int i=0; i<line.size(); i++){
			areaPlan.insert({{i,lineId},line[i]});
		}
		if(nRows==0){
			nRows=line.size();
		}
		lineId++;
	} //parsing end
	nLines=lineId;
	auto currentPos = findStartingPoint(areaPlan);
	std::vector<position> loopStartingPoints;
	std::vector<std::pair<float,float>> vertices;
	for(auto d: deltas){
		auto nodePosition = currentPos+d;
		if(!checkNextPipeElement(nodePosition,d))
			continue;

		vertices.clear();
		auto [fullLoop, nSteps] = traverseLoop(nodePosition,d,vertices);
		if(fullLoop){
			vertices.push_back({currentPos.first,currentPos.second});
			std::cout<<std::ceil(nSteps/2.)<<std::endl;
			break;
		}


	}

	int nInsideNodes=0;
	for(int line = 0; line<nLines; line++){
		for(int row = 0; row<nRows; row++){
			position pos{row,line};
			if(std::find(vertices.begin(),vertices.end(), std::make_pair((float)row,(float)line))==vertices.end())
				if(isIn(vertices,{row+0.01,line+0.1}))
					nInsideNodes++;
		}
	}

	std::cout<<nInsideNodes<<std::endl;

}