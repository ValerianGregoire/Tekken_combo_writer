# Tekken_combo_writer
## Quick program to write and save combos for Tekken 7

### How I got the Idea
Learning combos in arcade fighting games may be tough, especially when they are kept in a dark .txt file that no one can decode.
I've been looking for a way to write my combos quickly while I trained, but couldn't find any website that allowed me to do it the way I would have liked to do it, which was a good reason for me to code an app that does the job.

### What's the point of this app ?
It's an efficient way to type custom combos and to save them on your computer.
Also, I used PIL (from pillow library), which was a first for me. Projects like those are a good way to discover new libraries.

### How do I type my combos ?
The rules are simple:
> Each sequence is separated from the others by a space

> The directions are: f (forward), b (backward), u (up), d(down). You can combine them by first inputing up or down then forward or backward (e.g., uf or db)

> Hold directions are written with capital letters

> Attack buttons are 1,2,3,4 and the combinations are expressed with a "+" (e.g., 1+3).

An input like this:
![image](https://user-images.githubusercontent.com/96045631/235797848-2591b8a8-0b2a-4eaf-82ba-fe01dcc3d69a.png)

Outputs this:
![image](https://user-images.githubusercontent.com/96045631/235797909-fedd7083-18ca-4876-bcdd-86584b208cc6.png)

#### The Display Text option is to display which input led to which icon if you'd rather use this notation

Also, you can save your combos in the combos folder of the project to have a quick access to the combos you want to train on. 
