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


struct pattern{
	std::map<position, char> mapping;
	position size;
};

std::string getRow(const pattern &p, int row){
	std::string result;
	for(int col = 0; col<p.size.first;col++){
		result+=p.mapping.at({col,row});
	}
	return result;
}

std::string getCol(const pattern &p, int col){
	std::string result;
	for(int row = 0; row<p.size.second;row++){
		result+=p.mapping.at({col,row});
	}
	return result;
}

int findReflectionRow(pattern p, int ignore=-1){
	auto d = p.size;
	auto nRows = d.second;
	auto nCols = d.first;
	for(int row=0;row<nRows-1;row++){
		if(row==ignore)
			continue;
		bool allGood=true;
		for(int i=0;i<std::min(row+1,nRows-row-1);i++){
			if(getRow(p,row-i)!=getRow(p,row+i+1)){
				allGood=false;
				break;
			}
		}
		if(allGood)
			return row+1;
	}
	return 0;
}

int findReflectionCol(pattern p, int ignore=-1){
	auto d = p.size;
	auto nRows = d.second;
	auto nCols = d.first;
	for(int col=0; col<nCols-1;col++){
		if(col==ignore)
			continue;
		bool allGood=true;
		for(int i=0;i<std::min(col+1,nCols-col-1);i++){
			if(getCol(p,col-i)!=getCol(p,col+i+1)){
				allGood=false;
				break;
			}
		}
		if(allGood)
			return col+1;
	}
	return 0;
}

int findSmudgeScore(pattern p){
	auto d = p.size;
	auto nRows = d.second;
	auto nCols = d.first;

	auto origReflectionRow = findReflectionRow(p);
	auto origReflectionCol = findReflectionCol(p);

	pattern pNew;
	for(int row=0; row<nRows;row++){
		for(int col=0; col<nCols;col++){
			pNew = p;
			pNew.mapping[{col,row}]= (pNew.mapping[{col,row}]=='#') ? '.' : '#';
			auto score = 100*findReflectionRow(pNew,origReflectionRow-1)+
		                     findReflectionCol(pNew,origReflectionCol-1);
			if(score !=0){
				return score;
			}
		}
	}
	return 0;
}



int main(){
	std::vector<pattern> input;
	std::ifstream f{"in.txt"};
	std::string line;
	int rowId=0;
	int currrowId=0;
	int colId=0;
	pattern pat;
	while(std::getline(f,line)){
		if(line.size()==0){
			pat.size={colId, currrowId};
			input.push_back(pat);
			pat.mapping.clear();
			currrowId=0;
			continue;
		}
		colId=0;
		for(auto c : line){
			pat.mapping[{colId,currrowId}]=c;
			colId++;
		}
		rowId++;
		currrowId++;
	} //parsing end

	pat.size={colId, currrowId};
	input.push_back(pat);

	int sum1=0;
	int sum2=0;

	for(auto p: input){
		sum1+=100*findReflectionRow(p)+findReflectionCol(p);
		sum2+= findSmudgeScore(p);
	}

	std::cout<<sum1<<std::endl;
	std::cout<<sum2<<std::endl;

}