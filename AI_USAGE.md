# AI Usage

## AI Tool Used

ChatGPT

## Purpose

I used ChatGPT mainly as a learning and support tool during the assignment.

I used it to:
- Understand the assignment requirements
- Clarify Django concepts and project structure
- Understand errors and debugging approaches
- Get guidance while writing test cases
- Review my implementation and understand possible improvements

I did not rely on AI to independently build or complete the entire assignment.

## Prompts Used

Some examples of the prompts I used were:

1. "Can you explain the assignment requirements and suggest a step-by-step approach to implement it in Django?"

2. "I am getting this Django error. Can you explain what is causing it and how I can fix it?"

3. "Can you explain how I should write test cases for the box selection logic?"

4. "Can you help me understand this test error and identify what I need to correct?"

5. "Can you review this implementation and explain if the logic matches the assignment requirements?"

## Accepted Output

I mainly used the explanations and suggestions that helped me understand:

- Django project and app structure
- Product and Box model requirements
- Box selection logic
- Django testing concepts
- Debugging errors during development

I reviewed the suggestions and verified the implementation myself before using them.

## Rejected / Modified Output

I did not use every suggestion directly.

Some parts were modified according to my actual project structure and requirements. 
For example, I changed app names, file paths and parts of the implementation when they did not match my project.

## Mistakes Identified

During development, I found and corrected a few issues while testing:

- The URL configuration initially referenced the wrong Django app name.
- The home view initially did not return a response for a normal GET request.
- An assignment operator typo in the test setup caused a test error.
- I initially had only two automated tests and then added additional test cases to cover more scenarios.

## Verification

I verified the final implementation by:

- Running the Django development server
- Testing the application manually with different products and boxes
- Checking cases where no suitable box was available
- Checking weight capacity validation
- Running Django automated tests using `python manage.py test`
- Verifying that the tests completed successfully