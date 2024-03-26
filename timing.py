#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

void bubble(int *array);
void merge(int *left_array, int *right_array, int *array, int left_length, int right_length);
void merge_sort(int *array, int length);
void print_array(int *array);
void refresh_array_order(int *array);
void selection(int *array);

const int LENGTH = 20;

int main()
{

    // Populate array
    int data[LENGTH];
    refresh_array_order(data);

    // Bubble Algorithm
    printf("Bubble sorting algorithm:\n");
    printf("Pre sort: ");
    print_array(data);
    bubble(data);
    printf("Post sort: ");
    print_array(data);
    printf("\n");

    refresh_array_order(data);

    // Selection Algorithm
    printf("Selection sorting algorithm:\n");
    printf("Pre sort: ");
    print_array(data);
    selection(data);
    printf("Post sort: ");
    print_array(data);
    printf("\n");

    refresh_array_order(data);

    // Merge sort    
    printf("Merge sort algorithm:\n");
    printf("Pre sort: ");
    print_array(data);
    merge_sort(data, LENGTH);
    printf("Post sort: ");
    print_array(data);
    printf("\n");
}

void refresh_array_order(int *array)
// Sets the array values from LENGTH to 1
{
    for (int i = 0; i < LENGTH; i++)
    {
        array[i] = LENGTH - i;
    }
}

void selection(int *array)
// The selection array
{
    // Select 'I' number in the array starting from the start
    for (int i = 0; i < LENGTH; i++)
    {
        int smallest_index = i;
        // Iterate over all items at I + 1 and find the lowest value in the pool.
        for (int j = i + 1; j < LENGTH; j++)
        {
            if (array[j] < array[i])
            {
                smallest_index = j;
            }
        }
        // Swap the smallest and array i
        if (smallest_index != i)
        {
            int smallest_value = array[smallest_index];
            int current_i_value = array[i];

            array[i] = smallest_value;
            array[smallest_index] = current_i_value;
        }
    }
}

void bubble(int *array)
// Bubble sort algorithm
{
    // Check if the current selected int at J is larger than the next int. If so swap places.
    for (int i = 0; i < LENGTH; i++)
    {
        bool swap = false;

        for (int j = 0; j < LENGTH - 1; j++)
        {
            int current_number = array[j];
            int next_number = array[j + 1];

            if (current_number > next_number)
            {
                array[j] = next_number;
                array[j + 1] = current_number;
                swap = true;
            }
        }
        if (!swap)
        {
            break;
        }
    }
}

void merge_sort(int *array, int length)
{
    // Get the length of the current array we are working with
    int array_length = length;

    // Base case
    if (array_length <= 1)
    {
        return;
    }

    // Create 2 arrays for each half of the original array
    int middle_position = array_length / 2;
    int left_array[middle_position];
    int right_array[array_length - middle_position];

    // right array index
    int j = 0;

    // Populate arrays
    for (int i = 0; i < array_length; i++)
    {
        if (i < middle_position)
        {
            left_array[i] = array[i];
        }
        else
        {
            right_array[j] = array[i];
            j++;
        }
    }

    // Get the array lengths
    int left_array_length = sizeof(left_array) / sizeof(left_array[0]);
    int right_array_length = sizeof(right_array) / sizeof(right_array[0]);

    // Keep calling until we are at the base case.
    merge_sort(left_array, left_array_length);
    merge_sort(right_array, right_array_length);
    merge(left_array, right_array, array, left_array_length, right_array_length);
}

void merge(int *left_array, int *right_array, int *array, int left_length, int right_length)
{
    int i, l, r = 0;

    // Check the conditions for merging
    // While there are elements still in our arrays we will continue to add them to the original list
    while (l < left_length && r < right_length)
    {
        // If the element in our left array is smaller than the element in the right array add it to the original list
        if (left_array[l] < right_array[r])
        {
            array[i] = left_array[l];
            i++;
            l++;
        }
        // If the element in the right array is smaller add that to the original list
        else
        {
            array[i] = right_array[r];
            i++;
            r++;
        }
    }

    // If there are any left over elements that we can't compare add them to the array.
    while (l < left_length)
    {
        array[i] = left_array[l];
        i++;
        l++;
    }

    while (r < right_length)
    {
        array[i] = right_array[r];
        i++;
        r++;
    }
}

void print_array(int *array)
// Prints the array values for LENGTH items.
{
    for (int i = 0; i < LENGTH; i++)
    {
        printf("%i ", array[i]);
    }
    printf("\n");
}
