# Probabilistic CYK algorithm

This is an implementation of a probabilistic version of the CYK algorithm


S
|--VP
|  |--NP
|  |  |--Nom
|  |  |  |--PP
|  |  |  |  |--NP
|  |  |  |  |  |--Pro
|  |  |  |  |     |--denver
|  |  |  |  |--P
|  |  |  |     |--through
|  |  |  |--Nom
|  |  |     |--Noun
|  |  |     |  |--flight
|  |  |     |--Nom
|  |  |        |--Noun
|  |  |           |--morning
|  |  |--Det
|  |     |--the
|  |--Verb
|     |--prefer
|--NP
   |--Pro
      |--i

Best parse tree found:
S (6.491120624999999e-05)
|--VP (0.0007868025)
|  |--NP (0.0007868025)
|  |  |--Nom (0.0015736050000000003)
|  |  |  |--PP (0.17)
|  |  |  |  |--NP (0.17)
|  |  |  |  |  |--Pro (0.3400000000000001)
|  |  |  |  |     |--denver (1.0)
|  |  |  |  |--P (1.0)
|  |  |  |     |--through (1.0)
|  |  |  |--Nom (0.028050000000000002)
|  |  |     |--Noun (0.5)
|  |  |     |  |--flight (1.0)
|  |  |     |--Nom (0.17)
|  |  |        |--Noun (0.5)
|  |  |           |--morning (1.0)
|  |  |--Det (1.0)
|  |     |--the (1.0)
|  |--Verb (1.0)
|     |--prefer (1.0)
|--NP (0.16499999999999998)
   |--Pro (0.33)
      |--i (1.0)
