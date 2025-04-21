# Stock API Sorter

## Project Description

By applying web scraping techniques and parsing HTML documentation from Coursicle usign the BeautifulSoup4 library, a list of all professors who previously taught a given class was efficiently retrieved. Each entry includes the professor's name, a direct link to their profile, and their rating (if available), enabling quick access to relevant course data. This streamlined approach allows for fast and organized collection of instructor information.
***    

## Potential Info

![image](https://github.com/user-attachments/assets/eeee9b19-54d5-42bc-8e00-976d3a811edc)

## How to Use

1. Open your preferred code editor and navigate to the "Coursicle\coursicle>" directory
2. Activate the virtual environment by running: venv/scripts/activate
3. Install the required libraries by running: pip install -r requirements.txt
4. Run grabing: py grabing.py
5. Enter course name (abbreviated) and course number

## Bugs / Warnings

The default is set to Binghamton University, so you can change it if you'd like. Also, use the appropriate course name and number as it uses a url to pull the information, meaning a non-existent url will result in an error. You cannot repeatedly use this as coursicle has a captcha set up, which my program isn't designed to bypass. Repeatedly doing this may bypass Coursicle's Terms of Service, so I advice not to do this. Consider the ethics before you continue. 
