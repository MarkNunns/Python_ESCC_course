These are technical problems that have arisen during the course.

issue:     none of the code cells runs, I am prompted to select kernel
solution:  go to Extensions on RHS, go to Jupyter extension, select "switch to Pre-release version"
source:    https://github.com/microsoft/vscode-jupyter/issues/10043
           William's suggestion was to uninstall & reinstall the Jupyter extension.

issue:     Dataframe functions don't run
solution:  during your current session, have you run any code cells that define pd (i.e. "import pandas as pd")
           if not, you need to do that or any pd related tasks will fail

example of In & Out in Python code
In [5]: list(set(temp1) - set(temp2))
Out[5]: ['Four', 'Three']
That's not python code, its how IPython shows line codes, in this case is your line 5.
In[5] is your input and Out[5] is the result of that input.

issue:      reading a csv file from a web location.
            the filepath provided was:
        filename = 'https://raw.githubusercontent.com/data-to-insight/ERN-sessions/main/data/1980 2023 average house prices.csv'
            This did not work in the Python code.
Solution:   Paste the filepath into Edge.
            In Edge, the above filepath is converted automatically to:
            filename = 'https://raw.githubusercontent.com/data-to-insight/ERN-sessions/main/data/1980%202023%20average%20house%20prices.csv'
            If you copy this filepath from Edge, it DOES WORK in your Python code.

issue:      reading a csv file from a directory location.
Solution:   use GitHub Desktop - this can't be done on GitHub web version.

issue:      'Run All' button in GitHub does not run all the code on the page.
Solution:   I think patience is neeed here, don't press this button while the code is still loading up.
            If needed press the Run All button again after a minute, or if you run code sections that show errors, having previously worked OK.

issue:      how do I back up my cloud code to my PC?
Solution:   easy if using GitHub Desktop
            see MN Notes on GitHub backups, saved here:     D:\Mark\work\04 ESCC\a training\2024 Python\backups\