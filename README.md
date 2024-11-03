****Solving the General Quintic Equation - An Ultraradical Animation by John Michael Kerr****

***Progress to date***

The first stage in solving the _General_ (monic, univariate) quintic equation,

    y = x^5 + ax^4 + bx^3 + cx^2 + dx + e = 0,
    
is to eliminate the _quartic_ or _x^4_ term.
This code uses animated algebra _(see video)_ to illustrate how this is done using a linear Tschirnhaus Transformation 
_(see Adamchik et al)_, specifically this one:

    x = z + h.

This has the effect of reducing the quartic coefficient to zero when the particular value _-a/5_ is chosen for _h_.
The resulting equation has the so-called _Reduced_ form,

    y = z^5 + 0z^4 + pz^3 + qz^2 + rz + s,

and the following expressions for _p,q,r,s_ are found:

    p = b - 10h^2
    q = 3bh + c - 20h^3
    r = 3bh^2 + 2ch + d - 15h^4
    s = bh^3 + ch^2 + dh + e - 4h^5

***Notes***

The elimination of original coefficient _a_ in favour of _h_ yields expressions devoid of the usual ugly powers-of-five denominators!

This work is an extension of my original Google Slides deck:

https://docs.google.com/presentation/d/e/2PACX-1vTCx2Jhy_jxQD6LojP5uzsGuUnKFAMoMzgx-CM_BAVFJe_g3qNnz-YLOSz7S7xDEHUlu3_GBvADZB9v/pub?start=true&loop=false&delayms=1000

***To Do***

- Create similar videos covering
    - reduction to _Principal_ form (no cubic term),
    - reduction to _Bring-Jerrard_ form (no quadratic term),
    - the final five solutions, expressed using _ultraradical_ notation,
    - test cases ("Checkpoint" videos) for all of these steps,
- Design a LaTeX symbol for the _Bring Radical_ (aka the _ultraradical_).
- Record voiceovers, and adjust video pauses to sync with these explanations.

***References***

Video: please refer to the "results" folder for any mp3 file(s) mentioned above.

Polynomial Transformations of Tschirnhaus, Bring and Jerrard: https://www.uwo.ca/apmaths/faculty/jeffrey/pdfs/Adamchik.pdf
