# Abaqus: Path from Nodeset

Script to generate a path in postprocessing from predefined nodesets


How to:
- Define path location in preprocessing by defining the nodesets
- Specify setnames in script
- Run script in postprocessing to create path
- Validate created path


<br/>

Notes:
- Only one path is created by the script in each run
    - Creating multiple paths in one run might be a future enhancement
- A path can form a closed loop
    - Script asks if the first node shall be added also as last node into the path
    - Comment that portion of the script out if you generally don't need that
- Use the included example model to see what the nodeset might look like
    - Four predefined nodesets allow to test creating two different paths