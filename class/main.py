#!/usr/bin/env python
from flip import Flip

## array from the question
picture = [[80,80,255,80,80,255,80,80],
           [80,80,255,80,80,255,80,80],
           [255,80,120,120,120,120,255,80],
           [255,80,255,255,255,255,80,80],
           [255,80,120,120,120,120,80,80]]

## a non uniform array to show flip() can support array of variable length, even length being a odd number
non_uniform = [[0,1,0,2,3],
               [0,1,2,3,0,4,5,6,7],
               ["a","b","c","1","2","3"],
               ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]

## main call of the flip function
def main():
    print("paper example array")
    print(*picture,sep='\n')
    print()
    print(*Flip.flip(picture),sep='\n')
    print()

    print("custom non uniform array")
    print(*non_uniform,sep='\n')
    print()
    print(*Flip.flip(non_uniform),sep='\n')

if __name__ == "__main__":
    main()
