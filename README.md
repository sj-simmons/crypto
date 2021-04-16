# crypto senior sem
### From cryptography to cryptocurrencies

This course is about the state-of-the-art in modern cryptography &mdash; and,
therefore, the primary mathematical apparatus that has, of late, been artfully
fashioned into cryptocurrencies.  Cryptography is of course pervasive and
ubiquitous in the technological age, so that this course is ultimately about
certain cutting-edge information-theoretic advancements that are reshaping our
world.  In addition to crytographic primitives, their prevailing applications,
and underlying mathematics, topics include applications of zero-knowledge proofs
and their role in present-day FinTech.

Important: as far as speculating in cryptocurrencies, we think that you are likely
better off not doing so. Whether or not you take that advice, you might
do well to look under the hood of the new-fangled tech that is built atop a rather
striking assemblage of pure and applied Math and CS.

TLDR; this is not Sh*tcoin 101 (which can be found on Youtube, TikTok and
elsewhere); rather, this course is about new takes on exceptionally powerful
mathematics. And remember, always, to please use your math skills for good,
not for ill.

## Topics

#### Cryptography

* ECC
  * [A gentle intro to ECC](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/)
  * Neal Koblitz's 1985 paper [Elliptic Curve Cryptosystems](https://www.ams.org/journals/mcom/1987-48-177/S0025-5718-1987-0866109-5/S0025-5718-1987-0866109-5.pdf)

* Relevant
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


