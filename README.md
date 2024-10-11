****Solving the General Quintic Equation - An Ultraradical Animation by John Michael Kerr****

***Progress to date***

The first stage in solving the _General_ (monic, univariate) quintic,

    y = x^5 + ax^4 + bx^3 + cx^2 + dx + e = 0,
    
is to eliminate the quartic (_x^4_) term.
The code in "scene.py" uses animated algebra _(see video)_ to illustrate how this is done using a linear Tschirnhaus Transformation 
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

Note how the elimination of original coefficient _a_ in favour of _h_ yields expressions devoid of the usual ugly powers-of-five denominators!

***To Do***

- Create similar videos covering
    - reduction to _Principal_ form (no cubic term),
    - reduction to _Bring-Jerrard_ form (no quadratic term),
    - the final five solutions, expressed using _ultraradical_ notation.
- Design a LaTeX symbol for the _Bring Radical_ (aka the _ultraradical_).
- Record voiceovers, and adjust video pauses to sync with these explanations.

***References***

Video: 

Polynomial Transformations of Tschirnhaus, Bring and Jerrard: https://www.uwo.ca/apmaths/faculty/jeffrey/pdfs/Adamchik.pdf
