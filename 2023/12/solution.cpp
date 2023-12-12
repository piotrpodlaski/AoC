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
	while(ss >> tmp){
			result.push_back(tmp);
		if (ss.peek() == ',')
            ss.ignore();
	}
	return result;
}

std::vector<ll> findLayout(std::string s){
	int seqLen=0;
	std::vector<ll> layout;
	for(auto c : s){
		if(c=='.'){
			if(seqLen>0)
				layout.push_back(seqLen);
			seqLen=0;
		}
		else if(c=='#')
			seqLen++;
		else
			throw std::runtime_error("unexpected character!");
	}
	if(seqLen>0)
		layout.push_back(seqLen);
	return layout;
}

void findNumberOfWays(std::string s, std::vector<ll> layout, int& nWays){
	auto pos = s.find("?");
	if(pos==std::string::npos){
		if(findLayout(s)==layout)
			nWays++;
	}
	else{
		s[pos]='.';
		findNumberOfWays(s,layout,nWays);
		s[pos]='#';
		findNumberOfWays(s,layout,nWays);
	}
}


int main(){

	std::vector<std::pair<std::string,std::vector<ll>>> input;

	std::ifstream f{"in.txt"};
	std::string line;
	while(std::getline(f,line)){
		auto s = line.substr(0,line.find(" "));
		auto ints = getInts(line.substr(line.find(" ")+1));
		input.push_back({s,ints});
	} //parsing end

	int nWays=0;
	for(auto [s,lay] : input){
		std::cout<<s<<std::endl;
		findNumberOfWays(s, lay, nWays);
	}
	std::cout<<nWays<<std::endl;
}