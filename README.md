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
I. [Preliminaries](#i-preliminaries)
   * [The integers modululo n](#the-integers-modulo-n)
   * [Pseudo-random sequences](#pseudo-random-sequences)
   * [Cryptographic security](#cryptographic-security)

II. [Numero-algebraic practicalities](#ii-numero-algebraic-practicalities)
   * [Prime fields](#prime-fields)
   * [Generating primes](#generating-primes)
   * [Euler's totient function](#eulers-totient-function)
   * [Plain RSA](#plain-rsa)
     * [Fermat-factoring attack](#fermat-factoring-attack)
   * [Pseudo-random bit generation](#pseudo-random-bit-generation)
     * [Blum Blum Shub](#blum-blum-shub)
   * [Algebraic formulation of RSA](#algebraic-formulation-of-rsa)
   * [More attacks](#more-attacks)
   * [Toward semantic security](#toward-semantic-security)

## I. Preliminaries

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
```pycon
>>> 123 % 45
33
```
Alternatively, one can use numlib to work in <img alt="$\mathbb{Z}/45$" src="svgs/bdf2e4f3f1d0f1891a0bdcaf49a9b7be.svg" valign=-4.109589000000009px width="35.61656834999999pt" height="16.438356pt"/> as follows.
```pycon
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
```pycon
>>> x = R(123)
>>> 67 * x + 89  # no need to write R(67) * x + R(89)
5 + <45>
```

### Pseudo-random sequences

As a simple application, let us implement a
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
If you want to use a different seed, then you could do something like this:
```python
import lcg

lcg.state = 1728  # put any integer here

for _ in range(5):
    print(lcg.prng())

#225454543513
#9387149945987420262
#9368084995109636919
#5613612028674063196
#4053038556501675877
```
One can think of the above LCG implementation as generating a pseudo-random
*sequence* of numbers.  When the initial seed is 10000000001, the
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
low then successive terms of our pseudo-random sequence change too simply and hence
not very randomly.  A potency of 2, for instance, implies that the difference between
<img alt="$(n+1)$" src="svgs/949707b3bc37b3be0f8b25742664879e.svg" valign=-4.109589000000009px width="50.962710149999985pt" height="16.438356pt"/>st and the <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>th state of our PRNG is always <img alt="$c(1+(a-1)n).$" src="svgs/010edbd5f223fb0408f3f67e509f6f27.svg" valign=-4.109589000000009px width="112.42772639999998pt" height="16.438356pt"/>
Generally, a potency of at least 5 is necessary (but not sufficient) for randomness
(see [Knuth](#references1) pp. 24-25).

#### Exercises
1. Does the LCG defined by the program above satisfy all three bulleted conditions so that its period is <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/>, the largest possible? :heavy_check_mark: **We talked through this in class.**

2. If possible, compute the potency of the LCG above to see if it even has a chance
   of being sufficiently "random". :heavy_check_mark: **Marina did this and told us the answer in class.**

3. Show the following (we used this above):  if <img alt="$gcd(a, m) = d$" src="svgs/c80e3d64932bb680cf2d824d13827a15.svg" valign=-4.109589000000009px width="97.78729124999998pt" height="16.438356pt"/> then, modulo <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, for any integer <img alt="$x$" src="svgs/332cc365a4987aacce0ead01b8bdcc0b.svg" valign=0.0px width="9.39498779999999pt" height="7.0776222pt"/>, we have that <img alt="$ax$" src="svgs/1590372cccb08e52e5b844dda033b7aa.svg" valign=0.0px width="18.08414189999999pt" height="7.0776222pt"/> is always a multiple of <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/>.

4. In the previous discussion we used the fact that if <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> are relatively prime, then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> has a multiplicative inverse modulo <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>; that is, there exists <img alt="$a^{-1}\in \mathbb{Z}/m$" src="svgs/aa1f57396e688f3977a4394d3829566c.svg" valign=-4.109589000000009px width="80.04000015pt" height="17.4904653pt"/> such that <img alt="$a^{-1}a=1 \mod m$" src="svgs/d23399681b00a63da8212e00b487087d.svg" valign=0.0px width="127.54161914999999pt" height="13.380876299999999pt"/>. Above we only needed its existence but what is <img alt="$a^{-1}$" src="svgs/b42707f02d6a6fbbe96ce85d2d4ab42c.svg" valign=0.0px width="25.515722099999987pt" height="13.380876299999999pt"/> if <img alt="$a=123456789$" src="svgs/afa5f8f36ba3ce9a1f38d9fd25e4434b.svg" valign=0.0px width="104.57966969999998pt" height="10.5936072pt"/> and <img alt="$m=2^{64}?$" src="svgs/a03fbd5ed34bcedfd4082b5e04a8c412.svg" valign=0.0px width="66.25953344999999pt" height="13.380876299999999pt"/> :heavy_check_mark: **Simmons did this in class with numlib's Zmod (which essentially just calls numlib's xgcd).**

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

(The program [chisq_hist.py](https://github.com/sj-simmons/crypto/blob/main/chisq_hist.py)
generates and displays the histogram above.)

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

#### ~~Exercises~~ Projects
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
by <img alt="$\nu_t = 1/d_t.$" src="svgs/38963eb4ecbffeb9606ffba0ebabd81a.svg" valign=-4.109589000000009px width="71.17388519999999pt" height="16.438356pt"/> (The quantity <img alt="$\nu_t$" src="svgs/b96ce619e9618788ad604f351c957414.svg" valign=-2.4657286499999893px width="13.08606584999999pt" height="9.54335085pt"/> arises naturally in the sense that it
is the vector of minimal length in the dual of the lattice mentioned above;
cf. [Steele, Vigna](#references1) pp. 3-4.)

If <img alt="$0&lt;a&lt;m$" src="svgs/c723c4986c981ef012a4915ad205d443.svg" valign=-0.6427030499999951px width="75.17672579999999pt" height="11.23631025pt"/> and <img alt="$\gcd(a,m)=1$" src="svgs/1adf9488b49d92d50d2bf48e91e9db53.svg" valign=-4.109589000000009px width="98.00799524999998pt" height="16.438356pt"/>, then the accuracy <img alt="$\nu_t$" src="svgs/b96ce619e9618788ad604f351c957414.svg" valign=-2.4657286499999893px width="13.08606584999999pt" height="9.54335085pt"/> admits
a concise characterization:

<p align="center"><img alt="$$\nu_t = \min_{(x_1, \ldots, x_t)\in \mathbb{Z}^t}\left\{\sqrt{x_1^2+\cdots+x_t^2}~\bigg|~ x_1+ax_2+\cdots+a^{t-1}x_t = 0 \mod m\right\}$$" src="svgs/f5e567f281e5af11ee140baca0bb1fc7.svg" valign=0.0px width="533.71664775pt" height="39.45246194999999pt"/></p>

where the minimum is over all non-zero vectors with integer coefficients.

However, if <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is large, then even <img alt="$\nu_2$" src="svgs/9473daf474f8d39427c1a99ddb5ad626.svg" valign=-2.4657286499999893px width="14.672819699999991pt" height="9.54335085pt"/> can be difficult to brute-force compute.
[Knuth](#references1) (pg. 102) gives the following 3-step algorithm to
compute <img alt="$\nu_2$" src="svgs/9473daf474f8d39427c1a99ddb5ad626.svg" valign=-2.4657286499999893px width="14.672819699999991pt" height="9.54335085pt"/> (the algorithm for <img alt="$\nu_t,$" src="svgs/ede699741d5f4a7ccb70c527c870347e.svg" valign=-3.1963502999999895px width="18.47418539999999pt" height="10.2739725pt"/> <img alt="$t&gt;2,$" src="svgs/c44c088d3144b176acdcb65339ca5d09.svg" valign=-3.196350299999994px width="40.639161749999985pt" height="13.789957499999998pt"/> is more involved):

1. Initialize variables <img alt="$h, h', p, p', r$" src="svgs/1885ee8b398072d6a6882c6f3fa76090.svg" valign=-3.1963502999999998px width="81.80360099999999pt" height="15.5544147pt"/> and <img alt="$s$" src="svgs/6f9bad7347b91ceebebd3ad7e6f6f2d1.svg" valign=0.0px width="7.7054801999999905pt" height="7.0776222pt"/> as follows. Set <img alt="$h\leftarrow a,$" src="svgs/ba4d90f8718a9abf7abdc256257f82b8.svg" valign=-3.1963503000000055px width="48.297093899999986pt" height="14.611878599999999pt"/> <img alt="$h'\leftarrow m,$" src="svgs/5bd097ec7dc5155686a2d7bf871c06eb.svg" valign=-3.1963502999999998px width="58.652914649999985pt" height="15.5544147pt"/> <img alt="$p \leftarrow 1,$" src="svgs/762aa9943ae65b43dc6702d7e9eef128.svg" valign=-3.196350299999994px width="46.62660089999999pt" height="13.789957499999998pt"/> <img alt="$p' \leftarrow 0,$" src="svgs/54636acb26ede68ecbed257f91ad3d41.svg" valign=-3.1963502999999998px width="51.238476299999995pt" height="15.5544147pt"/> <img alt="$s \leftarrow 1+a^2.$" src="svgs/ee0e89fee5aa88e5e5e7bede8ae5347a.svg" valign=-1.3698729000000083px width="82.21631879999998pt" height="14.750749199999998pt"/>
2. Next, set <img alt="$q\leftarrow \lfloor h'/h \rfloor,$" src="svgs/20f9396d3e1d3d90cd913fdb47f07f4b.svg" valign=-4.109589px width="84.45013664999999pt" height="16.4676534pt"/> <img alt="$u \leftarrow h'-qh,$" src="svgs/45c1459d617e1a1df58883ec459ea7ba.svg" valign=-3.1963502999999998px width="91.12047944999999pt" height="15.5544147pt"/> <img alt="$v\leftarrow p'-qp.$" src="svgs/f5a827340b26f056a5af8ae5095d49a6.svg" valign=-3.1963502999999998px width="87.86695334999999pt" height="15.5544147pt"/>  If <img alt="$u^2+v^2&lt; s,$" src="svgs/5827192c35bdb75e01cc8d501d9ece8f.svg" valign=-3.1963503000000086px width="86.99756009999999pt" height="16.5772266pt"/> then set <img alt="$s=u^2+v^2,$" src="svgs/90f43f71c97f37f079138ea519b368c1.svg" valign=-3.1963503000000086px width="86.99756009999999pt" height="16.5772266pt"/> <img alt="$h'\leftarrow h,$" src="svgs/f6e10c172fced41e9a7ac13da86c3f42.svg" valign=-3.1963502999999998px width="53.69092904999999pt" height="15.5544147pt"/> <img alt="$h\leftarrow u,$" src="svgs/c575e4d4e508df4cf341ac223d82b5fc.svg" valign=-3.1963503000000055px width="49.01821154999999pt" height="14.611878599999999pt"/> <img alt="$p'\leftarrow p,$" src="svgs/085036e3e0786da85023f02800a628c9.svg" valign=-3.1963502999999998px width="51.289832549999986pt" height="15.5544147pt"/> <img alt="$p\leftarrow v$" src="svgs/083dc0bd63a15acb5b7632eb8f31eaea.svg" valign=-3.1963502999999895px width="42.39902699999999pt" height="10.2739725pt"/> and repeat step 2; otherwise, go to step 3.
3. Set <img alt="$u\leftarrow u -h,$" src="svgs/8dd82d2e01b67312a699f263c90efc69.svg" valign=-3.1963503000000055px width="78.51967529999999pt" height="14.611878599999999pt"/>  <img alt="$v \leftarrow v-p.$" src="svgs/aac212b5f4c9719c04914d025c537f23.svg" valign=-3.19635195px width="75.61426619999999pt" height="12.785402849999999pt"/> If <img alt="$u^2+v^2&lt; s,$" src="svgs/5827192c35bdb75e01cc8d501d9ece8f.svg" valign=-3.1963503000000086px width="86.99756009999999pt" height="16.5772266pt"/> then set <img alt="$s=u^2+v^2.$" src="svgs/cac28d8f2bc47c77c010e1e8adaa2901.svg" valign=-1.3698729000000083px width="86.99756009999999pt" height="14.750749199999998pt"/> Output <img alt="$\nu_2 = \sqrt{s}.$" src="svgs/693647fc4ca168023923d273eca84673.svg" valign=-3.940686749999999px width="63.382738649999986pt" height="16.438356pt"/>

How are the numbers <img alt="$\nu_j$" src="svgs/c7260eb4ab1637d03de7308f52f924a5.svg" valign=-4.7031731999999895px width="14.224781999999989pt" height="11.780795399999999pt"/> used to determine which LCG perform best? We want the <img alt="$d_t,$" src="svgs/10cd08470937e1ffdd2da17b17f31ab6.svg" valign=-3.1963503000000055px width="18.90987614999999pt" height="14.611878599999999pt"/>
<img alt="$t=2, \ldots, 7,$" src="svgs/2694751a2a66535c88159d27b3a87245.svg" valign=-3.196350299999994px width="85.38778709999998pt" height="13.789957499999998pt"/> to be small, though they will necessarily increase with <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/> even
if for good performing LCGs. Since <img alt="$\nu_t=1/d_t,$" src="svgs/7bb18e0c45fe84739e9bfcae3a125532.svg" valign=-4.109589000000009px width="71.17388519999999pt" height="16.438356pt"/> we want the <img alt="$\nu_t$" src="svgs/b96ce619e9618788ad604f351c957414.svg" valign=-2.4657286499999893px width="13.08606584999999pt" height="9.54335085pt"/> to be large.
[Knuth](#references1) (pg. 105) gives the following rule of thumb: <img alt="$\nu_t\ge 2^{30/t}.$" src="svgs/333a623fd09f05df04e433bb4baa8f2b.svg" valign=-2.465728649999995px width="74.2389681pt" height="17.06121615pt"/>

#### Exercises
7. Show that <img alt="$\nu_t \le \sqrt{a^2+1}$" src="svgs/7ae1ff3d92039dbc06e050ad364145d5.svg" valign=-2.465728650000001px width="93.89827754999999pt" height="16.821868799999997pt"/> for all <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>.
8. Implement the algorithm above and use it to compute the accuracy <img alt="$\nu_2$" src="svgs/9473daf474f8d39427c1a99ddb5ad626.svg" valign=-2.4657286499999893px width="14.672819699999991pt" height="9.54335085pt"/> for our LCG (for which <img alt="$a=123456789$" src="svgs/afa5f8f36ba3ce9a1f38d9fd25e4434b.svg" valign=0.0px width="104.57966969999998pt" height="10.5936072pt"/> and <img alt="$m=2^{64}$" src="svgs/2c0d775f4ac8a5e8615cdf9cf2c1db95.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/>). :heavy_check_mark: **Laura did this and told us the answer in class.**

Now, since <img alt="$m=2^{64}$" src="svgs/2c0d775f4ac8a5e8615cdf9cf2c1db95.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/> is so large, many smallish choices of the multiplier <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> immediately
determine <img alt="$\nu_2.$" src="svgs/79f155422f397afe48afe2bb036af005.svg" valign=-2.4657286499999893px width="20.06095739999999pt" height="9.54335085pt"/>  In fact, according to [Steele, Vigna](#references1), Proposition 1,
for a full period LCG with modulus <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and multiplier <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/>, one has <img alt="$\nu_t=\sqrt{a^2+1}$" src="svgs/e50073ff4ba2b4f7da22f38e75ecbf67.svg" valign=-2.465728650000001px width="93.89827754999999pt" height="16.821868799999997pt"/>
whenever <img alt="$a&lt;\sqrt[t]{m};$" src="svgs/93a28b794675fc4f3adb3a6107926aca.svg" valign=-3.940686749999999px width="63.37152689999999pt" height="16.438356pt"/> and this is true for all <img alt="$t\ge 2$" src="svgs/d0ee488bf730f627d5394f0bc3972ae5.svg" valign=-2.2351411499999947px width="36.07293689999999pt" height="12.82874835pt"/>.

For large <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, [Knuth](#references1) (on page 105) proposes another quantity
called the *merit*,

<p align="center"><img alt="$$\mu_t=\frac{\pi^{t/2}\nu_t^t}{(t/2)!}$$" src="svgs/c60f95dc8b9f5d5ca94ff9449b6105d8.svg" valign=0.0px width="83.5726749pt" height="41.101633650000004pt"/></p>

where, if <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/> is odd, <img alt="$\left(\frac{t}{2}\right)! = \left(\frac{t}{2}\right)&#10;\left(\frac{t-1}{2}\right) \cdots \left(\frac{1}{2}\right) \sqrt{\pi}.$" src="svgs/4467628e209c91d40d7a1f539598e56c.svg" valign=-5.753531849999993px width="202.35048734999998pt" height="19.726228499999998pt"/>

The merit <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> is the volume of a certain ellipsoid (called a *figure of merit*)
in <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>-space:

<p align="center"><img alt="$$(x_1m-x_2a-\cdots-x_ta^{t-1})^2+x_2^2+\cdots+x_t^2 \le \nu_t^2.$$" src="svgs/0affd46b9b28f924f744e7a6edfeaf54.svg" valign=0.0px width="358.77412065pt" height="18.312383099999998pt"/></p>

If <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> is small, say <img alt="$\mu_t&lt;0.1$" src="svgs/c38405962bf08af010a310c68f2a0bdd.svg" valign=-3.196350299999994px width="58.614885449999996pt" height="13.789957499999998pt"/>, then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is not a good
multiplier because said ellipsoid is unlikely to capture points corresponding
to random numbers generated by our LCG.  If <img alt="$\mu_t&gt;0.1$" src="svgs/b533f731e0256a92cfe5fe47fd15c732.svg" valign=-3.196350299999994px width="58.614885449999996pt" height="13.789957499999998pt"/> or, better, <img alt="$\mu_t&gt;1.0$" src="svgs/46dc8ee9f162c24e5faa3d3629f7384d.svg" valign=-3.196350299999994px width="58.614885449999996pt" height="13.789957499999998pt"/>,
then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is a good multiplier. (Note: it turns out that Knuth's condition
<img alt="$\mu_t &gt; 1.0$" src="svgs/6f215968c71e9a106c285db640cb8e13.svg" valign=-3.196350299999994px width="58.614885449999996pt" height="13.789957499999998pt"/> is essentially the requirement that the LCG's lattice behaves
like a random <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>-dimensional lattice in that,  up to scaling, <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> is the
expected length of the shortest vector in a random <img alt="$t$" src="svgs/4f4f4e395762a3af4575de74c019ebb5.svg" valign=0.0px width="5.936097749999991pt" height="10.110901349999999pt"/>-dimensional lattice. See
the discussion
[here](https://crypto.stackexchange.com/questions/97844/average-spectral-score-of-multiplier-in-lcg).)

The advantage of looking at <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> instead of just <img alt="$\nu_t$" src="svgs/b96ce619e9618788ad604f351c957414.svg" valign=-2.4657286499999893px width="13.08606584999999pt" height="9.54335085pt"/> is that <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> can
be used to compare different multipliers for a fixed <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/>  For instance, with
<img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> fixed at <img alt="$2^{64}$" src="svgs/f54c544f103d398bf9c036ff710d9361.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/>, we wish to find a multiplier <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> with not only <img alt="$\nu_2,$" src="svgs/c44c5c5de2f9993727644e337ce1dca2.svg" valign=-3.1963502999999895px width="20.06095739999999pt" height="10.2739725pt"/>
but also <img alt="$\mu_2,$" src="svgs/8615699836ecb78ef8a53e8d3263850c.svg" valign=-3.1963502999999895px width="21.84560729999999pt" height="10.2739725pt"/> sufficiently large relative to other multipliers.

#### Exercises
9. Compute <img alt="$\mu_2$" src="svgs/d9324c21b00105263d6f54123813d99c.svg" valign=-3.1963502999999895px width="16.45747124999999pt" height="10.2739725pt"/> for our LCG; i.e., <img alt="$a=123456789,$" src="svgs/7543ddf5c75fb86912c49588ae0fd6e2.svg" valign=-3.196350299999994px width="109.14589289999998pt" height="13.789957499999998pt"/> <img alt="$m=2^{64}.$" src="svgs/a404936c9122ffe075a49b205e698627.svg" valign=0.0px width="63.063166649999985pt" height="13.380876299999999pt"/> Is <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> a good multiplier based on <img alt="$\mu_2$" src="svgs/d9324c21b00105263d6f54123813d99c.svg" valign=-3.1963502999999895px width="16.45747124999999pt" height="10.2739725pt"/>?
10. What if we leave the modulus at <img alt="$m = 2^{64}$" src="svgs/c7fdaf695852cd6459cc4165d25b86b2.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/> but take the multiplier to be <img alt="$a =$" src="svgs/16a5f39906ca313c4ef3f388684127b8.svg" valign=0.0px width="26.04068609999999pt" height="7.0776222pt"/> 214319739410341? Is this <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> a good multiplier? (This multiplier is recommended in [Steele, Vigna](#references1) on pg. 18.)
11. :zap:**Challenge**:zap: When <img alt="$m = 2^{64}$" src="svgs/c7fdaf695852cd6459cc4165d25b86b2.svg" valign=0.0px width="57.67503389999999pt" height="13.380876299999999pt"/> and <img alt="$a =$" src="svgs/16a5f39906ca313c4ef3f388684127b8.svg" valign=0.0px width="26.04068609999999pt" height="7.0776222pt"/> 214319739410341, find <img alt="$\nu_t$" src="svgs/b96ce619e9618788ad604f351c957414.svg" valign=-2.4657286499999893px width="13.08606584999999pt" height="9.54335085pt"/> for <img alt="$3 \le t \le 6$" src="svgs/a1b101a367cf06ca257ded541b352ac1.svg" valign=-2.2351411499999947px width="66.20977769999999pt" height="12.82874835pt"/> by either directly implementing the algorithm in [Knuth](#references1) or by comparing
with the definitions and listed values in [Steele, Vigna](#references1).
Also compute <img alt="$\mu_t$" src="svgs/87eefe082e181864d1321025c2705ecd.svg" valign=-3.1963502999999895px width="14.870715749999988pt" height="10.2739725pt"/> for <img alt="$3 \le t \le 6.$" src="svgs/4572a9d4690118768057d1b4e6e1f08a.svg" valign=-2.2351411499999947px width="70.77600089999999pt" height="12.82874835pt"/> What do those gauges say about the randomness of our LCG?
12. (Optional) [Steele, Vigna](#references1) recommends the smaller multiplier <img alt="$a = 15828829061$" src="svgs/306767c88ebd3a3b9965443894593881.svg" valign=0.0px width="121.0180884pt" height="10.5936072pt"/> (where still <img alt="$m = 2^{64})$" src="svgs/f27dc0f5c226f6b1999562f2658836c1.svg" valign=-4.109589000000009px width="64.88965889999999pt" height="17.4904653pt"/>; hence, let us assume that that value for <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> leads to good performance on all spectral tests. But show that it rejected by the chi-square on chi-square test above. :heavy_check_mark: **Simmons did this in class.**

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
generator) though several additional tests would need to be applied to bar against
non-randomness. But what does pseudo-random really mean?

In Computational Complexity Theory, a distribution is *pseudo-random* against a class of
*adversaries* if no adversary (think of an adversary as an algorithm or a test or some
other *distinguisher* or *observer*) from the class can distinguish it (with not
insignificant advantage) from the uniform distribution.

That certain adversaries cannot distinguish a pseudo-random distribution from a
uniform distribution corresponds to our intuitive notion that pseudo-random numbers
should *look like* random numbers.
A PRNG is a deterministic algorithm whose generated sequence appears to be pseudo-random
based on whichever statistical tests (e.g., the spectral test) are appropriate given
the application at hand.

The difference, in the context of complexity-based modern *cryptography*, is that the
generated numbers *must* be indistinguishable from random numbers for *all* adversaries, even
adversaries with advanced computational capabilities; said differently, random numbers
in cryptography are numbers whose value cannot be predicted before they are
generated, even with knowledge of previously generated numbers.

More mathematically, if random numbers are to be drawn from a set with <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> elements
(such as <img alt="$\{0, 1, \ldots, n-1\}$" src="svgs/41e684c9fa6df2ed9a097c7c352629ca.svg" valign=-4.109589000000009px width="114.88941419999999pt" height="16.438356pt"/>), the requirement is that an adversary cannot predict the number
with likelihood non-negligibly greater than <img alt="$1/n$" src="svgs/2d77e685bfa7e0c249fa2e10b3d67677.svg" valign=-4.109589000000009px width="26.30529494999999pt" height="16.438356pt"/> &mdash; the same as guessing.

Equivalently, one can reformulate this as: given <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> consecutive random numbers from
our sequence, any observer given <img alt="$k-1$" src="svgs/aa9d1dc08f682f546eeee2869762ff90.svg" valign=-1.3698745500000056px width="37.38576269999999pt" height="12.785402849999999pt"/> of them cannot predict <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>th one with likelihood
significantly greater than <img alt="$1/n.$" src="svgs/3fbc1952936c005853aa5dcba1b29090.svg" valign=-4.109589000000009px width="30.87151979999999pt" height="16.438356pt"/>

Our LCG fails spectacularly to be cryptographically secure, as does any LCG whose
whose modulus is a power of 2 since its lower bits are easily seen to be predictable.
We will now work out.the details for those special moduli. Importantly, *any*
LCG is predictable in that, a partial sequence of the output can be used to
generate the rest of the sequence, even without explicit knowledge of <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/>, <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/>, and <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/>

Let <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> divide that modulus <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> of an LCG defined by
<img alt="$x_{n+1}=ax_n +c \mod m,$" src="svgs/60f1e89ee25580012c6674006bc5df57.svg" valign=-3.835608150000004px width="178.08578039999998pt" height="15.251136449999997pt"/> and set <img alt="$y_n = x_n \mod d.$" src="svgs/e942787b962c28fa9c219cfa29dfa581.svg" valign=-3.1963503000000055px width="118.33502504999997pt" height="14.611878599999999pt"/>
Now, for some integer <img alt="$\ell$" src="svgs/d30a65b936d8007addc9c789d5a7ae49.svg" valign=0.0px width="6.849367799999992pt" height="11.4155283pt"/>, we have

<p align="center"><img alt="$$x_{n+1} = ax_n + c + d\ell,$$" src="svgs/9dc89200c8b9584446387a91c6b00273.svg" valign=0.0px width="151.20428895pt" height="15.251136449999997pt"/></p>

so that, modulo <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/>,

<p align="center"><img alt="$$y_{n+1} = x_{n+1} = ax_n + c + d\ell = ax_n + c = ay_n + c.$$" src="svgs/c2c9cf76f4b7ed1bcebf8cbb7e25c47d.svg" valign=0.0px width="357.74705339999997pt" height="15.251136449999997pt"/></p>

In other words, if <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> divides <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, then when we reduce modulo <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/>, in turn, each of the
numbers <img alt="$x_0, x_1, \ldots$" src="svgs/1ef9a5a71de299847eb1f8a3e573f241.svg" valign=-3.1963502999999895px width="67.32865259999998pt" height="10.2739725pt"/> we get another LCG <img alt="$y_0, y_1, \ldots$" src="svgs/681a1278c3f92f50665ce825720522ee.svg" valign=-3.1963502999999895px width="64.65753854999998pt" height="10.2739725pt"/> but with modulus
<img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> &mdash; which, as such, can't have period greater than <img alt="$d.$" src="svgs/2d94d6868b0dbbea61050c0cabe84f89.svg" valign=0.0px width="13.12218764999999pt" height="11.4155283pt"/>

The LCG we constructed above has modulus <img alt="$m=2^{64}.$" src="svgs/a404936c9122ffe075a49b205e698627.svg" valign=0.0px width="63.063166649999985pt" height="13.380876299999999pt"/> Taking say <img alt="$d=16$" src="svgs/9ab78716524228e52e840ca8a0b08ac1.svg" valign=0.0px width="46.91201294999998pt" height="11.4155283pt"/> corresponds
to looking only at the least significant 4 bits of the numbers <img alt="$x_0, x_1, \ldots.$" src="svgs/4a456007b04b555833cbe67251952c59.svg" valign=-3.1963502999999895px width="74.63453579999998pt" height="10.2739725pt"/>
The sequence of those least significant 4 bits cannot be very random because its
period is at most 16.

Or just take <img alt="$d=2.$" src="svgs/3a0185bb14ebc07d6c47efb8b322ad3f.svg" valign=0.0px width="43.25902844999999pt" height="11.4155283pt"/>  Reducing modulo <img alt="$d=2$" src="svgs/e675da7c7f7c3d89bc6087aab1186a27.svg" valign=0.0px width="38.69280359999998pt" height="11.4155283pt"/> any LCG that has modulus a power of 2 and
both <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> odd we get <img alt="$y_{n+1} = y_n + 1.$" src="svgs/fe4e035666fca4c33110843c97204146.svg" valign=-3.835608149999995px width="105.45290414999998pt" height="14.42921535pt"/>  Hence, the least significant bit
always alternates, and the terms of our original sequence <img alt="$x_0, x_1,\ldots$" src="svgs/c535c09bb36ceeefb36eb2ece911b331.svg" valign=-3.1963502999999895px width="67.32865259999998pt" height="10.2739725pt"/> are,
alternatively, even and odd.

#### Exercise
13. Suppose we use our LCG to generate two consecutive numbers, and that you are given only one of them. Based solely on that value (suppose that you forgot <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/>, <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/>, and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>, other than that <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> are odd and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is a power of 2), can you predict the other with probability of success greater then <img alt="$1/(m-1)=1/(2^{64}-1)?$" src="svgs/1fba2581e53b2adee9136e4fb04c3ba6.svg" valign=-4.109589000000009px width="181.32803865pt" height="17.4904653pt"/> (I.e., better than guessing?) If so, with what likelihood? :heavy_check_mark: **Marina and Alvaro saw in class what to do here, and Simmons later sent an email about it.**

In modern cryptography, one assumes that adversaries know which methodology is
begin employed. The point is to develop tools in which say a *key* or maybe the
initial state of a PRNG must be kept secret but not the method and its theoretical
justification.  (But even the initial state of an LCG could potentially be uncovered
given partial output.)

To be clear, an LCG should *never* be used when a CSPRNG &mdash;  a cryptographically
secure pseudo-random number generator &mdash; is required.  Moreover, passing some
battery of statistical test is necessary but not sufficient for cryptographic
security. If your PRNG does not at least appear to be random, then it has no chance
whatever of being cryptographically secure.

LCGs are not appropriate for cryptographic applications, they are however useful in
that they are simple to implement and easy to understand so that they may be
of use in say embedded systems, or in simulations, or in applications where some
not necessarily robust stochasticity is needed.

Suppose one has an application in mind for which an LCG is appropriate. Often
the situation with the lower bits not being random is not an issue.  If it is
an issue, then there are fixes.
One fix is to lop off the lower bits, after maybe first increasing the power of 2
defining <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> &mdash; the idea being that the most significant bits should still be random.

#### Exercise
14. Another fix is to change the modulus to a prime or, in our case, to say <img alt="$2^{64}-1,$" src="svgs/169fc71c677bab4f7ed36d42f71e4edf.svg" valign=-3.1963503000000086px width="55.022835449999995pt" height="16.5772266pt"/> which factors as <img alt="$3\cdot 5\cdot 17\cdot 257\cdot 641\cdot 65537\cdot 6700417$" src="svgs/420447c84bd7f4130dc256cba7c87fef.svg" valign=0.0px width="252.05449829999992pt" height="10.5936072pt"/>. Change (only) the modulus in our LCG and print out say the first 100 numbers, each taken modulo 2.  Of course, we now have a tertiary problem.  Print out the first 100 numbers, each taken modulo 3. (Note: changing the modulus could potentially break full periodicity and favorable performance on tests, everything would have to be rechecked.)

See also [permuted congruential generators](https://en.wikipedia.org/wiki/Permuted_congruential_generator).

Lastly, are there any cryptographically secure PRNGs? Answer: yes. We'll look
at one below whose security is based on number theoretical considerations
(see [Blum Blum Shub](#blum-blum-shub)).

<a id="references1">

#### References

* Donald Knuth, The Art of Computer Programming, 3rd Edition,
  Volume 2: Seminumerical Algorithms, 1998.
* Guy Steele and Sebastian Vigna, Computationally Easy, Spectrally Good
  Multipliers for Congruential Pseudo-Random Number Generators.
  [arxiv.org/abs/2001.05304](https://arxiv.org/abs/2001.05304), 2021.

<p align="right">  <a href="#contents"> contents </a> </p>

## II. Numero-algebraic practicalities

### Prime fields

Note that <img alt="$2\cdot 11 = 1$" src="svgs/e927310f36765b5ad74fbd34bdb938dd.svg" valign=0.0px width="66.66644984999998pt" height="10.5936072pt"/> modulo 21 so that 2 has 11 as its multiplicative inverse in
<img alt="$\mathbb{Z}/21.$" src="svgs/3731d4bdedc964b8cdbf897e6ea86d26.svg" valign=-4.109589000000009px width="40.18279319999999pt" height="16.438356pt"/>  Meanwhile, in <img alt="$\mathbb{Z}/21,$" src="svgs/e4c03b084fef61df3489a70d833a595b.svg" valign=-4.109589000000009px width="40.18279319999999pt" height="16.438356pt"/> 3 can have no multiplicative inverse
since it is a zero divisor: <img alt="$3\cdot 7 = 0 \mod 21.$" src="svgs/4b23d5a39780a9df7da266ffb9e76e31.svg" valign=0.0px width="127.39679699999998pt" height="11.4155283pt"/>

A commutative ring (such as <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/>) for which every non-zero element has a
multiplicative inverse is called a *field*.

#### Exercises
1. Show that <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> is a field if and only if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is prime.
2. Show that multiplicative inverses in <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> (or any ring) are unique.

If an element of a ring admits a multiplicative inverse, it is called a *unit*.
The units in a ring form a multiplicative group.

The multiplicative group of units in <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> is often denoted <img alt="$(\mathbb{Z}/n)^*.$" src="svgs/b28f4c4bcb1bc94d5ff2e276a1f76558.svg" valign=-4.109589000000009px width="53.953772399999984pt" height="16.438356pt"/>

#### Exercise

3. How does the order of the group <img alt="$(\mathbb{Z}/n)^*$" src="svgs/cc450b1fd7ccdc41e54fbd9d0ee2bd9c.svg" valign=-4.109589000000009px width="48.565654499999994pt" height="16.438356pt"/> depend on <img alt="$n?$" src="svgs/d538473761d79a0d6d90fc487c6f4b06.svg" valign=0.0px width="17.62946624999999pt" height="11.4155283pt"/>

Above we used the numlib function **Zmod** to create a class representing <img alt="$\mathbb{Z}/n,$" src="svgs/4ee8f29e8fc6ff907c10277ad56123ba.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>
where <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> may or may not be prime.  We often want to work in a prime field so we pick <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>
to be a prime, <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>.  Then, it is best to go ahead tell that to numlib, by using **Zmodp**
instead of **Zmod** (because the resulting class is then faster and has more functionality).

Here is an example.

```pycon
>>> import numlib as nl
>>> PF = nl.Zmodp(2027)  # Note: 2027 is prime
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
Of course, depending on whether the most significant random bit is zero or one, we might get a
number somewhat less than <img alt="$2^{200};$" src="svgs/e46661a0be2003a6fba87fa4a557cf10.svg" valign=-3.1963503000000086px width="33.264976799999985pt" height="16.5772266pt"/> so let us set the most significant bit to one and, while
we are at it, set also the least significant bit to 1 since primes beyond 2 must be odd:
```python
decimal |= (1 << numbits - 1) | 1
```
The variable **decimal** is now an integer whose binary representation has length 200 and both begins
and ends with 1; i.e., **decimal** is a random (depending on the robustness of **getrandbits**)
odd integer between <img alt="$2^{200}$" src="svgs/acc9da0b19643e432619eb386d21261f.svg" valign=0.0px width="27.87685064999999pt" height="13.380876299999999pt"/> and <img alt="$2^{201}.$" src="svgs/26851296087784570cb81e1034cdb3f0.svg" valign=0.0px width="33.264976799999985pt" height="13.380876299999999pt"/>

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
4. Replace the <img alt="$200$" src="svgs/88db9c6bd8c9a0b1527a1cedb8501c55.svg" valign=0.0px width="24.657628049999992pt" height="10.5936072pt"/> above with say <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> and write a function, using the scheme outlined above, that returns a <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit prime.

At issue is the fact that larger primes are harder to find. The difficulty is gauged by the Prime
Number Theorem.  If we define <img alt="$\pi(n)$" src="svgs/ab6b1f726144febfe19f0c5d987822fa.svg" valign=-4.109589000000009px width="32.61239849999999pt" height="16.438356pt"/> to be the number of primes less than or equal to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, then
the theorem states that <img alt="$\pi(n)$" src="svgs/ab6b1f726144febfe19f0c5d987822fa.svg" valign=-4.109589000000009px width="32.61239849999999pt" height="16.438356pt"/> is well-approximated by <img alt="$n/\ln(n)$" src="svgs/9bbe784fa51a44e5989bc0b2cac489c3.svg" valign=-4.109589000000009px width="57.17672729999999pt" height="16.438356pt"/> in the sense that
<p align="center"><img alt="$$\lim_{n\rightarrow\infty}\pi(n)\cdot\ln(n)/n=1.$$" src="svgs/bbbfdbd8c7959c658b17fe94615640ac.svg" valign=0.0px width="170.7003078pt" height="22.1917806pt"/></p>

The Prime Number Theorem implies that the number of primes between <img alt="$2^k$" src="svgs/91f4e50a1561b60d45e7079ca70f2ed4.svg" valign=0.0px width="15.48523844999999pt" height="13.95621975pt"/> and <img alt="$2^{k+1}$" src="svgs/bf56939689dfdac754c6e27725da93c9.svg" valign=0.0px width="32.12915969999999pt" height="13.95621975pt"/>
is approximately

<p align="center"><img alt="$$\frac{2^{k+1}}{\ln(2^{k+1})}-\frac{2^{k}}{\ln(2^{k})}=\frac{2^k}{\ln(2)}\left(\frac{2}{k+1}-\frac{1}{k}\right)=\frac{2^k}{\ln(2)}\frac{k-1}{k(k+1)};$$" src="svgs/ee03776f623d8b1c2733d4ee1290e882.svg" valign=0.0px width="418.50896339999997pt" height="40.6935375pt"/></p>

hence, the probability of a randomly chosen number between <img alt="$2^k$" src="svgs/91f4e50a1561b60d45e7079ca70f2ed4.svg" valign=0.0px width="15.48523844999999pt" height="13.95621975pt"/> and <img alt="$2^{k+1}$" src="svgs/bf56939689dfdac754c6e27725da93c9.svg" valign=0.0px width="32.12915969999999pt" height="13.95621975pt"/> being
prime is approximately <img alt="$p = (k-1)/(\ln(2)k(k+1))\approx 1/(\ln(2)k).$" src="svgs/0e7d2a1e66b418706e1b00cb61c47fcd.svg" valign=-4.109589000000009px width="294.8002942499999pt" height="16.438356pt"/>  But since your
program from the last exercise doesn't bother with even numbers, a given candidate **decimal**
has a likelihood of about <img alt="$p = 2/(\ln(2)k)$" src="svgs/e555980e9b695645e92caf5d9af89aa7.svg" valign=-4.109589000000009px width="103.19072609999999pt" height="16.438356pt"/> of being prime.
It is an basic fact from probability theory (see e.g., section 2.1 of
[Simmons' primer on random variables](https://github.com/sj-simmons/probthry/blob/main/primer.pdf)) that,
on average, one expects to test about <img alt="$1/p=k\ln(2)/2$" src="svgs/6c97d8dd61ac519e745292cae1789830.svg" valign=-4.109589000000009px width="109.5833706pt" height="16.438356pt"/> numbers before turning up one that is
indeed prime.

#### Exercise
5. Write a program that verifies that the expected number of tries before your prime generating function returns a 200-bit prime is about <img alt="$200\ln(2)/2\approx 69.$" src="svgs/9e6f25ea02c1b59eff12628ea34c16eb.svg" valign=-4.109589000000009px width="121.46129489999998pt" height="16.438356pt"/>

Note: since <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> is small, the variance here is very large so that the time it takes for your
program to find a single prime can vary greatly; said variance is <img alt="$(1-p)/p^2 \approx 4735.2$" src="svgs/07b12faa29e1cf6d90eece6f9c72b99f.svg" valign=-4.109589000000009px width="140.81053799999998pt" height="17.4904653pt"/> so that
the standard deviation of the number of tries before finding a 200 bit prime is about <img alt="$68.8.$" src="svgs/6ce6d2d54a6388aaebd027e35aebb86b.svg" valign=0.0px width="33.79007609999999pt" height="10.5936072pt"/> (The
standard deviation is <img alt="$\sqrt{(1-p)/p^2},$" src="svgs/44ca9338a2247d7391f898c6588a020d.svg" valign=-5.013835199999992px width="94.23517949999999pt" height="19.726228499999998pt"/> which is approximately <img alt="$1/p$" src="svgs/b6bd4fb45663b60f83a799556b0eeffb.svg" valign=-4.109589000000009px width="24.70898594999999pt" height="16.438356pt"/> for small <img alt="$p.)$" src="svgs/c984e348f5a9e47e87ef86e2ed395d6c.svg" valign=-4.109589000000009px width="19.22950754999999pt" height="16.438356pt"/>

#### Exercises
6. Estimate the probability that two uniformly chosen <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit primes are equal.
7. What is the expected number of tries and the associated standard deviation when finding a 2048-bit
    prime.
8. (Optional) Write a program that displays the sampling distribution for the number of tries before finding a prime using the method outlined above. The mean and standard deviation should both be about <img alt="$69.$" src="svgs/bc2aede8e8ec573d7068e3c67fedf605.svg" valign=0.0px width="21.00464354999999pt" height="10.5936072pt"/>

### Euler's totient function

The following is a basic result in elementary number theory.

**Fermat's Little Theorem**:  If <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> is a prime and <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is an integer not divisible by <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>, then <img alt="$a^{p-1} = 1 \mod p$" src="svgs/21079acb0231ed9b118814f30cfb192d.svg" valign=-3.1963503000000086px width="119.46638879999998pt" height="16.5772266pt"/>.

For those who know a little group theory this follows immediately from the fact that the order of
any element of a finite group must divide the order of the group. Here, the relevant group is
<img alt="$(\mathbb{Z}/p\mathbb{Z})^*,$" src="svgs/2d4a5869404cba9f337568cf3e5f6817.svg" valign=-4.109589000000009px width="63.31640369999999pt" height="16.438356pt"/> the multiplicative group of units in <img alt="$\mathbb{Z}/p\mathbb{Z},$" src="svgs/4eb71a5f1d780863eb3bf3c2cf2c59d0.svg" valign=-4.109589000000009px width="42.973882049999986pt" height="16.438356pt"/>
which has order <img alt="$p-1.$" src="svgs/2ad55de588e0025342173e657988d28d.svg" valign=-3.196350299999994px width="41.14719179999999pt" height="13.789957499999998pt"/>

If you are not familiar with basic group theory, then see for example
[this wikipedia page](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem)
for various other proofs of Fermat's Little Theorem.

#### Exercise
9. Use your program above to generate a 200-bit prime <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and then verify that <img alt="$a^{p-1} \equiv 1 \mod p$" src="svgs/2e621949487c8c972e5637f0848ac82e.svg" valign=-3.1963503000000086px width="119.46638879999998pt" height="16.5772266pt"/> where <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is, say, 1234567, or any positive integer less than <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>. Note: you may wish to use Python's built-in [pow() function](https://docs.python.org/3/library/functions.html#pow).

Below we will need the following generalization of Fermat's Little Theorem.

**Euler's Theorem**:  If <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is positive integer and <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> is an integer relatively prime to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>,
then <img alt="$a^{\phi(n)} = 1 \mod n.$" src="svgs/ded672b0ccf534dd49610fd693275d5e.svg" valign=0.0px width="128.3300799pt" height="14.5954875pt"/>

Here <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/> is Euler's totient function which returns the number of positive integers less than
and relatively prime to <img alt="$n.$" src="svgs/ea8d90fb4a8d92af94283e10af3efb57.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>

Notice that Euler's Theorem specializes to Fermat's Little Theorem if <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is prime since, then,
<img alt="$\phi(n)=n-1.$" src="svgs/1b0d94292d544c37a22b1f0f7f9a7b13.svg" valign=-4.109589000000009px width="97.10798459999998pt" height="16.438356pt"/>  Moreover, Euler's Theorem also follows from basic group theory where the ambient
group is <img alt="$(\mathbb{Z}/n\mathbb{Z})^*$" src="svgs/3864234dcb7744587a117c9e1a7290ea.svg" valign=-4.109589000000009px width="59.52459479999999pt" height="16.438356pt"/>, the multiplicative group of units in <img alt="$\mathbb{Z}/n\mathbb{Z}$" src="svgs/94d333ba0aaa5e9c8ce88690986075c2.svg" valign=-4.109589000000009px width="40.00396784999999pt" height="16.438356pt"/>,
which has order <img alt="$\phi(n).$" src="svgs/4b539e947954886e594105a91f42f29b.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/>

An *arithmetic* (i.e., defined on positive integers) function <img alt="$f$" src="svgs/190083ef7a1625fbc75f243cffb9c96d.svg" valign=-3.1963503000000055px width="9.81741584999999pt" height="14.611878599999999pt"/>  is *multiplicative*
if <img alt="$f(mn)=f(m)f(n)$" src="svgs/4397377cf2d4936bc7c8e91b31aa8d24.svg" valign=-4.109589000000009px width="138.3261231pt" height="16.438356pt"/> whenever <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime. For instance, Euler's totient function,
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
Looking at just the first component of <img alt="$(g^k,h^k)=(g,h)^k=e_{G\times H}=(e_G,e_H)$" src="svgs/aaeed85b89084dd8b856a4631124a5d6.svg" valign=-4.109588999999991px width="265.5570373499999pt" height="18.06580875pt"/>, we see that <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>
divides <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>; similarly, looking at only the second component, <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> divides <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>. But then <img alt="$mn$" src="svgs/e482c73e1741b27cd59b521c3f47e0b1.svg" valign=0.0px width="24.29997734999999pt" height="7.0776222pt"/>
must divide <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> since <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime.

Finally, we show that <img alt="$\phi$" src="svgs/f50853d41be7d55874e952eb0d80c53e.svg" valign=-3.1963503000000055px width="9.794543549999991pt" height="14.611878599999999pt"/> is multiplicative.

**Proof that Euler's totient function is multiplicative**. Under our assumtions, the product group
<img alt="$G\times H$" src="svgs/bb6a5c9aca14cc04df52dc2b0175f8f3.svg" valign=-1.369874549999991px width="48.01582499999999pt" height="12.6027363pt"/> has order <img alt="$mn.$" src="svgs/57b4da86b04bbeb1e8cacc81bc6cf95c.svg" valign=0.0px width="28.86620054999999pt" height="7.0776222pt"/>  It's also cyclic (since <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime). Therefore,
the number of generators of <img alt="$G\times H$" src="svgs/bb6a5c9aca14cc04df52dc2b0175f8f3.svg" valign=-1.369874549999991px width="48.01582499999999pt" height="12.6027363pt"/> is <img alt="$\phi(mn)$" src="svgs/ce057debe3a7c04d3a5694e05225ad6a.svg" valign=-4.109589000000009px width="46.87995344999998pt" height="16.438356pt"/>.  On the other hand, <img alt="$(g,h)$" src="svgs/aac259452e7e6c3323a67127751b0420.svg" valign=-4.109589000000009px width="37.99278944999999pt" height="16.438356pt"/> is a generator
if and only if <img alt="$g$" src="svgs/3cf4fbd05970446973fc3d9fa3fe3c41.svg" valign=-3.1963502999999895px width="8.430376349999989pt" height="10.2739725pt"/> and <img alt="$h$" src="svgs/2ad9d098b937e46f9f58968551adac57.svg" valign=0.0px width="9.47111549999999pt" height="11.4155283pt"/> generate, respectively, <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> and <img alt="$H$" src="svgs/7b9a0316a2fcd7f01cfd556eedf72e96.svg" valign=0.0px width="14.99998994999999pt" height="11.232861749999998pt"/>.  But <img alt="$G$" src="svgs/5201385589993766eea584cd3aa6fa13.svg" valign=0.0px width="12.92464304999999pt" height="11.232861749999998pt"/> has <img alt="$\phi(m)$" src="svgs/432970ec6ad24aeb09c0b9dfd3953475.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/> generators
and <img alt="$H$" src="svgs/7b9a0316a2fcd7f01cfd556eedf72e96.svg" valign=0.0px width="14.99998994999999pt" height="11.232861749999998pt"/> has <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/>, so that <img alt="$\phi(mn)=\phi(m)\phi(n).$" src="svgs/38ce0d967ffd76c9dcbf729606c963a8.svg" valign=-4.109589000000009px width="142.82373929999997pt" height="16.438356pt"/> :black_medium_square:

#### Exercises
10. Let <img alt="$n=p_1p_2\cdots p_n$" src="svgs/621b951cef42642ea5a952eb172401e6.svg" valign=-3.1963503000000086px width="104.12845904999998pt" height="10.502306099999998pt"/> be a product of distinct primes. Show that <img alt="$\phi(n)=\prod_{i=1}^n (p_i-1).$" src="svgs/c0b068721938ed3edf5374996d6cfb6c.svg" valign=-4.931582700000004px width="151.41177479999996pt" height="18.150897599999997pt"/>

11. Show that for <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> prime and <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> a positive integer, we have <img alt="$\phi(p^e)=p^{e-1}(p-1).$" src="svgs/de6109f10acb98d33d39ffb55390c8e9.svg" valign=-4.109589000000009px width="145.91553734999997pt" height="17.4904653pt"/> Hint: this is just a counting argument. Which positive integers less than <img alt="$p^e$" src="svgs/45ac76e91416ad4fa83cd4d2462dea7a.svg" valign=-3.1963519500000044px width="14.50748474999999pt" height="14.116037099999998pt"/> are *not* relatively prime with <img alt="$p?$" src="svgs/f367873a30f9b543e23cbaa538dfae4e.svg" valign=-3.1963503000000055px width="16.03315724999999pt" height="14.611878599999999pt"/>

By the Fundamental Theorem of Arithmetic, any positive integer <img alt="$n&gt;1$" src="svgs/358039a361da9e2940dba6fc766af1c4.svg" valign=-0.6427030499999951px width="40.00371704999999pt" height="11.23631025pt"/> can be
written (uniquely, up to order) as a product of (positive powers of) distinct primes:
<img alt="$n=p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}$" src="svgs/6b7fd072681d124353c6692834a613f8.svg" valign=-4.958771399999998px width="120.80351909999999pt" height="17.3194725pt"/>;  hence,

<p align="center"><img alt="$$\phi(n)=\phi\left(\prod_{i=1}^k p_i^{e_i}\right)=\prod_{i=1}^k \phi\left(p_i^{e_i}\right)=\prod_{i=1}^k p_i^{e_i-1}(p_i-1).$$" src="svgs/d32849a7a1079a07ee6a67cee3781726.svg" valign=0.0px width="372.0267177pt" height="49.315569599999996pt"/></p>

While showing, above, that <img alt="$\phi$" src="svgs/f50853d41be7d55874e952eb0d80c53e.svg" valign=-3.1963503000000055px width="9.794543549999991pt" height="14.611878599999999pt"/> is multiplicative, we proved:

**Proposition**. If positive integers <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> are relatively prime, then <img alt="$\mathbb{Z}/mn\cong \mathbb{Z}/n\times\mathbb{Z}/m$" src="svgs/e80f294d6d2150aae9a2d709807e5e0f.svg" valign=-4.109589000000009px width="148.14322049999998pt" height="16.438356pt"/> as rings. Moreover, <img alt="$(\mathbb{Z}/mn)^* \cong (\mathbb{Z}/n)^* \times (\mathbb{Z}/m)^*$" src="svgs/d75a1fe265e71b8fbd39154cab485d7e.svg" valign=-4.109589000000009px width="208.3488924pt" height="16.438356pt"/>
as multiplicative groups.

**Proof**. Arguing as above, except additively, the map <img alt="$x \mapsto (x \mod m, x \mod n)$" src="svgs/995d140a6fe30225897e70143a750cd6.svg" valign=-4.109589000000009px width="194.03668349999998pt" height="16.438356pt"/>, where <img alt="$x$" src="svgs/332cc365a4987aacce0ead01b8bdcc0b.svg" valign=0.0px width="9.39498779999999pt" height="7.0776222pt"/> generates
<img alt="$\mathbb{Z}/mn$" src="svgs/c8b3d4f7d2deabec23c20e9348fc1b28.svg" valign=-4.109589000000009px width="43.478126999999986pt" height="16.438356pt"/>, is necessarily an isomorphism of additive groups that one easily checks is also a ring homomorphism (that, then, restricts to an isomorphism of multiplicative groups). :black_medium_square:

More generally, one has the [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n#General_composite_numbers).

### Plain RSA

:warning: *Plain*, or so-called *textbook*, RSA is inherently and dangerously insecure for
real-world cryptographical applications; nonetheless, it is an accessible illustration of the
fundamental *trap-door* mechanism in modern cryptography. And, it can be enhanced and made into
a secure public-key cryptosystem, as we will see.

In modern times, you can create and publish (on, say, your personal webpage) a *public key* that can
then be used (by someone called, say, Athena) to encrypt a private message to you.  Only you can
decrypt Athena's encrypted message, so it doesn't matter if a bad actor sees Athena's encrypted
message that she is sending to you.

#### How to set up your keys

Important: since your enciphering key is public, a bad actor might try to intercept Athena's
encrypted message and modify or replace it with a malicious message encrypted with your public key. Then you
decrypt the bad actor's message thinking that it is from Athena.  We need to bar against this
weakness but, for now, let us ignore it.

To create your public key in the
[RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)),
you first choose two large primes <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> (which you will keep
secret) and multiply them together obtaining <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/>.  You also choose a
positive integer <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> that is relative prime to <img alt="$\phi(n)=(p-1)(q-1)$" src="svgs/44a813ff292c05aaf762724c775fdc40.svg" valign=-4.109589000000009px width="152.75480549999997pt" height="16.438356pt"/>.
Your *public key* then consists of the pair of numbers <img alt="$\{n, e\}.$" src="svgs/e4c8fb755110974bbd1aa4b0fe60b068.svg" valign=-4.109589000000009px width="45.83154014999999pt" height="16.438356pt"/>

In order to, in the future, decrypt messages that were encrypted using
your public key, you go ahead and invert <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> modulo <img alt="$\phi(n);$" src="svgs/c537080963df3a027296931f59849a4c.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/> that is,
you find the least positive integer <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> that satisfies
<img alt="$ed= 1 \mod \phi(n).$" src="svgs/4e139ccf8ea1b40fd608d4c9631c3303.svg" valign=-4.109589000000009px width="131.30493255pt" height="16.438356pt"/> Then <img alt="$\{n, d\}$" src="svgs/de3bd9768742ee7537342ce023ae5d20.svg" valign=-4.109589000000009px width="42.167142599999984pt" height="16.438356pt"/> is your decryption key
*which you must keep secret*.

At this stage, you can actually delete, forget, and/or erase both <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and
<img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/>.  But keep <img alt="$\{n, d\}$" src="svgs/de3bd9768742ee7537342ce023ae5d20.svg" valign=-4.109589000000009px width="42.167142599999984pt" height="16.438356pt"/> and keep <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> secret always.

Now suppose that <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is a positive integer representing the *plaintext*
message that Athena wants to encrypt and send to you.  Athena encrypts <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>
producing another integer <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> called the *ciphertext* as follows:

<p align="center"><img alt="$$c = m^e \mod n.$$" src="svgs/aa9d5ede41bc7ae9036d7d74fe20f446.svg" valign=0.0px width="118.3806822pt" height="11.741602949999999pt"/></p>

Athena can then send the ciphertext <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> to you or, say, publish it on her
webpage. Short of discovering an efficient way to factor products of large primes
and assuming that you didn't leak <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>, <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> or <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/>, then you are the
only person on the planet who can decrypt <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> back into the plaintext <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/>

#### How to decrypt

Now, how do you decrypt Athena's encrypted message <img alt="$c?$" src="svgs/5d744b7f76c38e8f14aa14d9188b3e77.svg" valign=0.0px width="14.87639504999999pt" height="11.4155283pt"/>  Answer: you simply
compute <img alt="$c^d \mod n,$" src="svgs/cdee14a712c856276a74da4431d96b53.svg" valign=-3.1963519499999897px width="77.15681324999998pt" height="17.1525717pt"/> which is actually <img alt="$m,$" src="svgs/85e0696fc8ec9dcd16fd64c9f562ae0c.svg" valign=-3.1963502999999895px width="18.99932429999999pt" height="10.2739725pt"/> the original message. To
show this, we claim that, for any integer <img alt="$m,$" src="svgs/85e0696fc8ec9dcd16fd64c9f562ae0c.svg" valign=-3.1963502999999895px width="18.99932429999999pt" height="10.2739725pt"/>

<p align="center"><img alt="$$m^{ed}=m \mod n$$" src="svgs/360c3e13a9075dcd03afa35035cceb03.svg" valign=0.0px width="127.97683305pt" height="14.77813755pt"/></p>

since, then, <img alt="$c^d = (m^e)^d = m^{ed} = m \mod n,$" src="svgs/a6d60f9539627eeccb90fe2660a08527.svg" valign=-4.109588999999991px width="227.62014494999994pt" height="18.06580875pt"/> as desired.

**Proof of claim**. First assume that <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is relatively prime to <img alt="$n.$" src="svgs/ea8d90fb4a8d92af94283e10af3efb57.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> Then

<p align="center"><img alt="$$m^{ed} = m^{1+k \phi(n)} = m\left(m^{\phi(n)}\right)^k = m(1)^k = m \mod n,$$" src="svgs/ffd19f13eb0e8fced268e67ea80da16d.svg" valign=0.0px width="393.7453476pt" height="33.5163048pt"/></p>

where <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/> is an integer satisfying <img alt="$ed = 1 + k \phi(n),$" src="svgs/91fcc71ea647cc943d91ca6153a24274.svg" valign=-4.109589000000009px width="112.52657294999997pt" height="16.438356pt"/> and we have used
the fact that, by Euler's Theorem, <img alt="$m^{\phi(n)} = 1 \mod n,$" src="svgs/a62aeb4d9f1c28081b41ef1b68af5b27.svg" valign=-3.1963502999999966px width="134.07402525pt" height="17.7918378pt"/> whenever <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is relatively
prime to <img alt="$n.$" src="svgs/ea8d90fb4a8d92af94283e10af3efb57.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>

If <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is not relatively prime to <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/> then either <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> divides <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> or <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> divides
<img alt="$m,$" src="svgs/85e0696fc8ec9dcd16fd64c9f562ae0c.svg" valign=-3.1963502999999895px width="18.99932429999999pt" height="10.2739725pt"/> or both <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> divide <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/>  In the latter case, since <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are distinct
primes, <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> must be a multiple of <img alt="$n,$" src="svgs/85bc1f723bdc744666d4f2241b1031f7.svg" valign=-3.1963502999999895px width="14.433101099999991pt" height="10.2739725pt"/>
and so <img alt="$m^{ed}=m \mod n,$" src="svgs/75d303d9bd9548d63536de253ae9844f.svg" valign=-3.1963519499999897px width="127.06373954999998pt" height="17.1525717pt"/> since, modulo <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, both <img alt="$m^{ed}$" src="svgs/9d7ff1dd3de851361fc4f6ec02eea159.svg" valign=0.0px width="27.51309659999999pt" height="13.95621975pt"/> and <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> are zero.

Assume without loss of generality that <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/>, but not <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/>, divides <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/> Then, clearly
<img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> divides <img alt="$m^{ed}-m.$" src="svgs/7885bcab49010c5e69a3d12371607ba4.svg" valign=-1.3698745499999894px width="67.42550924999999pt" height="15.3260943pt"/> Also, by Fermat's Little Theorem, <img alt="$m^{p-1} = 1 \mod p$" src="svgs/17a23b47cc8707b524557383d72b139a.svg" valign=-3.1963503000000086px width="125.21033579999997pt" height="16.5772266pt"/> since
<img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> doesn't divide <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/> Hence, similarly to above,

<p align="center"><img alt="$$m^{ed} = m^{1+k \phi(n)} = m\left(m^{\phi(n)}\right)^k = m\left(m^{(p-1)(q-1)}\right)^k = m\left(m^{p-1}\right)^{(q-1)k}= m \mod p;$$" src="svgs/aed1597905995874f4633e46ec986bcf.svg" valign=0.0px width="610.8324948pt" height="33.5163048pt"/></p>

so that, also, <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> divides <img alt="$m^{ed}-m.$" src="svgs/7885bcab49010c5e69a3d12371607ba4.svg" valign=-1.3698745499999894px width="67.42550924999999pt" height="15.3260943pt"/> Now, since <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are distinct primes, each
of which divide <img alt="$m^{ed}-m,$" src="svgs/52f839ba44523f0c909dd150e1b525d9.svg" valign=-3.1963519499999897px width="67.42550924999999pt" height="17.1525717pt"/> it must be the case that <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/> divides <img alt="$m^{ed}-m;$" src="svgs/a2c0789c86768f334a5f7b29b53f1c3d.svg" valign=-3.1963519499999897px width="67.42550924999999pt" height="17.1525717pt"/> that is,
<img alt="$m^{ed} = m \mod n$" src="svgs/953990e51132a0378e65834691c5acae.svg" valign=0.0px width="122.49751469999998pt" height="13.95621975pt"/> when <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is not relatively prime <img alt="$n.$" src="svgs/ea8d90fb4a8d92af94283e10af3efb57.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>

Therefore, the equality <img alt="$m^{ed} = m \mod n$" src="svgs/953990e51132a0378e65834691c5acae.svg" valign=0.0px width="122.49751469999998pt" height="13.95621975pt"/> holds for all <img alt="$m,$" src="svgs/85e0696fc8ec9dcd16fd64c9f562ae0c.svg" valign=-3.1963502999999895px width="18.99932429999999pt" height="10.2739725pt"/> since it holds when <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> is
relatively prime to <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, and also when it is not. :black_medium_square:

Note that not even Athena can decrypt her own ciphertext <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> since she does
not have <img alt="$d.$" src="svgs/2d94d6868b0dbbea61050c0cabe84f89.svg" valign=0.0px width="13.12218764999999pt" height="11.4155283pt"/> She only has <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> (and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>) so she can only encrypt.

So how is it that your public key can't be reverse engineered by a bad actor?
Everyone has your encryption key <img alt="$\{n, e\}.$" src="svgs/e4c8fb755110974bbd1aa4b0fe60b068.svg" valign=-4.109589000000009px width="45.83154014999999pt" height="16.438356pt"/> But to compute <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> from <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/>, one
must invert <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> modulo not <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, but modulo <img alt="$\phi(n).$" src="svgs/4b539e947954886e594105a91f42f29b.svg" valign=-4.109589000000009px width="37.01307719999999pt" height="16.438356pt"/>  And that's the rub,
computing <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/> when <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/>, a product of large primes, is very, very time
consuming &mdash; it's essentially equivalent to factoring <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> into <img alt="$pq$" src="svgs/45448f736dff1ed4d20005287b78bdb5.svg" valign=-3.1963502999999895px width="16.19867369999999pt" height="10.2739725pt"/>; i.e.,
finding a divisor of <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>.

Let us test drive the RSA scheme.

Cryptographers very often use the Fermat prime <img alt="$e=2^{16}+1=65537$" src="svgs/246dcb0ee0fb9e9f1e803ccd8a99f694.svg" valign=-1.3698729000000083px width="143.04205739999998pt" height="14.750749199999998pt"/> for
their RSA encrypting exponent (partly because raising to the 65537th power mainly
consists of squarings). Then they generate primes until they
find distinct <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> that satisfy <img alt="$\gcd(e, (p-1)(q-1))=1.$" src="svgs/458780abcbdf019c1decf5f58ea19ba0.svg" valign=-4.109589000000009px width="185.49642539999996pt" height="16.438356pt"/>

Suppose that you use your program above and find the following two
200-bit primes, <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/>:
```python
p = 1162281642500018516457695142918123385886797686236787603454999
q = 1576485350800305182150586120662765326256410287326195239351103
```
Let your public key be <img alt="$\{n, e\},$" src="svgs/8cbafb9a3db34ec0c1a7e97b39ce1922.svg" valign=-4.109589000000009px width="45.83154014999999pt" height="16.438356pt"/> where <img alt="$e=65537$" src="svgs/9031a800c7cdc076f354cc5ff9cafbb8.svg" valign=0.0px width="70.66781535pt" height="10.5936072pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is the product
of the two primes in the previous code-block.

#### Exercises
12. Verify that your key <img alt="$e=65537$" src="svgs/9031a800c7cdc076f354cc5ff9cafbb8.svg" valign=0.0px width="70.66781535pt" height="10.5936072pt"/> is indeed relatively prime to <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/> for your <img alt="$n.$" src="svgs/ea8d90fb4a8d92af94283e10af3efb57.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/>

13. Suppose that Carmichael uses your private key <img alt="$\{n, e\}$" src="svgs/5dbdee6d2f28cec315050f4a14b95b0c.svg" valign=-4.109589000000009px width="41.265316949999985pt" height="16.438356pt"/> to encrypt a (numeric) message. What is your
decrypting exponent, <img alt="$d,$" src="svgs/7194e1d4b173c3ff8fec4422c3f90097.svg" valign=-3.1963503000000055px width="13.12218764999999pt" height="14.611878599999999pt"/> and what was the original message if the ciphertext you receive from Carmichael is:
    ```python
    1228656544646342294930925759475188964963998457780851975302427012554675014888739125369008335923675038120110871984093074455
    ```

<a id="arthurmarvin">

14. :zap:**Challenge**:zap: Marvin can't be bothered to use large primes, so his public key is <img alt="$\{n, e\}=$" src="svgs/08190cb050929da6f85279c0ab82dc8a.svg" valign=-4.109589000000009px width="58.616848949999984pt" height="16.438356pt"/> \{932311734169679424087726241879, 65537\}. Arthur sends Marvin the following encrypted very secret message. You break Marvin's encryption, and intercept and decode the following ciphertext.
    ```python
    504779851614048359547310249856
    ```
    What is Arthur's plaintext to Marvin? :medal_sports: **Marina**, **Laura**, **Alvaro**

    Can you also decrypt the following intercepted ciphertext? :medal_sports: **Laura**, **Marina**, **Alvaro**
    ```python
    538940096304536933932071588652
    ```

#### Fermat-factoring attack

This attack on RSA is in play when the two primes <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are relatively
close together. Why is <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> being close a weakness?  First, notice that

<p align="center"><img alt="\begin{align}&#10; n = pq &amp;= \left(\frac{p+q}{2}\right)^2 - \left(\frac{p-q}{2}\right)^2. \notag&#10;\end{align}" src="svgs/120ca06a6b4c9aa73c839222e9ca541a.svg" valign=0.0px width="240.91877535pt" height="42.80407395pt"/></p>

Let us assume that <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are distinct odd primes with <img alt="$p&gt;q.$" src="svgs/fe18ee93b206e9cd5410c2687f1fbc49.svg" valign=-3.1963502999999966px width="42.68250854999999pt" height="12.05823135pt"/>  If we set
<img alt="$a=(p+q)/2$" src="svgs/6dabf8768ec7dd1dca58ce2a7a4b8b89.svg" valign=-4.109589000000009px width="96.12048269999998pt" height="16.438356pt"/> and <img alt="$b=(p-q)/2$" src="svgs/40b11dcb40a1cfe374eda802d9e93f23.svg" valign=-4.109589000000009px width="94.48612469999999pt" height="16.438356pt"/>, then <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$b$" src="svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg" valign=0.0px width="7.054796099999991pt" height="11.4155283pt"/> are positive integers and the last expression
on the right in the equality above factors, so that

<p align="center"><img alt="$$n=a^2-b^2=(a+b)(a-b),$$" src="svgs/f37302ade02cf04f6d42d65d86be5704.svg" valign=0.0px width="206.0935734pt" height="18.312383099999998pt"/></p>

which is just <img alt="$pq.$" src="svgs/7c81531e7dd2a54da35d1f8a8e6dd385.svg" valign=-3.1963502999999895px width="20.764878749999987pt" height="10.2739725pt"/>  If we can efficiently find <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> and <img alt="$b$" src="svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg" valign=0.0px width="7.054796099999991pt" height="11.4155283pt"/>, then we've
effectively found <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q.$" src="svgs/2e25588bd69787207bf5da9706a3070f.svg" valign=-3.1963502999999895px width="12.49431149999999pt" height="10.2739725pt"/>

If <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are close to each other, then <img alt="$b$" src="svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg" valign=0.0px width="7.054796099999991pt" height="11.4155283pt"/> is small. Looking at <img alt="$n+b^2 = a^2,$" src="svgs/17d49a25b3f451a80cbed84595e910f3.svg" valign=-3.1963503000000086px width="86.93479244999999pt" height="16.5772266pt"/>
we could incrementally look for the smallest positive integer <img alt="$b$" src="svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg" valign=0.0px width="7.054796099999991pt" height="11.4155283pt"/> such that <img alt="$n+b^2$" src="svgs/b0e51415eb6e5ce6c19eeea5cd862534.svg" valign=-1.3698729000000083px width="43.565410349999986pt" height="14.750749199999998pt"/> is
a perfect square (which would have to be <img alt="$a.)$" src="svgs/1e9b6e2f485383925290e2fcd16ac508.svg" valign=-4.109589000000009px width="19.64809439999999pt" height="16.438356pt"/> That would take <img alt="$b=(p-q)/2$" src="svgs/40b11dcb40a1cfe374eda802d9e93f23.svg" valign=-4.109589000000009px width="94.48612469999999pt" height="16.438356pt"/> steps and,
each step, we'd have check whether the number <img alt="$n+b^2$" src="svgs/b0e51415eb6e5ce6c19eeea5cd862534.svg" valign=-1.3698729000000083px width="43.565410349999986pt" height="14.750749199999998pt"/> is a perfect square. Fermat's
factoring method does better.

First, notice that, if <img alt="$b$" src="svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg" valign=0.0px width="7.054796099999991pt" height="11.4155283pt"/> is manageably small in the equality <img alt="$n+b^2=a^2$" src="svgs/87f2706d0438596747159a030c363d5e.svg" valign=-1.3698729000000083px width="81.54665474999999pt" height="14.750749199999998pt"/>, then we
have that <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/>, which is bounded below by <img alt="$\sqrt{n}$" src="svgs/4fd78aba72015f7697ab298a89ec8a9c.svg" valign=-3.940686749999999px width="23.565549149999992pt" height="16.438356pt"/>, shouldn't be hugely larger than <img alt="$\sqrt{n}.$" src="svgs/17b40019388603fede3e78d493732825.svg" valign=-3.940686749999999px width="28.13177234999999pt" height="16.438356pt"/>
Also, <img alt="$a^2-n =b^2;$" src="svgs/5a9aa6721384bd8fe11df516dd003e64.svg" valign=-3.1963503000000086px width="86.93479244999999pt" height="16.5772266pt"/> so let us try to find <img alt="$a$" src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" valign=0.0px width="8.68915409999999pt" height="7.0776222pt"/> by starting with <img alt="$a = \lceil\sqrt{n}\rceil$" src="svgs/8b88a03370f2f59aada5be95bb364b74.svg" valign=-4.109588999999997px width="68.78424299999999pt" height="16.607258249999997pt"/>
and incrementing it until <img alt="$a^2-n$" src="svgs/c5405a628f1c3bd1bea686634a9db29c.svg" valign=-1.3698729000000083px width="46.02168119999999pt" height="14.750749199999998pt"/> is a perfect square (which must be <img alt="$b^2).$" src="svgs/294092b5fadf2bcf89f34e837ec61dc3.svg" valign=-4.109589000000009px width="25.38819689999999pt" height="17.4904653pt"/>
Algorithmically, one could do something like:

1. Set <img alt="$a \leftarrow \lceil\sqrt{n}\rceil$" src="svgs/fb42dfd64b0590b4ff097cdc307b9396.svg" valign=-4.109588999999997px width="72.43721264999999pt" height="16.607258249999997pt"/> and <img alt="$b2\leftarrow a^2-n.$" src="svgs/4b119712635ff64a33861b150b04341c.svg" valign=-1.3698729000000083px width="91.4325126pt" height="14.750749199999998pt"/>
2. If <img alt="$b2$" src="svgs/b5522aeb42ad4c7fed8330a435caced5.svg" valign=0.0px width="15.274005449999992pt" height="11.4155283pt"/> is a perfect square, go to step 3; otherwise set <img alt="$a \leftarrow a + 1$" src="svgs/94ed1f7251b3a458f663664586034777.svg" valign=-1.3698745499999938px width="71.25930899999999pt" height="11.96348175pt"/>,  <img alt="$b2\leftarrow a^2-n$" src="svgs/3301faf4a8768eda399103e0655c89af.svg" valign=-1.3698729000000083px width="86.86628774999998pt" height="14.750749199999998pt"/> and repeat step 2.
3. Return <img alt="$a- \sqrt{b2}.$" src="svgs/fe7f3ca3e995e638f765c40703475869.svg" valign=-1.7717139000000102px width="62.31922289999999pt" height="16.438356pt"/>

Notice that the discussion above doesn't use that <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are prime, so that the algorithm
returns a factor for any product of odd (positive) integers &mdash; not just odd primes.

How many steps should this take? Consider <img alt="$(\sqrt{n}+i)^2-n=b^2.$" src="svgs/aec0f32946eb20f122ace7f9e7c3b318.svg" valign=-4.109589000000009px width="140.35103775pt" height="17.4904653pt"/> Solving this for <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg" valign=0.0px width="5.663225699999989pt" height="10.84150485pt"/>, we
get

<p align="center"><img alt="\begin{align}&#10;i =\sqrt{b^2+n}-\sqrt{n}&amp;=\left(\sqrt{b^2+n}-\sqrt{n}\right)\frac{\sqrt{b^2+n}+\sqrt{n}}{\sqrt{b^2+n}+\sqrt{n}}\notag\\&#10;&amp;=\frac{b^2}{\sqrt{b^2+n}+\sqrt{n}}.\notag&#10;\end{align}" src="svgs/7b3e647097116322de4ee061842fc5c8.svg" valign=0.0px width="384.55300124999997pt" height="90.84562079999999pt"/></p>

Looking just at the denominator in the last expression,

<p align="center"><img alt="\begin{align}&#10;\sqrt{b^2+n}+\sqrt{n}=\sqrt{a^2}+\sqrt{n}&amp;=a+\sqrt{n} \notag\\&#10;&amp;=\frac{p+q}{2}+\sqrt{n} \notag\\&#10;&amp;&gt;\frac{q+q}{2}+\sqrt{q^2} = 2q;  \notag&#10;\end{align}" src="svgs/4aef6531b17b0e4c690f1da18eb7ec02.svg" valign=0.0px width="356.09242515pt" height="99.84233984999999pt"/></p>

so that <img alt="$i&lt;\frac{b^2}{2q}=\frac{(p-q)^2}{8q}.$" src="svgs/a1f437e1cce7af2f4cab5b4ab455ab6f.svg" valign=-7.906039350000006px width="115.12336274999998pt" height="26.13616665pt"/>  If <img alt="$(p-q)^2$" src="svgs/d0d363e77ee37cf60874f95302961af5.svg" valign=-4.109589000000009px width="55.627826099999986pt" height="17.4904653pt"/> is small relative to <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/>, then
the algorithm has a chance of completing and, in each step, we check whether a number
less than <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is a perfect square.

The next exercise test-drives this attack. First, though, the following code snippets
may prove useful if you are using Python.  The issue is that an obvious way to check if
an integer <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is a square is to check if its square root is an integer.  The problem is that
Python's float method **is_integer** fails for large values of <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, as do other obvious
methods employing floats.

To stay completely in the realm of integers, one could use a bisection method:

```python
def sqroot(n):
    """return sqrt(n) if integer n is a perfect square; otherwise, return 0"""
    assert type(n) is int and n > 0
    lower, upper = 1, n
    while lower + 1 < upper:
        middle = (lower + upper)//2
        if middle * middle < n:
            lower = middle
        else:
            upper = middle
    return lower if lower ** 2 == n else upper if upper ** 2 == n else 0
```
Similarly, taking the ceiling of the square root of a large integer fails; consider
using this instead:
```python
def ceil_sqroot(n):
    """return integer ceiling(sqrt(n)) where n is a positive integer"""
    assert type(n) is int and n > 0
    lower, upper = 1, n
    while lower + 1 < upper:
        middle = (lower + upper)//2
        if middle * middle < n:
            lower = middle
        else:
            upper = middle
    return upper
```
Note that the algorithm in each function has order <img alt="$\log(n).$" src="svgs/19c4da6002a94773ccd0397302d0fd3f.svg" valign=-4.109589000000009px width="48.45144479999999pt" height="16.438356pt"/>

#### ~~Exercises~~ :zap:Challenges:zap:

15. Robertson uses 512-bit primes to generate his RSA public-key.  For his encryption key <img alt="$\{n, e\}$" src="svgs/5dbdee6d2f28cec315050f4a14b95b0c.svg" valign=-4.109589000000009px width="41.265316949999985pt" height="16.438356pt"/>, he uses <img alt="$e =$" src="svgs/5ea054d9d68928a88e3fac889ab224ac.svg" valign=0.0px width="25.00566914999999pt" height="7.0776222pt"/> 65537 and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> equal to (in hex):
    ```python
    0x50886174e2215b2a1af3aa90b4856cc816f2d93732342613699c424c8b4a9e022974cf8aadd449dd8c80149f76854c61f139b4f7180acbdf49971d867809d4cb06603a3c5645295f0083b276f0f751f5bc71630d0c1c84ef65306ae9efd9820fc8bc162d07ea1ff9bf5dc4720f72dc4a6d33ffdcfc4a1f7847df61eeaa56c5bd
    ```
    Simmons encrypts a very important message and sends it to Robertson. Here is the (hex)
    ciphertext:
    ```python
    0x50886174e2215b2a1af3aa90b4856cc816f2d93732342613699c424c8b4a9e022974cf8aadd449dd8c80149f76854c61f139b4f7180acbdf49971d867809d4cb06603a3c5645295f0083b276f0f751f5bc71630d0c1c84ef65306ae9efd9820fc8bc162d07ea1ff9bf5dc4720f72dc4a6d33ffdcfc4a1f7847df61eeaa56c5bd
    ```
    You break the key and you intercept the ciphertext.  What is the plaintext?

16. How big is the difference between Robertson's <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/>? E.g., what's the smallest integer <img alt="$j$" src="svgs/36b5afebdba34564d884d347484ac0c7.svg" valign=-3.1963519500000044px width="7.710416999999989pt" height="14.0378568pt"/> such that <img alt="$|p-q|&lt;2^{j}?$" src="svgs/5a888367a595b9e5156ed97f480fa342.svg" valign=-4.109589000000009px width="90.2481261pt" height="17.689090649999997pt"/>

Realizing that there are many other tricks and optimizations useful when Fermat factoring (see, for
example, the [Wikipedia page](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method)), let
us make some estimates based on our naive algorithm above.

Suppose that <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are uniformly randomly and independently chosen <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit primes. What is
the likelihood that <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are such that their product <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/> can be factored in less than,
say, a trillion &mdash; which is about <img alt="$2^{40}$" src="svgs/da84b223b752b66b6fcf378630d8d16c.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/> &mdash; steps of the algorithm outlined above?

We know that the number of steps is bounded by <img alt="$\frac{(p-q)^2}{8q},$" src="svgs/0a49627bf8cd62bb435fbbaf03c6b44a.svg" valign=-7.906039350000006px width="46.71672555pt" height="26.13616665pt"/>
which we, in turn, want bounded by <img alt="$2^{40}.$" src="svgs/c6fa98c50d09cd1df1229f4e9720822b.svg" valign=0.0px width="26.71243574999999pt" height="13.380876299999999pt"/> We know that <img alt="$q&gt;2^k$" src="svgs/fd7da8bdce7a50528af1115a2bfe0742.svg" valign=-3.1963519499999897px width="45.33095654999998pt" height="17.1525717pt"/>; hence

<p align="center"><img alt="$$\frac{(p-q)^2}{8q}&lt;\frac{(p-q)^2}{8\cdot 2^{k}}=\frac{(p-q)^2}{2^{k+3}}.$$" src="svgs/93b031e1e7752dd98e62910186588068.svg" valign=0.0px width="227.6135301pt" height="38.973783749999996pt"/></p>

We are guaranteed that the number of steps is less than <img alt="$2^{40}$" src="svgs/da84b223b752b66b6fcf378630d8d16c.svg" valign=0.0px width="21.324302999999993pt" height="13.380876299999999pt"/> if <img alt="$(p-q)^2&lt;2^{40}2^{k+3}=2^{43+k};$" src="svgs/0a49a2084ccf9520c2cb741d51b2f6c9.svg" valign=-4.109588999999991px width="199.45210559999998pt" height="18.06580875pt"/>
that is, if <img alt="$|p-q|&lt;2^{21.5+k/2}.$" src="svgs/3ba13f464b334fcd9aa8fa3b5166b830.svg" valign=-4.109588999999997px width="135.15411855pt" height="18.7050765pt"/>

Using the Prime Number Theorem, we previously estimated the probability of a <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit number
being prime to be about <img alt="$1/(\ln(2)k).$" src="svgs/319c8b6d7530cdbd9498afef1bfe2852.svg" valign=-4.109589000000009px width="77.56875389999999pt" height="16.438356pt"/>  Suppose <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> has been chosen, We can now very roughly
estimate of the probability, <img alt="$P,$" src="svgs/d514f3df2bd7d47a9400ca5ce79a755d.svg" valign=-3.196350299999991px width="15.57648179999999pt" height="14.42921205pt"/> that a <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit random <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> satifies <img alt="$|p-q|&lt;2^{21.5+k/2}:$" src="svgs/dd72555c3512084b4d21dcddff20d22e.svg" valign=-4.109588999999997px width="139.720218pt" height="18.7050765pt"/>

<p align="center"><img alt="$$P = \frac{1}{\ln(2)k}\frac{2|p-q|}{2^k}=\frac{2^{22.5-k/2}}{\ln(2)k}.$$" src="svgs/edcd1f7ffae9d5979aa25b5a2abcc5a5.svg" valign=0.0px width="233.92454745pt" height="41.101633650000004pt"/></p>

#### Exercise

17. If Robertson picked his <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> at random, how unlucky was he, given that he used 512-bit primes?  Asked differently, if one picks two 512-bit primes uniformly randomly, how likely is it that the resulting <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is factorable using less than a trillion steps in our implementation of Fermat factoring?  What if one uses 100-bit primes? 200-bit primes?

On page 40 of the appendix of the draft standard [DSS](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5-draft.pdf) (from [NIST](https://csrc.nist.gov/publications/fips)), the requirement is <img alt="$|p-q|&gt;2^{nlen/2-100}.$" src="svgs/898d9ade224f35c6ca1644093ecdc5e8.svg" valign=-4.109588999999997px width="150.8793165pt" height="18.7050765pt"/>  Here <img alt="$nlen$" src="svgs/376ce454e223b514ba4111a8e79e6aa0.svg" valign=0.0px width="32.61623474999999pt" height="11.4155283pt"/> is the bit-length of <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, so <img alt="$nlen/2$" src="svgs/8d8c02f5af80bda3bea2bc832ff00a14.svg" valign=-4.109589000000009px width="49.05465509999999pt" height="16.438356pt"/> is
our <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>, the bit-length of each of <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q.$" src="svgs/2e25588bd69787207bf5da9706a3070f.svg" valign=-3.1963502999999895px width="12.49431149999999pt" height="10.2739725pt"/> So, for 512-bit primes, they require that
<img alt="$|p-q|&gt;2^{412}\approx 10^{124}.$" src="svgs/dcd90f790069cd4082c06b9bad48b1a9.svg" valign=-4.109589000000009px width="159.44049495pt" height="17.4904653pt"/> Comparing with our very rough estimates above, NIST clearly anticipates adversaries armed with state-of-the-art machinery and advanced computational skill.

### Pseudo-random bit generation

True random number generation is challenging.  Hardware-based generators that rely on
time between emissions in radioactive decay or on atmospheric noise
(see [random.org](https://www.random.org/)) use some physical source the data
from which has to be rendered bias-free and uncorrelated.  For cryptographic
applications the equipment must be tamper-proof and the generators themselves
must bar against manipulation or even observation by adversaries.

Those challenges and more await designers of software-based generators that
harness user mouse movement or, say, system load as an initial source of randomness.
Running out of such randomness, along with a host of other potential weaknesses
including timing attacks, can lead to breaches of security.  Performant software
generators mix many sources of randomness, often using a
*cryptographic hash function* (discussed later).

A theme in modern, complexity-based cryptography is that if the output of a PRNG cannot
be practically distinguished from a truly random sequence, then it *is* effectively
truly random.
To formalize this, cryptographers employ a few basic constructs.

First, a *random bit generator* is a device or algorithm that
produces a list of bits (zeros or ones) in such a way that (1) a given position's bit being a zero
or one is independent of the value of any other position's bit, and (2) in each position, the value
one and zero occur with equal likelihood.

From a random bit sequence, we could fashion a uniform random number generator that
takes values in <img alt="$\{0, 1, \ldots, n\}$" src="svgs/a276c274f0bbc26672b049818b59c0fe.svg" valign=-4.109589000000009px width="86.57901284999998pt" height="16.438356pt"/> by collecting sequences consisting of
<img alt="$\lfloor \log_2n \rfloor + 1$" src="svgs/0e18562a5c452a3dbed7932a9f8cecdf.svg" valign=-4.109589000000009px width="84.13621754999998pt" height="16.438356pt"/> bits and then
regard those as the binary representation of a decimal number (and ignore any number
that turns out to be larger than <img alt="$n).$" src="svgs/55330dfdf24d21eb3637971c696f4436.svg" valign=-4.109589000000009px width="20.82581654999999pt" height="16.438356pt"/>

Next, let <img alt="$\{0,1\}^n$" src="svgs/9204ef16072dd8ab9a3430cb99a55ab2.svg" valign=-4.109589000000009px width="48.308744549999986pt" height="16.438356pt"/> denote the set of all strings of length <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, each character of which
is either <img alt="$0$" src="svgs/29632a9bf827ce0200454dd32fc3be82.svg" valign=0.0px width="8.219209349999991pt" height="10.5936072pt"/> or <img alt="$1.$" src="svgs/a083f757cc7bf6ee27f93c7c57301c52.svg" valign=0.0px width="12.785434199999989pt" height="10.5936072pt"/>

**Definition.** A *pseudo-random bit generator* (PRBG) is a (deterministic) algorithm
that takes a truly random initial *seed* in <img alt="$\{0,1\}^k$" src="svgs/dd464f1b586787ca7b2e3d1677b4606a.svg" valign=-4.109588999999991px width="47.44874969999999pt" height="18.06580875pt"/> and outputs a
*pseudo-random bit sequence* in <img alt="$\{0,1\}^\ell$" src="svgs/e434ff8adbce40478c5d742f16515cb5.svg" valign=-4.109588999999991px width="45.68506469999999pt" height="18.06580875pt"/> where <img alt="$\ell \gg k$" src="svgs/772cfa5be0f9ae28c7ed9a62d18eb147.svg" valign=-0.6427030500000053px width="41.49533684999999pt" height="12.05823135pt"/> (that is, <img alt="$\ell$" src="svgs/d30a65b936d8007addc9c789d5a7ae49.svg" valign=0.0px width="6.849367799999992pt" height="11.4155283pt"/> is
much greater than <img alt="$k).$" src="svgs/fd94a07cc857fe32f93c4e2724a376fa.svg" valign=-4.109589000000009px width="20.03430329999999pt" height="16.438356pt"/>

Notice straightaway that a PRBG has no chance of being uniformly random on <img alt="$\{0,1\}^\ell$" src="svgs/e434ff8adbce40478c5d742f16515cb5.svg" valign=-4.109588999999991px width="45.68506469999999pt" height="18.06580875pt"/>
since at most <img alt="$2^k$" src="svgs/91f4e50a1561b60d45e7079ca70f2ed4.svg" valign=0.0px width="15.48523844999999pt" height="13.95621975pt"/> elements of the <img alt="$2^\ell$" src="svgs/4210bd91bac363b5d4848d0155634610.svg" valign=0.0px width="13.721553449999991pt" height="13.95621975pt"/> bit-strings in <img alt="$\{0,1\}^\ell$" src="svgs/e434ff8adbce40478c5d742f16515cb5.svg" valign=-4.109588999999991px width="45.68506469999999pt" height="18.06580875pt"/> have a chance
of being selected, the others have likelihood zero of being selected.

#### Blum Blum Shub

Similarly to the RSA public-key encryption scheme, one can implement a PRBG as follows.

Generate two distinct large primes, each congruent to 3 modulo 4. Suppose you get these 512-bit primes:
```python
p = 0x9072333555dff36dfea913a9ec05574996cd9ff582a938970d1013740291f65c80f0ea660acf6c9e8b50546732806f9ae52fa6c505de974030e713f06ab8beeb
q = 0x8dbade2d14b9602b54517e6ae519b59194b72878598530df5b021431b2bb7eeea49031fe81b0c337e851bab97956f722c22b3e562e76ace4b7fc2e75497172df
```
Calculate <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/>:
```python
0x4ff8568a0d39836d32dbf022675362b03ae6c566b8027ad9811b71cbe8c5fa37bc60188e4b915cc8de90d2c24ecba81c42f5bd601cc93c4c880ccb0539ed68c5435fc1cb83e1ddf840293eaaef32c46a3366bfd4fb907a1623c9fd5478f5b0ef749c40aebd56509b67e4b08c87d54f910f6fc8b310ce2d10c0cab35784adf4b5
```
Now, delete or keep secret <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/>.  Assuming that factoring products of large primes remains intractable,
the following is a cryptographically-secure pseudo-random bit generator.
```python
#blumblumshub.py
import random
import numlib

n = 0x4ff8568a0d39836d32dbf022675362b03ae6c566b8027ad9811b71cbe8c5fa37bc60188e4b915cc8de90d2c24ecba81c42f5bd601cc93c4c880ccb0539ed68c5435fc1cb83e1ddf840293eaaef32c46a3366bfd4fb907a1623c9fd5478f5b0ef749c40aebd56509b67e4b08c87d54f910f6fc8b310ce2d10c0cab35784adf4b5

state = random.randint(1,n-1)
while numlib.gcd(state, n) != 1:
    state = random.randint(1,n-1)

state = state  * state  % n

def prbg_():
    global state
    state  = state  * state  % n
    return state  % 2

def prbg(length):
    bitstring = ''
    for _ in range(length):
        bitstring += str(prbg_())
    return bitstring
```

To use this, do something like:
```pycon
>>> from blumblumshub import prbg
>>> prbg(100)
```
Example output is:
```python
1111111000101111100110111111000011011000011101111000100110001010001010011111000100010001010001001010
```
The "random" bit-string starts with 7 ones and, soon after, a run of 5 ones, then 6 ones.  Maybe
there is something wrong with our PRBG.

#### ~~Exercises~~ Projects

18. Write a program that collects, say, 10,000 zeros and ones from an instance of our Blum Blum
    Shub PRBG and tally up the total number of ones that occur.
    There likely won't be exactly 5000 ones, which is not cause for alarm, of course. How do
    we analyze this? Formulate an carry out an appropriate statistical test. How does our
    Blum Blum Shub PRBG perform?

19. Formulate and perform a statistical "runs" test which analyzes appropriately the length
    of *runs* in samples bit-strings. How did our PRBG do?

    Here a *run* refers to a substring consisting of consecutive zeros (called a *gap*) or
    of successive ones (called a *block*).


20. Apply the test above to our final LCG from before &mdash; you might want to construct
    some other LCG(s). How to do they perform?

    Note that you don't want to simply take the outputs modulo 2 on our final LCG. That
    LCG has modulus a power of 2, so the final bit just alternates (as we saw explicitly).
    But you could do something different, like output the parity of the numbers, or take
    some high-significance bit instead of the lowest.  Or you use a different modulus
    but then you'd likely want to ensure that your LCG is full period and performs well
    on other test such as the chi-squared and spectral tests, and so on.

Previously, we used Python's **randint** in our program to generate <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit primes.
Then we used that program to generate primes for our Blum Blum Shub PRBG. Now,
we could use our Blum Blum Shub PRBG to provably uniformly generate a <img alt="$k$" src="svgs/63bb9849783d01d91403bc9a5fea12a2.svg" valign=0.0px width="9.075367949999992pt" height="11.4155283pt"/>-bit integer
as follows.
```pycon
>>> blumblumshub import prbg
>>> k = 200
>>> int(prbg(k), 2) # 1475114190501915896846876012970414686611326105418089001441857
```

Cryptographers do not often use the Blum Blum Shub PRBG in practice, for two main
(and related) reasons. First, Blum Blum Shub is in danger of being unviably slow, even when
generating a modest number of random bits; second, generating bits more efficiently
can jeopardize security.

Let us perform a quick and dirty assessment of the first issue (comparing with Python's
**randint**). Run the following from your commandline:
```bash
simmons> python3 -m timeit -s 'import random; k = 2048' 'random.randint(2**k, 2**(k+1))'
100000 loops, best of 5: 3.7 usec per loop
```
Here we are using Python's (builtin) [timeit](https://docs.python.org/3/library/timeit.html)
module. The output, on Simmons' Corei5 office machine, is shown.

Next run this:
```bash
simmons> python3 -m timeit -s 'from blumblumshub import prbg; k = 2048' 'prbg(k)'
50 loops, best of 5: 6.35 msec per loop
```
Python's **randint** is about 2000 times faster (partly due, no doubt, to C byte-code).
Now, looking back at our code, we are currently only drawing a single bit for each
call to **prbg_**.  One could try drawing more bits each pass but then one might have
to increase the size of the modulus to maintain security; each iteration,
<img alt="$O(\log(\log(n)))$" src="svgs/9cfb757e7a532bd2b60bedda7eecd0ed.svg" valign=-4.109589000000009px width="103.68442259999999pt" height="16.438356pt"/> bits can be extracted, where <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is modulus (see, for example,
[Sidorenko, Schoenmakers](#references2)).

### Algebraic formulation of RSA

Let <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/> be the product of two large primes, and let <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> be relatively prime to <img alt="$\phi(n)=(p-1)(q-1)$" src="svgs/44a813ff292c05aaf762724c775fdc40.svg" valign=-4.109589000000009px width="152.75480549999997pt" height="16.438356pt"/>, as
is the requirement in the RSA scheme. Then <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> is naturally a unit in the ring <img alt="$\mathbb{Z}/\phi(n)$" src="svgs/ca13f370ea412c16d503fe9cfd115bd6.svg" valign=-4.109589000000009px width="51.62500364999998pt" height="16.438356pt"/> or, to
say the same thing, an element of the group <img alt="$(\mathbb{Z}/\phi(n))^*.$" src="svgs/59b5e95b97ab12ffdab142041f543b6c.svg" valign=-4.109589000000009px width="76.53375014999999pt" height="16.438356pt"/> If <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> is your RSA encrypting
exponent, then <img alt="$d=e^{-1}\in(\mathbb{Z}/\phi(n))^* $" src="svgs/45e8b8efc8391e14e6380609da2d6ac5.svg" valign=-4.109589000000009px width="147.01295894999998pt" height="17.4904653pt"/> is the exponent that you use to decrypt.

Let <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> be an element of <img alt="$\mathbb{Z}/n.$" src="svgs/b2db6c8686053451d402312789bf8098.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>  Then <img alt="$m\mapsto m^e$" src="svgs/b01d456ec4b11056a006a150293a1169.svg" valign=0.0px width="60.673720799999984pt" height="10.91968515pt"/> defines a function
<img alt="$\mathbb{Z}/n\rightarrow \mathbb{Z}/n$" src="svgs/8b369b20e937a35c3d23597934ff4182.svg" valign=-4.109589000000009px width="83.66065289999999pt" height="16.438356pt"/> with inverse <img alt="$m\mapsto m^d.$" src="svgs/c4a4cd79e765ef3ab8c0753af2c53992.svg" valign=0.0px width="66.66802064999999pt" height="13.95621975pt"/> Since <img alt="$m\mapsto m^e$" src="svgs/b01d456ec4b11056a006a150293a1169.svg" valign=0.0px width="60.673720799999984pt" height="10.91968515pt"/>
is an invertible mapping, it is a permutation of (the set) <img alt="$\mathbb{Z}/n.$" src="svgs/b2db6c8686053451d402312789bf8098.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>
If <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> represents our plaintext message, then our ciphertext <img alt="$m^e$" src="svgs/e5df490f9386a96b3f4e66c5040e069a.svg" valign=0.0px width="20.670018599999988pt" height="10.91968515pt"/> is just the image of
<img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> under this permutation. Moreover, decrypting our ciphertext <img alt="$c=m^e$" src="svgs/1436d3cf9e0a368740082b75397824b9.svg" valign=0.0px width="49.70145344999999pt" height="10.91968515pt"/> is just applying
the inverse permutation, <img alt="$m\mapsto m^d,$" src="svgs/3a63a97b6acc27f7a4bf766402523ff4.svg" valign=-3.1963519499999897px width="66.66802064999999pt" height="17.1525717pt"/> to <img alt="$c.$" src="svgs/857431164e0fb928019e5dcd76861f58.svg" valign=0.0px width="11.680028249999989pt" height="7.0776222pt"/>

### More attacks

:warning: Plain RSA is inherently insecure and admits all manner of attack; only a few are outlined below; c.f., [Boneh](#references) and some of the citations [here](https://www.researchgate.net/publication/331390347_Forty_years_of_attacks_on_the_RSA_cryptosystem_A_brief_survey).

Anyone familiar with pop culture in the 80s might have guessed the numerical plaintext message in
the Arthur-to-Marvin Challenge above, and then verified correctness by simply encrypting that number
and verifying that it matches the ciphertext. Alternatively, if an attacker guessed correctly that
the plaintext was likely a smallish number, then they could encrypt every number less that say
1,000,000 and check if they hit the ciphertext.

#### Exercise

21. Write a tiny program to mount this sort of attack and uncover the first plaintext message
    that Arthur sends to Marvin in [this problem above](#arthurmarvin). Why doesn't this method
    reveal Arthur's second message?

If <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> and <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> are small, and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is large, then an attacker might be able to decrypt <img alt="$m^e$" src="svgs/e5df490f9386a96b3f4e66c5040e069a.svg" valign=0.0px width="20.670018599999988pt" height="10.91968515pt"/> by
simply taking the non-modular <img alt="$e\text{th}$" src="svgs/3ad6531a8759b4dace07a79f6bfea026.svg" valign=0.0px width="23.17930229999999pt" height="11.4155283pt"/> root.  More generally, an attacker who can significantly narrow
the set of possible messages could potentially mount a brute-force attack involving encrypting
a bunch of possible messages and checking for a match with the ciphertext.

The protocol would have to be modified, were the RSA scheme to even have a chance of being
equally secure for all messages.  Some flavor of *padding* (discussed below) is in order.

Thinking about the (plain) RSA setup in algebraic terms is simple and natural, but the
tight, wholly algebra structure leads to serious weakness, cryptographically.

Notice that of the  <img alt="$n!$" src="svgs/50c0357224674ab662b8ea5e5ca3eb8a.svg" valign=0.0px width="14.433101099999991pt" height="11.4155283pt"/> permutations of the set <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/>, only <img alt="$\phi(n)=(p-1)(q-1)$" src="svgs/44a813ff292c05aaf762724c775fdc40.svg" valign=-4.109589000000009px width="152.75480549999997pt" height="16.438356pt"/>
are of the form <img alt="$m\mapsto m^e$" src="svgs/b01d456ec4b11056a006a150293a1169.svg" valign=0.0px width="60.673720799999984pt" height="10.91968515pt"/>.  If <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are large then this is
still a very large *key space*.  However, suppose that one is extremely unlucky
and picks <img alt="$e$" src="svgs/8cd34385ed61aca950a6b06d09fb50ac.svg" valign=0.0px width="7.654137149999991pt" height="7.0776222pt"/> in such a way that <img alt="$d = e^{-1}$" src="svgs/2597d9d9033dc4d5f1c2d8e9f3d9ddfb.svg" valign=0.0px width="54.95429939999998pt" height="13.380876299999999pt"/> is small (as a positive integer less than <img alt="$n).$" src="svgs/55330dfdf24d21eb3637971c696f4436.svg" valign=-4.109589000000009px width="20.82581654999999pt" height="16.438356pt"/>
Then an attacker who intercepts the ciphertext <img alt="$m^e$" src="svgs/e5df490f9386a96b3f4e66c5040e069a.svg" valign=0.0px width="20.670018599999988pt" height="10.91968515pt"/> need only compute increasing powers
<img alt="$m^em^e=(m^e)^2=m^{2e}$" src="svgs/b9d1d1592a14673e41cc8bff7aa70817.svg" valign=-4.109589000000009px width="155.69347034999998pt" height="17.4904653pt"/>, <img alt="$(m^e)^2m^e=(m^e)^3=m^{3e}$" src="svgs/24a7fa6694aa0b5ebb0acf7f1554c091.svg" valign=-4.109589000000009px width="175.85336339999998pt" height="17.4904653pt"/>, <img alt="$\ldots$" src="svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg" valign=0.0px width="19.17798959999999pt" height="7.0776222pt"/> until they reach
<img alt="$(m^e)^d=m^{de}=m.$" src="svgs/ef446cdc32bf02e6cb4aea9feaf7a9b6.svg" valign=-4.109588999999991px width="133.11192509999998pt" height="18.06580875pt"/> (This is the same as trying to brute-force solve
<img alt="$ed = 1 \mod \phi(n)$" src="svgs/bf8a5c3efb534ac4ce5f6506ebb2ce09.svg" valign=-4.109589000000009px width="126.73870769999998pt" height="16.438356pt"/> for <img alt="$d,$" src="svgs/7194e1d4b173c3ff8fec4422c3f90097.svg" valign=-3.1963503000000055px width="13.12218764999999pt" height="14.611878599999999pt"/> but that is not directly in play since the attacker doesn't
know <img alt="$\phi(n).)$" src="svgs/1f86e92ecabc84d928d62d94b317f6b7.svg" valign=-4.109589000000009px width="43.40579429999999pt" height="16.438356pt"/>

So an attacker could eventually produce <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> by taking higher powers
<img alt="$c^\ell = (m^e)^\ell=m^{e\ell},$" src="svgs/0d9db41a007a7a0bc4a784e5c77ea18d.svg" valign=-4.109588999999991px width="129.4354248pt" height="18.06580875pt"/> but how would they know when to stop?  At each step,
they could check whether <img alt="$(c^\ell)^e=c;$" src="svgs/31f29c08a30f1cf5e71249ea5e13cb87.svg" valign=-4.109588999999991px width="66.87997469999999pt" height="18.06580875pt"/> if so, then <img alt="$m=c^\ell.$" src="svgs/c1b42e45d7c92ed892a81b4c88c15862.svg" valign=0.0px width="54.35502104999998pt" height="13.95621975pt"/> Alternatively, they
could continually multiply <img alt="$c^e$" src="svgs/5bcaf5cc289f68a9c90676a2849d44ec.svg" valign=0.0px width="13.350722549999988pt" height="10.91968515pt"/> by itself, obtaining <img alt="$(c^{e})^\ell=(c^{\ell})^e,$" src="svgs/438f1212a56075e55741b2de07c1df92.svg" valign=-4.109588999999991px width="93.0484863pt" height="18.06580875pt"/> until
they get <img alt="$c.$" src="svgs/857431164e0fb928019e5dcd76861f58.svg" valign=0.0px width="11.680028249999989pt" height="7.0776222pt"/>

If <img alt="$ed=1$" src="svgs/78289bd1e9f7ded7c6346a6d3a9b79a7.svg" valign=0.0px width="46.34694074999999pt" height="11.4155283pt"/> in <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/> then, as positive integers less than <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/>, <img alt="$ed &gt; n;$" src="svgs/73472f7d0ffb93f0386395e64454a83a.svg" valign=-3.1963503000000055px width="52.56083249999998pt" height="14.611878599999999pt"/>
hence <img alt="$d &gt; \lfloor n/e \rfloor.$" src="svgs/cb2c771bcdae95cd8e334b40637c0988.svg" valign=-4.109589000000009px width="75.39195179999999pt" height="16.438356pt"/>
Now, if <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q$" src="svgs/d5c18a8ca1894fd3a7d25f242cbe8890.svg" valign=-3.1963502999999895px width="7.928106449999989pt" height="10.2739725pt"/> are fairly large k-bit primes, then <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> and <img alt="$\phi(n)$" src="svgs/f4bdf2149704f6b9d6d0068d05021138.svg" valign=-4.109589000000009px width="32.44685399999999pt" height="16.438356pt"/> are 2k-bit numbers;
and, if <img alt="$e=65337,$" src="svgs/2b862298f3fc4340cc8116e95936f4a7.svg" valign=-3.196350299999994px width="75.2340402pt" height="13.789957499999998pt"/> which is a 16-bit number, then <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> must be at least (2k-16)-bits.  An attacker
could start computing incremental powers <img alt="$(m^e)^\ell=m^{\ell e}$" src="svgs/670af095a8c2fcc76f4d96ffa385ad2a.svg" valign=-4.109588999999991px width="88.69160684999999pt" height="18.06580875pt"/> starting from <img alt="$\ell=2^{2k-16}.$" src="svgs/4b7f7bb2695f01f4e4800c44c84aa83c.svg" valign=0.0px width="79.57199909999999pt" height="13.95621975pt"/>
The (uniform) likelihood of <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> being one of the first, say, <img alt="$2^{100}$" src="svgs/1df3384987fc3eba4ba24d84956ed539.svg" valign=0.0px width="27.87685064999999pt" height="13.380876299999999pt"/> integers in
<img alt="$[2^{2k-16}, 2^{2k}]$" src="svgs/91db863b80f16fd065994500d6809299.svg" valign=-4.109588999999991px width="85.53680354999999pt" height="18.06580875pt"/> is <img alt="$1/2^{2k-116}.$" src="svgs/fd0d6b70d6281088afe54c98ebea404b.svg" valign=-4.109588999999991px width="73.79596289999998pt" height="18.06580875pt"/> Hence, 100-bit or larger primes should suffice to
prohibit this sort of naive attack.

The point of the previous discussion, in algebraic terms, is that, if large enough primes are
used, then the cyclic subgroup (of the permutation group of the set <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/>) generated
by <img alt="$m\mapsto m^e$" src="svgs/b01d456ec4b11056a006a150293a1169.svg" valign=0.0px width="60.673720799999984pt" height="10.91968515pt"/> likely has very large order. An attacker cannot simply iterate the
permutation to that order; rather, <img alt="$d$" src="svgs/2103f85b8b1477f430fc407cad462224.svg" valign=0.0px width="8.55596444999999pt" height="11.4155283pt"/> is must be know which requires knowledge of <img alt="$p$" src="svgs/2ec6e630f199f589a2402fdf3e0289d5.svg" valign=-3.1963502999999895px width="8.270567249999992pt" height="10.2739725pt"/> and <img alt="$q.$" src="svgs/2e25588bd69787207bf5da9706a3070f.svg" valign=-3.1963502999999895px width="12.49431149999999pt" height="10.2739725pt"/>

#### Chosen-ciphertext attack

The algebraic nature of the RSA scheme leads to another flavor of attack, a
*chosen ciphertext attack*.
This exploit hinges on the fact that the map <img alt="$m\mapsto m^e$" src="svgs/b01d456ec4b11056a006a150293a1169.svg" valign=0.0px width="60.673720799999984pt" height="10.91968515pt"/> is a monoid homomorphism
<img alt="$\mathbb{Z}/n\rightarrow \mathbb{Z}/n$" src="svgs/8b369b20e937a35c3d23597934ff4182.svg" valign=-4.109589000000009px width="83.66065289999999pt" height="16.438356pt"/> with respect to multiplication in <img alt="$\mathbb{Z}/n;$" src="svgs/2d674892121fded6bbe718fc852b8a64.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>
that is, <img alt="$m'm\mapsto (m'm)^e=(m')^em^e.$" src="svgs/b2b18f3b61342ed10e037dd116ce037f.svg" valign=-4.109589px width="199.2359985pt" height="16.4676534pt"/>

Suppose that the attacker has intercepted <img alt="$c=m^e,$" src="svgs/c21223909224afca54749906c4e29c91.svg" valign=-3.1963519500000044px width="55.08957464999999pt" height="14.116037099999998pt"/> and assume that the attacker has the ability to
obtain the plaintext associated to any ciphertext (except c) chosen by them (the attacker).

#### :zap: Challenge :zap:

Harshad's RSA public-key is <img alt="$\{n, e\}$" src="svgs/5dbdee6d2f28cec315050f4a14b95b0c.svg" valign=-4.109589000000009px width="41.265316949999985pt" height="16.438356pt"/> where <img alt="$e=65537$" src="svgs/9031a800c7cdc076f354cc5ff9cafbb8.svg" valign=0.0px width="70.66781535pt" height="10.5936072pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is:
```python
0x799c5302bf9d09bf7b39874f23880bf5102d9f11a792c07aa822e9cd1289c198378e30eda452c88d46d6bc2f3393834c9252ff79d6cb53e876011acbb49b0ba305bbc1ce204cfb2c7c0610051c63752d9b8cd8e8a16e6b92dda67242ee8e8e62bccd87250638d9d751c565917bef78b7b929a7a9900f06ab66962776260900fd
```
Suppose that Bloem discovers a very special number, encrypts it using Harshad's public key, and sends the resulting ciphertext to Harshad.  You, of course, intercept the ciphertext, which is:
```python
0xa8713dfdd0acb832e983ad568087001493afb8de806d45dedcf8cc2f35607e3aa7bf9fed857ee35aeb3c880962dbf5491b596528908007f1c89504c03b948917704fe29eef5afe934a9bcd5e7334daa994584109d704ee8bd6d3733323d7ce14e5f7bfd63e92441206e95d8316b8c25d8093c7afc219032ef56d354830c81f2
```
22. Next, you use Harshad's public key to encrypt, say, <img alt="$m'=142857$" src="svgs/91688f5ff10555c58f3052647d17ef46.svg" valign=0.0px width="90.27786239999999pt" height="12.358064399999998pt"/> obtaining <img alt="$c'$" src="svgs/3ce681234d1b2ad17008503143e3ed8b.svg" valign=0.0px width="10.90376594999999pt" height="12.358064399999998pt"/>. Then you trick Harshad into deciphering the product <img alt="$c'c$" src="svgs/a3555722ecd81027239508a8d75bd575.svg" valign=0.0px width="18.839483849999993pt" height="12.358064399999998pt"/> and sending the resulting plaintext to you.  If he sends you <img alt="$288071548868146555184504832$" src="svgs/7803dcdee68289fd1b7f60f7ce8c8016.svg" valign=0.0px width="221.91865409999997pt" height="10.5936072pt"/>, how can you now compute Bloem's original plaintext?  What is Bloem's original plaintext?

In algebraic terms, the attacker picks any <img alt="$m'\in (\mathbb{Z}/n)^*$" src="svgs/21e3ec33ebbafec11263001d6e76a59a.svg" valign=-4.109589px width="87.70176855pt" height="16.4676534pt"/> and encrypts it using the public key <img alt="$\{n, e\}$" src="svgs/5dbdee6d2f28cec315050f4a14b95b0c.svg" valign=-4.109589000000009px width="41.265316949999985pt" height="16.438356pt"/> obtaining <img alt="$c'=(m')^e.$" src="svgs/746fed1486569b6e9ad56e48833ec0d3.svg" valign=-4.109589px width="77.09875799999999pt" height="16.4676534pt"/>   Then the attacker somehow tricks Harshad into decrypting <img alt="$c'c \in \mathbb{Z}/n$" src="svgs/1b658c365ea1e2931cadbd60058f850f.svg" valign=-4.109589px width="67.97564729999998pt" height="16.4676534pt"/> where, of course, <img alt="$c=m^e$" src="svgs/1436d3cf9e0a368740082b75397824b9.svg" valign=0.0px width="49.70145344999999pt" height="10.91968515pt"/>, which can then easily be used to compute <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> since <img alt="$m'$" src="svgs/6a0d5b419381f23bef964dd9f443238f.svg" valign=0.0px width="18.223061999999988pt" height="12.358064399999998pt"/> is invertible.

It may seem disingenuous to imagine the target of an attack cooperating with the attacker by decrypting
whatever the attacker wishes. In fact, complexity-based cryptography often assumes that an attacker
has access to an *oracle* that does exactly that &mdash; decrypt anything the attacker wishes
(besides the ciphertext <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> itself).  The idea is to devise protocols that can withstand even
so-called *chosen-ciphertext attacks*.

#### Malleability

An adversary intercepts a ciphertext <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> encoding a secret message <img alt="$m\in\mathbb{Z}/n.$" src="svgs/bcefac416d525f8ddff381534eebe8c1.svg" valign=-4.109589000000009px width="68.1354894pt" height="16.438356pt"/>  Suppose
that the eavesdropper gains some advantage if they can multiply the message <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> by 2 (or any element of
<img alt="$\mathbb{Z}/n).$" src="svgs/01bc4b9ee8aedd4b2c20074242d0ee03.svg" valign=-4.109589000000009px width="40.00396784999999pt" height="16.438356pt"/>

First, the eavesdropper computes <img alt="$c'=2^e$" src="svgs/7f60d34ae4428788305beb2fd3191a49.svg" valign=0.0px width="48.09943874999999pt" height="12.358064399999998pt"/> and then replaces the intercepted message <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.svg" valign=0.0px width="7.11380504999999pt" height="7.0776222pt"/> with <img alt="$c'c,$" src="svgs/c323c892a2cac9c98405fcb537e3f453.svg" valign=-3.1963502999999998px width="23.405707049999993pt" height="15.5544147pt"/>
and sends it along to it's final destination.  The intended receiver of the ciphertext decodes <img alt="$c'c$" src="svgs/a3555722ecd81027239508a8d75bd575.svg" valign=0.0px width="18.839483849999993pt" height="12.358064399999998pt"/>
obtaining <img alt="$(c'c)^d = (c')^dc^d = 2m$" src="svgs/d2eb26f3d95bbf2ed58cbfd1cd6a3180.svg" valign=-4.109588999999991px width="152.73239189999998pt" height="18.06580875pt"/> instead of <img alt="$m.$" src="svgs/4bc868b30aee0dfd5de42ea15b2cb2d8.svg" valign=0.0px width="18.99932429999999pt" height="7.0776222pt"/>

### Toward semantic security

As we saw above, Plain RSA is not secure against choosen-ciphertext attacks; worse, it is not
even secure against so-called *passive* attacks that assume that attacker has access only to
the public-key and so can only choose plaintexts and encrypt them.

For a public-key cryptosystem to be [semantically secure](https://en.wikipedia.org/wiki/Semantic_security)
it must provably bar against an attacker gaining any practical advantagous partial information
about a plaintext given only the corresponding ciphertext and the public key. The technical
definition requires *chosen-plaintext* indistinguishability which, in turn, imagines an oracle
that randomly selects from two equal-length messages submitted by an adversary, encrypts it with
a randomly selected public-key, and returns the resulting ciphertext along with the public-key
to the adversary.  The requirement is that the attacker cannot practically distinguish which
message was chosen by the oracle with probability significantly greater that 1/2.

Plain RSA immediately fails this test because it is deterministic: the attacker need
only use the public-key to encrypt two messages &mdash; 0 and 1, say &mdash; and then submit
those ciphertexts to the oracle.  The one randomly selected by the oracle can be identified
with 100% accuracy.

That is to say, Plain RSA has to be enhanced in order to have a chance of being
semantically secure which, even then, may be still be open to chosen-ciphertext attacks.
The modern solution is to use randomly-generated padding to augment messages before they
are encrypted using the public-key &mdash;
[OAEP](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding)
(Optimal Asymmetric Encryption Padding) is usual method for doing this with RSA.
RSA with OAEP is non-deterministic; multiple ciphertexts corresponding to the same message
will, with extremely high-probability, be mutually distinct.

#### Encoding human-readable messages

In our plain RSA scheme, our
message has so far been some element of <img alt="$\mathbb{Z}/n$" src="svgs/5a25068b686730b0d5c6d3c047688395.svg" valign=-4.109589000000009px width="29.04502589999999pt" height="16.438356pt"/>, which we naturally represent
with a positive integer less than <img alt="$n.$" src="svgs/ea8d90fb4a8d92af94283e10af3efb57.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> What's the standard way to implement messages
containing letters and other characters?

In RSA, the modulus <img alt="$n=pq$" src="svgs/dd91a3c974e35acb9bfc9b9833a127b8.svg" valign=-3.1963502999999895px width="47.98317974999999pt" height="10.2739725pt"/> is large &mdash; 1024-bit, say.  Suppose that we
use a small *alphabet* to construct human-readable messages. For English speakers one
might minimally choose the 26 lowercase letters *a* to *z*. If we allow arbitrary messages,
using those letters, of length, say, <img alt="$\ell,$" src="svgs/ac83c4d50a360c128227d15fb6d25884.svg" valign=-3.1963503000000055px width="11.41559099999999pt" height="14.611878599999999pt"/> then we already have a problem if
<img alt="$\ell^{26}\ge n$" src="svgs/4032298ea417792e6c43b9b3ad12182f.svg" valign=-2.235141150000008px width="52.56087704999999pt" height="15.616017449999998pt"/> &mdash; if <img alt="$\ell &gt; 1024/\log_2(26)\approx 217$" src="svgs/293c7cbec4fcccf9e3d571f0322e3aa7.svg" valign=-4.109589000000009px width="177.00918509999997pt" height="16.438356pt"/> &mdash; since then we
cannot *injectively* map the human-readable messages to <img alt="$\mathbb{Z}/n.$" src="svgs/b2db6c8686053451d402312789bf8098.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/>

If we want spaces and punctuation, we could use [ASCII](https://en.wikipedia.org/wiki/ASCII)
which is a character encoding comprising upper- and lower-case letters, single-digit decimals,
and various punctuation, along with 32 control characters that we probably don't need. There
are 95 printable characters.
All together, ASCII encodes 128 characters into 7-bit integers
(see this [chart](https://en.wikipedia.org/wiki/ASCII#/media/File:USASCII_code_chart.png)).

[PKCS #1](https://en.wikipedia.org/wiki/PKCS_1) (Public-key Cryptography Standards)
provides basic definitions and mathematical constructs underlying the RSA encryption
scheme and makes recommendations in terms of *primitives* for implementations.
Since PKCS recommends an 8-bit &mdash; so one byte, or, octet &mdash; encoding, it makes
sense to use [UTF-8](https://en.wikipedia.org/wiki/UTF-8) (which includes ASCII as its
first 128 characters).

Using an 8-bit encoding, we can encode UTF-8 messages of length <img alt="$\log_2(n)/8$" src="svgs/07ccdb74af1b821937c2af6522666825.svg" valign=-4.109589000000009px width="67.69809914999998pt" height="16.438356pt"/>
(<img alt="$\approx 128$" src="svgs/1c3a2564437192713d94f081a20dee3d.svg" valign=0.0px width="42.00916004999999pt" height="10.5936072pt"/> if <img alt="$n\approx 2^{1024}).$" src="svgs/a5275f955b85f5b684e0a440b1baa1fd.svg" valign=-4.109589000000009px width="77.99474264999999pt" height="17.4904653pt"/> Longer messages would have to be broken up into blocks, each of which would be encrypted in turn.

PKCS #1 defines a primitive called
[OS2IP](http://mpqs.free.fr/h11300-pkcs-1v2-2-rsa-cryptography-standard-wp_EMC_Corporation_Public-Key_Cryptography_Standards_(PKCS).pdf#page=9)
(Octet String to Integer
Primitive) which takes a sequence of bytes and returns a non-negative integer.
Let us implement OS2IP in Python.

First, we convert a string holding our message to a Python
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes) object.
```pycon
>>> message = b'"Information: the negative reciprocal value of probability." -- Shannon, 1948'
>>> message
b'"Information: the negative reciprocal value of probability." -- Shannon, 1948'
>>> type(message) # <class 'bytes'>
```

Note: if you want to include unicode characters beyond ASCII, then you may need to specify
UTF-8 when converting to bytes:.
```pycon
>>> message = '« Secret de deux, secret de Dieu; secret de trois, secret de tous. » -- proverbe français'.encode('utf8')
>>> message
b'\xc2\xab Secret de deux, secret de Dieu; secret de trois, secret de tous. \xc2\xbb -- proverbe fran\xc3\xa7ais'
```
A Python [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) object behaves somewhat like a string:
```pycon
>>> message[0]
194
```
UTF-8 is a *variable-length* encoding (see, for example, [here](https://sethmlarson.dev/blog/utf-8));
each character is encoded using one to four octets (bytes). More frequently occurring characters
generally use less bytes.  The [left guillemet](https://unicode-table.com/en/00AB/)
uses two bytes: **C2 AB** in hex, which is **194 171** in decimal.

Let us now implement
[OS2IP](http://mpqs.free.fr/h11300-pkcs-1v2-2-rsa-cryptography-standard-wp_EMC_Corporation_Public-Key_Cryptography_Standards_(PKCS).pdf#page=9).

```python
def OS2IP(X):
    """Return the integer primitive x for the octet-string X."""
    # the sum below is the same as: int.from_bytes(X, byteorder = 'big', signed = False)
    return sum([x * 256**i for i, x in enumerate(X[::-1])])
```

The standard uses the notation <img alt="$xLen$" src="svgs/ccd980f9aeab6b5d4b9bee60ff66c017.svg" valign=0.0px width="38.103245399999984pt" height="11.232861749999998pt"/> for the number of octets in the input octet string.
If <img alt="$x_{xLen-1}x_{xLen-2}\ldots x_{1}x_{0},$" src="svgs/4e948ff57f32be23156b9828b90923ca.svg" valign=-3.8356081499999894px width="178.52049599999998pt" height="10.91323035pt"/> where each <img alt="$x_i\in\{0, 1, 2, \ldots,255\},$" src="svgs/cece3527405b121c79ccf48dc01f5c27.svg" valign=-4.109589000000009px width="156.4200033pt" height="16.438356pt"/> represents
our octet string, then **OS2IP** maps this to the integer <img alt="$\sum_{i=0}^{xLen-1}x_i 256^i$" src="svgs/c2cc9102cd83bcb426ae0ef47b2cdaf9.svg" valign=-4.931582699999996px width="112.75166759999999pt" height="21.0595869pt"/>
(the left-most octet determines the most significant portion of the integer).

For fixed <img alt="$xLen$" src="svgs/ccd980f9aeab6b5d4b9bee60ff66c017.svg" valign=0.0px width="38.103245399999984pt" height="11.232861749999998pt"/>, the map defines a bijection from the set of octet strings of length <img alt="$xLen$" src="svgs/ccd980f9aeab6b5d4b9bee60ff66c017.svg" valign=0.0px width="38.103245399999984pt" height="11.232861749999998pt"/>
to the set <img alt="$\{j\in\mathbb{Z}~|~ 0 \le j&lt; 256^{xLen}\}.$" src="svgs/ba02457a75e8aad93cda348c5c1c5b3d.svg" valign=-4.109589px width="191.3702736pt" height="17.9379651pt"/>
The inverse mapping is called
[I20SP](http://mpqs.free.fr/h11300-pkcs-1v2-2-rsa-cryptography-standard-wp_EMC_Corporation_Public-Key_Cryptography_Standards_(PKCS).pdf#page=8):
```python
def I2OSP(x, xLen):
    """Map an integer x to an octet-string X."""
    assert x < 256**xLen, "integer too large"
    return x.to_bytes(xLen, byteorder = 'big', signed = False)
```

Test driving those two functions on the message above, we have:
```pycon
>>> m = OS2IP(message)
>>> m
274873227007013220853194865361031398209358857387795228459596366470548372698409537461728865739289920635511061986596506444387159296380925336687869159143300946529393908706703078375797190040253439843230647079564428903853418867
>>> I2OSP(m, len(message)).decode('utf8')
« Secret de deux, secret de Dieu; secret de trois, secret de tous. » -- proverbe français
```

#### Exercise

23.  The following integers were obtained by partitioning the **bytes** version of a long human-readable message into pieces and applying OS2IP to each piece in turn.  Decode the 3 integers back into a single human-readable message assuming that <img alt="$xLen = 125$" src="svgs/f8d7227d277962cfbf35e34a12bfbca7.svg" valign=0.0px width="84.67850324999999pt" height="11.232861749999998pt"/>.
     ```python
     8148005161556551804043142199660631494681528140650822600136084998387357112108317491287436260923406505931864938073161946364938332791368570105875948573513727327591104929790537105755837082151488779548034635309275341934058978012160570568794235012357380859739572435669585019614245512029471707669863116139888
     4536349843976346312836460170468749286561964424351466747171040921929279400531580926025621971360458028850193810030292112586186499583889141942059093666096467348224496980293734851564288662520367071658728765218415511795671620978766949287934200652050299193168658544707334905806785657101906068685821747491616
     12208130087930690061449158021184773120883647178368244218281293496571934819926953
     ```

#### Padding

A short input to OS2IP results in small output, and we've already seen that small <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> (relative
to <img alt="$n)$" src="svgs/d5832d8437237f9b3dbe873f044d5de9.svg" valign=-4.109589000000009px width="16.25959334999999pt" height="16.438356pt"/> can lead to weak encryption.   We want a given plaintext <img alt="$m$" src="svgs/0e51a2dede42189d77627c4d742822c3.svg" valign=0.0px width="14.433101099999991pt" height="7.0776222pt"/> to land essentially
uniformly in <img alt="$\mathbb{Z}/n,$" src="svgs/4ee8f29e8fc6ff907c10277ad56123ba.svg" valign=-4.109589000000009px width="33.61125074999999pt" height="16.438356pt"/> regardless of specifics such length of our human-readable message.
A good approximation to uniformly distributed plaintexts can be achieved by padding our
human-readable messages in such a way that they are of more or less maximum length. Also,
if we pad with randomly generated bytes, then the same message leads to distinct plaintexts
under repeated encodings.

Let us implement the padding scheme recommended in
[PKCS #1 v2.2: RSA Cryptography Standard](http://mpqs.free.fr/h11300-pkcs-1v2-2-rsa-cryptography-standard-wp_EMC_Corporation_Public-Key_Cryptography_Standards_(PKCS).pdf#page=24).
:warning: This padding scheme bars against the exploits mentioned above but is still open to compromise.  An improved padding involving hashing is implemented below.

The function **RSAencrypt** in the following codeblock implements the encryption protocol in the
standard except that it outputs the ciphertext in the form of an integer (note that it uses the
Blum Blum Shub PRBG that we constructed above).  Likewise, the function **RSAdecrypt** takes the
ciphertext in the form of a positive integer.

```python
import math
from blumblumshub import prbg

def RSAencrypt(n, e, message):
    """Return ciphertext given an RSA key {n, e} and a message.

    Args:
        n (int): the modulus.
        e (int): the encrypting exponent.
        message (bytes): the message (as a bytestring) to encrypt.

    Returns:
        int. A non-negative integer less than n.
    """
    # the length of n in whole octets
    k = math.floor(math.log(n, 256))

    # check that message is short enough leaving room for padding
    mLen = len(message)
    if mLen > k - 11:
        raise ValueError("message too long")

    # generate a random bytes-string consisting of non-zero bytes
    # (this will have length at least 8)
    ps = b''
    while len(ps) < k - mLen - 3:
        decimal = int(prbg(8), 2)
        if decimal != 0:
            ps += decimal.to_bytes(1, byteorder = 'big')

    # pad message and convert to integer, encrypt, and return
    m = OS2IP(b'\x00' + b'\x02' + ps + b'\x00' + message)
    return pow(m, e, n)

def RSAdecrypt(n, d, ciphertext):
    """Return message decrypted from ciphertext using key {n, d}.

    Args:
        n (int): the modulus.
        d (int): the decrypting exponent.
        ciphertext (int): the message to decrypt.

    Returns:
        bytes. A bytes-string representing the decrypted message.
    """
    # get the padded message
    m = pow(ciphertext, d, n)
    k = math.floor(math.log(n, 256))
    message = I2OSP(m, k)

    # strip away the padding
    error = False
    if message[0] != 0:
        error = True
    message = message[1:]
    if message[0] != 2:
        error = True
    message = message[1:]
    while message[0] != 0:
        message = message[1:]
    if message[0] != 0:
        error = True
    message = message[1:]

    assert not error, "decryption error"

    return message
```
#### Exercises

24. Send Simmons a human-readable message that you have encoded using UTF-8 and encrypted using padding. Simmons' RSA key is <img alt="$\{n, e\}$" src="svgs/5dbdee6d2f28cec315050f4a14b95b0c.svg" valign=-4.109589000000009px width="41.265316949999985pt" height="16.438356pt"/> where <img alt="$e=65537$" src="svgs/9031a800c7cdc076f354cc5ff9cafbb8.svg" valign=0.0px width="70.66781535pt" height="10.5936072pt"/> and <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg" valign=0.0px width="9.86687624999999pt" height="7.0776222pt"/> is below.
    ```python
    0xba8bc3ac255165d1175b0c4fc74c8f2563aa5ad3ff80787d8849f0049d1202baa0eb667a837d0c5c6f49da4120cbc949fed060f92960c150526b7e0704dae798b5739363a5cac39323a03f7ac2cd5c5bca2a59a7b78dc3dfc5613f1a3d5804e3f4d990a98042724e1ab25b87a30e935d3ad36a270d879d23f19432006367ce7b3822f94038044eb66790aa1d61587c6d46ef7cf95818fb59df4ebb1d87b3a1a08bcb5e1e5416e9ca136ffe64c7742cfb048c316ca5a595aab3cd151d28c66a31
    ```
25. :zap:**Challenge**:zap: Send Simmons a long (encrypted) message that you had to break up
    into pieces, where you used the minimal number of pieces.


<a id="references2">

#### References

* Boneh, Twenty Years of Attacks on the RSA Cryptosystem. Available at [crypto.standford.edu](https://crypto.stanford.edu/~dabo/pubs/papers/RSA-survey.pdf).
* Hikima, Iwasaki, and Umeno, The reference distributions of Maurer's universal statistical test and its improved tests. [arxiv.org/abs/2103.10660](https://arxiv.org/abs/2103.10660), 2021.
* Sidorenko, Schoenmakers, Concrete security of the blum-blum-shub pseudorandom generator.
[scinapse](https://www.scinapse.io/papers/2165645235), 2005.






<p align="right">  <a href="#contents"> contents </a></p>

&nbsp;  

<p align="center"> :stop_sign: STOP :stop_sign: </p>

&nbsp;  

---

<p align="center"> :construction: BELOW IS CURRENTLY UNDER CONSTRUCTION :construction: </p>





### Hashing and Signing

The Plain RSA protocol can be augmented in such a way to bar against the exploits mentioned
above. But doing so is all for naught if we cannot prevent an attacker from replacing a ciphertext
in transit.  How can the recipient of a ciphertext guarantee the identity of the sender &mdash; or,
at least, detect whether a received ciphertext has been tampered with? Answer, the sender needs
to sign the message, and the receiver needs to verify the signature.

First, what if we want to use, say, RSA to en/decrypt human readable messages? How do we map
characters to integers when encoding and inters back to characters when decoding?

:warning: For the following discussion and exercise, we continue to use plain RSA;
i.e., non-padded, and so not secure.

A standard way to do this encode the

 let us encode, in Python, a string of




## III. Cryptographic primitives

*Cryptography* is the study of *cipher algorithms* by which we obscure data.
The cipher algorithm involves a *key* that is used to encrypt *plaintext* data
into *ciphertext*.  In *symmetric cryptography* (or *symmetric-key encryption*)
the key used for encryption is also used to decrypt the ciphertext back into
plaintext so that they key must be kept secret.

Cryptanalysis deals with the process by which attackers might "break" the
encryption

Cryptology

In *asymmetric cryptography* (or *public-key encryption*)

### Symmetric Cryptography



### Elliptic Curves

For ECDSA, Bitcoin uses [secp256k1](https://en.bitcoinwiki.org/wiki/Secp256k1) &mdash; which
refers the curve <img alt="$y^2=x^3+7$" src="svgs/ef8074c158e4356135b8122fb6068c03.svg" valign=-3.1963503000000086px width="83.02114589999998pt" height="16.5772266pt"/> over the primefield <img alt="$\mathbb{Z}/p$" src="svgs/73c9c321abfaf561fdbde1304ada12c1.svg" valign=-4.109589000000009px width="27.448716899999987pt" height="16.438356pt"/> where
<img alt="$p = 2^{256} - 2^{32} - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1$" src="svgs/aa8eafdca40e7443a9e647146f705d02.svg" valign=-3.1963503000000086px width="307.85905590000004pt" height="16.5772266pt"/> with parameters given on page 6
of [SEC2-v2](http://www.secg.org/sec2-v2.pdf) from the Standards for Efficient Cryptography.

We can use **numlib** to get our hands on this curve:

```pycon
>>> import numlib as nl
>>>
>>> p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
>>> F = nl.Zmodp(p)
>>>
>>> E = nl.EllCurve(0, F(7))
>>> E
y^2 = x^3 + 7 over Z/115792089237316195423570985008687907853269984665640564039457584007908834671663
```
Let us define the basepoint specified in [SEC2-v2](http://www.secg.org/sec2-v2.pdf):
```pycon
>>> G = E(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
```
The order of **G** is large and also given in the specification.  Let us verify that G has the given
order.
```pycon
>>> G_order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
>>> G_order * G
[0: 1: 0]
```

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

  assert gmpy2.gcd(e, phi) == 1  # {n, e} is our public key

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


