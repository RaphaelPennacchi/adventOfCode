#include <iostream>
#include <vector>
#include <cstdlib>

int main(int argc, char *argv[]){
    std::vector<int> vetor; 
    int entry;
    char comma;
    int halt = 0; 
    while(std::cin >> entry >> comma){
        vetor.push_back(entry);
    }
    vetor.push_back(entry);
    vetor[1] = 12;
    vetor[2] = 2;
    for(entry = 0; entry < vetor.size() && !halt; entry += 4){
        switch (vetor[entry]){
            case 1:
                vetor[vetor[entry+3]] = vetor[vetor[entry + 1]] + vetor[vetor[entry + 2]];
                break;
            case 2:
                vetor[vetor[entry+3]] = vetor[vetor[entry + 1]] * vetor[vetor[entry + 2]];
                break;
            case 99:
                std::cout << "Entrou no 99" << std::endl;
                halt = 1;
                break;
            default:
                std::cout << "Failed" << " " << entry << " " << vetor.size() << std::endl;
                break;
        }
    }

    std::cout << vetor[0] << std::endl;
    return 0;
}
