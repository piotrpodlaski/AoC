#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>
#include <cmath>
//durtion of the race: T
//button holding:      t
//travel time:         T-t
//distance:            t*(T-t)
//distance to beat:    D
//equation:            t*t-t*T+D>0
//solutions:           0.5(T+sqrt(T2-4D))

typedef unsigned long long ull;

struct game{
	ull t;
	ull d;
};

int winningInterval(game g){
	long double x1=0.5*(g.t-sqrtl(g.t*g.t-4*g.d));
	long double x2=0.5*(g.t+sqrtl(g.t*g.t-4*g.d));
	int winLeft = ceil(x1);
	int winRight = floor(x2);
	if(winLeft==x1)
		winLeft++;
	if(winRight==x2)
		winRight--;
	return winRight-winLeft+1;
}


int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	std::getline(f,line);
	line=line.substr(9);
	std::stringstream sst{line};
	line.erase(std::remove_if(line.begin(), line.end(),[](unsigned char x) { return std::isspace(x); }),line.end());
	ull time = std::stoll(line);

	std::getline(f,line);
	line=line.substr(9);
	std::stringstream ssd{line};
	line.erase(std::remove_if(line.begin(), line.end(),[](unsigned char x) { return std::isspace(x); }),line.end());
	ull distance = std::stoll(line);
	std::vector<game> games;
	while(!sst.eof() && !ssd.eof()){
		ull t,d;
		sst>>t;
		ssd>>d;
		games.push_back({t,d});
	}

	int mult=1;
	for(auto g: games){
		mult*=winningInterval(g);
	}
	std::cout<<mult<<std::endl;
	std::cout<<winningInterval({time,distance})<<std::endl;
}