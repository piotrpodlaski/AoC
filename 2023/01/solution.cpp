#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <ctype.h>

std::map<std::string,int> digitValues={
	{"1", 1},
	{"2", 2},
	{"3", 3},
	{"4", 4},
	{"5", 5},
	{"6", 6},
	{"7", 7},
	{"8", 8},
	{"9", 9}
};

std::map<std::string,int> digitValues2={
	{"1", 1},
	{"2", 2},
	{"3", 3},
	{"4", 4},
	{"5", 5},
	{"6", 6},
	{"7", 7},
	{"8", 8},
	{"9", 9},
	{"one", 1},
	{"two", 2},
	{"three", 3},
	{"four", 4},
	{"five", 5},
	{"six", 6},
	{"seven", 7},
	{"eight", 8},
	{"nine", 9}
};

std::pair<int,int> findDigits(std::string s,std::map<std::string,int> m){
	int minPos=s.size();
	int maxPos=0;
	int min=-1,max=-1;
	for(const auto& [sdig,dig] : m){
		std::string::size_type found=0;
		while(true){
			found = s.find(sdig,found);
			if(found==std::string::npos)
				break;
			if(found<minPos){
				minPos=found;
				min=dig;
			}
			if(found>=maxPos){
				maxPos=found;
				max=dig;
			}
			found++;
		}
	}
	return {min,max};
}

int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	int sum1=0;
	int sum2=0;
	while(std::getline(f,line)){
		auto [min1, max1] = findDigits(line,digitValues);
		sum1+=10*min1+max1;
		auto [min2, max2] = findDigits(line,digitValues2);
		sum2+=10*min2+max2;
	}
	std::cout<<sum1<<std::endl;
	std::cout<<sum2<<std::endl;
}