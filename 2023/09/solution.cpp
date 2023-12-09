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
#include <exception>
#include <ranges>

typedef unsigned long long ull;

typedef unsigned long long ll;


std::vector<ll> getInts(std::string s){
	std::stringstream ss{s};
	ll tmp;
	std::vector<ll> result;
	while(!ss.eof()){
		if(ss>>tmp)
			result.push_back(tmp);
	}
	return result;
}

template<typename T>
void print(std::vector<T> v, char delim = '\n'){
	for(auto i : v)
		std::cout<<i<<delim;
	std::cout<<std::endl;
}

bool checkAllZero(std::vector<ll> v){
	for(auto i: v){
		if(i)
			return false;
	}
	return true;
}

std::vector<ll> derivative(std::vector<ll> v){
	if(v.size()<2)
		throw std::runtime_error("vector too small to calculate derivative");
	std::vector<ll> result;
	auto prev = v[0];
	for(auto x : v | std::views::drop(1)){
		result.push_back(x-prev);
		prev=x;
	}
	return result;
}

int predictNext(std::vector<ll> in){
	std::vector<std::vector<ll>> derivatives;
	auto current = in;
	derivatives.push_back(current);
	while(true){
		auto derr = derivative(current);
		derivatives.push_back(derr);
		current=derr;
		if(checkAllZero(derr))
			break;
	}
	for(int i=derivatives.size()-2;i>=0;i--){
		derivatives[i].push_back(derivatives[i].back()+derivatives[i+1].back());
	}
	return derivatives[0].back();
}


int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	std::vector<std::vector<ll>> input;
	while(std::getline(f,line)){
		input.push_back(getInts(line));
	} //parsing end
	
	ll sum1=0;
	ll sum2=0;
	for(auto &numbers: input){
		sum1+=predictNext(numbers);
		std::ranges::reverse(numbers);
		sum2+=predictNext(numbers);
	}
	std::cout<<sum1<<std::endl;
	std::cout<<sum2<<std::endl;
}