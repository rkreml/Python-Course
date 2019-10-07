## Name: Robert Kreml
## Date: October 1, 2019
## Class: EPSY 5200

## Exercise 26 from LP3TH by Zed Shaw

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# The following define was missing a colon at the end of line 17. Also, was missing parenthesis around word on line 20. Fixed spelling on pop.
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)

# the following define was missing brackets on line 25 around -1 and an ending paranthesis. Also, needed parenthesis around word on line 26.
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop([-1])
    print (word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# The following line needed parenthesis around the printed quotes.
print ("Let's practice everything.")

# The following line needed parenthesis around the printed quotes.
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

# The three following prints needed parentheses around each of the lines.
print ("--------------")
print (poem)
print ("--------------")

# The following line did not end up with 5, so changed the equation to end up with 5.
five = 10 - 5
# The following line was missing a formatted print line and needed to recall the variable 'five'.
print (f"This should be five: %s" % {five})

# The tabing needed to be fixed and there was a backwards / so it was not able to divide on line 73. Made jelly_beans to be beans
def secret_formula(started):
    beans = started * 500
    jars = beans / 1000
    crates = jars / 100
    return beans, jars, crates

# Fixed underscore between 'start' and 'point' also deleted the second = in the equation below.
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# Print functions were missing parentheses and needed to have formatted print lines. Made beans, jars, and crates into 'secret_formula'
print (f"With a starting point of: %d" % {start_point})
print (f"We'd have %d jeans, %d jars, and %d crates." % {secret_formula})

start_point = start_point / 10

# Print functions needed parenthesis. Also, line 89 needed two ending parenthesis. Fixed spelling on 'point'.
print ("We can also do that this way:")
print (f"We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

# Removed 'ex25' from variable names.
words = break_words(sentence)
sorted_words = sort_words(words)

# Removed the period on line 100. needed a t in print on line 103 and needed parenthesis around the variable. Removed 'ex25'.
print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print (sorted_words)

# Fixed 'first' spelling.
print_first_and_last(sentence)

# Removed unneeded tab on line 108. Fixed spelling on sentence. Fixed 'and' in function name.
print_first_and_last_sorted(sentence)

## Study Drills
# 1) Commented on mistakes and fixes throughout.

## Mistakes
# 1) I missed the == on line 79 and that stumped me for a bit.