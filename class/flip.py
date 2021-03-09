#!/usr/bin/env python
class Flip:
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
