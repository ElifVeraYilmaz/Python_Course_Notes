'''
             !!! Lessons Learned !!!

Learning Experience: 
Dealing with __pycache__

The Discovery:
While working with local modules, I noticed an auto generated folder named __pycache__ appearing in my directory.

The Technical Insight:
I learned that this isn't just "garbage." Python creates this folder to store compiled bytecode (.pyc files). By doing this, Python doesn't have to re-translate the source code every time I run the program, making the import process much faster.

The Professional Solution:
While useful for local performance, pushing these files to GitHub is considered poor practice since they are platform-dependent and clutter the repository.

Action taken: 
I created a .gitignore file and added __pycache__/ to it.

Result: My repository stays clean, professional, and focused only on the source code.

'''