#include <stdio.h>
#include <string.h>

void ClearLineFromReadBuffer(void);
void print2dArr(int colLen, int rowLen, int arr[colLen][rowLen], int space);
void BFS(int colLen, int rowLen, int arr[colLen][rowLen]);

int main(void)
{
	
	int height, width;
	scanf("%d %d", &height, &width);
	ClearLineFromReadBuffer();
	
	int maze[height][width];
	char tempRow[width+1];
	for(int i=0; i<height; i++)
	{
		fgets(tempRow, sizeof(tempRow), stdin);
		ClearLineFromReadBuffer();
		
		// available cell = 0
		// unavailable cell = -1 
		for(int j=0; j<width; j++)
			maze[i][j] = tempRow[j]-'0'-1;
	}
	
	maze[0][0] = 1;
	BFS(height, width, maze);
	
	printf("%d", maze[height-1][width-1]);
	
//	printf("\n");
//	print2dArr(height, width, maze, 2);

	return 0;
}

void ClearLineFromReadBuffer(void)
{
	while(getchar() != '\n');
}

/*
	print 2 dimension array

    it's for debug.
*/
void print2dArr(int colLen, int rowLen, int arr[colLen][rowLen], int space)
{
	for(int i=0; i<colLen; i++)
	{
		for(int j=0; j<rowLen; j++)
		{
			printf("%*d ", space, arr[i][j]);
		}
		printf("\n");
	}
}

void BFS(int colLen, int rowLen, int arr[colLen][rowLen])
{
	int dx[4] = {-1, 0, 1, 0};
	int dy[4] = {0, -1, 0, 1};
	
	int queue[colLen*rowLen][2];
	memset(queue, -1, sizeof(queue));
	
	queue[0][0] = 0;
	queue[0][1] = 0;
	int topOfQueue = 0;
	
	for(int i=0; i <= topOfQueue; i++)
	{
		int currentX = queue[i][0];
		int currentY = queue[i][1];
		
		for(int j=0; j<4; j++)
		{
			int neighborX = currentX + dx[j];
			int neighborY = currentY + dy[j];
			if((((neighborX >= 0) && (neighborX <= rowLen-1)) && ((neighborY >= 0) && (neighborY <= colLen-1))) && (arr[neighborY][neighborX] == 0))
			{
				arr[neighborY][neighborX] = arr[currentY][currentX] + 1;
				
				if((neighborX == rowLen-1) && (neighborY == colLen-1)) return;
				
				topOfQueue++;
				queue[topOfQueue][0] = neighborX;
				queue[topOfQueue][1] = neighborY;
			}
		}
	}
	
	return;
}
