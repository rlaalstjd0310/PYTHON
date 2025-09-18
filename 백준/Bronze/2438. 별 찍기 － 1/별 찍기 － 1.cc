#include<stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int r;
	for (r = 2; r <= n+1;++r) {
		int k;
		for (k = 1; k < r; ++k) {
			printf("*");
			}
		printf("\n");
	}
}