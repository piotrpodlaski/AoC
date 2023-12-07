#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <set>

std::vector<std::pair<int,int>> findNumbers(std::string& s){
	std::vector<std::pair<int,int>> result;
	size_t begin=0, end=0;
	while(end!=std::string::npos){
		begin=s.find_first_of("0123456789",end);
		if(begin!=std::string::npos){
			end=s.find_first_not_of("0123456789",begin);
			std::string num = s.substr(begin,end-begin);
			int number = std::stoi(num);
			result.push_back({begin,number});
		}
		else
			break;
	}
	return result;
}

std::vector<int> findSymbols(std::string& s){
	std::vector<int> result;
	size_t pos=0;
	while(pos!=std::string::npos){
		pos=s.find_first_not_of("0123456789.",pos);
		if(pos!=std::string::npos){
			result.push_back(pos);
		}
		else
			break;
		pos+=1;
	}
	return result;
}

int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	int lineId=0;
	std::vector<int> numbers;
	std::map<std::pair<int,int>,int> numPointers;
	std::vector<std::pair<int,int>> symbols;
	std::map<std::pair<int,int>,char> symbolsTypes;
	while(std::getline(f,line)){
		auto nums = findNumbers(line);
		auto syms = findSymbols(line);
		for(auto [pos,num] : nums){
			int len = std::to_string(num).size();
			numbers.push_back(num);
			for(int i=0;i<len;i++){
				numPointers[{lineId,pos+i}]=numbers.size()-1;
			}

		}
		for(auto sym: syms){
			symbols.push_back({lineId,sym});
			symbolsTypes[{lineId,sym}]=line[sym];
		}
		lineId++;
	} //parsing end

	std::vector<std::pair<int,int>> deltas = {{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0}};

	std::set<int> partIndeces;
	for(auto [x,y] : symbols){
		for(auto [dx,dy] : deltas){
			std::pair<int,int> pos = {x+dx,y+dy};
			if(numPointers.contains(pos))
				partIndeces.insert(numPointers[pos]);
		}
	}
	int sum1=0;
	int sum2=0;
	for(auto id : partIndeces)
		sum1+=numbers[id];

	for(auto [x,y] : symbols){
		if(symbolsTypes[{x,y}]!='*')
			continue;
		std::set<int> tmp;
		for(auto [dx,dy] : deltas){
			std::pair<int,int> pos = {x+dx,y+dy};
			if(numPointers.contains(pos)){
				partIndeces.insert(numPointers[pos]);
				tmp.insert(numPointers[pos]);
			}
		}
		if(tmp.size()==2){
			auto n1 = numbers[*next(tmp.begin(),0)];
			auto n2 = numbers[*next(tmp.begin(),1)];
			sum2+=n1*n2;
		}

	}

	std::cout<<sum1<<std::endl;
	std::cout<<sum2<<std::endl;


}