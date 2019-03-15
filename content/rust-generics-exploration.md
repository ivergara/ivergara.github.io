Title: Exploring Rust
Date: 2019-03-15 11:00
Category: rust, 
Tags: rust, generics
Slug: Rust-generics-exploration
Summary: 
Status: Published

For a while I've been interested in Rust, reading articles and books, and trying to do some small exercises in it, but in general still rather superficial. Now, after reading the following the [second part](https://www.lpalmieri.com/posts/2019-03-12-scientific-computing-a-rust-adventure-part-1-zero-cost-abstractions/) of a series of articles on *Scientific computing in Rust, I decided to use that example to explore a bit more and challenge myself. The article mentions very early the following 
> But what happens when someone else comes up with a new numerical type with a legitimate concept of addition and multiplication (e.g. complex numbers)?

to motivate exploring generics, but the scenario of complex numbers was not explored. Thus, I wondered how to use the example function used in it, namely `generic_scalar_product`, with a more complex type., e.g., complex numbers. This means to implement the `num_traits::Zero` trait into a type implementing a complex number since the function has such trait as type bound for its arguments.

## Complex number
(Un)Fortunately, this case is easy by using the related crate `num_complex` that indeed implements the `Complex` type with the needed trait `num_traits::Zero`. Thus, taking the code from the article and making use of the `num_complex` crate we get the following ([playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=7e7c7e7e7f84b084f1aceb92b7a8757b))

```rust
extern crate num_traits;
extern crate num_complex;

use num_complex::Complex64;

fn generic_scalar_product<T>(v: &[T], w: &[T]) -> T
where
    T: num_traits::Zero + std::ops::Mul<Output = T> + Copy
{
    let length = v.len(); 
    assert_eq!(length, w.len()); 
    
    // We initialise `sum` to a "zero" of type T
    // using the `zero` method provided by the `Zero` trait
    let mut sum = T::zero(); 
    for index in 0..length {
        sum = sum + v[index] * w[index];
    }
    sum
}

fn main() {
    // Complex
    let v: Vec<Complex64> = vec![Complex64 { re: 1.0, im: 0.0 }, Complex64 { re: 1.0, im: 0.0 }, Complex64 { re: 1.0, im: 0.0 }];
    let w: Vec<Complex64> = vec![Complex64 { re: 1.0, im: 0.0 }, Complex64 { re: 1.0, im: 0.0 }, Complex64 { re: 1.0, im: 0.0 }];
    assert_eq!(generic_scalar_product(&v, &w), Complex64 { re: 3.0, im: 0.0 });
}
```

So, this was not much of a challenge... still a nice excercise/warmup for a beginner (like myself) in Rust to gain some confidence. But then, I was already commited to explore some more. This leads then to the _real_ challenge of how to use this `generic_scalar_product` with a type of our own making. We could take for example quaternions or some other thing.

## (Local) Custom type

We could take two paths to develop this example:
* Build piece by piece doing _pair programming_ with the rust compiler implementing all needed traits to our new type until we stop having compilation errors.
* Write our type already implementing commonly expected traits like `Add` and `Mul` as if it were a "mature" piece of code we already have and we want to use with the `generic_scalar_product` function.

I'll take the second option, and then set out to extend it to make it compatible with `generic_scalar_product`.

Our new type will be `NAlgebra`, which will be implemented as two underlaying `f64` types. This is to make our task easier by not needing to take care for generics at this point, but it'd be a good next exercise.
```rust
use std::ops::Add;
use std::ops::Mul;

#[derive(Debug)] // debug to be allowed to be printed
struct NAlgebra {
    a: f64,
    b: f64,
}

impl NAlgebra {
    fn new(x: f64, y: f64) -> NAlgebra {
        NAlgebra { a: x, b: y }
    }
}

impl Add for NAlgebra {
    type Output = NAlgebra;

    fn add(self, other: NAlgebra) -> NAlgebra {
        NAlgebra {
            a: self.a + other.a,
            b: self.b + other.b,
        }
    }
}

impl Mul for NAlgebra {
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        let a = -self.a * rhs.a;
        let b = -self.b * rhs.b;
        NAlgebra::new(a, b)
    }
}

fn main() {
    let v: Vec<NAlgebra> = vec![NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }];
    let w: Vec<NAlgebra> = vec![NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }];
    assert_eq!(generic_scalar_product(&v, &w), NAlgebra { a: -3.0, b: 0.0 });
}
```
It works, in the extent of our test and for the purposes of our example. Now the interesting part starts. We need to implement the relevant trait for our `generic_scalar_product` function, namely `num_traits::Zero`. We can check the documentation of the [`Zero` trait](https://docs.rs/num-traits/0.2.6/num_traits/identities/trait.Zero.html), and we see the following
```rust
pub trait Zero: Sized + Add<Self, Output = Self> {
    fn zero() -> Self;
    fn is_zero(&self) -> bool;
}
```
Thus, the methods to be implemented are `fn zero() -> Self` and `fn is_zero(&self) -> bool`. This can be easily achieved as follow (for some help/inspiration see [the code](https://docs.rs/num-complex/0.1.40/src/num_complex/lib.rs.html#764-774) in `num_complex` crate for the implementation onto `Complex`)

```rust
// implementing the Zero trait for our custom type
impl num_traits::Zero for NAlgebra {
    fn zero() -> Self {
        NAlgebra::new(Zero::zero(), Zero::zero())
    }
    fn is_zero(&self) -> bool {
        self.a.is_zero() && self.b.is_zero()
    }
}
```
Here we're assuming that the fields `a` and `b` in `NAlgebra` are supported by the `num_traits` crate, which is the case since our underlaying data is `f64`. Thus, the whole code looks as follows ([playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=13523cd71628685ee333627637005c61))

```rust
extern crate num_traits;

use num_traits::Zero;  // importing trait Zero into local scope

use std::ops::{Add,Mul};

#[derive(Debug, PartialEq, Copy, Clone)]
struct NAlgebra {
    a: f64,
    b: f64,
}

impl NAlgebra {
    // Another static method, taking two arguments:
    fn new(x: f64, y: f64) -> NAlgebra {
        NAlgebra { a: x, b: y }
    }
}

impl Add for NAlgebra {
    type Output = NAlgebra;

    fn add(self, other: NAlgebra) -> NAlgebra {
        NAlgebra {
            a: self.a + other.a,
            b: self.b + other.b,
        }
    }
}

impl Mul for NAlgebra {
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        let a = self.a * rhs.a;
        let b = self.b * rhs.b;
        NAlgebra::new(a, b)
    }
}

impl Zero for NAlgebra {
    fn zero() -> Self {
        NAlgebra::new(Zero::zero(), Zero::zero())
    }
    fn is_zero(&self) -> bool {
        self.a.is_zero() && self.b.is_zero()
    }
}

fn generic_scalar_product<T>(v: &[T], w: &[T]) -> T
where
    T: num_traits::Zero + std::ops::Mul<Output = T> + Copy
{
    let length = v.len(); 
    assert_eq!(length, w.len()); 
    
    // We initialise `sum` to a "zero" of type T
    // using the `zero` method provided by the `Zero` trait
    let mut sum = T::zero(); 
    for index in 0..length {
        sum = sum + v[index] * w[index];
    }
    sum
}

fn main() {
    // NAlgebra
    let v: Vec<NAlgebra> = vec![NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }];
    let w: Vec<NAlgebra> = vec![NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }, NAlgebra { a: 1.0, b: 0.0 }];
    assert_eq!(generic_scalar_product(&v, &w), NAlgebra { a: 3.0, b: 0.0 });
}
```
Besides having to implement the `Zero` trait onto `NAlgebra`, the struct had algo to be extended with the `Clone+Copy` annotations due to the `sum = sum + v[index] * w[index];` line. This was nicely provided by the compiler, and while I understand why `Copy` is needed I'm not sure why `Copy` and `Clone` have to be specified. This is something I've encountered before too in other examples and should give some more thought.

There are quite some more ways to keep working on this little example, to extract more learning nuggets. I'll list a few that come to mind:
1. Generalizing the definition of `NAlgebra` to support a generic underlaying type would be an interesting next step. 
2. Taking an external crate like [quaternion](https://docs.rs/quaternion/0.3.1/quaternion/) and extending it from outside to be able to be used in `generic_scalar_product`. 
3. Improve the structure of this example and put all the `NAlgebra` stuff in its own module within the same crate.
4. Use Rust's testing capabilities to produce proper testing of `NAlgebra` and its later added behavior.

I'd say that the first two have some overlap, while the last two ones could be tackled together.

So, go on... explore and play with these ideas!

---

## Bonus

At the end of this excursion, there was one thing that kinda bothered me. The return value of `generic_scalar_product` is `T`. As an example is fine, and avoids burdening the begginer reader with error handling, but I believe that showing proper error handling early on is extremely important. This means, that the return of that function should be something more like `Result<T,Err>` with the `assert_eq!(length, w.len());` replaced with an early return with the error. To make it easy, the error returned will be just a string thus the type will be `Result<T,String>`

Quickly attending to this last quibble ([playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=bc2d0efa591b0a0edd64bba21267a325))

```rust
extern crate num_traits;

fn generic_scalar_product<T>(v: &[T], w: &[T]) -> Result<T,String>
where
    T: num_traits::Zero + std::ops::Mul<Output = T> + Copy
{
    let length = v.len(); 
    
    if length != w.len() {
        return Err("The vectors have different lengths!".to_string());
    }
    
    // We initialise `sum` to a "zero" of type T
    // using the `zero` method provided by the `Zero` trait
    let mut sum = T::zero(); 
    for index in 0..length {
        sum = sum + v[index] * w[index];
    }
    Ok(sum)
}

fn main() {
    // Unsigned integers
    let x: Vec<u32> = vec![1, 1, 1];
    let y: Vec<u32> = vec![1, 0, 1];
    assert_eq!(generic_scalar_product(&x, &y).unwrap(), 2);
}
```
And sure, the `unwrap()` at the end might seem less than ideal, but the `main()` function is acting as a test suite and we're handcrafting the inputs. In this case, to me, it seems completely fine to just unwrap the result.