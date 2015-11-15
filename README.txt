Cauldron is a simple password generator inspired by the idea of mental password cryptograpy
created by Manuel Blum.

To use Blum's method you must memorize two things: a random mapping of letters to digits,
and a random permutation of the digits 0 through 9. The random map and the random permutation
are your personal keys so you must keep them secret. They must be truly random — any pattern
that makes them easier to memorize may make your system easier to break — and that's why this
up-front memorization is hard. But it only has to be done once.

Call your mapping of letters to digits f. You might have, for example, f(a) = 8, f(b) = 3,
f(c) = 7, etc. Since there are more letters than digits, some letters will be mapped to
the same digit.

Let g be the function that sends each digit to the next one in your permutation. So if your
permutation was 0298736514 then g(0) = 2, g(2) = 9, g(9) = 8, etc.

Now here is how you use the method to generate passwords.

1. Convert the name of your account to a sequence of n letters.

2. Turn this sequence of letters into a sequence of digits using your map f.
   Call this sequence of digits a0,a1,a2..an.

3. Compute b1, the first digit of your password, by adding a1 and an, taking the last digit,
   and applying the permutation g. In symbols, b1 = g( (a1 + an) mod 10 ).

4. Compute the subsequent digits by bj = g( (bj-1 + aj) mod 10 ).

So if your account name converts to "abc" in step 1, this becomes 837 in step 2. The first digit
of your password would be 1 because the first and last digits of 837 add to 15, and g(5) = 1.
The second digit would be 0 because the previously computed password digit, 1, and the second
digit of 837 add to 4 and g(4) = 0. The third digit would be 3 because 0+7 = 7 and g(7) = 3.
Thus your password would be 103.

