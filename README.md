# Nested Square Python Generator

![image](https://github.com/YoYoFreakCJ/C4D-NestedSquarePythonGenerator/assets/59722190/90f18634-b877-48ff-a2e6-e0d48cfca000)

## tldr
Creates a nested square which is good for making Discs with quads instead of triangles.

## How To Use
Take the code from the NestedSquarePythonGenerator.py file and paste it into a Python Generator. Either:

a. Create a new User Data on the Python Generator for the radius (make sure it gets the ID 1),

_or_

b. Change the line where the radius is defined to your desired hard coded radius.

I suggest creating the user data, then saving the python generator as an asset to your asset database. You can use the provided NestedSquareIcon.png if you wish.

![chrome_uwBNKjNOJF](https://github.com/YoYoFreakCJ/C4D-NestedSquarePythonGenerator/assets/59722190/b0a98934-81c6-4b75-9b86-f87a4e4f3628)

## What This Solves

Take this example:

I created a Disc, added a Displacer deformer with a noise, and put the Disc in a Subdivision Surface. Take a look at the center:

![image](https://github.com/YoYoFreakCJ/C4D-NestedSquarePythonGenerator/assets/59722190/d77e5f32-2e13-43e5-8842-81410b5a3a47)
![image](https://github.com/YoYoFreakCJ/C4D-NestedSquarePythonGenerator/assets/59722190/2ad4233d-ab89-4ca1-8da3-0901f3644a07)

To solve these weird subdivisions you need quads. You could easily create this geometry by yourself but since I like to keep things parametric I came up with this easy solution. Take a look:

![image](https://github.com/YoYoFreakCJ/C4D-NestedSquarePythonGenerator/assets/59722190/ed5b4455-4dfb-403b-92b1-3b96ff17b157)
![image](https://github.com/YoYoFreakCJ/C4D-NestedSquarePythonGenerator/assets/59722190/989033c4-bbc6-4c71-bd9d-531f37abfd3a)

Note that the object is Z- oriented.

# Disclaimer

This code is provided as-is. I do not take any responsibility for any harm this may cause. You may use this code however you see fit except selling it.
Let's be real, this is literally 46 lines of code.
