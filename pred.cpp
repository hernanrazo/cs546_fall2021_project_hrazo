#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <iostream>

// function prototype
int predict(double features[4]) {

	int classes[3];

	if (features[2] <= 2095136.5) {
		if (features[2] <= 32.5) {
			classes[0] = 0; 
			classes[1] = 103; 
			classes[2] = 1601; 
		} else {
			classes[0] = 0; 
			classes[1] = 5412; 
			classes[2] = 3978; 
		}
	} else {
		if (features[1] <= 2171703.0) {
			classes[0] = 5480; 
			classes[1] = 8; 
			classes[2] = 0; 
		} else {
			classes[0] = 914; 
			classes[1] = 862; 
			classes[2] = 842; 
		}
	}

	int index = 0;
	for (int i = 0; i < 3; i++) {
		index = classes[i] > classes[index] ? i : index;
	}
	return index;
}

int main(int argc, char *argv[]) {

	// get features from command line arg
	double features[argc-1];

	for (int i = 1; i < argc; i++) {
		features[i-1] = atof(argv[i]);
	}

	// print out prediction
	std::cout << predict(features) << std::endl;
	return 0;
}
