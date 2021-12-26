# crypto senior sem
### From cryptography to cryptocurrencies

This course is about the state-of-the-art in modern cryptography, which
finds application as the primary mathematical apparatus that has of late been
artfully fashioned into cryptocurrencies.  Cryptography is of course pervasive and
ubiquitous in the technological age, so that this course is ultimately about
certain cutting-edge information-theoretic advancements that are reshaping our
world.  In addition to cryptographic primitives, their prevailing applications
and underlying mathematics, topics include applications of zero-knowledge proofs
and their role in present-day FinTech.

Important: as far as speculating in cryptocurrencies, we think that you are likely
better off not doing so. Whether or not you take that advice, you might
do well to look under the hood of the new-fangled tech that is built atop a rather
striking assemblage of pure and applied Math and CS.

### Contents
1. [Preliminaries](#preliminaries)
   * [The integers modululo n](#the-integers-modulo-n)
   * [Pseudo-random sequences](#pseudo-random-sequences)
   * [Cryptographic security](#cryptographic-security)
2. [Number-theoretic practicalities](#number-theoretic-practicalities)
   * [Prime fields](#prime-fields)
   * [Generating primes](#generating-primes)
   * [Euler's phi function](#eulers-phi-function)
   * [Plain RSA](#plain-rsa)

## Preliminaries

### Getting started

* First, install [polylib](https://github.com/sj-simmons/polylib),
* then install [numlib](https://github.com/sj-simmons/numlib),
* then read on.

### The integers modulo n

Let <img alt="$n\in\mathbb{Z}$" src="svgs/a3f3ee66a29182d90ff26e24025b8cc2.svg" valign=-0.6427030499999994px width="40.916955749999985pt" height="11.966898899999999pt"/> be a fixed positive integer. We say that integers <img alt="$x$" src="svgs/332cc365a4987aacce0ead01b8bdcc0b.svg" valign=0.0px width="9.39498779999999pt" height="7.0776222pt"/> and <img alt="$y$" src="svgs/deceeaf6940a8c7a5a02373728002b0f.svg" valign=-3.1963502999999895px width="8.649225749999989pt" height="10.2739725pt"/>
are *congruent* modulo <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> divides their difference, <img alt="$x-y;$" src="svgs/9f2c06cdc6a6490da6493c39ee7fff19.svg" valign=-3.19635195px width="42.70160894999999pt" height="12.785402849999999pt"/> and we write
<img alt="$x = y \mod n.$" src="svgs/54ff76854f257251fee7728c3bd6a660.svg" valign=-3.1963503000000055px width="102.33983759999998pt" height="14.611878599999999pt"/> For instance, <img alt="$17 = 2 \mod 5.$" src="svgs/891a6985cade5e203bf81ee5fad5642d.svg" valign=0.0px width="107.30560499999999pt" height="11.4155283pt"/>

One can consider the
[ring](https://en.wikipedia.org/wiki/Ring_(mathematics)) of integers modulo <img alt="$n,$" src="svgs/85bc1f723bdc744666d4f2241b1031f7.svg" valign=-3.1963502999999895px width="14.433101099999991pt" height="10.2739725pt"/>
denoted <img alt="$\mathbb{Z}/n\mathbb{Z}$" src="svgs/94d333ba0aaa5e9c8ce88690986075c2.svg" valign=-4.109589000000009px width="40.00396784999999pt" height="16.438356pt"/> or, more succinctly, <img alt="$\mathbb{Z}/n.$" src="svgs/b2db6c8686053451d402312789bf8098.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>
Congruence modulo a given <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> defines an
[equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation)
on the integers and, as a set, <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> consists precisely of the resulting
equivalence classes.

An equivalence relation partitions a set into disjoint subsets. For instance,
<img alt="$\mathbb{Z}/6$" src="svgs/34178db573bc75259b7edcfa36f7a3cc.svg" valign=-4.109589000000009px width="27.39735899999999pt" height="16.438356pt"/> consists of the 6 equivalence classes <img alt="$\{[0],[1],[2],[3],[4],[5]\}$" src="svgs/894c828a46f3ad0f1232271f1d216c12.svg" valign=-4.109589000000009px width="157.0777791pt" height="16.438356pt"/>
where, for example,

<p align="center"><img alt="$$[2]=\{\ldots, -10, -4, 2, 8, 14 \ldots\}.$$" src="svgs/e02c8523dd8bf6edd8277bfcc574720c.svg" valign=0.0px width="223.74397814999998pt" height="16.438356pt"/></p>

Congruence modulo <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is more than just an equivalence relation. The familiar
algebraic (ring) structure of the integers consistently descends to equivalence
classes; e.g., <img alt="$[3] + [4] = [3 + 4] = [7] = [1]$" src="svgs/a025aa0fb774d541e26f41ecbc1b6084.svg" valign=-4.109589000000009px width="200.91276975pt" height="16.438356pt"/> and <img alt="$[3]*[4] = [12] = [0]$" src="svgs/fabd08d9b3e345dc177462d18af34a35.svg" valign=-4.109589000000009px width="136.98606734999998pt" height="16.438356pt"/> in
<img alt="$\mathbb{Z}/6.$" src="svgs/b72a5807386b06a8f15ac82f41bd3eb7.svg" valign=-4.109589000000009px width="31.96358384999999pt" height="16.438356pt"/> Notationally, we usually drop the square brackets and write,
for example, <img alt="$3-4 = 5 \mod 6$" src="svgs/6001c19bf6f4ce3779f9344a826ab8cc.svg" valign=-1.3698745500000056px width="122.83057214999998pt" height="12.785402849999999pt"/>; or we might write simply <img alt="$3\cdot 4=0$" src="svgs/d361396bb4e8e788e0c7fb9ddc39cde2.svg" valign=0.0px width="58.447240499999985pt" height="10.5936072pt"/> if it
is already clear that we are working in <img alt="$\mathbb{Z}/6.$" src="svgs/b72a5807386b06a8f15ac82f41bd3eb7.svg" valign=-4.109589000000009px width="31.96358384999999pt" height="16.438356pt"/>

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
Here <img alt="$\langle 45\rangle$" src="svgs/cf296d4f4491ba376822fa1933ea099f.svg" valign=-4.109589000000009px width="29.22385289999999pt" height="16.438356pt"/> is the equivalence class <img alt="$[0] = \{45k~|~ k \in \mathbb{Z}\}$" src="svgs/2b761bb36685aa1e815d610294d94eab.svg" valign=-4.109589000000009px width="136.87204079999998pt" height="16.438356pt"/>
(which is in fact an [ideal](https://en.wikipedia.org/wiki/Ideal_(ring_theory))
in the ring of integers) so that the notation <img alt="$33 + \langle 45\rangle$" src="svgs/aabe56f4ceb2dfc83627b3ab99dc2c60.svg" valign=-4.109589000000009px width="65.75346194999999pt" height="16.438356pt"/> reminds us
that we are working modulo <img alt="$45$" src="svgs/f2ebeadd36ad2620cbe7f02c861c9da3.svg" valign=0.0px width="16.438418699999993pt" height="10.5936072pt"/> (or, more abstract algebraically, modulo the ideal
generated by <img alt="$45$" src="svgs/f2ebeadd36ad2620cbe7f02c861c9da3.svg" valign=0.0px width="16.438418699999993pt" height="10.5936072pt"/>).

Technical note: numlib conveniently coerces types, for instance:
```python
>>> x = R(123)
>>> 67 * x + 89  # no need to write R(67) * x + R(89)
5 + <45>
```

### Pseudo-random sequences

As a simple application let us implement a
[Linear Congruence Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator).
*Linear congruence* here means that we generate the next "random" output
by applying a linear function to the current state and taking the result modulo
some fixed large number, <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, called the modulus.  It doesn't matter as much in Python3,
but for C or say Rust, it makes good sense to mod by the large number <img alt="$2^{64}.$" src="svgs/5b7205ff89e43c26f8140c42f4b8cdc2.svg" valign=0.0px width="26.71243574999999pt" height="13.380876299999999pt"/>
Here is some code that implements an LCG using numlib:

```python
#lcg.py
import numlib as nl

# set the modulus
m = 2**64
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 123456789
c = R(12121212121) # an element of R
state = 10**10+1

def prng():
    """Return the next sequential integer between 0 and m-1, inclusive."""
    global state
    state = int(a*state+c) # a*state+c is an element of R = Z/m
    return state
```
Copy the code block above to a file called **lcg.py**.  Then the following program,
when run in the same directory, prints five "randomly" generated numbers.
```python
from lcg import prng

for _ in range(5):
    print(prng())

#1234567902244668910
#8826425326919980895
#10890877254142952100
#15231402302547497037
#10264820975732655146
```
One can think of the above LCG implementation as generating a pseudo-random
*sequence* of numbers.  Due to the initial seed being 10000000001, the
determinism is exhibited rather explicitly in the first number of the output.
Of course, the next number is always completely determined by the current state.

The quality of "randomness" in the sequence generated by an LCG such as the one
above, or any PRNG, is a bit subtle to assess.  A battery of tests is often deployed
when trying to detect bad PRNGs.

Since there are only <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/> possible outputs, the period of our pseudo-random number
generator **prng** is at most <img alt="$2^{64}.$" src="svgs/5b7205ff89e43c26f8140c42f4b8cdc2.svg" valign=0.0px width="26.71243574999999pt" height="13.380876299999999pt"/>

Important: the PRNG above is *not* a CSPRNG &mdash; a
*cryptographically secure* pseudo random number generator &mdash; hence it is not
of suitable quality for cryptographic applications. More on CSPRNGs later.

In fact, the PRNG defined above may not even have the largest possible period
(which is the modulus <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> in general and <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/> for our PRNG). Any positive <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> resulting
in <img alt="$x_{n+k} = x_n$" src="svgs/1d73f7557110d4433a0cf718f299dc6b.svg" valign=-3.8356081499999894px width="75.13896224999999pt" height="10.91323035pt"/> for some <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> leads obviously to the sequence repeating. The
smallest such <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> is the *period* &mdash; the length of the smallest *cycle* of numbers
which our pseudo-random sequence repeats.

Iterating the definition <img alt="$x_{n+1}=ax_n+c \mod m$" src="svgs/0e358a7c266bc77fd48b2150cbce0805.svg" valign=-3.835608150000004px width="173.51955554999998pt" height="15.251136449999997pt"/>, one arrives at the more general
formula for <img alt="$x_{n+k}$" src="svgs/c595a3f54070ca66c9252ccd45ca1732.svg" valign=-3.8356081499999894px width="34.878414449999994pt" height="10.91323035pt"/> in terms of <img alt="$x_n:$" src="svgs/90b8e9cb0a081795c49c5615819d5d21.svg" valign=-2.4657286499999893px width="27.47524889999999pt" height="9.54335085pt"/>

<p align="center"><img alt="\begin{align}&#10;x_{n+k}=a^kx_n+\frac{a^k-1}{a-1}c \mod m, \notag&#10;\end{align}" src="svgs/ee2113485df040f2fc9693b67a9a27c7.svg" valign=0.0px width="241.39918605pt" height="37.72265145pt"/></p>

where we have assumed that <img alt="$a \ne 1$" src="svgs/a27e3b950c87020be8bb4ebf02facc3f.svg" valign=-3.1963189500000055px width="38.82599489999999pt" height="14.61184725pt"/> since otherwise each term in our sequence
differs, modulo <img alt="$m,$" src="svgs/85e0696fc8ec9dcd16fd64c9f562ae0c.svg" valign=-3.1963502999999895px width="18.99932429999999pt" height="10.2739725pt"/> from the previous term by simply <img alt="$c.$" src="svgs/857431164e0fb928019e5dcd76861f58.svg" valign=0.0px width="11.680028249999989pt" height="7.0776222pt"/>

If <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> are not relatively prime, say <img alt="$\gcd(a,m)=d,$" src="svgs/7ddcc9953295b42a028ea52e81e412e1.svg" valign=-4.109589000000009px width="102.91097354999998pt" height="16.438356pt"/> then, modulo <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, <img alt="$ax_n$" src="svgs/207458e1a12e90cde6ffea1dddf3672d.svg" valign=-2.4657286499999893px width="26.210165849999992pt" height="9.54335085pt"/>
is always a multiple of <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/>. Since adding <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> just shifts those numbers, larger
values of <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> result in a smaller periods for our LCG.  We don't want a small period
so we generally pick <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> relatively prime.

In fact, since <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is a power of <img alt="$2$" src="svgs/76c5792347bb90ef71cfbace628572cf.svg" valign=0.0px width="8.219209349999991pt" height="10.5936072pt"/> in our LCG, were <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> even,
then the expression above for <img alt="$x_{n+k}$" src="svgs/c595a3f54070ca66c9252ccd45ca1732.svg" valign=-3.8356081499999894px width="34.878414449999994pt" height="10.91323035pt"/> would specialize to

<p align="center"><img alt="\begin{align}&#10;x_{n+k}&amp;=(2\ell)^kx_n+\frac{(2\ell)^k-1}{2\ell-1}c \notag \\&#10;       &amp;=2^k\ell^kx_n+((2\ell)^{k-1} + (2\ell)^{k-2} + \cdots + 2\ell + 1)c \notag \\&#10;       &amp;=2^k\ell^kx_n+(2^{k-1}\ell^{k-1} + 2^{k-2}\ell^{k-2} + \cdots + 2\ell + 1)c \mod 2^{64}.\notag&#10;\end{align}" src="svgs/45da3fa0c5bac197f0b492f71223bd46.svg" valign=0.0px width="479.9580456pt" height="90.45703259999999pt"/></p>

If <img alt="$k \ge 64$" src="svgs/608af5d2967c5090bb77eccfb84cabda.svg" valign=-2.235141150000005px width="47.43141149999999pt" height="13.650669449999999pt"/>, then the first term on the right vanishes and the constant term stops
depending on <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>; hence our sequence degenerates to a constant sequence &mdash;
pretty much the worst thing that can happen to one's PRNG.

If <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> are indeed, as is generally preferable, relatively prime, then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/>
is invertible modulo <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> so that <img alt="$x_{n+1}$" src="svgs/14e12a1273c346610e9daaf5e3aee29a.svg" valign=-3.8356081499999894px width="34.16493134999999pt" height="10.91323035pt"/> determines <img alt="$x_n;$" src="svgs/257055757fc84868cb108b5f78a1a186.svg" valign=-3.1963502999999895px width="22.90914944999999pt" height="10.2739725pt"/> explicitly, we
have <img alt="$x_n = a^{-1}(x_{n+1}-c) \mod m.$" src="svgs/68b635c3a48f4da6878d8005ce71f1b5.svg" valign=-4.109589000000009px width="208.51967069999998pt" height="17.4904653pt"/> In this case, the first repeated value,
call it <img alt="$x_r$" src="svgs/cb6f9168a549331aa3c962c22659d695.svg" valign=-2.4657286499999893px width="15.85243604999999pt" height="9.54335085pt"/>, in our sequence has to be equal to <img alt="$x_0$" src="svgs/e714a3139958da04b41e3e607a544455.svg" valign=-2.4657286499999893px width="15.94753544999999pt" height="9.54335085pt"/> (the initial state of our LCG)
since if the first repeated value were equal to <img alt="$x_j$" src="svgs/4d8443b72a1de913b4a3995119296c90.svg" valign=-4.7031731999999895px width="15.499497749999989pt" height="11.780795399999999pt"/> with <img alt="$0&lt; j &lt; r$" src="svgs/f85c6d002939aa5068a61da99ac32f02.svg" valign=-3.1963519500000044px width="67.63784279999999pt" height="14.0378568pt"/> then necessarily
<img alt="$x_{j-1} = a^{-1}(x_j-c) = a^{-1}(x_r-c) = x_{r-1}$" src="svgs/3d73533e351ffb9b7dd759a2ece0f5bf.svg" valign=-4.703173200000008px width="297.23158409999996pt" height="18.0840495pt"/>, violating that fact <img alt="$r$" src="svgs/89f2e0d2d24bcf44db73aab8fc03252c.svg" valign=0.0px width="7.87295519999999pt" height="7.0776222pt"/> is the
index of the first repeated value.

For our LCG, <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is a power of 2 and <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is odd; hence the first repeated value
is the initial state <img alt="$x_0$" src="svgs/e714a3139958da04b41e3e607a544455.svg" valign=-2.4657286499999893px width="15.94753544999999pt" height="9.54335085pt"/>.  The question is whether that value recurs before
the <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/>th term in our sequence (which is not what we want).

One can guarantee that the period of an LCG is in fact as large as possible using
the Hull-Dobell Theorem; i.e., by ensuring that

* <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> are relatively prime,
* <img alt="$a-1$" src="svgs/e181cdf64450bcc9902678c74a33a624.svg" valign=-1.3698745499999938px width="36.99955544999999pt" height="11.96348175pt"/> is divisible by all prime factors of <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, and
* <img alt="$a-1$" src="svgs/e181cdf64450bcc9902678c74a33a624.svg" valign=-1.3698745499999938px width="36.99955544999999pt" height="11.96348175pt"/> is divisible by 4 if <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is divisible by <img alt="$4$" src="svgs/ecf4fe2774fd9244b4fd56f7e76dc882.svg" valign=0.0px width="8.219209349999991pt" height="10.5936072pt"/>.

For a proof that the three bullet points guarantee the maximum period
see [Knuth](#references1) pp. 17-19.

If the second bullet point is satisfied then there exists a least power, <img alt="$s$" src="svgs/6f9bad7347b91ceebebd3ad7e6f6f2d1.svg" valign=0.0px width="7.7054801999999905pt" height="7.0776222pt"/>, called
the *potency* of the LCG, such that <img alt="$(a-1)^s = 0 \mod m.$" src="svgs/5337508b48bc15988009509ccf128bd7.svg" valign=-4.109589000000009px width="153.8923485pt" height="16.438356pt"/> If the potency is
low then successive terms of our pseudorandom sequence change too simply and hence
not very randomly.  A potency of 2, for instance, implies that the difference between
<img alt="$(n+1)$" src="svgs/949707b3bc37b3be0f8b25742664879e.svg" valign=-4.109589000000009px width="50.962710149999985pt" height="16.438356pt"/>st and the <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>th state of our PRNG is always <img alt="$c(1+(a-1)n).$" src="svgs/010edbd5f223fb0408f3f67e509f6f27.svg" valign=-4.109589000000009px width="112.42772639999998pt" height="16.438356pt"/>
Generally, a potency of at least 5 is necessary (but not sufficient) for randomness
(see [Knuth](#references1) pp. 24-25).

#### Exercises
1. Does the LCG defined by the program above satisfy all three bulleted conditions so that its period is <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/>, the largest possible?

2. If possible, compute the potency of the LCG above to see if it even has a chance
   of being sufficiently "random".

3. Show the following (we used this above):  if <img alt="$gcd(a, m) = d$" src="svgs/c80e3d64932bb680cf2d824d13827a15.svg" valign=-4.109589000000009px width="97.78729124999998pt" height="16.438356pt"/> then, modulo <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, for any integer <img alt="$x$" src="svgs/332cc365a4987aacce0ead01b8bdcc0b.svg" valign=0.0px width="9.39498779999999pt" height="7.0776222pt"/>, we have that <img alt="$ax$" src="svgs/1590372cccb08e52e5b844dda033b7aa.svg" valign=0.0px width="18.08414189999999pt" height="7.0776222pt"/> is always a multiple of <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/>.

4. In the previous discussion we used the fact that if <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> are relatively prime, then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> has a multiplicative inverse modulo <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>; that is, there exists <img alt="$a^{-1}\in \mathbb{Z}/m$" src="svgs/aa1f57396e688f3977a4394d3829566c.svg" valign=-4.109589000000009px width="80.04000015pt" height="17.4904653pt"/> such that <img alt="$a^{-1}a=1 \mod m$" src="svgs/d23399681b00a63da8212e00b487087d.svg" valign=0.0px width="127.54161914999999pt" height="13.380876299999999pt"/>. Above we only needed its existence but what is <img alt="$a^{-1}$" src="svgs/b42707f02d6a6fbbe96ce85d2d4ab42c.svg" valign=0.0px width="25.515722099999987pt" height="13.380876299999999pt"/> if <img alt="$a=123456789$" src="svgs/afa5f8f36ba3ce9a1f38d9fd25e4434b.svg" valign=0.0px width="104.57966969999998pt" height="10.5936072pt"/> and <img alt="$m=2^{64}?$" src="svgs/a03fbd5ed34bcedfd4082b5e04a8c412.svg" valign=0.0px width="66.25953344999999pt" height="13.380876299999999pt"/>

Notes:
* In addition to **Zmod** (introduced above), numlib functions such as **gcd**,
  **xgcd**, **factor**, **isprime** may be helpful for some of the exercises. To get
  help on a function and see example usage, start the Python interpreter and
  **import numlib as nl**, and then issue a command such as **help(nl.xgcd)**.
  To see all objects defined in numlib, type **nl.** and hit the TAB key twice.
* If speed is of the essence, replace **lcg.py** with the following. (This is functionally
  equivalent but a little over twice as fast without the overhead of numlib.)
  ```python
  m = 2**64
  a = 123456789
  c = 12121212121
  state = 10**10+1

  def prng():
      """Return the next sequential integer between 0 and m-1, inclusive."""
      global state
      state = (a * state + c) % m
      return state
  ```

A common initial test to gauge whether a given PRNG is *not* worthy of the term
"random" employs the
[Chi-squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution),
and works as follows.

Suppose that we partition the possible outputs into a small number of *cells* (or
*bins*). We can then use the LCG to generate a large sample of values and tally
how many land in each bin.

```python
from lcg import prng

sample_size = 12000
bins = 30

# let us split the sampled random numbers into equal bins
sample = [prng()//(2**64//bins) for _ in range(sample_size)]

def get_frequencies():
    """return the list of frequencies for successive bins"""
    frequencies = dict()
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    return list(frequencies.values())

print(*get_frequencies())
```
The output is
```python
410 401 448 376 398 388 399 408 410 371 402 395 388 412 389 422 410 406 412 398 404 404 395 364 408 390 416 369 420 387
```
The generated numbers appear to be fairly evenly distributed
across the 30 bins so that our PRNG appears to sample *uniformly*.  On the
other hand, note that we should be concerned if each bin contained exactly the
same number (400) of sample values; we wouldn't expect that even from an
actual (uniform) random number generator.

One way to analyze whether we have enough, but not too much, variation in
the frequencies is to compute the test statistic

<p align="center"><img alt="$$\widetilde{\chi}^2=\frac{1}{400}\sum (f_i - 400)^2,$$" src="svgs/1677857c4c0df1f93f1cc9e57600904b.svg" valign=0.0px width="177.65995005pt" height="32.990165999999995pt"/></p>

where <img alt="$f_i$" src="svgs/9b6dbadab1b122f6d297345e9d3b8dd7.svg" valign=-3.1963503000000055px width="12.69888674999999pt" height="14.611878599999999pt"/> is the observed frequency of values falling in the <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg" valign=0.0px width="5.663225699999989pt" height="10.84150485pt"/>th bin.
For a legitimate PRNG, this statistic follows a chi-square distribution with
degrees of freedom equal to one less than the number of bins.

The sampling distribution (over 5000 samples) for the <img alt="$\widetilde{\chi}^2$" src="svgs/3ceecab1c4459bcbc669891b2b81a671.svg" valign=-3.1963503000000086px width="16.837900199999993pt" height="16.5772266pt"/>
statistic for our PRNG looks like this (superimposed with the <img alt="$\chi^2$" src="svgs/a67d576e7d59b991dd010277c7351ae0.svg" valign=-3.1963503000000086px width="16.837900199999993pt" height="16.5772266pt"/> distribution
with appropriate degrees of freedom):

<p align="center">
  <img height="400" src="images/chisq.svg">
</p>

(The program [chisq_hist.py]() generates and displays the histogram above.)

Were the sampling distribution to precisely follow the <img alt="$\chi^2$" src="svgs/a67d576e7d59b991dd010277c7351ae0.svg" valign=-3.1963503000000086px width="16.837900199999993pt" height="16.5772266pt"/> distribution,
then the lower 5 percent of values would fall in the interval <img alt="$[0, 17.71]$" src="svgs/53c00e8e3c8d36bcf72471ab2d2841aa.svg" valign=-4.109589000000009px width="62.10060284999999pt" height="16.438356pt"/>, the
second lowest 5 percent in <img alt="$[17.71, 19.77]$" src="svgs/29e6c48eeff07e575a415fd40f1c6810.svg" valign=-4.109589000000009px width="91.32445409999998pt" height="16.438356pt"/>, and so on.  An easy way to get these
values in Python is to install [scipy](https://scipy.org/) and use it as follows.

```python
from scipy import stats
percentiles = [round(.05*n, 2) for n in range(20)] # [0.0, 0.05, 0.1, 0.15, ..., 1.0]
[round(stats.chi2.ppf(x, df = 29), 2) for x in percentiles]
# [0.0, 17.71, 19.77, 21.25, 22.48, 23.57, 24.58, 25.54, ..., 42.56, inf]
```

The quality of one's PRNG comes into question if the bottom or top 5 percent
of the sampling distribution is too heavy (since then the corresponding
hypothesis tests would provide evidence of non-randomness); likewise, one
becomes *somewhat* concerned if the bottom or top 10 percent is too heavy (see
[Knuth](#references1) pg. 47).

Drawing a sample, computing the test statistic above, and interpreting that
(along the lines of the previous paragraph) in the context of say a hypothesis test
would be considered a *local* test in the sense that are sample usually does not include
all of the random numbers spit out by our PRNG  &mdash; even though one should always
use a fairly large sample size for a chi-squared test.

We can bump this up to more of a *global* test if we take say 5000 samples
(each still with sample size of 12000).
Here is the relevant bar chart for our LCG where the expected frequency for
each interval is 250.

<p align="center">
  <img height="400" src="images/chisq_chisq.svg">
</p>

The raw frequencies are

```python
255 260 239 278 261 254 256 234 251 252 220 237 255 248 251 254 242 245 235 273
```
which we can use to perform the so-called *chi-squared on chi-squared* test, the
idea being to check if those latest frequencies are more-or-less what they should be.
The degrees of freedom for the <img alt="$\chi^2$" src="svgs/a67d576e7d59b991dd010277c7351ae0.svg" valign=-3.1963503000000086px width="16.837900199999993pt" height="16.5772266pt"/> distribution appropriate for our chi-squared
on chi-squared test is <img alt="$30-20-1 = 9.$" src="svgs/35424cbb8185e419dbb3279a6e71d4c3.svg" valign=-1.3698745499999938px width="115.98149309999998pt" height="11.96348175pt"/>

The test statistic is <img alt="$13.688$" src="svgs/dee13aa9f323d25a42aca3c7b1b80005.svg" valign=0.0px width="45.66227159999998pt" height="10.5936072pt"/>. The area to the right under the <img alt="$\chi^2$" src="svgs/a67d576e7d59b991dd010277c7351ae0.svg" valign=-3.1963503000000086px width="16.837900199999993pt" height="16.5772266pt"/> distribution
with df=9 is <img alt="$0.13$" src="svgs/619592087e8219141eb96df340222866.svg" valign=0.0px width="29.22385289999999pt" height="10.5936072pt"/>. Hence, in a right-tailed hypothesis test with a 10% cutoff, we
fail to reject the null hypothesis that our LCG (globally) generates random numbers.

#### Exercises (optional)
5. The histogram and analysis above look pretty good but the original sampling was always split into 30 bins. Conduct the same sort of <img alt="$\chi^2$" src="svgs/a67d576e7d59b991dd010277c7351ae0.svg" valign=-3.1963503000000086px width="16.837900199999993pt" height="16.5772266pt"/> analysis but use different (smallish) numbers of bins and varying (large) sample sizes.

6. Replace our LCG with a Python's random number generator and compare.
     The following might be helpful.
     ``` python
     import random
     def prng():
         return random.randint(0, 2**64-1)
     ```

The [spectral test](https://en.wikipedia.org/wiki/Spectral_test) is the test
most likely to uncover weakness in a LCG. For this test, we first
use the LCG to successively generate points in 2-space:
<img alt="$(x_0, x_1), (x_1, x_2), \ldots$" src="svgs/e9d55cbd2cc4d57d6a13a807ff73df76.svg" valign=-4.109589000000009px width="141.05018069999997pt" height="16.438356pt"/> where <img alt="$x_0, x_1, x_2, \ldots$" src="svgs/fda0e4fdacdd806c1f6c8b2af0ce68da.svg" valign=-3.1963502999999895px width="91.40398244999999pt" height="10.2739725pt"/> is the pseudo-random
sequence kicked out by our LCG.  Here we have tacitly divided each <img alt="$x_n$" src="svgs/d7084ce258ffe96f77e4f3647b250bbf.svg" valign=-2.4657286499999893px width="17.521011749999992pt" height="9.54335085pt"/> by <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> so
that the 2D points in fact lie in the unit square <img alt="$[0,1]\times [0,1].$" src="svgs/895386960ce4e2b78a141073901b8e71.svg" valign=-4.109589000000009px width="90.41091509999998pt" height="16.438356pt"/>

Due to periodicity, only a finite number of distinct points will be
produced; hence, all the points can be captured by a set of parallel lines.
The maximum distance between the lines, over all arrangements of such sets of
lines, is the number in which we are interested, call it <img alt="$d_2$" src="svgs/25eda7b7741f869a00061a631b356db9.svg" valign=-2.4657286500000066px width="15.10851044999999pt" height="13.881256950000001pt"/>.

In fact, we want to bump up the scheme outlined above to higher dimensions;
that is, we want to compute the maximum distance, <img alt="$d_3$" src="svgs/c3fa8de7a8089002ea5653ad6b67aa67.svg" valign=-2.4657286500000066px width="15.10851044999999pt" height="13.881256950000001pt"/>, between parallel planes
over all arrangements in 3-space that capture all of
<img alt="$(x_0, x_1, x_2), (x_1, x_2, x_3), \ldots$" src="svgs/b38aa07e6131068bec11e42928de000a.svg" valign=-4.109589000000009px width="189.20084369999998pt" height="16.438356pt"/>, and so on up to the maximum
distance, <img alt="$d_7$" src="svgs/64b2437b794d4a3c8ee3812f039898de.svg" valign=-2.4657286500000066px width="15.10851044999999pt" height="13.881256950000001pt"/>, between 6-dimensional parallel hyperplanes that capture all points
constructed from our sequence in 7-space.

The maximum distances <img alt="$d_2, d_3, \ldots, d_7$" src="svgs/0a73c30cfdb1fd3eebfe5b2263c9bc7d.svg" valign=-3.1963503000000055px width="90.80465624999998pt" height="14.611878599999999pt"/> will all be positive since
our LCG is periodic so that each set of parallel planes need only capture
a finite number of points. Also, the distances <img alt="$d_t$" src="svgs/ccc82fe267d4bb138ce39c263e5264f4.svg" valign=-2.4657286500000066px width="13.52175494999999pt" height="13.881256950000001pt"/> necessarily increase with the
dimension <img alt="$t.$" src="svgs/f942031b7fb6eec9c50bd70766082b86.svg" valign=0.0px width="10.50232094999999pt" height="10.110901349999999pt"/>  Heuristically, this is due to the fact that <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> more-or-less
evenly distributed points in, for instance, 3-space are necessarily more spread
out than <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> such points in 2-space.

The idea behind the spectral test is that, were the coordinates of the points drawn
from a truly random sequence of numbers in <img alt="$[0,1],$" src="svgs/0ae2faac7f0b6f04f2d00a80b1a93c95.svg" valign=-4.109589000000009px width="37.44297479999999pt" height="16.438356pt"/> the numbers <img alt="$d_2,\ldots, d_7$" src="svgs/dd820c16ce8477afe22065e05d11258a.svg" valign=-3.1963503000000055px width="67.56834975pt" height="14.611878599999999pt"/>
would each still of course be positive due to finite machine precision, but they would
not increase with <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>.

Returning to the case in which the <img alt="$x_i$" src="svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg" valign=-2.4657286499999893px width="14.045887349999989pt" height="9.54335085pt"/> are generated by our LCG, we wish to
compute the distances <img alt="$d_t$" src="svgs/ccc82fe267d4bb138ce39c263e5264f4.svg" valign=-2.4657286500000066px width="13.52175494999999pt" height="13.881256950000001pt"/> and see if they are sufficiently close to zero. Since
our LCG is based on a linear function, we are naturally led to consider
a lattice of points in <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>-space ([Knuth](#references1) pp. 96-98).  And when
considering families of parallel hyperplanes that capture all points, we can assume
that neighboring hyperplanes are separated by a fixed distance which is of course
the desired <img alt="$d_t$" src="svgs/ccc82fe267d4bb138ce39c263e5264f4.svg" valign=-2.4657286500000066px width="13.52175494999999pt" height="13.881256950000001pt"/>.

[Knuth](#references1) and other authors consider the *accuracy*, defined
by <img alt="$v_t = 1/d_t.$" src="svgs/a512957582c7c90107a734f18e641bdc.svg" valign=-4.109589000000009px width="71.02167929999999pt" height="16.438356pt"/> (The quantity <img alt="$v_t$" src="svgs/3e3c6ee78813607a4d976d92c19dd36e.svg" valign=-2.4657286499999893px width="12.93385829999999pt" height="9.54335085pt"/> arises naturally in the sense that it
is the vector of minimal length in the dual of the lattice mentioned above;
cf. [Steele, Vigna](#references1) pp. 3-4.)

If <img alt="$0&lt;a&lt;m$" src="svgs/c723c4986c981ef012a4915ad205d443.svg" valign=-0.6427030499999951px width="75.17672579999999pt" height="11.23631025pt"/> and <img alt="$\gcd(a,m)=1$" src="svgs/1adf9488b49d92d50d2bf48e91e9db53.svg" valign=-4.109589000000009px width="98.00799524999998pt" height="16.438356pt"/>, then the accuracy <img alt="$v_t$" src="svgs/3e3c6ee78813607a4d976d92c19dd36e.svg" valign=-2.4657286499999893px width="12.93385829999999pt" height="9.54335085pt"/> admits
a concise characterization:

<p align="center"><img alt="$$v_t = \min_{(x_1, \ldots, x_t)\in \mathbb{Z}^t}\left\{\sqrt{x_1^2+\cdots+x_t^2}~\bigg|~ x_1+ax_2+\cdots+a^{t-1}x_t = 0 \mod m\right\}$$" src="svgs/6b278b078eaedfdf630e6089ea42b119.svg" valign=0.0px width="533.56444185pt" height="39.45246194999999pt"/></p>

where the minimum is over all non-zero vectors with integer coefficients.

However, if <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is large, then even <img alt="$v_2$" src="svgs/53292819177dbb29ba6d92fe3aa2880c.svg" valign=-2.4657286499999893px width="14.520613799999989pt" height="9.54335085pt"/> can be difficult to brute-force compute.
[Knuth](#references1) (pg. 102) gives the following 3-step algorithm to
compute <img alt="$v_2$" src="svgs/53292819177dbb29ba6d92fe3aa2880c.svg" valign=-2.4657286499999893px width="14.520613799999989pt" height="9.54335085pt"/> (the algorithm for <img alt="$v_t,$" src="svgs/bec5cc0fb02e3c5d7aef2bfaa739ad93.svg" valign=-3.1963502999999895px width="18.32197784999999pt" height="10.2739725pt"/> <img alt="$t&gt;2,$" src="svgs/c44c088d3144b176acdcb65339ca5d09.svg" valign=-3.196350299999994px width="40.639161749999985pt" height="13.789957499999998pt"/> is more involved):

1. Initialize variables <img alt="$h, h', p, p', r$" src="svgs/1885ee8b398072d6a6882c6f3fa76090.svg" valign=-3.1963502999999998px width="81.80360099999999pt" height="15.5544147pt"/> and <img alt="$s$" src="svgs/6f9bad7347b91ceebebd3ad7e6f6f2d1.svg" valign=0.0px width="7.7054801999999905pt" height="7.0776222pt"/> as follows. Set <img alt="$h\leftarrow a,$" src="svgs/ba4d90f8718a9abf7abdc256257f82b8.svg" valign=-3.1963503000000055px width="48.297093899999986pt" height="14.611878599999999pt"/> <img alt="$h'\leftarrow m,$" src="svgs/5bd097ec7dc5155686a2d7bf871c06eb.svg" valign=-3.1963502999999998px width="58.652914649999985pt" height="15.5544147pt"/> <img alt="$p \leftarrow 1,$" src="svgs/762aa9943ae65b43dc6702d7e9eef128.svg" valign=-3.196350299999994px width="46.62660089999999pt" height="13.789957499999998pt"/> <img alt="$p' \leftarrow 0,$" src="svgs/54636acb26ede68ecbed257f91ad3d41.svg" valign=-3.1963502999999998px width="51.238476299999995pt" height="15.5544147pt"/> <img alt="$r \leftarrow a,$" src="svgs/9600fe34955bb4ac4f4ed288780d8cb9.svg" valign=-3.1963502999999895px width="46.69893359999999pt" height="10.2739725pt"/> <img alt="$s \leftarrow 1+a^2.$" src="svgs/ee0e89fee5aa88e5e5e7bede8ae5347a.svg" valign=-1.3698729000000083px width="82.21631879999998pt" height="14.750749199999998pt"/>
2. Next, set <img alt="$q\leftarrow \lfloor h'/h \rfloor,$" src="svgs/20f9396d3e1d3d90cd913fdb47f07f4b.svg" valign=-4.109589px width="84.45013664999999pt" height="16.4676534pt"/> <img alt="$u \leftarrow h'-qh,$" src="svgs/45c1459d617e1a1df58883ec459ea7ba.svg" valign=-3.1963502999999998px width="91.12047944999999pt" height="15.5544147pt"/> <img alt="$v\leftarrow p'-qp.$" src="svgs/f5a827340b26f056a5af8ae5095d49a6.svg" valign=-3.1963502999999998px width="87.86695334999999pt" height="15.5544147pt"/>  If <img alt="$u^2+v^2&lt; s,$" src="svgs/5827192c35bdb75e01cc8d501d9ece8f.svg" valign=-3.1963503000000086px width="86.99756009999999pt" height="16.5772266pt"/> then set <img alt="$s=u^2+v^2,$" src="svgs/90f43f71c97f37f079138ea519b368c1.svg" valign=-3.1963503000000086px width="86.99756009999999pt" height="16.5772266pt"/> <img alt="$h'\leftarrow h,$" src="svgs/f6e10c172fced41e9a7ac13da86c3f42.svg" valign=-3.1963502999999998px width="53.69092904999999pt" height="15.5544147pt"/> <img alt="$h\leftarrow u,$" src="svgs/c575e4d4e508df4cf341ac223d82b5fc.svg" valign=-3.1963503000000055px width="49.01821154999999pt" height="14.611878599999999pt"/> <img alt="$p'\leftarrow p,$" src="svgs/085036e3e0786da85023f02800a628c9.svg" valign=-3.1963502999999998px width="51.289832549999986pt" height="15.5544147pt"/> <img alt="$p\leftarrow v$" src="svgs/083dc0bd63a15acb5b7632eb8f31eaea.svg" valign=-3.1963502999999895px width="42.39902699999999pt" height="10.2739725pt"/> and repeat step 2; otherwise, go to step 3.
3. Set <img alt="$u\leftarrow u -h,$" src="svgs/8dd82d2e01b67312a699f263c90efc69.svg" valign=-3.1963503000000055px width="78.51967529999999pt" height="14.611878599999999pt"/>  <img alt="$v \leftarrow v-p.$" src="svgs/aac212b5f4c9719c04914d025c537f23.svg" valign=-3.19635195px width="75.61426619999999pt" height="12.785402849999999pt"/> If <img alt="$u^2+v^2&lt; s,$" src="svgs/5827192c35bdb75e01cc8d501d9ece8f.svg" valign=-3.1963503000000086px width="86.99756009999999pt" height="16.5772266pt"/> then set <img alt="$s=u^2+v^2.$" src="svgs/cac28d8f2bc47c77c010e1e8adaa2901.svg" valign=-1.3698729000000083px width="86.99756009999999pt" height="14.750749199999998pt"/> Output <img alt="$\nu_2 = \sqrt{s}.$" src="svgs/693647fc4ca168023923d273eca84673.svg" valign=-3.940686749999999px width="63.382738649999986pt" height="16.438356pt"/>

How are the numbers <img alt="$v_j$" src="svgs/50d9c77ead499fc4f5d70cbdd9320f1f.svg" valign=-4.7031731999999895px width="14.07257609999999pt" height="11.780795399999999pt"/> used to determine which LCG perform best? We want the <img alt="$d_t,$" src="svgs/10cd08470937e1ffdd2da17b17f31ab6.svg" valign=-3.1963503000000055px width="18.90987614999999pt" height="14.611878599999999pt"/>
<img alt="$t=2, \ldots, 7,$" src="svgs/2694751a2a66535c88159d27b3a87245.svg" valign=-3.196350299999994px width="85.38778709999998pt" height="13.789957499999998pt"/> to be small, though they will necessarily increase with <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/> even
if for good performing LCGs. Since <img alt="$v_t=1/d_t,$" src="svgs/90bad28f438c91af8e9992305f6f4834.svg" valign=-4.109589000000009px width="71.02167929999999pt" height="16.438356pt"/> we want the <img alt="$v_t$" src="svgs/3e3c6ee78813607a4d976d92c19dd36e.svg" valign=-2.4657286499999893px width="12.93385829999999pt" height="9.54335085pt"/> to be large.
[Knuth](#references1) (pg. 105) gives the following rule of thumb: <img alt="$v_t\ge 2^{30/t}.$" src="svgs/70240927e39634bd74c06c1497951c51.svg" valign=-2.465728649999995px width="74.08676219999998pt" height="17.06121615pt"/>

#### Exercises
7. Show that <img alt="$v_t \le \sqrt{a^2+1}$" src="svgs/793f20875748a755f466bb3c43c5e213.svg" valign=-2.465728650000001px width="93.74607164999999pt" height="16.821868799999997pt"/> for all <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>.
8. Implement the algorithm above and use it to compute the accuracy <img alt="$v_2$" src="svgs/53292819177dbb29ba6d92fe3aa2880c.svg" valign=-2.4657286499999893px width="14.520613799999989pt" height="9.54335085pt"/> for our LCG
(for which <img alt="$a=123456789$" src="svgs/afa5f8f36ba3ce9a1f38d9fd25e4434b.svg" valign=0.0px width="104.57966969999998pt" height="10.5936072pt"/> and <img alt="$m=2^{64}$" src="svgs/2c0d775f4ac8a5e8615cdf9cf2c1db95.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/>).

Now, since <img alt="$m=2^{64}$" src="svgs/2c0d775f4ac8a5e8615cdf9cf2c1db95.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/> is so large, many smallish choices of the multiplier <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> immediately
determine <img alt="$v_2.$" src="svgs/364b4e2317b6fc37a867cc1973183caa.svg" valign=-2.4657286499999893px width="19.90874984999999pt" height="9.54335085pt"/>  In fact, according to [Steele, Vigna](#references1), Proposition 1,
for a full period LCG with modulus <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and multiplier <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/>, one has <img alt="$v_t=\sqrt{a^2+1}$" src="svgs/3041b8e626d87f07d501018d8df06213.svg" valign=-2.465728650000001px width="93.74607164999999pt" height="16.821868799999997pt"/>
whenever <img alt="$a&lt;\sqrt[t]{m};$" src="svgs/93a28b794675fc4f3adb3a6107926aca.svg" valign=-3.940686749999999px width="63.37152689999999pt" height="16.438356pt"/> and this is true for all <img alt="$t\ge 2$" src="svgs/d0ee488bf730f627d5394f0bc3972ae5.svg" valign=-2.2351411499999947px width="36.07293689999999pt" height="12.82874835pt"/>.

For large <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, [Knuth](#references1) (on page 105) proposes another quantity
called the *merit*,

<p align="center"><img alt="$$\mu_t=\frac{\pi^{t/2}v_t^t}{(t/2)!}$$" src="svgs/c921de9fc2c88fe6aaab46bc831bfc55.svg" valign=0.0px width="82.96383644999999pt" height="41.101633650000004pt"/></p>

where, if <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/> is odd, <img alt="$\left(\frac{t}{2}\right)! = \left(\frac{t}{2}\right)&#10;\left(\frac{t-1}{2}\right) \cdots \left(\frac{1}{2}\right) \sqrt{\pi}.$" src="svgs/4467628e209c91d40d7a1f539598e56c.svg" valign=-5.753531849999993px width="202.35048734999998pt" height="19.726228499999998pt"/>

The merit <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> is the volume of a certain ellipsoid (called a *figure of merit*)
in <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>-space:

<p align="center"><img alt="$$(x_1m-x_2a-\cdots-x_ta^{t-1})^2+x_2^2+\cdots+x_t^2 \le v_t^2.$$" src="svgs/f4c6ef94862fd49a38c1ffcc1a8f7e37.svg" valign=0.0px width="358.16528055pt" height="18.312383099999998pt"/></p>

If <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> is small, say <img alt="$\mu_t&lt;0.1$" src="svgs/c38405962bf08af010a310c68f2a0bdd.svg" valign=-3.196350299999994px width="58.614885449999996pt" height="13.789957499999998pt"/>, then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is not a good
multiplier because said ellipsoid is unlikely to capture points corresponding
to random numbers generated by our LCG.  If <img alt="$\mu_t&gt;0.1$" src="svgs/b533f731e0256a92cfe5fe47fd15c732.svg" valign=-3.196350299999994px width="58.614885449999996pt" height="13.789957499999998pt"/> or, better, <img alt="$\mu_t&gt;1.0$" src="svgs/46dc8ee9f162c24e5faa3d3629f7384d.svg" valign=-3.196350299999994px width="58.614885449999996pt" height="13.789957499999998pt"/>,
then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is a good multiplier.

The advantage of looking at <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> instead of just <img alt="$v_t$" src="svgs/3e3c6ee78813607a4d976d92c19dd36e.svg" valign=-2.4657286499999893px width="12.93385829999999pt" height="9.54335085pt"/> is that <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> can
be used to compare different multipliers for a fixed <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/>  For instance, with
<img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> fixed at <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/>, we wish to find a multiplier <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> with not only <img alt="$\nu_2,$" src="svgs/c44c5c5de2f9993727644e337ce1dca2.svg" valign=-3.1963502999999895px width="20.06095739999999pt" height="10.2739725pt"/>
but also <img alt="$\mu_2,$" src="svgs/8615699836ecb78ef8a53e8d3263850c.svg" valign=-3.1963502999999895px width="21.84560729999999pt" height="10.2739725pt"/> sufficiently large relative to other multipliers.

#### Exercises
9. Compute <img alt="$\mu_2$" src="svgs/d9324c21b00105263d6f54123813d99c.svg" valign=-3.1963502999999895px width="16.45747124999999pt" height="10.2739725pt"/> for our LCG; i.e., <img alt="$a=123456789,$" src="svgs/7543ddf5c75fb86912c49588ae0fd6e2.svg" valign=-3.196350299999994px width="109.14589289999998pt" height="13.789957499999998pt"/> <img alt="$m=2^{64}.$" src="svgs/a404936c9122ffe075a49b205e698627.svg" valign=0.0px width="63.063166649999985pt" height="13.380876299999999pt"/> Is <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> a good multiplier based on <img alt="$\mu_2$" src="svgs/d9324c21b00105263d6f54123813d99c.svg" valign=-3.1963502999999895px width="16.45747124999999pt" height="10.2739725pt"/>?
10. What if we leave the modulus at <img alt="$m = 2^{64}$" src="svgs/c7fdaf695852cd6459cc4165d25b86b2.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/> but take the multiplier to be <img alt="$a = 214319739410341?$" src="svgs/db48c9add022da5915966d599ffd43c7.svg" valign=0.0px width="161.65751579999997pt" height="11.4155283pt"/> Is this <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> a good multiplier? (This multiplier is recommended in [Steele, Vigna](#references1) on pg. 18.)
11. (Optional) When <img alt="$m = 2^{64}$" src="svgs/c7fdaf695852cd6459cc4165d25b86b2.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/> and <img alt="$a = 214319739410341,$" src="svgs/606b90321a4de27fee5b52d2a117a902.svg" valign=-3.196350299999994px width="158.46115064999998pt" height="13.789957499999998pt"/> find <img alt="$\nu_t$" src="svgs/b96ce619e9618788ad604f351c957414.svg" valign=-2.4657286499999893px width="13.08606584999999pt" height="9.54335085pt"/> for <img alt="$3 \le t \le 6$" src="svgs/a1b101a367cf06ca257ded541b352ac1.svg" valign=-2.2351411499999947px width="66.20977769999999pt" height="12.82874835pt"/> by either directly implementing the algorithm in [Knuth](#references1) or by comparing
with the definitions and listed values in [Steele, Vigna](#references1).
Also compute <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> for <img alt="$3 \le t \le 6.$" src="svgs/4572a9d4690118768057d1b4e6e1f08a.svg" valign=-2.2351411499999947px width="70.77600089999999pt" height="12.82874835pt"/> What do those gauges say about the randomness of our LCG?
12. (Optional) [Steele, Vigna](#references1) recommends the smaller multiplier <img alt="$a = 15828829061$" src="svgs/306767c88ebd3a3b9965443894593881.svg" valign=0.0px width="121.0180884pt" height="10.5936072pt"/> (where still <img alt="$m = 2^{64})$" src="svgs/f27dc0f5c226f6b1999562f2658836c1.svg" valign=-4.109589000000009px width="64.88965889999999pt" height="17.4904653pt"/>; hence, let us assume that value for <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> leads to good performance on all spectral tests. But show that it rejected by the chi-square on chi-square test above.

In addition to the chi-squared and spectral tests, there are several other
commonly applied tests to assess the performance of an LCG or, more generally,
a PRNG.  The *Kolmogorov-Smirnov* test works well with small sample sizes and therefore
applies locally but perhaps not globally (to the entire cycle of ones PRNG) &mdash;
unless one uses a *Kolmogorov-Smirnov on Kolmogorov-Smirnov* test.

Similarly global tests may not apply locally.  The spectral test (discussed above)
looks at the complete cycle and hence applies globally, but that alone has nothing
to do with non-randomness.  In our case the complete cycle as a set is just the
numbers from <img alt="$0$" src="svgs/29632a9bf827ce0200454dd32fc3be82.svg" valign=0.0px width="8.219209349999991pt" height="10.5936072pt"/> to <img alt="$2^{64}-1.$" src="svgs/70919d0639b61c93f2ba69ed9151b157.svg" valign=-1.3698729000000083px width="55.022835449999995pt" height="14.750749199999998pt"/>
In the spectral test the *order* of the numbers determines the location of the points
in 2-, 3-, 4-dimensional, etc., space.  (If we did a spectral test in 1-space, we would
get simply <img alt="$d_1=\nu_1=1.$" src="svgs/1608b7b22440e2629345d65cc6ab25bf.svg" valign=-2.4657286500000066px width="88.04585129999998pt" height="13.881256950000001pt"/>)

In modern times, researchers might perform a deeper analysis by applying a spectral
test to sequences with lag <img alt="$\ell$" src="svgs/d30a65b936d8007addc9c789d5a7ae49.svg" valign=0.0px width="6.849367799999992pt" height="11.4155283pt"/> &mdash; for an LCG where the lag is
<img alt="$\ell=3$" src="svgs/324bb9a44b26d043ac3a75823ee59f2b.svg" valign=0.0px width="36.98620694999999pt" height="11.4155283pt"/>, one would apply the spectral test to, for instance, points in 3-space that
look like <img alt="$(x_0,x_2,x_4),(x_1, x_3, x_5),\ldots.$" src="svgs/714736f073b3fb5998266181214e88a2.svg" valign=-4.109589000000009px width="196.5067269pt" height="16.438356pt"/>

The spectral test is a *theoretical* test in the sense that we has an algorithm
for computing <img alt="$\nu_t$" src="svgs/b96ce619e9618788ad604f351c957414.svg" valign=-2.4657286499999893px width="13.08606584999999pt" height="9.54335085pt"/> and <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> before even implementing the actual PRNG.  Meanwhile,
the chi-squared and Kolmogorov-Smirnov test are *empirical* in that we first implement
the our LCG and perform statistical test on samples drawn from it.

### Cryptographic security

The discussion and exercises above did not turn up evidence of non-randomness for the
following LCG.

```python
m = 2**64
a = 214319739410341
c = 12121212121
state = 10**10+1

def prng():
    """Return the next sequential integer between 0 and m-1, inclusive."""
    global state
    state = (a * state + c) % m
    return state
```
The LCG above is still, at least, a candidate for a viable PRNG (Pseudo-random number
generator). But what does pseudorandom really mean?

In Computational Complexity Theory, a distribution is *pseudorandom* against a class of
*adversaries* if no adversary (think of an adversary as an algorithm or a test or some
other *distinguisher* or *observer*) from the class can distinguish it (with not
insignificant advantage) from the uniform distribution.

This concept that certain adversaries cannot distinguish a high-quality PRNG from a
uniform distribution corresponds to our intuitive notion of pseudorandom numbers
*looking like* random numbers. The difference, in cryptography, is that the numbers
*must* be indistinguishable from random number for *all* adversaries, even ones with
advance computation capabilities.


<a id="references1">

#### References

* Donald Knuth, The Art of Computer Programming, 3rd Edition,
  Volume 2: Seminumerical Algorithms, 1998.
* Guy Steele and Sebastian Vigna, Computationally Easy, Spectrally Good
  Multipliers for Congruential PseudoRandom Number Generators.
  [arxiv.org/abs/2001.05304](https://arxiv.org/abs/2001.05304), 2021.

## Number-theoretic practicalities

### Prime fields

Note that <img alt="$2\cdot 11 = 1$" src="svgs/e927310f36765b5ad74fbd34bdb938dd.svg" valign=0.0px width="66.66644984999998pt" height="10.5936072pt"/> modulo 21 so that 2 has 11 as its multiplicative inverse in
<img alt="$\mathbb{Z}/21.$" src="svgs/3731d4bdedc964b8cdbf897e6ea86d26.svg" valign=-4.109589000000009px width="40.18279319999999pt" height="16.438356pt"/>  Meanwhile, in <img alt="$\mathbb{Z}/21,$" src="svgs/e4c03b084fef61df3489a70d833a595b.svg" valign=-4.109589000000009px width="40.18279319999999pt" height="16.438356pt"/> 3 can have no multiplicative inverse
since it is a zero divisor : <img alt="$3\cdot 7 = 0 \mod 21.$" src="svgs/4b23d5a39780a9df7da266ffb9e76e31.svg" valign=0.0px width="127.39679699999998pt" height="11.4155283pt"/>

A commutative ring (such as <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/>) for which every non-zero element has a
multiplicative inverse, is called a *field*.

#### Exercises
12. Show that <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> is a field if and only if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is prime.
13. Show that multiplicative inverses in <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> are unique.

Above we used the numlib function **Zmod** to create a class representing <img alt="$\mathbb{Z}/n,$" src="svgs/4ee8f29e8fc6ff907c10277ad56123ba.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>
where <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> may or may not be prime.  We often want to work in prime field so we pick <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>
to be a prime, <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>.  Then, it is best to go ahead tell that to numlib, by using **Zmodp**
instead of **Zmod** (because the resulting class is then faster and has more functionality).

Here is an example.

```pycon
>>> import numlib as nl
>>> PF = nl.Zmodp(2027)
>>> PF  # Z/2027
>>> x = PF(100)
>>> x   # 100 + <2027>
>>> x**1000  # 2022 + <2027>
>>> x**-1  # 750 + <2027>
```

### Generating primes

We will need some fairly large prime numbers &mdash; 200 bits, say, for now; so primes of size
around <img alt="$2^{200}.$" src="svgs/8ead495e1e0f713f33e7a75e00656907.svg" valign=0.0px width="33.264976799999985pt" height="13.380876299999999pt"/>

One way to generate such a prime would be to iterate through numbers larger that <img alt="$2^{200}$" src="svgs/acc9da0b19643e432619eb386d21261f.svg" valign=0.0px width="27.87685064999999pt" height="13.380876299999999pt"/> until we
find one that is prime.  Alternatively, one could randomly generate sequences of zeros and ones of
length 200 and check if the corresponding decimal number is prime.  Python has a built-in function that
generates an integer from random bits:

```python
import random
decimal = random.getrandbits(200)
```
Of course, depending on whether the most significant random bit is zero or one, we might get a number somewhat
less than <img alt="$2^{200};$" src="svgs/e46661a0be2003a6fba87fa4a557cf10.svg" valign=-3.1963503000000086px width="33.264976799999985pt" height="16.5772266pt"/> so let us set the most significant bit to one and, while we are at it, set
also the least significant bit to 1 since primes beyond 2 must be odd:
```python
decimal |= (1 << numbits - 1) | 1
```
The variable **decimal** is now an integer whose binary representation has length 200 and both begins
and ends with 1; i.e., **decimal** is a random (depending on the robustness of **getrandbits**)
odd integer strictly between <img alt="$2^{200}$" src="svgs/acc9da0b19643e432619eb386d21261f.svg" valign=0.0px width="27.87685064999999pt" height="13.380876299999999pt"/> and <img alt="$2^{201}.$" src="svgs/26851296087784570cb81e1034cdb3f0.svg" valign=0.0px width="33.264976799999985pt" height="13.380876299999999pt"/>

Beyond using the fact that a prime larger than 2 must be odd, there are various other quick ways
to test whether a candidate large, odd integer <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is *likely* prime.  These include
[Fermat's primality test](https://en.wikipedia.org/wiki/Fermat_primality_test) which checks to see
if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> *acts like* a prime: namely, whether <img alt="$a^{n-1} = 1 \mod n$" src="svgs/7e196034fb79710624494a8bb1d4813b.svg" valign=0.0px width="122.41226084999998pt" height="13.380876299999999pt"/> for <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> equal,
in turn, to say 2, 3, and 5, as would be the case, by Fermat's Little Theorem (see below), if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>
were in fact prime.

Rather than implement Fermat's and related primality tests yourself to detect whether **decimal** is prime,
feel free to use [numlib](https://github.com/sj-simmons/numlib)'s implementation:

```python
import numlib
numlib.isprime(decimal) # True or False according to whether decimal is prime
```
#### Exercise
14. Replace the <img alt="$200$" src="svgs/88db9c6bd8c9a0b1527a1cedb8501c55.svg" valign=0.0px width="24.657628049999992pt" height="10.5936072pt"/> above with say <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> and write a function, using the scheme outlined above, that returns a <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit prime.

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
on average, one expects to test about <img alt="$1/p=k\ln(2)/2$" src="svgs/6c97d8dd61ac519e745292cae1789830.svg" valign=-4.109589000000009px width="109.5833706pt" height="16.438356pt"/> numbers before turning up one that is
indeed prime.

#### Exercise
15. Write a program that verifies that the expected number of tries before your function from exercise 1 returns a prime is about <img alt="$200\ln(2)/2\approx 69$" src="svgs/d593e0b8122513765f33fdc1e83baf49.svg" valign=-4.109589000000009px width="116.89507004999999pt" height="16.438356pt"/>.

Note: since <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> is small, the variance here is very large so that the time it takes for your
program to find a single prime can vary greatly; said variance is <img alt="$(1-p)/p^2 \approx 4735.2$" src="svgs/07b12faa29e1cf6d90eece6f9c72b99f.svg" valign=-4.109589000000009px width="140.81053799999998pt" height="17.4904653pt"/> so that
the standard deviation of the number of tries before finding a 200 bit prime is about <img alt="$68.8.$" src="svgs/6ce6d2d54a6388aaebd027e35aebb86b.svg" valign=0.0px width="33.79007609999999pt" height="10.5936072pt"/> (The
standard deviation is <img alt="$\sqrt{(1-p)/p^2},$" src="svgs/44ca9338a2247d7391f898c6588a020d.svg" valign=-5.013835199999992px width="94.23517949999999pt" height="19.726228499999998pt"/> which is approximately <img alt="$1/p$" src="svgs/b6bd4fb45663b60f83a799556b0eeffb.svg" valign=-4.109589000000009px width="24.70898594999999pt" height="16.438356pt"/> for small <img alt="$p.$" src="svgs/bb44dfbad95f04997776cfe375c4eac3.svg" valign=-3.1963502999999895px width="12.836790449999992pt" height="10.2739725pt"/>)

#### Exercises
16. What is the expected number of tries and the associated standard deviation when finding a 2048-bit
    prime.
17. (Optional) Write a program that displays the sampling distribution for the number of tries before
    finding prime using the method outlined above. The mean and standard deviation should both be
    about 69.

### Euler's phi function

This is a basic result:

**Fermat's Little Theorem**:  If <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> is a prime and <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is an integer not divisible by <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>, then <img alt="$a^{p-1} = 1 \mod p$" src="svgs/21079acb0231ed9b118814f30cfb192d.svg" valign=-3.1963503000000086px width="119.46638879999998pt" height="16.5772266pt"/>.

For those who know a little group theory this follows immediately from the fact that the order of
any element of a finite group must divide the order of the group. Here, the relevant group is
<img alt="$(\mathbb{Z}/p\mathbb{Z})^*,$" src="svgs/2d4a5869404cba9f337568cf3e5f6817.svg" valign=-4.109589000000009px width="63.31640369999999pt" height="16.438356pt"/> the multiplicative group of units in <img alt="$\mathbb{Z}/p\mathbb{Z},$" src="svgs/4eb71a5f1d780863eb3bf3c2cf2c59d0.svg" valign=-4.109589000000009px width="42.973882049999986pt" height="16.438356pt"/>
which has order <img alt="$p-1.$" src="svgs/2ad55de588e0025342173e657988d28d.svg" valign=-3.196350299999994px width="41.14719179999999pt" height="13.789957499999998pt"/>

If you are not familiar with basic group theory, then see for example
[this wikipedia page](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem)
for various other proofs of Fermat's Little Theorem.

#### Exercise
16. Use your program above to generate a 200-bit prime <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and then verify that the <img alt="$a^{p-1} \equiv 1 \mod p$" src="svgs/2e621949487c8c972e5637f0848ac82e.svg" valign=-3.1963503000000086px width="119.46638879999998pt" height="16.5772266pt"/> where <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is, say, 1234567, or any positive integer less than <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>. Note: you may wish to use Python's built-in [pow() function](https://docs.python.org/3/library/functions.html#pow).

Below we will need the following generalization of Fermat's Little Theorem.

**Euler's Theorem**:  If <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is positive integer and <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is an integer relatively prime to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>,
then <img alt="$a^{\phi(n)} = 1 \mod n.$" src="svgs/ded672b0ccf534dd49610fd693275d5e.svg" valign=0.0px width="128.3300799pt" height="14.5954875pt"/>

Here <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/> is Euler's Phi function which returns the number of positive integers less than
and relatively prime to <img alt="$n.$" src="svgs/ea8d90fb4a8d92af94283e10af3efb57.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>

Notice that Euler's Theorem specializes to Fermat's Little Theorem if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is prime since, then,
<img alt="$\phi(n)=n-1.$" src="svgs/1b0d94292d544c37a22b1f0f7f9a7b13.svg" valign=-4.109589000000009px width="97.10798459999998pt" height="16.438356pt"/>  Moreover, Euler's Theorem also follows from basic group theory where the ambient
group is <img alt="$(\mathbb{Z}/n\mathbb{Z})^*$" src="svgs/3864234dcb7744587a117c9e1a7290ea.svg" valign=-4.109589000000009px width="59.52459479999999pt" height="16.438356pt"/>, the multiplicative group of units in <img alt="$\mathbb{Z}/n\mathbb{Z}$" src="svgs/94d333ba0aaa5e9c8ce88690986075c2.svg" valign=-4.109589000000009px width="40.00396784999999pt" height="16.438356pt"/>,
which has order <img alt="$\phi(n).$" src="svgs/4b539e947954886e594105a91f42f29b.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/>

An *arithmetic* (i.e., defined on positive integers) function <img alt="$f$" src="svgs/190083ef7a1625fbc75f243cffb9c96d.svg" valign=-3.1963503000000055px width="9.81741584999999pt" height="14.611878599999999pt"/>  is *multiplicative*
if <img alt="$f(mn)=f(m)f(n)$" src="svgs/4397377cf2d4936bc7c8e91b31aa8d24.svg" valign=-4.109589000000009px width="138.3261231pt" height="16.438356pt"/> whenever <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime. For instance, Euler's Phi function,
<img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/>, is multiplicative &mdash; a fact which we will fairly easily establish using, yet again,
elementary group theory.

We noted above that the order of an element of a finite group necessarily divides the order of the
group.  For cyclic groups, this situation is particularly nice.  Let <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> be a cyclic group of order
<img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> (feel free to think <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/>, to which <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> is necessarily isomorphic). Let us show that
for any divisor <img alt="$\ell$" src="svgs/d30a65b936d8007addc9c789d5a7ae49.svg" valign=0.0px width="6.849367799999992pt" height="11.4155283pt"/> of <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, there are <img alt="$\phi(\ell)$" src="svgs/5f5759f7d5f03fa367a510e38faa9564.svg" valign=-4.109589000000009px width="29.429343899999992pt" height="16.438356pt"/> elements of <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> with order <img alt="$\ell.$" src="svgs/fb1f7152c7b8bdf9af1fe835ef63d16f.svg" valign=0.0px width="11.41559099999999pt" height="11.4155283pt"/>

If <img alt="$g$" src="svgs/3cf4fbd05970446973fc3d9fa3fe3c41.svg" valign=-3.1963502999999895px width="8.430376349999989pt" height="10.2739725pt"/> is a generator for <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> then, <img alt="$g^{n/\ell}$" src="svgs/1c2ad7b226d405075b7e0ddc1c06d4fc.svg" valign=-3.1963502999999966px width="28.793918999999992pt" height="17.7918378pt"/> must have order <img alt="$\ell.$" src="svgs/fb1f7152c7b8bdf9af1fe835ef63d16f.svg" valign=0.0px width="11.41559099999999pt" height="11.4155283pt"/>  So that's
one element of order <img alt="$\ell.$" src="svgs/fb1f7152c7b8bdf9af1fe835ef63d16f.svg" valign=0.0px width="11.41559099999999pt" height="11.4155283pt"/>  To get all elements of order <img alt="$\ell$" src="svgs/d30a65b936d8007addc9c789d5a7ae49.svg" valign=0.0px width="6.849367799999992pt" height="11.4155283pt"/>, consider elements of <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> of the
form <img alt="$g^{jn/\ell}$" src="svgs/a4e92cbcb8062164d549fb5be7c4486c.svg" valign=-3.1963502999999966px width="34.89840749999999pt" height="17.7918378pt"/> for positive integers <img alt="$j.$" src="svgs/e3f1da1aaacd6a674d0b71c67336cc8b.svg" valign=-3.1963519500000044px width="11.363396549999988pt" height="14.0378568pt"/> Plainly, <img alt="$(g^{jn/\ell})^\ell=g^{jn}=(g^n)^j=e_G^j=e_G$" src="svgs/b54ba8b3a68a276df50a9245327894d7.svg" valign=-4.830949199999992px width="239.67260624999997pt" height="20.3445957pt"/>
where <img alt="$e_G$" src="svgs/9429b25a05247d478d2bc0dd5dd8c5fb.svg" valign=-2.4657286499999893px width="17.88863174999999pt" height="9.54335085pt"/> is the identity element in <img alt="$G.$" src="svgs/e1cceaa699790e2e9b0a14a958434239.svg" valign=0.0px width="17.49086789999999pt" height="11.232861749999998pt"/> But, in general, the order of <img alt="$g^{jn/\ell}$" src="svgs/a4e92cbcb8062164d549fb5be7c4486c.svg" valign=-3.1963502999999966px width="34.89840749999999pt" height="17.7918378pt"/> could be less
than <img alt="$\ell$" src="svgs/d30a65b936d8007addc9c789d5a7ae49.svg" valign=0.0px width="6.849367799999992pt" height="11.4155283pt"/>.  That happens precisely when <img alt="$\gcd(j,\ell)=d&gt;1$" src="svgs/f90975402559b778ebd2536d9db864e5.svg" valign=-4.109589000000009px width="119.00587544999998pt" height="16.438356pt"/> since, then,
<img alt="$(g^{jn/\ell})^{\ell/d}=g^{jn/d}=(g^n)^{j/d}=e_G^{j/d}=e_G$" src="svgs/0f219bd42b33f2290d50e54b162229a1.svg" valign=-4.8309492000000045px width="289.8555957pt" height="21.99987075pt"/> so that <img alt="$g^{jn/\ell}$" src="svgs/a4e92cbcb8062164d549fb5be7c4486c.svg" valign=-3.1963502999999966px width="34.89840749999999pt" height="17.7918378pt"/> has order dividing <img alt="$\ell/d.$" src="svgs/5fc195293a644038cf8e808d8c142036.svg" valign=-4.109589000000009px width="28.19076479999999pt" height="16.438356pt"/>
Hence, there are exactly <img alt="$\phi(\ell)$" src="svgs/5f5759f7d5f03fa367a510e38faa9564.svg" valign=-4.109589000000009px width="29.429343899999992pt" height="16.438356pt"/> elements of <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> of order <img alt="$\ell;$" src="svgs/78880a93871995159c9b84e1adcb28c4.svg" valign=-3.1963503000000055px width="11.41559099999999pt" height="14.611878599999999pt"/> namely, <img alt="$g^{jn/\ell}$" src="svgs/a4e92cbcb8062164d549fb5be7c4486c.svg" valign=-3.1963502999999966px width="34.89840749999999pt" height="17.7918378pt"/> where
<img alt="$1\le j&lt; d$" src="svgs/72e89b1806f48ed2f77b94acec8cfcb6.svg" valign=-3.1963503000000055px width="68.32085204999998pt" height="14.611878599999999pt"/> and <img alt="$\gcd(j,\ell)=1.$" src="svgs/10849dc45db1c776493beeca9d8ef751.svg" valign=-4.109589000000009px width="93.09850439999998pt" height="16.438356pt"/>

Applying the proceeding discussion in a special case: notice that <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> has <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/>
generators; namely, the elements <img alt="$j$" src="svgs/36b5afebdba34564d884d347484ac0c7.svg" valign=-3.1963519500000044px width="7.710416999999989pt" height="14.0378568pt"/> that are relatively prime to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> as integers.

Let us also note down that if <img alt="$g$" src="svgs/3cf4fbd05970446973fc3d9fa3fe3c41.svg" valign=-3.1963502999999895px width="8.430376349999989pt" height="10.2739725pt"/> is a generator of a group <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> of order <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is an integer
satisfying <img alt="$g^m=e_G,$" src="svgs/507a9feb099894d3e45b0a0a75963a4f.svg" valign=-3.1963519500000044px width="66.11152514999999pt" height="14.116037099999998pt"/> then <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> necessarily divides <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>. To see this, first recall that, by the
definition of *order*, <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is the *least* positive integer satisfying <img alt="$g^n=e_G.$" src="svgs/ec144d80e243cbf773dc26098d90cf9c.svg" valign=-3.1963519500000044px width="62.572697549999994pt" height="14.116037099999998pt"/> Then use the
division algorithm to write <img alt="$m=qn+r$" src="svgs/98575f149192ef4cf4f39fc8ef815d77.svg" valign=-3.19635195px width="82.10984099999999pt" height="12.785402849999999pt"/> for some integers <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> and <img alt="$r$" src="svgs/89f2e0d2d24bcf44db73aab8fc03252c.svg" valign=0.0px width="7.87295519999999pt" height="7.0776222pt"/> with <img alt="$0\le r &lt; n$" src="svgs/7633545dac4328a6866b724e6564d331.svg" valign=-2.2351411499999947px width="69.79430204999998pt" height="12.82874835pt"/>. We have
<img alt="$e_G=g^m=g^{qn+r}=(g^n)^qg^r = g^r.$" src="svgs/7d9dfa709c06b120aec786840f32f1d6.svg" valign=-4.109589000000009px width="241.07211149999998pt" height="17.1982437pt"/> If follows immediately that <img alt="$r=0$" src="svgs/1b0129678603dff06573a74c88866a5a.svg" valign=0.0px width="38.009795999999994pt" height="10.5936072pt"/> since otherwise <img alt="$r$" src="svgs/89f2e0d2d24bcf44db73aab8fc03252c.svg" valign=0.0px width="7.87295519999999pt" height="7.0776222pt"/> is
a positive integer less than <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> satisfying <img alt="$g^r=e_G.$" src="svgs/c39926d74ccdf01b9e002e44b76fc6bc.svg" valign=-3.1963519500000044px width="60.90408059999998pt" height="14.116037099999998pt"/>

Now, to see that <img alt="$\phi$" src="svgs/f50853d41be7d55874e952eb0d80c53e.svg" valign=-3.1963503000000055px width="9.794543549999991pt" height="14.611878599999999pt"/> is multiplicative, let <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> and <img alt="$H$" src="svgs/7b9a0316a2fcd7f01cfd556eedf72e96.svg" valign=0.0px width="14.99998994999999pt" height="11.232861749999998pt"/> be cyclic groups of order <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>
and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, respectively, and let <img alt="$g$" src="svgs/3cf4fbd05970446973fc3d9fa3fe3c41.svg" valign=-3.1963502999999895px width="8.430376349999989pt" height="10.2739725pt"/> and <img alt="$h$" src="svgs/2ad9d098b937e46f9f58968551adac57.svg" valign=0.0px width="9.47111549999999pt" height="11.4155283pt"/> be, respectively, generators for <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> and <img alt="$H$" src="svgs/7b9a0316a2fcd7f01cfd556eedf72e96.svg" valign=0.0px width="14.99998994999999pt" height="11.232861749999998pt"/>. Consider
the product <img alt="$G\times H$" src="svgs/bb6a5c9aca14cc04df52dc2b0175f8f3.svg" valign=-1.369874549999991px width="48.01582499999999pt" height="12.6027363pt"/>.  We claim that, if <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime, then <img alt="$G\times H$" src="svgs/bb6a5c9aca14cc04df52dc2b0175f8f3.svg" valign=-1.369874549999991px width="48.01582499999999pt" height="12.6027363pt"/> is a
cyclic group of order <img alt="$mn.$" src="svgs/57b4da86b04bbeb1e8cacc81bc6cf95c.svg" valign=0.0px width="28.86620054999999pt" height="7.0776222pt"/> Note that

<p align="center"><img alt="$$(g,h)^{mn}=(g^{mn},h^{mn})=((g^m)^n,(h^n)^m)=(e_G, e_H)=e_{G\times H}.$$" src="svgs/bdb157e24bb85127e8b81bbbebe2095a.svg" valign=0.0px width="436.04847329999996pt" height="16.438356pt"/></p>

Hence, whatever the order of <img alt="$(g,h)$" src="svgs/aac259452e7e6c3323a67127751b0420.svg" valign=-4.109589000000009px width="37.99278944999999pt" height="16.438356pt"/>, call it <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>, we must have that it divides <img alt="$mn.$" src="svgs/57b4da86b04bbeb1e8cacc81bc6cf95c.svg" valign=0.0px width="28.86620054999999pt" height="7.0776222pt"/>
To prove our claim, we must show that <img alt="$mn$" src="svgs/e482c73e1741b27cd59b521c3f47e0b1.svg" valign=0.0px width="24.29997734999999pt" height="7.0776222pt"/> divides <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>, so that <img alt="$k=mn.$" src="svgs/9da8276d1af83f61442b78e3e88a8e42.svg" valign=0.0px width="59.85919334999999pt" height="11.4155283pt"/>
Looking at just the first component of <img alt="$(g^k,h^k)=(g,h)^k=e_{G\times H}=(e_G,e_H)$" src="svgs/aaeed85b89084dd8b856a4631124a5d6.svg" valign=-4.109588999999991px width="265.5570373499999pt" height="18.06580875pt"/>, we see <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>
divides <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>; similarly, looking at only the second component, <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> divides <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>. But then <img alt="$mn$" src="svgs/e482c73e1741b27cd59b521c3f47e0b1.svg" valign=0.0px width="24.29997734999999pt" height="7.0776222pt"/>
must divide <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> since <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime.

Finally, we show that <img alt="$\phi$" src="svgs/f50853d41be7d55874e952eb0d80c53e.svg" valign=-3.1963503000000055px width="9.794543549999991pt" height="14.611878599999999pt"/> is multiplicative. Under our assumtions, the product group
<img alt="$G\times H$" src="svgs/bb6a5c9aca14cc04df52dc2b0175f8f3.svg" valign=-1.369874549999991px width="48.01582499999999pt" height="12.6027363pt"/> has order <img alt="$mn.$" src="svgs/57b4da86b04bbeb1e8cacc81bc6cf95c.svg" valign=0.0px width="28.86620054999999pt" height="7.0776222pt"/>  It's also cyclic (since <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime). Therefore,
the number of generators of <img alt="$G\times H$" src="svgs/bb6a5c9aca14cc04df52dc2b0175f8f3.svg" valign=-1.369874549999991px width="48.01582499999999pt" height="12.6027363pt"/> is <img alt="$\phi(mn)$" src="svgs/ce057debe3a7c04d3a5694e05225ad6a.svg" valign=-4.109589000000009px width="46.87995344999998pt" height="16.438356pt"/>.  On the other hand, <img alt="$(g,h)$" src="svgs/aac259452e7e6c3323a67127751b0420.svg" valign=-4.109589000000009px width="37.99278944999999pt" height="16.438356pt"/> is a generator
if and only if <img alt="$g$" src="svgs/3cf4fbd05970446973fc3d9fa3fe3c41.svg" valign=-3.1963502999999895px width="8.430376349999989pt" height="10.2739725pt"/> and <img alt="$h$" src="svgs/2ad9d098b937e46f9f58968551adac57.svg" valign=0.0px width="9.47111549999999pt" height="11.4155283pt"/> generate, respectively, <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> and <img alt="$H$" src="svgs/7b9a0316a2fcd7f01cfd556eedf72e96.svg" valign=0.0px width="14.99998994999999pt" height="11.232861749999998pt"/>.  But <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> has <img alt="$\phi(m)$" src="svgs/432970ec6ad24aeb09c0b9dfd3953475.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/> generators
and <img alt="$H$" src="svgs/7b9a0316a2fcd7f01cfd556eedf72e96.svg" valign=0.0px width="14.99998994999999pt" height="11.232861749999998pt"/> has <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/>, so that <img alt="$\phi(mn)=\phi(m)\phi(n).$" src="svgs/38ce0d967ffd76c9dcbf729606c963a8.svg" valign=-4.109589000000009px width="142.82373929999997pt" height="16.438356pt"/>

#### Exercises
17. Let <img alt="$n=p_1p_2\cdots p_n$" src="svgs/621b951cef42642ea5a952eb172401e6.svg" valign=-3.1963503000000086px width="104.12845904999998pt" height="10.502306099999998pt"/> be a product of distinct primes. Show that <img alt="$\phi(n)=\prod_{i=1}^n p_i.$" src="svgs/479fdef2d7615099624428269eeab7b7.svg" valign=-4.931582700000004px width="113.05559924999997pt" height="18.150897599999997pt"/>

18. Show that for <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> prime and <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> a positive integer, we have <img alt="$\phi(p^e)=p^{e-1}(p-1).$" src="svgs/de6109f10acb98d33d39ffb55390c8e9.svg" valign=-4.109589000000009px width="145.91553734999997pt" height="17.4904653pt"/> Hint: this is just a counting argument. Which positive integers less than <img alt="$p^e$" src="svgs/45ac76e91416ad4fa83cd4d2462dea7a.svg" valign=-3.1963519500000044px width="14.50748474999999pt" height="14.116037099999998pt"/> are *not* relatively prime with <img alt="$p?$" src="svgs/f367873a30f9b543e23cbaa538dfae4e.svg" valign=-3.1963503000000055px width="16.03315724999999pt" height="14.611878599999999pt"/>

By the Fundamental Theorem of Arithmetic, any positive integer <img alt="$n&gt;1$" src="svgs/358039a361da9e2940dba6fc766af1c4.svg" valign=-0.6427030499999951px width="40.00371704999999pt" height="11.23631025pt"/> can be
written (uniquely, up to order) as a product of (positive powers of) distinct primes:
<img alt="$n=p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}$" src="svgs/6b7fd072681d124353c6692834a613f8.svg" valign=-4.958771399999998px width="120.80351909999999pt" height="17.3194725pt"/>;  hence,

<p align="center"><img alt="$$\phi(n)=\phi\left(\prod_{i=1}^k p_i^{e_i}\right)=\prod_{i=1}^k \phi\left(p_i^{e_i}\right)=\prod_{i=1}^k p_i^{e_i-1}(p_i-1).$$" src="svgs/d32849a7a1079a07ee6a67cee3781726.svg" valign=0.0px width="372.0267177pt" height="49.315569599999996pt"/></p>

#### Plain RSA

In modern times, you can create and publish (on, say, your personal webpage) a *public key* that can
then be used (by, say, someone called Athena) to encrypt a private message to you.  Only you can
decrypt Athena's encrypted message, so it doesn't matter if a bad actor sees Athena's encrypted
message that she is sending to you.

Important: since your enciphering key is public, a bad actor might try to intercept Athena's
encrypted message and replace it with a malicious message encrypted with your public key. Then you
decrypt the bad actor's message thinking that it is from Athena.  We need to bar against this
weakness but, for now, let us ignore it.

To create your public key in the
[RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)),
you first choose two large primes <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> (which you will keep
secret) and multiply them together obtaining <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/>.  You also choose a
positive integer <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> that is relative prime to <img alt="$\phi(n)=(p-1)(q-1)$" src="svgs/44a813ff292c05aaf762724c775fdc40.svg" valign=-4.109589000000009px width="152.75480549999997pt" height="16.438356pt"/>.
Your *public key* then consists of the pair of numbers <img alt="$(e, n)$" src="svgs/1ea602d667e6403959572fffbd4671bc.svg" valign=-4.109589000000009px width="37.61233079999999pt" height="16.438356pt"/>.

In order to, in the future, decrypt messages that were encrypted using
your public key, you go ahead and invert <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> modulo <img alt="$\phi(n);$" src="svgs/c537080963df3a027296931f59849a4c.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/> that is,
you find <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> that satisfies <img alt="$ed= 1 \mod \phi(n).$" src="svgs/4e139ccf8ea1b40fd608d4c9631c3303.svg" valign=-4.109589000000009px width="131.30493255pt" height="16.438356pt"/> Then <img alt="$(d, n)$" src="svgs/68cdc2991f340e2038c29e3ac3167db9.svg" valign=-4.109589000000009px width="38.51415644999999pt" height="16.438356pt"/> is your
decryption key *which you must keep secret*.

At this stage, you can actually delete, forget, and/or erase both <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and
<img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/>.  But keep <img alt="$(d, n)$" src="svgs/68cdc2991f340e2038c29e3ac3167db9.svg" valign=-4.109589000000009px width="38.51415644999999pt" height="16.438356pt"/> and keep <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> secret always.

Now suppose that <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is a positive integer representing the *plaintext*
message that Athena wants to encrypt and send to you.  Athena encrypts <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>
producing another integer <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> called the *ciphertext* as follows:

<p align="center"><img alt="$$c = m^e \mod n.$$" src="svgs/aa9d5ede41bc7ae9036d7d74fe20f446.svg" valign=0.0px width="118.3806822pt" height="11.741602949999999pt"/></p>

Athena can then send the ciphertext <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> to you or, say, publish it on her
webpage. Short of discovering a way to factor products of large primes
and assuming that you didn't leak <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>, <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> or <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/>, then you are the
only person on the planet who can decrypt <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> back into the plaintext <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/>

Now, how do you decrypt Athena's encrypted message <img alt="$c?$" src="svgs/5d744b7f76c38e8f14aa14d9188b3e77.svg" valign=0.0px width="14.87639504999999pt" height="11.4155283pt"/>  Answer: you simply
compute <img alt="$c^d \mod n,$" src="svgs/cdee14a712c856276a74da4431d96b53.svg" valign=-3.1963519499999897px width="77.15681324999998pt" height="17.1525717pt"/> which is actually the original message since, by
Euler's Theorem,

<p align="center"><img alt="$$c^d = (m^e)^d = m^{ed} = m^{1+k \phi(n)} = m(m^{\phi(n)})^k = m \mod n,$$" src="svgs/3674970a2b6b205033b9fdb5d617681c.svg" valign=0.0px width="419.2694847pt" height="19.526994300000002pt"/></p>

where <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> is an integer satisfying <img alt="$ed = 1 + k \phi(n).$" src="svgs/1db10a7b8d686bbb1de24ea3cdf16376.svg" valign=-4.109589000000009px width="112.52657294999997pt" height="16.438356pt"/>

Note that not even Athena can decrypt her own ciphertext <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> since she does
not have <img alt="$d.$" src="svgs/2d94d6868b0dbbea61050c0cabe84f89.svg" valign=0.0px width="13.12218764999999pt" height="11.4155283pt"/> She only has <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> (and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>) so she can only encrypt.

So how is it that your public key can't be reverse engineered by a bad actor?
Everyone has your encryption key <img alt="$(e, n).$" src="svgs/0b82a810c38d5f69ce7483d4671a68d5.svg" valign=-4.109589000000009px width="42.178555649999986pt" height="16.438356pt"/> But to compute <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> from <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/>, one
must invert <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> modulo not <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, but modulo <img alt="$\phi(n).$" src="svgs/4b539e947954886e594105a91f42f29b.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/>  And that's the rub,
computing <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/> when <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/>, a product of large primes, is very, very time
consuming &mdash; it's essentially equivalent to factoring <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> into <img alt="$pq$" src="svgs/45448f736dff1ed4d20005287b78bdb5.svg" valign=-3.1963502999999895px width="16.19867369999999pt" height="10.2739725pt"/>; i.e.,
finding a prime divisor of <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>.



---

### BELOW CURRENTLY UNDER CONSTRUCTION

---

*Cryptography* is the study of *cipher algorithms* by which we obscure data.
The cipher algorithm involves a *key* that is used to encrypt *plaintext* data
into *ciphertext*.  In *symmetric cryptography* (or *symmetric-key encryption*)
the key used for encryption is also used to decrypt the ciphertext back into
plaintext so that they key must be kept secret.

In *asymmetric cryptography* (or *public-key encryption*)

Cryptanalysis deals with the process by which attackers might "break" the
encryption

Cryptology



## Symmetric Cryptography



## Preliminaries

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

#### Quick start on making basic number-theoretic/cryptography computations in high-performance Python
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
* Instantiate and work in a Galois field of order 7^3:
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


