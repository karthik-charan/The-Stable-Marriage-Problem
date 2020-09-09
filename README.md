# The-Stable-Marriage-Problem

The Stable marriage prolem is one of the most important problem when it comes to algorithms, but often the solution on the internet seems to be quite confusing. Hence I decided to pulish my own version of solving the problem which I find relatively easy to understand. Feel free to use this to schedule your next blind date within your friends circle :p, or to assign the issues to developers within your organisation according to their preference so that everyone gets to enjoy their work!

###Problem:
The stable marriage problem is defined as follows:
Suppose you have N men and N women, and each person has ranked their prospective opposite-sex partners in order of preference.
For example, if N = 3, the input could be something like this:

guy_preferences = { 'andrew': ['caroline', 'abigail', 'betty'], 
                    'bill': ['caroline', 'betty', 'abigail'], 
                    'chester': ['betty', 'caroline', 'abigail'], } 
                    
gal_preferences = { 'abigail': ['andrew', 'bill', 'chester'], 
                    'betty': ['bill', 'andrew', 'chester'], 
                    'caroline': ['bill', 'chester', 'andrew'] }

Write an algorithm that pairs the men and women together in such a way that no two people of opposite sex would both rather be with each other than with their current partners.
