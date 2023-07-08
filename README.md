# python-image-process-exercise

## sphere_on_sphere.ipynb

The purpose of this code is to calculate and store various geometric properties related to the interaction between small particles and larger particles.

The code calculates the following properties for each small particle:

1. Relative positions (`rcxSmall`, `rcySmall`, `rczSmall`):
   - `rcxSmall`: The X-coordinate of the small particle relative to the center of the large particle.
   - `rcySmall`: The Y-coordinate of the small particle relative to the center of the large particle.
   - `rczSmall`: The Z-coordinate of the small particle relative to the center of the large particle.

2. Contact point coordinates (`rcxTouch`, `rcyTouch`, `rczTouch`):
   - `rcxTouch`: The X-coordinate of the point where the small particle touches the surface of the large particle.
   - `rcyTouch`: The Y-coordinate of the point where the small particle touches the surface of the large particle.
   - `rczTouch`: The Z-coordinate of the point where the small particle touches the surface of the large particle.

3. Angles (`phi`, `theta`):
   - `phi`: The angle between the line connecting the centers of the large and small particles and the Y-axis.
   - `theta`: The angle between the line connecting the centers of the large and small particles and the X-Z plane.

These calculated properties are then stored in the `smallParticlesJson` dictionary for each small particle, with additional keys `"rPointTouching"`, `"rPointCenter"`, `"phi"`, and `"theta"`.

Finally, the updated `smallParticlesJson` dictionary is converted to a JSON string using `json.dumps` and printed.

## Python Naming Conventions

1. Variables and Function Names:
   - Use lowercase letters and words separated by underscores.
   - Example: `my_variable`, `calculate_area()`

2. Class Names:
   - Use CamelCase style, starting with an uppercase letter.
   - Example: `MyClass`, `CircleShape`

3. Constants:
   - Use uppercase letters and underscores to separate words.
   - Example: `MAX_SIZE`, `PI`

4. Module Names:
   - Use lowercase letters and words separated by underscores.
   - Example: `my_module.py`, `data_operations.py`

5. Method Names:
   - Use lowercase letters and words separated by underscores.
   - Example: `calculate_area()`, `get_data()`

6. Private Instance Variables and Methods:
   - Use a single leading underscore to indicate that it is intended for internal use within the class.
   - Example: `_my_variable`, `_internal_method()`

7. Protected Instance Variables and Methods:
   - Use a single leading underscore to indicate that it is intended for internal use within the class and its subclasses.
   - Example: `_protected_variable`, `_protected_method()`

8. Inheritance:
   - When subclassing, use CamelCase style for the subclass name.
   - Example: `class MySubClass(MySuperClass)`

Remember that following these naming conventions improves code readability and consistency, making it easier for others to understand and collaborate on your code.
