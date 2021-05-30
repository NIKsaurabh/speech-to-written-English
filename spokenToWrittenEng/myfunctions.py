#function to combine single abbriviated texts
"""
Working of this function:
First find single element in the string and store it's index number.
From that index search whether more single texts are present after that and is alphabet, if yes
iterate througn all of them and store index of last iterated element. 
Now we have start and end point, then join the element from start to end end index of the list
and return the list.
"""
def combine_single_elements(lst):
    i = 0
    while i<len(lst):
        if (lst[i].isalpha() and len(lst[i]) == 1):
            start = i
            end = i
            while (i<len(lst) and len(lst[i]) == 1 and lst[i].isalpha()):
                end = i
                i+=1
            lst[start:end+1] = [''.join(lst[start:end+1])]
            i = start+1
        else:
            i+=1      
    return lst

#function to handle currency sign in the text
"""
Working of this function:
Iterare through each element of the list, if 'dollar' or 'dollars' string is present them 
change it to '$', if there is a digit before the dollar them join them and return the text.
"""
def currency(lst):
    i = 0
    while i<len(lst):
        if (lst[i].lower() == 'dollar' or lst[i].lower() == 'dollars') and i>0:
            lst[i] = '$'
            if lst[i-1].isdigit():
                lst[i-1 : i+1] = [''.join(lst[i-1 : i+1])] 
        else:
            i+=1
    return lst

#function to handle n_tuple type texts in the string
"""
Working of this function:
Iterate through the list and search for n_tuple type text in the string, if found then change it
to digit and multiply it with text present after that and return the list.
"""
def n_tuple(lst):
    n_tpl = {'single':1,'double':2,'triple':3,'quadruple':4}
    i=0
    while i<len(lst):
        if lst[i].lower() in n_tpl and len(lst)>=i+1 and len(lst[i+1]) == 1:
            lst[i:i+2] = [n_tpl[lst[i]] * lst[i+1]]
        else:
            i+=1
    return(lst)

#This function will return final text after processing
def spoken_to_written(text):
    units = {
        "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
        "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
        "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
      }
    #splitting each words of the text seperated with space and storing them in a list
    lst = text.split()

    for i in range(len(lst)):    #If digits present in the form of words, change them to number
        if lst[i] in units:
            lst[i] = str(units[lst[i]])

    n_lst = combine_single_elements(lst)    #calling combine_single_elements function
    n_lst = currency(n_lst)                 #calling currency function
    n_lst = n_tuple(n_lst)                  #calling n_tuple function
    
    return ' '.join(n_lst)    #returning processed string
