#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

std::vector<int> getInts(std::string s){
	std::stringstream ss{s};
	int tmp;
	std::vector<int> result;
	while(!ss.eof()){
		if(ss>>tmp)
			result.push_back(tmp);
	}
	return result;
}

std::pair<std::vector<int>,std::vector<int>> parseLine(std::string& line){
	auto colon=line.find(":");
	auto dash = line.find("|");
	auto winning=line.substr(colon+1,dash-colon-1);
	auto my=line.substr(dash+1);
	return {getInts(winning), getInts(my)};
}

int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	std::vector<int> numbers;
	int sum1=0;
	int sum2=0;
	std::vector<int> scores;
	while(std::getline(f,line)){
		auto [win,my]=parseLine(line);
		int nWin=0;
		for(auto w: win){
			if(std::find(my.begin(), my.end(), w) != my.end()){
				nWin++;
			}
		}
		scores.push_back(nWin);
		if(nWin>0)
			sum1+=1UL<<(nWin-1);
	} //parsing end
	std::vector<int> nCards(scores.size(),1);
	for(int i=0;i<scores.size();i++){
		for(int j=1;j<=scores[i];j++){
			nCards[i+j]+=nCards[i];
		}
	}
	for(auto c : nCards)
		sum2+=c;


	std::cout<<sum1<<std::endl;
	std::cout<<sum2<<std::endl;


}