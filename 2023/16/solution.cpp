#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>
#include <list>
#include <numeric>

typedef unsigned long long ull;

typedef unsigned long long ll;

typedef std::pair<int,int> position;

template<typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1,T2>& p){
	os<<"("<<p.first<<","<<p.second<<")";
	return os;
}

template<typename T1, typename T2>
std::pair<T1,T2> operator+(std::pair<T1,T2> p1, std::pair<T1,T2> p2){
	return {p1.first+p2.first, p1.second+p2.second};
}

typedef std::pair<position,position> laserBeam;

std::map<char,std::map<position,std::vector<position>>> elements ={
	{'|', {
			{{1,0}, {{0,1},{0,-1}}},
			{{-1,0}, {{0,1},{0,-1}}}

		}
	},
	{'-', {
			{{0,1}, {{1,0},{-1,0}}},
			{{0,-1}, {{1,0},{-1,0}}}

		}
	},
	{'/', {
			{{1,0}, {{0,-1}}},
			{{-1,0}, {{0,1}}},
			{{0,1}, {{-1,0}}},
			{{0,-1}, {{1,0}}}

		}
	},
	{'\\', {
			{{1,0}, {{0,1}}},
			{{-1,0}, {{0,-1}}},
			{{0,1}, {{1,0}}},
			{{0,-1}, {{-1,0}}}

		}
	}
};



void propagateBeam(const std::map<position,char>& layout, laserBeam laser, std::set<laserBeam>& visitedPositions){
	if(visitedPositions.contains(laser))
		return;
	if(!layout.contains(laser.first))
		return;
	visitedPositions.insert(laser);
	auto e = layout.at(laser.first);
	if(elements.contains(e)&&elements[e].contains(laser.second)){
		for(auto d : elements[e][laser.second]){
			propagateBeam(layout,{laser.first+d,d},visitedPositions);
		}
	}
	else{
		propagateBeam(layout,{laser.first+laser.second,laser.second},visitedPositions);
	}
}

int getNumberOfLiveTiles(std::set<laserBeam> visitedPositions){
	std::set<position> s;
	for(auto l: visitedPositions)
		s.insert(l.first);
	return s.size();
}

int doStep(const std::map<position,char>& layout, laserBeam laser){
	std::set<laserBeam> visitedPositions;
	propagateBeam(layout, laser, visitedPositions);
	return getNumberOfLiveTiles(visitedPositions);
}


int main(){
	std::map<position,char> input;
	std::ifstream f{"in.txt"};
	std::string line;
	int colId = 0;
	int rowId=0;
	while(std::getline(f,line)){
		colId=0;
		for(auto c : line){
			input[{colId,rowId}]=c;
			colId++;
		}
		rowId++;
	} //parsing end



	std::cout<<doStep(input, {{0,0},{1,0}})<<std::endl;

	std::set<int> liveOnes;

	for(int row = 0;row<rowId;row++){
		liveOnes.insert(doStep(input,{{0,row},{1,0}}));
		liveOnes.insert(doStep(input,{{colId-1,row},{-1,0}}));
	}
	for(int col = 0;col<colId;col++){
		liveOnes.insert(doStep(input,{{col,0},{0,1}}));
		liveOnes.insert(doStep(input,{{col,rowId-1},{0,-1}}));
	}

	std::cout<<*liveOnes.rbegin()<<std::endl;
	
}