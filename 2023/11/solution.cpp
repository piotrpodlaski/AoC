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

typedef std::pair<ull,ull> position;

template<typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1,T2>& p){
	os<<"("<<p.first<<","<<p.second<<")";
	return os;
}

std::vector<ll> getInts(std::string s){
	std::stringstream ss{s};
	ll tmp;
	std::vector<ll> result;
	while(!ss.eof()){
		if(ss>>tmp)
			result.push_back(tmp);
	}
	return result;
}

std::vector<position> expandGalaxy(std::vector<position> galaxies, int nRows, int nCols, ull increment=1){
	std::list<int> rowsNoGalaxy(nRows);
	std::iota(rowsNoGalaxy.begin(),rowsNoGalaxy.end(),0);
	std::list<int> colsNoGalaxy(nCols);
	std::iota(colsNoGalaxy.begin(),colsNoGalaxy.end(),0);

	for(auto g : galaxies){
		rowsNoGalaxy.remove(g.second);
		colsNoGalaxy.remove(g.first);
	}


	int incrementedRows=0;
	for(auto r : rowsNoGalaxy){
		for(auto &g : galaxies){
			if(g.second>r+incrementedRows){
				g.second+=increment;
			}
		}
		incrementedRows+=increment;

	}

	int incrementedCols=0;
	for(auto c : colsNoGalaxy){
		for(auto &g : galaxies){
			if(g.first>c+incrementedCols){
				g.first+=increment;
			}
		}
		incrementedCols+=increment;
	}
	return galaxies;
}

ull calculateSumOfDistances(std::vector<position> galaxies){
	ull sum = 0;
	for(int i=0; i<galaxies.size(); i++){
		for(int j=i+1;j<galaxies.size();j++){
			auto g1 = galaxies[i];
			auto g2 = galaxies[j];
			sum+=std::llabs(g1.first-g2.first);
			sum+=std::llabs(g1.second-g2.second);
		}
	}
	return sum;
}


int main(){
	std::ifstream f{"in.txt"};
	std::vector<position> galaxies;
	std::string line;
	int lineId=0;
	int nCols=0;
	while(std::getline(f,line)){
		for(size_t i=0;i<line.size();i++){
			if(line[i]=='#')
				galaxies.push_back({i,lineId});
		}
		nCols=line.size();
		lineId++;
	} //parsing end
	int nRows=lineId;

	
	std::cout<<calculateSumOfDistances(expandGalaxy(galaxies,nRows,nCols,1))<<std::endl;
	std::cout<<calculateSumOfDistances(expandGalaxy(galaxies,nRows,nCols,999999))<<std::endl;
}