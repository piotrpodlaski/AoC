#include <iostream>
#include <fstream>
#include <map>
#include <unordered_map>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>
#include <numeric>

typedef unsigned long long ull;


struct node{
	std::string l;
	std::string r;
};

ull gcd(ull num1, ull num2)
{
	if (num2 == 0)
		return num1;
	return gcd(num2, num1 % num2);
}

ull lcm_of_array(std::vector<ull> arr)
{
	ull lcm = arr[0];
	for (int i = 1; i < arr.size(); i++) {
		ull num1 = lcm;
		ull num2 = arr[i];
		ull gcd_val = gcd(num1, num2);
		lcm = (lcm * arr[i]) / gcd_val;
	}
	return lcm;
}


int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	std::string steps;

	std::getline(f,steps);

	std::getline(f,line);

	std::unordered_map<std::string,node> nodes;

	std::vector<std::string> startNodes;

	while(std::getline(f,line)){
		auto key=line.substr(0,3);
		auto l=line.substr(7,3);
		auto r=line.substr(12,3);
		nodes[key]={l,r};
		if(key[2]=='A')
			startNodes.push_back(key);
	} //parsing end

	std::string position = "AAA";
	int nSteps=0;
	while(true){
		for(auto c : steps){
			if(c=='L')
				position=nodes[position].l;
			if(c=='R')
				position=nodes[position].r;
			nSteps++;
			if(position=="ZZZ")
				break;
		}
		if(position=="ZZZ")
			break;
	}
	std::cout<<nSteps<<std::endl;

	nSteps==0;
	std::vector<ull> numberOfSteps;
	for(auto position: startNodes){
		nSteps=0;
		while(true){
			for(int i = 0; i<steps.size(); i++){
				auto c=steps[i];
				if(c=='L')
					position=nodes[position].l;
				if(c=='R')
					position=nodes[position].r;
				nSteps++;
				if(position[2]=='Z'){
					break;
				}
			}
			if(position[2]=='Z'){
				numberOfSteps.push_back(nSteps);
				break;
			}
		}
	}

	std::cout<<lcm_of_array(numberOfSteps)<<std::endl;
}