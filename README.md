# Mini Project: Data Mining - Scraping/Extracting Information from Files

This mini project focuses on extracting specific information from files using regular expressions. It demonstrates the usage of regular expressions in data mining and the benefits they offer in data science projects. The code follows a waterfall method and employs various libraries for file handling and regex operations.

## Code Description

The code in this project performs the following tasks:

1. Sort names that end with a dot and extract them into a new file.
2. Sort numbers by their company key numbers and extract them into a new file.
3. Sort and collect emails and extract them into a new file.
4. Count occurrences of various elements in the data.
5. Handle the current working directory automatically.

## Libraries Used

The code utilizes the following libraries:

- `random`: Used for generating a random phone number.
- `re` (regular expression): Used for pattern matching and extracting information from the data file.
- `os`: Used for handling file operations and managing the current working directory.

## Benefits of Regular Expressions in Data Science

Regular expressions provide powerful pattern matching capabilities, making them valuable in data science tasks. Some benefits of using regular expressions include:

- Efficiently searching and extracting specific patterns from text data.
- Simplifying complex string manipulations and data extraction tasks.
- Enabling flexible and customizable data cleaning and preprocessing.
- Facilitating feature extraction from unstructured text data.

## Code Structure

The code follows a waterfall method, where each step is sequentially executed and the results are processed accordingly. The steps involved are as follows:
1. Reading the input file and loading its content.
2. Applying regular expressions to extract specific patterns (names, numbers, emails) from the file.
3. Sorting and organizing the extracted data.
4. Writing the sorted data into separate output files.
5. Counting and displaying the results.

## Difference between Waterfall Method and Functions Coding Methods

The waterfall method, as demonstrated in this code, involves a step-by-step sequential execution of tasks. Each task is performed in a specific order, and the output of one task becomes the input for the next. This method is suitable for linear workflows and when the order of operations matters.

On the other hand, functions coding methods involve organizing the code into reusable functions. Each function performs a specific task, and they can be called and combined as needed. Functions coding methods offer modularity, code reusability, and flexibility for complex projects with multiple interdependent components.

Please note that the code can be further optimized and improved based on specific requirements.

## Author

This mini project was developed by Ahmed Rifai.
