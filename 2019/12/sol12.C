#include <string>

typedef std::pair<std::vector<int>,std::vector<int>> moonType;


/**
 * @brief      Prints all.
 *
 * @param[in]  v     { parameter_description }
 */
void printAll(std::vector<moonType> v)
{
	for(auto moon:v)
	{
		auto a=moon.first;
		std::cout<<"pos:\t";
		for(auto aa:a)
			std::cout<<aa<<"\t";
		a=moon.second;
		std::cout<<"vel:\t";
		for(auto aa:a)
			std::cout<<aa<<"\t";
		std::cout<<std::endl;
	}
}


void sol12()
{
	typedef std::pair<std::vector<int>,std::vector<int>> moonType;
	std::vector<moonType> moons;
	moons.push_back(std::make_pair(std::vector<int>{-8,-10,0},std::vector<int>{0,0,0}));
	moons.push_back(std::make_pair(std::vector<int>{5,5,10},std::vector<int>{0,0,0}));
	moons.push_back(std::make_pair(std::vector<int>{2,-7,3},std::vector<int>{0,0,0}));
	moons.push_back(std::make_pair(std::vector<int>{9,-8,-3},std::vector<int>{0,0,0}));
	printAll(moons);
}