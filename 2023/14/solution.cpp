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


int calcLoad(std::map<position,char> input, int nRows){
	int load=0;
	for(auto [p,c] : input){
		if(c=='O'){
			load+=nRows-p.second;
		}
	}
	return load;
}



int main(){
	std::map<position,char> input;
	std::ifstream f{"in.txt"};
	std::string line;
	int colId = 0;
	int rowId=0;
	while(std::getline(f,line)){
		std::cout<<line<<std::endl;
		colId=0;
		for(auto c : line){
			input[{colId,rowId}]=c;
			colId++;
		}
		rowId++;
	} //parsing end


	for(int c=0;c<colId;c++){
		for(int r=0;r<rowId;r++){
			if(input[{c,r}]!='O')
				continue;
			int firstNonEmptyRow=r;
			while(firstNonEmptyRow>0){
				if(input[{c,firstNonEmptyRow-1}]!='.')
					break;
				firstNonEmptyRow--;
			}
			input[{c,r}]='.';
			input[{c,firstNonEmptyRow}]='O';
		}
	}

	std::cout<<std::endl;

	for(int r=0;r<rowId;r++){
		for(int c=0;c<colId;c++){
			std::cout<<input[{c,r}];
		}
		std::cout<<std::endl;
	}

	std::cout<<calcLoad(input,rowId)<<std::endl;


}