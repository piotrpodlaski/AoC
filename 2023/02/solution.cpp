#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>

struct round{
	int r;
	int g;
	int b;
	bool operator<=(const round other){
		return (r<=other.r) && (g<=other.g) && (b<=other.b);
	}
};

std::vector<round> parseLine(std::string line){
	std::vector<round> result;
	std::stringstream s{line};
	std::string dummy;
	s>>dummy;
	int gameId;
	s>>gameId;
	char a;
	s>>a>>a;
	std::string singleGame;
	line=line.substr(line.find(":")+2);
	std::stringstream ss{line};
	while(std::getline(ss, singleGame, ';')){
	 	std::stringstream sss{singleGame};
	 	std::string singleRound;
	 	std::map<std::string,int> gameInput;
	 	int r=0,g=0,b=0;
	 	while(std::getline(sss, singleRound, ',')){
	 		std::stringstream ssss{singleRound};
	 		int num;
	 		std::string color;
	 		ssss>>num>>color;
	 		if(color.find("red")!=std::string::npos)
	 		  r=num;
	 		if(color.find("green")!=std::string::npos)
	 		 	g=num;
	 		if(color.find("blue")!=std::string::npos)
	 			b=num;
	 	}
	 	result.push_back({r,g,b});


	}
	return result;
}

int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	round minimalRound{12,13,14};
	int sum1=0, sum2=0, id=0;
	while(std::getline(f,line)){
		++id;
		auto rounds=parseLine(line);
		bool good=true;
		int minR=0, minG=0, minB=0;
		for(auto rnd: rounds){
			if(!(rnd<=minimalRound))
				good=false;
			minR=std::max(minR,rnd.r);
			minG=std::max(minG,rnd.g);
			minB=std::max(minB,rnd.b);

		}
		if(good)
			sum1+=id;
		sum2+=minR*minG*minB;
	}
	std::cout<<sum1<<std::endl;
	std::cout<<sum2<<std::endl;
}