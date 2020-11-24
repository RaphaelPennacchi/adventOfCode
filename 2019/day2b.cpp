#include <iostream>
#include <vector>
#include <cstdlib>

int memory(std::vector <int> vetor, int noun, int verb){
    vetor[1] = noun;
    vetor[2] = verb;
    int halt = 0;
    for(int entry = 0; entry < vetor.size() && !halt; entry += 4){
        switch (vetor[entry]){
            case 1:
                vetor[vetor[entry+3]] = vetor[vetor[entry + 1]] + vetor[vetor[entry + 2]];
                break;
            case 2:
                vetor[vetor[entry+3]] = vetor[vetor[entry + 1]] * vetor[vetor[entry + 2]];
                break;
            case 99:
                halt = 1;
                break;
            default:
                std::cout << "Failed" << " " << entry << " " << vetor.size() << std::endl;
                break;
        }
    }

    return vetor[0];
}

int main(int argc, char *argv[]){
    std::vector<int> vetor; 
    int entry, i, j;
    char comma;
    while(std::cin >> entry >> comma){
        vetor.push_back(entry);
    }
    vetor.push_back(entry);

    for(i = 0; i < 100; i++){
        for(j = 0; j < 100; j++){
            if(memory(vetor, i, j) == 19690720){
                std::cout << i * 100 + j << std::endl;
                break;
            }
        }
    }

    return 0;
}
