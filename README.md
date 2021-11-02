# crypto senior sem
### From cryptography to cryptocurrencies

This course is about the state-of-the-art in modern cryptography, which
finds application as the primary mathematical apparatus that has, of late, been
artfully fashioned into cryptocurrencies.  Cryptography is of course pervasive and
ubiquitous in the technological age, so that this course is ultimately about
certain cutting-edge information-theoretic advancements that are reshaping our
world.  In addition to crytographic primitives, their prevailing applications,
and underlying mathematics, topics include applications of zero-knowledge proofs
and their role in present-day FinTech.

Important: as far as speculating in cryptocurrencies, we think that you are likely
better off not doing so. Whether or not you take that advice, you might
do well to look under the hood of the new-fangled tech that is built atop a rather
striking assemblage of pure and applied Math and CS.

## Preliminaries

### Getting started

* First, install [polylib](https://github.com/sj-simmons/polylib),
* then install [numlib](https://github.com/sj-simmons/numlib),
* then read on.

### The integers modulo n

Let <img alt="$n\in\mathbb{Z}$" src="svgs/a3f3ee66a29182d90ff26e24025b8cc2.svg" valign=-0.6427030499999994px width="40.916955749999985pt" height="11.966898899999999pt"/> be a fixed positive integer. We say that integers <img alt="$x$" src="svgs/332cc365a4987aacce0ead01b8bdcc0b.svg" valign=0.0px width="9.39498779999999pt" height="7.0776222pt"/> and <img alt="$y$" src="svgs/deceeaf6940a8c7a5a02373728002b0f.svg" valign=-3.1963502999999895px width="8.649225749999989pt" height="10.2739725pt"/> are
*congruent* modulo <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> divides their difference, <img alt="$x-y;$" src="svgs/9f2c06cdc6a6490da6493c39ee7fff19.svg" valign=-3.19635195px width="42.70160894999999pt" height="12.785402849999999pt"/> and we write <img alt="$x\equiv y \mod n.$" src="svgs/302d8e8125e43f8920cd02f92872cb54.svg" valign=-3.1963503000000055px width="102.33983759999998pt" height="14.611878599999999pt"/>
For instance, <img alt="$17 \equiv 2 \mod 5.$" src="svgs/9c6a23824157e2ef6366d33b5b037282.svg" valign=0.0px width="107.30560499999999pt" height="11.4155283pt"/>

One can consider the
[ring](https://en.wikipedia.org/wiki/Ring_(mathematics)) of integers modulo <img alt="$n,$" src="svgs/85bc1f723bdc744666d4f2241b1031f7.svg" valign=-3.1963502999999895px width="14.433101099999991pt" height="10.2739725pt"/>
denoted <img alt="$\mathbb{Z}/n\mathbb{Z}$" src="svgs/94d333ba0aaa5e9c8ce88690986075c2.svg" valign=-4.109589000000009px width="40.00396784999999pt" height="16.438356pt"/> or, more succinctly, <img alt="$\mathbb{Z}/n.$" src="svgs/b2db6c8686053451d402312789bf8098.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>
Congruence modulo a given <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> defines an
[equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation)
on the integers and, as a set, <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> consists precisely of the resulting
equivalence classes.

An equivalence relation partitions a set into disjoint subsets. For instance, <img alt="$\mathbb{Z}/6$" src="svgs/34178db573bc75259b7edcfa36f7a3cc.svg" valign=-4.109589000000009px width="27.39735899999999pt" height="16.438356pt"/>
consists of 5 equivalence classes <img alt="$\{[0],[1],[2],[3],[4],[5]\}$" src="svgs/894c828a46f3ad0f1232271f1d216c12.svg" valign=-4.109589000000009px width="157.0777791pt" height="16.438356pt"/> where, for example,

<p align="center"><img alt="$$[2]=\{\ldots, -10, -4, 2, 8, 14 \ldots\}$$" src="svgs/bc59bfdbeed0f5109303d953ba7277c3.svg" valign=0.0px width="219.1777533pt" height="16.438356pt"/></p>

Congruence modulo <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is more than just an equivalence relation. The familiar
algebraic (ring) structure of the integers consistently descends to equivalence
classes; e.g., <img alt="$[3] + [4] = [1]$" src="svgs/4561339549f79f4347f45b2b5eb9bb62.svg" valign=-4.109589000000009px width="94.06379399999999pt" height="16.438356pt"/> and <img alt="$[3]*[4] = [0]$" src="svgs/f4efa67cd923ae2b646b041e1365439a.svg" valign=-4.109589000000009px width="89.49756914999999pt" height="16.438356pt"/> in <img alt="$\mathbb{Z}/6.$" src="svgs/b72a5807386b06a8f15ac82f41bd3eb7.svg" valign=-4.109589000000009px width="31.96358384999999pt" height="16.438356pt"/> Notationally, we usually
drop the square brackets and write, for example, <img alt="$3-4\equiv 5 \mod 6$" src="svgs/1a743d61128261019c5e6ed8382c8b1d.svg" valign=-1.3698745500000056px width="122.83057214999998pt" height="12.785402849999999pt"/> or just <img alt="$3\cdot 4=0$" src="svgs/d361396bb4e8e788e0c7fb9ddc39cde2.svg" valign=0.0px width="58.447240499999985pt" height="10.5936072pt"/> if
we know we are in <img alt="$\mathbb{Z}/6.$" src="svgs/b72a5807386b06a8f15ac82f41bd3eb7.svg" valign=-4.109589000000009px width="31.96358384999999pt" height="16.438356pt"/>

In Python, one can use the percent-sign operator to work modulo <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>:
```python
>>> 123 % 45
33
```
Alternatively, one can use numlib to work in <img alt="$\mathbb{Z}/45$" src="svgs/bdf2e4f3f1d0f1891a0bdcaf49a9b7be.svg" valign=-4.109589000000009px width="35.61656834999999pt" height="16.438356pt"/> as follows.
```python
>>> import numlib as nl
>>> R = nl.Zmod(45)
>>> R
Z/45
>>> R(123)
33 + <45>
```

### Pseudorandom number generation

This is an aside but, as a simple application, let us implement a
[Linear Congruence Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator).
*Linear congruence* here means that we generate the next "random" output by applying
a linear function to the state and taking the result modulo some fixed large number.
It doesn't matter as much in Python3, but for C or say Rust, it makes good sense to
mod by the large number <img alt="$2^{64}.$" src="svgs/5b7205ff89e43c26f8140c42f4b8cdc2.svg" valign=0.0px width="26.71243574999999pt" height="13.380876299999999pt"/>  Here is some code that implements an LCG using numlib:

```python
#lcg.py
import numlib as nl

# set the modulus
m = 2**64
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 123456789
c = 12121212121
state = R(10**10+1)  # an element of R

def prng():
    """Return the next sequential integer between 1 and m, inclusive."""
    global state
    state =  a * state + c
    return state + 1
```
Copy the code block above a file called **lcg.py**.  Then the following program,
when run in the same directory, prints 5 randomly generated numbers.
```python
from lcg import prng

for _ in range(5):
    print(prng())

#1234567902244668911
#8826425326919980896
#10890877254142952101
#15231402302547497038
#10264820975732655147
```
One can think of the above implementation of a LCG a generated pseudo-random
*sequence* of numbers.  Due to the initial seed being 10000000001, the
determinism is exhibited rather explicitly in the first number of the output.
Of course, the next number is completely determined by the current state in
any case.

The quality of "randomness" in the sequence generated by an LCG such as the one
above, or any PRNG, is a bit subtle to assess.  A battery of tests is often deployed
when trying to detect bad RNGs.

Since there are only <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/> possible outputs, the period of the random number
generator**prng** is **at most** <img alt="$2^{64}.$" src="svgs/5b7205ff89e43c26f8140c42f4b8cdc2.svg" valign=0.0px width="26.71243574999999pt" height="13.380876299999999pt"/>

Important: the PRNG above is *not* a CSPRNG &mdash; a
*cryptographically secure random number generator &mdash; hence it is not
of suitable quality for crytographic applications.

In fact, it may not even have the largest possible period (which is <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/>). In
the code block above, one can guarantee that the period is in fact as large as
possible using the Hull-Dobell Theorem; i.e., be ensuring that

* <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> are relatively prime,
* <img alt="$a-1$" src="svgs/e181cdf64450bcc9902678c74a33a624.svg" valign=-1.3698745499999938px width="36.99955544999999pt" height="11.96348175pt"/> is divisible by all prime factors of <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, and
* <img alt="$a-1$" src="svgs/e181cdf64450bcc9902678c74a33a624.svg" valign=-1.3698745499999938px width="36.99955544999999pt" height="11.96348175pt"/> is divisible by 4 if <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is divisible by <img alt="$4$" src="svgs/ecf4fe2774fd9244b4fd56f7e76dc882.svg" valign=0.0px width="8.219209349999991pt" height="10.5936072pt"/>.

#### Exercise
1.1. Does the LCG defined above satisfy all three bulleted conditions?

A common test to gauge whether a PRNG is worthy of the term "random" employs the
[Chi-squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution),
which works as follows.

Suppose that we partition the possible outputs into a small number of *cells* (or
*bins*). We can then use the LCG to generate a large sample of values and tally
how many land in each bin.

```python
from lcg import prng

sample_size = 12000
bins = 30 # we will split the sampled random numbers into equal bins

sample = [prng()//(2**64//bins) for _ in range(sample_size)]

def get_frequencies():
    frequencies = dict()
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    return list(frequencies.values())

print(*get_frequencies())
```
The output is
```
410 401 448 376 398 388 399 408 410 371 402 395 388 412 389 422 410 406 412 398 404 404 395 364 408 390 416 369 420 387
```
It appears that the numbers generated are fairly evenly distributed
across the 30 bins so that our PRNG appears to sample uniformly.  One the
other hand, note that we should be concerned if each bin contained exactly the
same number (400) of sample values; we wouldn't expect that even from an
actual (uniform) random number generator.

One way to analyze whether we have enough, but not too much, variation in
the frequencies is to compute the test statistic

<p align="center"><img alt="$$\widetilde{\chi}^2=\frac{1}{400}\sum (f_i - 400)^2,$$" src="svgs/1677857c4c0df1f93f1cc9e57600904b.svg" valign=0.0px width="177.65995005pt" height="32.990165999999995pt"/></p>

where <img alt="$f_i$" src="svgs/9b6dbadab1b122f6d297345e9d3b8dd7.svg" valign=-3.1963503000000055px width="12.69888674999999pt" height="14.611878599999999pt"/> is the observed frequency of values falling in the <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg" valign=0.0px width="5.663225699999989pt" height="10.84150485pt"/>th bin.
For a legitimate PRNG, this statistic follows a chi-squared distribution with
degrees of freedom equal to one less than the number of bins.

The sampling distribution (over 5000 samples) for the <img alt="$\chi^2$" src="svgs/a67d576e7d59b991dd010277c7351ae0.svg" valign=-3.1963503000000086px width="16.837900199999993pt" height="16.5772266pt"/> statistic for our
PRNG looks like this:

<p align="center">
  <img height="600" src="images/chisq.png">
</p>


### Prime fields

Note that <img alt="$2\cdot 11 = 1$" src="svgs/e927310f36765b5ad74fbd34bdb938dd.svg" valign=0.0px width="66.66644984999998pt" height="10.5936072pt"/> in <img alt="$\mathbb{Z}/21,$" src="svgs/e4c03b084fef61df3489a70d833a595b.svg" valign=-4.109589000000009px width="40.18279319999999pt" height="16.438356pt"/> so, 2 has 11 as its multiplicative inverse.
Meanwhile <img alt="$3$" src="svgs/5dc642f297e291cfdde8982599601d7e.svg" valign=0.0px width="8.219209349999991pt" height="10.5936072pt"/> can have no multiplicative inverse since it is a zero divisor in
<img alt="$\mathbb{Z}/21.$" src="svgs/3731d4bdedc964b8cdbf897e6ea86d26.svg" valign=-4.109589000000009px width="40.18279319999999pt" height="16.438356pt"/> If every nonzero



### Generating primes

We will need some prime numbers that are fairly large  &mdash; 200 bits, say, for now; so primes of size
around <img alt="$2^{200}.$" src="svgs/8ead495e1e0f713f33e7a75e00656907.svg" valign=0.0px width="33.264976799999985pt" height="13.380876299999999pt"/>

One way to generate such a prime would be to iterate through numbers larger that <img alt="$2^{200}$" src="svgs/acc9da0b19643e432619eb386d21261f.svg" valign=0.0px width="27.87685064999999pt" height="13.380876299999999pt"/> until we
find one that is prime.  Alternatively, one could randomly generate sequences of zeros and ones of
length 200 and check if the corresponding decimal number is prime.  Python has a built-in function that
generates an integer from random bits:

```python
import random
decimal = random.getrandbits(200)
```
Of course, depending on whether the most significant random bit was zero or one, we might get a number somewhat
less than <img alt="$2^{200};$" src="svgs/e46661a0be2003a6fba87fa4a557cf10.svg" valign=-3.1963503000000086px width="33.264976799999985pt" height="16.5772266pt"/> so let us set the most significant bit to one and, while we are at it, set
also the least significant bit to 1 since primes beyond 2 must be odd:
```python
decimal |= (1 << numbits - 1) | 1
```
The variable **decimal** is now an integer whose binary representation has length 200 and both begins
and ends with 1; i.e., **decimal** is a random (depending on the robustness of **getrandbits**)
odd integer strictly between <img alt="$2^{200}$" src="svgs/acc9da0b19643e432619eb386d21261f.svg" valign=0.0px width="27.87685064999999pt" height="13.380876299999999pt"/> and <img alt="$2^{201}.$" src="svgs/26851296087784570cb81e1034cdb3f0.svg" valign=0.0px width="33.264976799999985pt" height="13.380876299999999pt"/>

Beyond using the fact that a prime larger than 2 must be odd, there are various other quick ways
to test whether a candidate odd integer <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is *likely* prime.  These include
[Fermat's primality test](https://en.wikipedia.org/wiki/Fermat_primality_test) which checks to see
if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> *acts like* a prime: namely, whether <img alt="$a^{n-1} \equiv 1 \mod n$" src="svgs/d366fecb67ec763d517425469c45fd90.svg" valign=0.0px width="122.41226084999998pt" height="13.380876299999999pt"/> for <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> equal,
in turn, to say 2, 3, and 5, as would be the case, by Fermat's Little Theorem (see below), if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>
were in fact prime.

Rather than implement Fermat's and related primality tests yourself to detect whether **decimal** is prime,
feel free to use [numlib](https://github.com/sj-simmons/numlib)'s implementation:

```python
import numlib
numlib.isprime(decimal) # True or False according to whether decimal is prime
```
#### Exercise
1. Replace the <img alt="$200$" src="svgs/88db9c6bd8c9a0b1527a1cedb8501c55.svg" valign=0.0px width="24.657628049999992pt" height="10.5936072pt"/> above with say <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> and write a function, using the scheme outlined above, that returns a <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit prime.

At issue is the fact that larger primes are harder to find. The difficulty is gauged by the Prime
Number Theorem.  If we define <img alt="$\pi(n)$" src="svgs/ab6b1f726144febfe19f0c5d987822fa.svg" valign=-4.109589000000009px width="32.61239849999999pt" height="16.438356pt"/> to be the number of primes less than or equal to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, then
the theorem states that <img alt="$\pi(n)$" src="svgs/ab6b1f726144febfe19f0c5d987822fa.svg" valign=-4.109589000000009px width="32.61239849999999pt" height="16.438356pt"/> is well-approximated by <img alt="$n/\ln(n)$" src="svgs/9bbe784fa51a44e5989bc0b2cac489c3.svg" valign=-4.109589000000009px width="57.17672729999999pt" height="16.438356pt"/> in the sense that
<p align="center"><img alt="$$\lim_{n\rightarrow\infty}\pi(n)\cdot\ln(n)/n=1.$$" src="svgs/bbbfdbd8c7959c658b17fe94615640ac.svg" valign=0.0px width="170.7003078pt" height="22.1917806pt"/></p>

The Prime Number Theorem implies that the number of primes between <img alt="$2^k$" src="svgs/91f4e50a1561b60d45e7079ca70f2ed4.svg" valign=0.0px width="15.48523844999999pt" height="13.95621975pt"/> and <img alt="$2^{k+1}$" src="svgs/bf56939689dfdac754c6e27725da93c9.svg" valign=0.0px width="32.12915969999999pt" height="13.95621975pt"/>
is approximately

<p align="center"><img alt="$$\frac{2^{k+1}}{\ln(2^{k+1})}-\frac{2^{k}}{\ln(2^{k})}=\frac{2^k}{\ln(2)}\left(\frac{2}{k+1}-\frac{1}{k}\right)=\frac{2^k}{\ln(2)}\frac{k-1}{k(k+1)};$$" src="svgs/ee03776f623d8b1c2733d4ee1290e882.svg" valign=0.0px width="418.50896339999997pt" height="40.6935375pt"/></p>

hence, the probability of a randomly chosen number between <img alt="$2^k$" src="svgs/91f4e50a1561b60d45e7079ca70f2ed4.svg" valign=0.0px width="15.48523844999999pt" height="13.95621975pt"/> and <img alt="$2^{k+1}$" src="svgs/bf56939689dfdac754c6e27725da93c9.svg" valign=0.0px width="32.12915969999999pt" height="13.95621975pt"/> being
prime is approximately <img alt="$p = (k-1)/(\ln(2)k(k+1))\approx 1/(\ln(2)k).$" src="svgs/0e7d2a1e66b418706e1b00cb61c47fcd.svg" valign=-4.109589000000009px width="294.8002942499999pt" height="16.438356pt"/>  But since your
program from exercise 1 doesn't bother with even numbers, a given candidate **decimal**
has a likelihood of about <img alt="$p = 2/(\ln(2)k)$" src="svgs/e555980e9b695645e92caf5d9af89aa7.svg" valign=-4.109589000000009px width="103.19072609999999pt" height="16.438356pt"/> of being prime.
It is an elementary fact from probability theory (see e.g., section 2.1 of
[primer on random variables](https://github.com/sj-simmons/probthry/blob/main/primer.pdf)) that,
on average, one expects to test about <img alt="$1/p=k\ln(2)/2$" src="svgs/6c97d8dd61ac519e745292cae1789830.svg" valign=-4.109589000000009px width="109.5833706pt" height="16.438356pt"/> numbers before turning one up that is
indeed prime.

#### Exercise
2. Write a program that verifies that the expected number of tries before your function from exercise 1 returns a prime is about <img alt="$200\ln(2)/2\approx 69$" src="svgs/d593e0b8122513765f33fdc1e83baf49.svg" valign=-4.109589000000009px width="116.89507004999999pt" height="16.438356pt"/>.

Note: since <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> is small, the variance here is very large so that the time it takes for your
program to find a single prime can vary greatly.

### Euler's Theorem

This is a basic result:

**Fermat's Little Theorem**:  If <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> is a prime and <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is an integer not divisible by <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>, then <img alt="$a^{p-1} \equiv 1 \mod p$" src="svgs/2e621949487c8c972e5637f0848ac82e.svg" valign=-3.1963503000000086px width="119.46638879999998pt" height="16.5772266pt"/>.

For those who know a little group theory this follows immediately from the fact that the order of
any element of a finite group must divide the order of the group. Here the relevant group is
<img alt="$(\mathbb{Z}/p\mathbb{Z})^*$" src="svgs/d2c33048356c6fe9be608ea115f0bf8a.svg" valign=-4.109589000000009px width="57.92828579999998pt" height="16.438356pt"/>, the multiplicative group of units in <img alt="$\mathbb{Z}/p\mathbb{Z}$" src="svgs/a05b826333ec801b65201f7764c6754f.svg" valign=-4.109589000000009px width="38.40765719999999pt" height="16.438356pt"/>,
which has order <img alt="$p-1.$" src="svgs/2ad55de588e0025342173e657988d28d.svg" valign=-3.196350299999994px width="41.14719179999999pt" height="13.789957499999998pt"/>

If you are not familiar with basic group theory, then see for example
[this wikipedia page](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem)
for various other proofs of Fermat's Little Theorem.

#### Exercise
3. Use your program above to generate a 200-bit prime <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and then verify that the <img alt="$a^{p-1} \equiv 1 \mod p$" src="svgs/2e621949487c8c972e5637f0848ac82e.svg" valign=-3.1963503000000086px width="119.46638879999998pt" height="16.5772266pt"/> where <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is, say, 1234567, or any positive integer less than <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>. Note: you may wish to use Python's built-in [pow() function](https://docs.python.org/3/library/functions.html#pow).

Below we will need the following generalization of Fermat's Little Theorem.

**Euler's Theorem**:  If <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is positive integer and <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is an integer relatively prime to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>,
then <img alt="$a^{\phi(n)} \equiv 1 \mod n$" src="svgs/43209724f91855df0b2d1ff33ff21559.svg" valign=0.0px width="123.76385504999998pt" height="14.5954875pt"/>.

Here <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/> is the Euler Phi function which returns the number of positive integers less than
and relatively prime to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>.
Notice that Euler's Theorem specializes to Fermat's Little Theorem if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is prime since, then,
<img alt="$\phi(n)=n-1.$" src="svgs/1b0d94292d544c37a22b1f0f7f9a7b13.svg" valign=-4.109589000000009px width="97.10798459999998pt" height="16.438356pt"/>  Moreover, Euler's Theorem also follows from basic group theory where the ambient
group is <img alt="$(\mathbb{Z}/n\mathbb{Z})^*$" src="svgs/3864234dcb7744587a117c9e1a7290ea.svg" valign=-4.109589000000009px width="59.52459479999999pt" height="16.438356pt"/>, the multiplicative group of units in <img alt="$\mathbb{Z}/n\mathbb{Z}$" src="svgs/94d333ba0aaa5e9c8ce88690986075c2.svg" valign=-4.109589000000009px width="40.00396784999999pt" height="16.438356pt"/>,
which has order <img alt="$\phi(n).$" src="svgs/4b539e947954886e594105a91f42f29b.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/>

### Public-key Cryptography

In modern times, you can create and publish (on, say, your personal webpage) a *public key* that
can then be used (by, say, someone called Athena) to encrypt a private message to you.  You can decrypt
Athena's message but no else can, so it doesn't matter if a bad actor sees Athena's encrypted message
that she is sending to you.

Important: since your enciphering key is public, a bad actor might try to intercept Athena's message
and replace it with a malicious message encrypted with your public key. Then you encrypt the bad actors
message thinking that it is from Athena.  We need to bar against this weakness but, for now, let us
ignore it.

To create your public key, you first choose two large primes <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> (which you will keep
secret) and multiply them together obtaining <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>.  You also choose a positive integer <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> that is relative
prime to <img alt="$\phi(n)=(p-1)*(q-1)$" src="svgs/5d28570761d98da2134694296c4ca9e6.svg" valign=-4.109589000000009px width="168.27977264999998pt" height="16.438356pt"/>.  Your public key then consists of the pair of numbers <img alt="$(e, n)$" src="svgs/1ea602d667e6403959572fffbd4671bc.svg" valign=-4.109589000000009px width="37.61233079999999pt" height="16.438356pt"/>.

Now suppose that <img alt="$M$" src="svgs/fb97d38bcc19230b0acd442e17db879c.svg" valign=0.0px width="17.73973739999999pt" height="11.232861749999998pt"/> is a positive integer representing the message that Athena wants to encrypt and
send to you.  If <img alt="$M$" src="svgs/fb97d38bcc19230b0acd442e17db879c.svg" valign=0.0px width="17.73973739999999pt" height="11.232861749999998pt"/> is the numeric version of your message, then we encrypt <img alt="$M$" src="svgs/fb97d38bcc19230b0acd442e17db879c.svg" valign=0.0px width="17.73973739999999pt" height="11.232861749999998pt"/>

Now, in order for you to decrypt Athena's message you must (see below) derive your
So how is it that your public key can't be reverse engineered by a bad actor

And example

* ECC (Elliptic Curve Cryptography
  * [A gentle intro to ECC](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/)
  * Neal Koblitz's 1985 paper [Elliptic Curve Cryptosystems](https://www.ams.org/journals/mcom/1987-48-177/S0025-5718-1987-0866109-5/S0025-5718-1987-0866109-5.pdf)

* Potentially relevant
  * MC Frontalot's [Secrets of the future](https://www.youtube.com/watch?v=FUPstXCqyus)

#### Cryptocurrencies
* [Chart showing which coins use which flavors of cryptography and curves](http://ethanfast.com/top-crypto.html)

* Literature
  * [The Mathematics of Bitcoin](https://arxiv.org/abs/2003.00001)

#### Zero knowledge
* [math primer](http://extropy.foundation/workshops/zkp/primer.html)

#### More literature
* [evervault.com/papers](https://evervault.com/papers)

## Tools/tutorials

#### Quick start on making basic  number-theoretic/cryptography computations in high-performance Python
* Install the multi-precision library [gmpy2](https://gmpy2.readthedocs.io/en/latest/intro.html)
  in a Debian-like environment such as Ubuntu by issuing, at your commandline, the command
  ```shell
  sudo apt install gmpy2
  ```
* Then, if you say want to generate some large primes in Python:
  ```python
  import gmpy2

  randstate = gmpy2.random_state(1728)

  def getprime(nbits):
      """ Return an n-bit prime of type mpz. """
      return gmpy2.next_prime(gmpy2.mpz_rrandomb(randstate, nbits))
  ```
  The function **getprime()** generates primes. Let us check that they are roughly n-bits.
  ```python
  import math

  for _ in range(10):
     p = getprime(128)
     print(f'{p}  approx. bit-length: {math.log2(p)}')

  # output:
  # 170141183460778792299372374151321878621  approx. bit-length: 127.00000000000263
  # 340281722954356176270385562639172354083  approx. bit-length: 127.9999972697725
  # 340282366920938463463374607431768080437  approx. bit-length: 128.0
  # 340282366920938461102191365996962381853  approx. bit-length: 128.0
  # 340282366919700523719237132310450012183  approx. bit-length: 127.99999999999476
  # 329648544222309736707797093892948492193  approx. bit-length: 127.95419631593471
  # 338953138926372144816642355375684713631  approx. bit-length: 127.99435343686405
  # 340282366920937254539860835811807199379  approx. bit-length: 128.0
  # 170141183460470440657506916146035556433  approx. bit-length: 127.00000000000001
  # 340282366920937292316486855759755210761  approx. bit-length: 128.0
  ```
* Now suppose that we want to (naively) pick two large primes, set up an RSA
  encryption scheme, and encode the message 98765432123456789.
  ```python
  p, q = getprime(128), getprime(128)
  n = p * q  # type mpz

  phi = (p - 1) * (q - 1) # keep this secret

  # find a (naive) encryption key
  e = 1
  while (e < 2 or gmpy2.gcd(e, phi) != 1):
    e = gmpy2.mpz_random(randstate, phi) # type mpz

  assert gmpy2.gcd(e, phi) == 1  # (e, n) is our public key

  m = 98765432123456789 # our message

  c = gmpy2.powmod(m, e, n) # m^e (mod n) our ciphertext (encrypted message)
  ```
* Lastly, let us check things by finding a deciphering key and decrypting the message.
  ```python
  _, d, _ = gmpy2.gcdext(e, phi) # d is our deciphering (private) key
  d = gmpy2.t_mod(d, phi)  # we only need d modulo phi

  # Note: the function gcdext used above applies the extended Euclidean algorithm;
  # i.e., gcdext(e, phi) returns a triple of integers (gcd(d, phi), d, f) satisfying
  #                    gcd(e, phi) = d * e + f * phi.
  # Since gcd(e, phi) = 1, d is just the multiplicative inverse of e (modulo phi)

  assert gmpy2.t_mod(d*e, phi) == 1

  # Alternatively, one can compute d with
  #                    d = gmpy2.inverse(e, phi)

  print(gmpy2.powmod(c, d, n)) # c^d (mod n) = 98765432123456789
  ```
#### Use Simmons' [numlib](https://github.com/sj-simmons/numlib) to instantiate and compute, in Python, in a finite field or in an elliptic curve over a finite field.
*  First install the library by typing, at your commandline,
   ```shell
   pip install polylib --user
   pip install numlib --user
   ```
*  Then, you can create in Python a primefield (i.e., Z/pZ where p is a prime) of order say 2027:
   ```pycon
   >>> import numlib as nl
   >>> PF = nl.Zmodp(2027)
   >>> PF  # Z/2027
   >>> x = PF(100)
   >>> x   # 100 + <2027>
   >>> x**1000  # 2022 + <2027>
   >>> x**-1  # 750 + <2027>
   ```
* Instantiate an work in a Galois field of order 7^3:
  ```pycon
  >>> GF = nl.GaloisField(7, 3)
  >>> GF  # Z/7[t]/<t^3+3t^2-3>
  >>> t = GF.t()
  >>> t   # t + <t^3+3t^2-3>
  >>> t**1000  # -3t^2+3t+2 + <t^3+3t^2-3>
  >>> t**-1  # -2t^2+t + <t^3+3t^2-3>
  ```
* Work in an elliptic curve over the Galois field of order 7^3:
  ```pycon
  >>> E = nl.EllCurve(t**2+5*t+2,t-2)
  >>> E  # y^2 = x^3 + (t^2-2t+2)x + (t-2) over Z/7[t]/<t^3+3t^2-3>
  >>> E.j  # 3t^2+t+3
  >>> # Let us list a few point on this curve:
  >>> finite_points = list(nl.finite(E)) # nl.finite(E) is a generator
  >>> for point in finite_points:
  ...     print(point)
  ...
  (-t^2-t-2, -3t^2-3t-3)
  (-t^2-t-2, 3t^2+3t+3)
  (2t^2-t+3, -2t^2-3t-3)
  (2t^2-t+3, 2t^2+3t+3)
  (3t+2, -3t-3)
       ...
  >>> len(finite_points)  # this curve has order 320 (including the point at infinity)
  319
  >>> # Let's pick point and find its order
  >>> pt = finite_points[0]
  >>> pt  # (-t^2-t-2, -3t^2-3t-3) on y^2 = x^3 + (t^2-2t+2)x + (t-2) over Z/7[t]/<t^3+3t^2-3>
  >>> print(1000 * pt)  # (t^2+2t, 2t^2-3t-2)
  >>> print(-pt)  # (-t^2-t-2, 3t^2+3t+3)
  >>> nl.addorder(pt, exponent = 320)  # 160
  ```

#### Install and use Sage as a Python library
On a debian-like (again, including WSL):
```shell
sudo apt install sagemath
```

#### Install PARI/GP and use it as a Python library
* First, one needs to install [pari-gp](http://pari.math.u-bordeaux.fr/) (so that the
  program **gp**) is in one's PATH.

  On a Debian-like system this is as easy as:
  ```shell
  sudo apt install pari-gp
  ```
  PARI includes its own interactive shell:
  ```shell
  > gp -q
  ?
  ```
  For more, see the PARI/GP [documentation](http://pari.math.u-bordeaux.fr/doc.html) and
  [tutorials](http://pari.math.u-bordeaux.fr/tutorials.html)
* Then there's the python interface to PARI/GP. It's called
  [cypari2](https://github.com/sagemath/cypari2)

## Reference

### Resources
* [Freaking blockchain's: how do they work](https://norswap.com/blockchain-how/)
* [keylength.com](https://www.keylength.com/)

### Libraries
* [Comparison of cryptography libraries](https://en.wikipedia.org/wiki/Comparison_of_cryptography_libraries)

### [Homomophic encryption](https://homomorphicencryption.org/introduction/)
* [HElib's design](https://homenc.github.io/HElib/documentation/Design_Document/HElib-design.pdf)
* [FHEW](https://github.com/lducas/FHEW)
* [Cupcake](https://github.com/facebookresearch/Cupcake) from FacebookResearch; Rust, implements
  lattice-based homomophic encryption
  * [Somewhat practicle homomorphic encryption](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.400.6346&rep=rep1&type=pdf)
* [zama](https://zama.ai/concrete/)
* Google's [FHE](https://github.com/google/fully-homomorphic-encryption)

### Curves
* [Safecurves](https://safecurves.cr.yp.to/index.html)
* [Standard Curve Database](https://neuromancer.sk/std/)

### More
* [Cryptol](https://cryptol.net/) A DSL for cryptography that sits on top of Haskell.
* [Theoretical description and formal security analysis of Signal's protocol](https://eprint.iacr.org/2016/1013)
* [Cryptohack](https://cryptohack.org/)


