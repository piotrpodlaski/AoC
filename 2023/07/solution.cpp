#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>
#include <functional>

struct hand{
	std::string cards;
	int bet;
	int rank=0;
};

template<typename T>
bool has(std::vector<T> v, T val){
	return std::ranges::find(v,val)!=v.end();
}

int rankHand(std::string card){
	//five of a kind  - 6
	//four of a kind  - 5
	//full house      - 4
	//three of a kind - 3
	//two pairs       - 2
	//one pair        - 1
	//high card       - 0
	std::map<char,int> freq;
	for(auto c:card)
		freq[c]++;
	std::vector<int> freqV;
	for(auto [c,f] : freq){
		freqV.push_back(f);
	}
	auto size=freqV.size();
	//five of a kind:
	if(size==1)
		return 6;

	if(size==2){
		//four of a kind:
		if(has(freqV,4))
			return 5;

		//full house
		return 4;
	}
	//three of a kind
	if(has(freqV,3))
		return 3;

	//two pairs
	if(size==3)
		return 2;

	//one pair
	if(has(freqV,2))
		return 1;
	return 0;
}

int findStrongestRank(std::string card){
	std::vector<int> cardList{
		'A',
		'K',
		'Q',
		'J',
		'T',
		'9',
		'8',
		'7',
		'6',
		'5',
		'4',
		'3',
		'2',
	};
	std::vector<size_t> Jpos;
	for(size_t i=0;i<5;i++){
		if(card[i]=='J')
			Jpos.push_back(i);
	}

	if(Jpos.size()==0)
		return rankHand(card);

	std::string strongest = card;
	std::function<void(std::vector<size_t>)> mangle= [&](std::vector<size_t> positions){
		auto elem=positions.back();
		positions.pop_back();
		for(auto c: cardList){
			card[elem]=c;
			if(rankHand(strongest)<rankHand(card))
				strongest=card;
			if(positions.size()>0)
				mangle(positions);
		}
	};
	mangle(Jpos);
	return rankHand(strongest);
}

int rankHand2(std::string card){
	//five of a kind  - 6
	//four of a kind  - 5
	//full house      - 4
	//three of a kind - 3
	//two pairs       - 2
	//one pair        - 1
	//high card       - 0
	std::map<char,int> freq;
	for(auto c:card)
		freq[c]++;
	std::vector<int> freqV;
	for(auto [c,f] : freq){
		freqV.push_back(f);
	}
	auto size=freqV.size();
	//five of a kind:
	if(size==1)
		return 6;

	if(size==2){
		//four of a kind:
		if(has(freqV,4))
			return 5;

		//full house
		return 4;
	}
	//three of a kind
	if(has(freqV,3))
		return 3;

	//two pairs
	if(size==3)
		return 2;

	//one pair
	if(has(freqV,2))
		return 1;
	return 0;
}






bool compareHands(const hand& a, const hand& b){
	std::map<char,int> cardRanking{
		{'A',12},
		{'K',11},
		{'Q',10},
		{'J',9},
		{'T',8},
		{'9',7},
		{'8',6},
		{'7',5},
		{'6',4},
		{'5',3},
		{'4',2},
		{'3',1},
		{'2',0}
	};
	auto rankA = a.rank;
	auto rankB = b.rank;
	if(rankA!=rankB)
		return rankA<rankB;

	for(int i=0;i<5;i++){
		auto cA=cardRanking[a.cards[i]];
		auto cB=cardRanking[b.cards[i]];
		if(cA!=cB)
			return cA<cB;
	}
	return false;
}

bool compareHands2(const hand& a, const hand& b){
	std::map<char,int> cardRanking{
		{'A',12},
		{'K',11},
		{'Q',10},
		{'J',0},
		{'T',9},
		{'9',8},
		{'8',7},
		{'7',6},
		{'6',5},
		{'5',4},
		{'4',3},
		{'3',2},
		{'2',1}
	};
	auto rankA = a.rank;
	auto rankB = b.rank;
	if(rankA!=rankB)
		return rankA<rankB;

	for(int i=0;i<5;i++){
		auto cA=cardRanking[a.cards[i]];
		auto cB=cardRanking[b.cards[i]];
		if(cA!=cB)
			return cA<cB;
	}
	return false;
}




int main(){
	std::ifstream f{"in.txt"};
	std::string line;
	std::vector<hand> game, game2;
	std::vector<hand> gameJokers;
	while(std::getline(f,line)){
		std::stringstream ss{line};
		std::string card;
		int bet;
		ss>>card>>bet;
		auto realRank = rankHand(card);
		auto strongestRank = findStrongestRank(card);
		game.push_back({card,bet,realRank});
		game2.push_back({card,bet,strongestRank});
		//gameJokers.push_back({findStrongest(card),bet});
	}
	std::ranges::sort(game,compareHands);
	std::ranges::sort(game2,compareHands2);
	int totlalWin=0;
	int rank=1;
	for(auto g : game){
		totlalWin+=g.bet*rank;
		rank++;
	}
	std::cout<<totlalWin<<std::endl;
	rank=1;
	totlalWin=0;
	for(auto g : game2){
		totlalWin+=g.bet*rank;
		rank++;
	}
	std::cout<<totlalWin<<std::endl;
}