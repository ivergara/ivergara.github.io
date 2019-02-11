Title: Having fun with dataclasses and abstract base classes
Date: 2019-01-28 10:20
Category: Python
Tags: dataclasses, ABC, collections, boilerplate, Python 3.7
Slug: ABC-and-dataclasses
Summary: 
Status: Published
<!-- Series:  abc and dataclasses -->

Python is well known for the little boilerplate needed to get something to work. But even Python can get a bit cumbersome when a whole bunch of relatively trivial methods have to be defined to get the desired behavior of a class.
In this article we're going to explore how to combine [`dataclases`](https://docs.python.org/3/library/dataclasses.html) with the [`abc`](https://docs.python.org/3.7/library/abc.html) and [`collections.abc`](https://docs.python.org/3.7/library/collections.abc.html) modules of the standard library in Python. I'll assume that you know/understand what `abc`, `collections.abc` and `dataclases`. With the last two one could get a lot of behavior for **free**!

If you don't know about abstract base classes then I strongly recommend to check articles like [this](http://blog.thedigitalcatonline.com/blog/2016/04/03/abstract-base-classes-in-python/) and [this](http://stupidpythonideas.blogspot.com/2015/07/creating-new-sequence-type-is-easy.html), for `abc`, and `abc.collections`, respectivelly. Likewise, if you don't know why `dataclasses` are interesting and about their advantages, you should check [this](https://realpython.com/python-data-classes/) other article. Or if you prefer some more visual guide check [this](https://www.youtube.com/watch?v=epKegvx_Jws) talk. Take the time to learn these tools, it'll be worth it. Personally, since I discovered the `abc` and `collections.abc` modules, I've been trying to use them every time I can. 

When I saw the inclusion of the `dataclass` module in the standard library of Python 3.7, I told myself I wanted to use it. Being able to reduce even more the boilerplate in Python seemed like a great idea. Of course I could have already been using [`attrs`](https://www.attrs.org/) for basically the same effect, but when I tried it it didn't feel natural. That was most likely due to a lack of experience on my part.

Thus, it's very obvious that I'd end up mixing abstract classes, abstract collections, and dataclasses eventually at some point. Unfortunatelly, I haven't taken the time to refactor the code at work to this effect. To ammend that, I decided to explore the combination of `abc+dataclasses` and `abc.collections+dataclasses` with a toy example to see how straightforward, or not, the combination works. And since I didn't find any article mixing these two concepts (not that I looked too much around), I decided to write about it.

Now, getting our fingers dirty. First let's use `pipenv` to create an environment (as you should do to keep some environment hygene). It can feel slightly an overkill to do so, but I find it easier than trying to create a virtual environment from scratch. So, we initialize a Python 3.7 environment as follows `pipenv --python 3.7`. 

To guide this experiment, we'll write a simple test. You could for sure skip this and manually play with the code in the REPL of choice, which I'd recommend in any case in this case to freely explore and discover your use case, but having tests makes the process easier. Install `pytest` to run the tests by executing `pipenv install pytest`. Note that I'm not using a separate `dev` environment for this, as this is just an experimentation environment. Now, we can activate the virtual environment by using `pipenv shell`.

The simplest test I can come up with, is that the abstract class `Base` should raise a `TypeError` exception if you try to instantiate it directly.

```python
# test_demo.py
import pytest
from demo import Base

def test_abstract_base_class():
    with pytest.raises(TypeError):
        Base()
```

Before executing `pytest`, since it'll fail, we can quickly write an implementation based on `dataclasses` and `abc`. As such, the class is decorated with `@dataclass` and inherits from `abc.ABC`. Furthermore, it'll define one field `a` of type `str` with a `__post_init__` and a `process` method, the last one defined as abstract.

```python
# demo.py
import abc
from dataclasses import dataclass

@dataclass
class Base(abc.ABC):
    a: str
    
    def __post_init__(self):
      self.a = self.a.upper()
    
    @abc.abstractmethod
    def process(self) -> str:
        pass
```
So far so good. Since the `__post_init__` method is not an abstract one, it'll be executed in each class that inherits from `Base`.

Now it's time to create a class that implements the abstract class. As it is described in the [reference](https://docs.python.org/3/library/dataclasses.html#inheritance), for inheritance in `dataclasses` to work, both classes have to be decorated.
In this case, the implementation will define another field, `b` of type `str`, reimplement the `__post_init__` method, and implement the abstract method `process`.

```python
# demo.py
@dataclass
class Implementation(Base):
    b: str
    
    def __post_init__(self):
        super().__post_init__()
        self.b = self.b.lower()

    def process(self) -> str:
        return f"{self.a} {self.b}"
```

We're reimplementing the `__post_init__` method just to show that we could cover more sophisticated use cases easily. This forces us to call `super().__post_init__()` to get the post initialization of the base class. Now we can cover the behavior of this new class in a test as follows.

```python
# test_demo.py
from demo import Implementation

def test_implementation():
    implemented_instance = Implementation("Pythonic", "Musings")
    assert isinstance(implemented_instance, Base)
    assert implemented_instance.process() == "PYTHONIC musings"
```

In this test, the first `assert` is to make sure that the `Implemented` class is really an instance of `Base`. We could have just trusted Python, but since this article has an educational purpose, better to be explicit about our expectations.

One great advantage of dataclasses is that you're forced to do type annotation. So we can see what happens if we run a type checker like `mypy` on it. Executing `pipenv install mypy` and then `mypy .` we get the following

```python
demo.py:7: error: Only concrete class can be given where "Type[Base]" is expected
...
```
Only one error! That's worse than what we'd expected. Searching a bit, I found the following [issue](https://github.com/python/mypy/issues/5374) discussing this situation. Otherwise all checks up fine, and we're not interested in `mypy`'s edge cases so we could ignore it, or silence it in case you're running `mypy` as part of a CI.

At last we reach now to combining `dataclasses` and the `collections.abc` module. This combination is great since both modules provide ways to reduce boilerplate while also making intent very clear. To keep it simple it'll be a straight container with a field `c` of type `List` and a custom method `capitalize`.

```python
# demo.py
import collections.abc
from typing import List

@dataclass
class Derived(collections.abc.Container):
    c: List[str]

    def __contains__(self, value):
        return value in self.c
        
    def capitalize(self) -> List[str]:
        return list([e.upper() for e in self.c])
```

Here we get the full power of combining two boilerplate reducing approaches.
This example, by no means shows all the potential of the `collections.abc` since we chose the simplest collection possible. But it's only here to show that the combination with dataclasses works. I really recommend using the `collections.abs` module as it will allows you to encapsulate a lot, and leads to a better design.

To test it, we can go with the following code
```python
# test_demo.py
from demo import Derived

def test_derived():
    instance = Derived(["Hi", "Bye"])

    for element in ["Hi", "Bye"]:
        assert element in instance
        
    assert instance.capitalize() == ["HI", "BYE"]
```
The first assertion checks if our method works as intended. The second group of assertions, those inside the `for` loop, has only a pedagogical objective since we are ultimately testing that the `collections.abs` is working. Although sometimes, such a test is valid to comply with specification. Anyhow, will not go into epistemology of tests in here. Here again we see that the mix of `collections.abs` and `dataclasses` just works.

Our implementation of the `Derived` class is very rough. As an exercise, try to turn the `capitalize` method into a `classmethod` that takes an instance of `Derived` and returns an instance of the class with the capitalized elements. This would improve the ergonomics, since is not too coherent to return a `list` in such an implicit way. Bonus points for proper type annotation! (Hint: check PEP 563.)

With this we conclude the article. Not surprisingly, the `dataclasses` module work extremely well together with `abc` and `collections.abs`. Certainly, after this exploration, I'll start using these combinations into the future and going through older code to make use of it.

Teaser: there is another thing in Python I enjoy using, the '@property' decorator. Personally, I also wonder how that mixes with `dataclasses`, luckily someone already told their story [here](https://blog.florimondmanca.com/reconciling-dataclasses-and-properties-in-python). Spoiler alert, has a happy ending ;). Although while playing with it I've found some edge cases where things stop working nicely. I hope to explore it in more detail and show some alternative/solution.