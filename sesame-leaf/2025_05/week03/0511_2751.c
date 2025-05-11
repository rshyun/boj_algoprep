#include <stdio.h>

typedef struct 
{
	int * heapArray;
	int nodeCount; 
} Heap;

void MinHeapAdd(Heap * inputHeap, int data);
void MinHeapDelete(Heap * inputHeap);

int main(void)
{
	int N;
	scanf("%d", &N);
	
	int inputData[N];
	Heap heap;
	heap.heapArray = inputData;
	heap.nodeCount = 0;
	
	for(int i=0; i<N; i++)
	{
		scanf("%d", &inputData[i]);
		MinHeapAdd(&heap, inputData[i]);
	}
	
	for(int i=0; i<N; i++)
	{
		printf("%d\n", heap.heapArray[0]);
		MinHeapDelete(&heap);
	}
	
	return 0;
}

void MinHeapAdd(Heap * inputHeap, int data)
{
	(inputHeap->nodeCount)++;
	inputHeap->heapArray[(inputHeap->nodeCount)-1] = data;
	
	int childNodeIdx = inputHeap->nodeCount;
	int parentNodeIdx = childNodeIdx/2;
	int * childValue;
	int * parentValue;
	while(childNodeIdx != 1)
	{
		childValue = &(inputHeap->heapArray[childNodeIdx-1]);
		parentValue = &(inputHeap->heapArray[parentNodeIdx-1]);
		
		if(*childValue >= *parentValue) return;
		
		int temp = *childValue;
		*childValue = *parentValue;
		*parentValue = temp;
		
		childNodeIdx /= 2;
		parentNodeIdx /= 2;
	}
}

void MinHeapDelete(Heap * inputHeap)
{
	inputHeap->heapArray[0] = inputHeap->heapArray[(inputHeap->nodeCount)-1];
	(inputHeap->nodeCount)--;
	
	int parentNodeIdx = 1;
	int child1_NodeIdx = parentNodeIdx * 2;
	int child2_NodeIdx = (parentNodeIdx * 2) + 1;
	int smallerChildNodeIdx;
	int * parentValue;
	int * child1_Value;
	int * child2_Value;
	int * smallerChildValue;
	while(child1_NodeIdx <= (inputHeap->nodeCount))
	{
		parentValue = &(inputHeap->heapArray[parentNodeIdx-1]);
		child1_Value = &(inputHeap->heapArray[child1_NodeIdx-1]);
		child2_Value = &(inputHeap->heapArray[child2_NodeIdx-1]);
		
		if(child2_NodeIdx > inputHeap->nodeCount)
		{
			smallerChildValue = child1_Value;
			smallerChildNodeIdx = child1_NodeIdx;
		}
		else
		{
			smallerChildValue = (*child1_Value < *child2_Value) ? (child1_Value) : (child2_Value);
			smallerChildNodeIdx = (*child1_Value < *child2_Value) ? (child1_NodeIdx) : (child2_NodeIdx);
		}
		
		if(*smallerChildValue >= *parentValue) return;
		
		int temp = *smallerChildValue;
		*smallerChildValue = *parentValue;
		*parentValue = temp;
		
		parentNodeIdx = smallerChildNodeIdx;
		child1_NodeIdx = parentNodeIdx * 2;
		child2_NodeIdx = (parentNodeIdx * 2) + 1;
	}
}
