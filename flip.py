#!/usr/bin/env python

# Name: Mubashir Haroon
# Class: A1
# School: Musab School System


## array from the question
picture = [[80,80,255,80,80,255,80,80],
           [80,80,255,80,80,255,80,23],
           [255,80,120,120,120,120,255,80],
           [255,80,255,255,255,255,80,80],
           [255,80,120,120,120,120,80,80]]

## a non uniform array to show flip() can support array of variable length, even length being a odd number
non_uniform = [[0,1,0,2,3],
               [0,1,2,3,0,4,5,6,7],
               ["a","b","c","1","2","3"],
               ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]

## function which flips a 2D array, pass in the array and it will return the flipped version
def flip(array):
    ## total number of rows, no need to reduce by 1 for index correction as range() does it automatically
    max_rows = len(array)

    for row in range(max_rows):
        ## total number of columns with index corrected
        max_column = len(array[row]) - 1

        ## number of times loop shall run
        ## used // for integer division so even if there are odd number of columns, it gives integer value
        loop_max = len(array[row]) // 2

        for column in range(loop_max):
            ## don't swap if the value is same on both sides
            if array[row][column] != array[row][max_column]:
                ## python specific swap syntax, a,b=b,a
                array[row][column],array[row][max_column] = array[row][max_column],array[row][column]
            ## max_column reduced by 1
            max_column -= 1

    return array

## main call of the flip function
def main():
    print("paper example array")
    print(*picture,sep='\n')
    print()
    print(*flip(picture),sep='\n')
    print()

    print("custom non uniform array")
    print(*non_uniform,sep='\n')
    print()
    print(*flip(non_uniform),sep='\n')

if __name__ == "__main__":
    main()
