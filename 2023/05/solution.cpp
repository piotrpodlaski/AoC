#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

typedef unsigned long long ull;


std::vector<ull> getInts(std::string s){
	std::stringstream ss{s};
	ull tmp;
	std::vector<ull> result;
	while(!ss.eof()){
		if(ss>>tmp)
			result.push_back(tmp);
	}
	return result;
}

struct interval{
	ull beg;
	ull end;
};

class mapping{
	struct rng{
		ull src;
		ull dst;
		ull len;
	};
	std::vector<rng> ranges;
public:
	void addRange(rng r){
		ranges.push_back(r);
	}
	ull map(ull src){
		for(auto r : ranges){
			if(src>=r.src && src<r.src+r.len)
				return r.dst+src-r.src;
		}
		return src;
	}

	std::vector<interval> mapInterval(interval in){
		std::vector<interval> tmp;
		for(auto [src,dst,len] : ranges){
			auto end = src+len-1;
			if(!((end<in.beg) || src>in.end)){
				tmp.push_back({std::max(src,in.beg),std::min(end,in.end)});
			}
		}
		auto size = tmp.size();
		for(size_t i = 0; i<size;i++){
			if(i<size-1 && tmp[i+1].beg>tmp[i].end+1)
				tmp.push_back({tmp[i].end+1,tmp[i+1].beg-1});
		}

		if(tmp.size()==0){
			tmp.push_back(in);
		}

		if(tmp[0].beg!=in.beg){
			tmp.push_back({in.beg,tmp[0].beg-1});
		}

		if(tmp[tmp.size()-1].end!=in.end){
			tmp.push_back({tmp[size-1].end+1,in.end});
		}

		std::vector<interval> result;
		for(auto [left,right]:tmp){
			result.push_back({map(left),map(right)});
		}

		return result;

	}
	void clear(){
		ranges.clear();
	}
	void sort(){
		std::ranges::sort(ranges,[](const rng &a, rng &b){
			return a.src<b.src;
		});
	}
	void dropRanges(){
		for(auto r : ranges){
			std::cout<<"["<<r.src<<","<<r.src+r.len-1<<"] ->";
			std::cout<<"["<<r.dst<<","<<r.dst+r.len-1<<"]"<<std::endl;
		}
	}
};

int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	
	std::getline(f,line);

	auto seeds=getInts(line.substr(line.find(":")+1));

	std::getline(f,line);
	std::getline(f,line);
	std::vector<mapping> maps;
	mapping singleMap;
	while(std::getline(f,line)){
		if(line==""){
			singleMap.sort();
			maps.push_back(singleMap);
			singleMap.clear();
			continue;
		}

		if(line.find("map")!=std::string::npos)
			continue;

		unsigned long long dest, src, len;
		std::stringstream ss{line};
		ss>>dest>>src>>len;
		singleMap.addRange({src,dest,len});
	}
	singleMap.sort();
	maps.push_back(singleMap);


	std::vector<ull> locations;

	for(auto s : seeds){
		for(unsigned int i=0;i<maps.size();i++){
			s=maps[i].map(s);
		}
		locations.push_back(s);
	}

	std::cout<<*std::ranges::min_element(locations)<<std::endl;


	std::vector<interval> resultingIntervals;

	for(unsigned int i=0;i<seeds.size()/2;i++)
	{
		std::vector<interval> s{{seeds[2*i],seeds[2*i]+seeds[2*i+1]-1}};
		for(auto &m:maps){
			std::vector<interval> tmp;
			for(auto intv: s){
				auto a = m.mapInterval(intv);
				tmp.insert(tmp.end(),a.begin(),a.end());
			}
			s=tmp;
		}
		resultingIntervals.insert(resultingIntervals.begin(),s.begin(),s.end());
	}

	std::cout<<(*std::ranges::min_element(resultingIntervals,[](const interval &a, interval &b){
			return a.beg<b.end;
		})).beg<<std::endl;

	
}