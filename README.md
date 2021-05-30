# Library
spokenToWrittenEng folder contains all the files that are required to create the library.
## Python code  to create the library:
Path to code is **spokenToWrittenEng/spokenToWrittenEng/myfunctions.py** 
### Features implemented:
* It can convert abbreviated texts such as 'H T M L' to 'HTML'. These type of texts can be present any where in the sentence and any number of times.
* It can convert abbreviated texts such as 'triple A' to 'AAA'.
* It can handel currency related queries such as 'five dollars' to '5$'. (Only implemented for dollar).
* It can convert single digit written in words to number.
### Features to be implemented:
* Convert numbers written in words to digits such as 'twenty five' to '25'.
### Installation process of the library (Linux(Ubuntu)):
* Download wheel file (spokenToWrittenEng-0.1.0-py3-none-any.whl) present in 'spokenToWrittenEng/dist/' folder.
* Open terminal.
* Run 'pip install /path/to/spokenToWrittenEng-0.1.0-py3-none-any.whl' in terminal.
* Once installed import it using:<br>
    \> import spokenToWrittenEng<br>
    \> from spokenToWrittenEng import myfunctions
### Code:
**Code is present in 'spokenToWrittenEng/spokenToWrittenEng/myfunctions.py' path**

# REST API
REST API folder contains **'app.py' (contains code)** file.
I have used 'streamlit' to create this app.
### How to run this app (Linux(Ubuntu))
* Download app.py file from REST API folder.
* Open terminal and locate where app.py is present.
* Run "streamlit run app.py" on terminal.
* It will open a page in browser.
