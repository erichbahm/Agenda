# Coding Ideas

```
CODE IDEAS
Jan 10
0 + 10 = 10
Feb 12
31 + 12 = 43
etc.
```

```
CODE STEPS
0. Create the following Variables
  a) Current date (Str)
  b) Frontend md file name (Str)
  c) Backend md file names (Lst)
  d) Categories + Activities (OrderedDict)
  e) Categories + Goals (OrderedDict)
  f) COMPLETED Categories + Actions (OrderedDict)
1. Check and save current date (from datetime import date > date.today)
2. Check and save to a list the current markdown files (os.scandir)
3. Check for the frontend md file
- If none exists, create one and skip straight to step 5
4. Iterate through each line, determining which lines have completed activities/goals
- Save categories as keys, and actions as values
5. Iterate through the list doing the following:
  a) Open and read the document ('someFileName.md',)
  b) Iterate through the lines of the document:
    I. For each Category, create a key
    II. For each Activity that is between 0 & Current Date + 8, assign the entire line as a value to the most recent key
    - The Activity must not already be checked off
    - If the activity has a single * boundary (italics), paste it into the Goals Dict
    - If the Action matches one in the completed Action dictionary, remove mark it as done here, and do not add it to the other dictionary
    III. At the final line, stop the iteration
  c) Close the current document
6. Open the frontend md document to write to
7. Paste '## Activities'
8. Iterate through the activities dict and paste in each value in order, with the key as a footnote (some formatting may be required)
[COULD POSSIBLY ALSO INCLUDE THE TITLES OF THE DOCUMENT AS MARKERS]
9. Paste '## Goals'
10. Iterate through the goals dict and paste in each value in order, with the key as a footnote
11. Paste a legend at the bottom with all the footnotes with references to their documents or folders
[Needs to somehow be created and accessed beforehand]
12. Close the frontend md document
```

# Task Themes

```
ACTIVITIES/GOALS
Classes
- CHEM 1100
- PHYS 1200
- ENGR 2090
- MATH 2400
- ECON 2020
- ENGR 1300
FSAE
- Ergonomics
- Engine & Cooling
LTCP (Long term career planning)
- Degree Planning
- Job Search (Fairs, Handshake)
- Job Prep (Interviews, LinkedIn)
Skills
- Programming Languages (Python)
- CAD (NX, Solidworks, Certification)
Financial Aid
- Scholarships
- Accelerated Degree Program
Misc
- Cleaning up files (Hard Drive)
- Reorganizing Expenses Sheet
- Creating Python Sorter
```

# Formatting Ideas

```
TABLE
|First Header | Second Header| Second Header| Second Header| Second Header| Second Header| Second Header| Second Header|
|------------ | -------------| -------------| -------------| -------------| -------------| -------------| -------------|
|Content from cell 1 | Content from cell 2| Content from cell 2| Content from cell 2| Content from cell 2| Content from cell 2| Content from cell 2|
|Content in the first column | Content in the second column| Content in the second column| Content in the second column| Content in the second column| Content in the second column| Content in the second column|
```

```
FOOTNOTE
123 [^456]
[^456]:789
```

``` 
HORIZONTAL LINE
---
```

```
LINK
[123](https://...)
[123](C:\...)
[123](#456)
<www...>
```

- [ ] (MMM DD)[^ENGR 1300]Assignment 1
- [ ] (MMM DD)[^ENGR 1300]Assignment 2
- [ ] (MMM DD)[^ENGR 1300]**Assignment 3**
- [ ] (MMM DD) [^MATH 2400] *Goal 1*
- [ ] (MMM DD) [^Solidworks] *Goal 2*

# Possible Designs

1

![image-20220112184342035](C:\Users\Erich\AppData\Roaming\Typora\typora-user-images\image-20220112184342035.png)

2

![image-20220112184436543](C:\Users\Erich\AppData\Roaming\Typora\typora-user-images\image-20220112184436543.png)

3

![image-20220112184520628](C:\Users\Erich\AppData\Roaming\Typora\typora-user-images\image-20220112184520628.png)

