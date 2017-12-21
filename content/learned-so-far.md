Title: What I've learned so far - my first six months
Date: 2017-12-30 16:20
Category: job
Summary: A list of a bunch of stuff that I've learned during my first six months working at Odoscope.
Status: published

Soon I'll complete my first six months of working as a software developer. Here in Germany, that coincides with the legal trial period. Luckily, the transition from academia to my current job has been extremely smooth, due to a relaxed working atmosphere and particularly due a very scientifically oriented first task. Implementing an evolutionary strategy optimization procedure is something that is very much in the realm of possible Bachelor/Master thesis or a segment of a doctoral work for a physicist.

Overall, these first six months have been a good learning experience. Most of what I've had to learn can be categorized as "software engineering', like dealing with logs, reliance, deployment, and testing.

I want to take the opportunity to list and comment a bit on the things I've learned, explored, and played with during this time. Implicitly in this list, is the fact that most of it applies in the context of Python since it's the programming language that I know the best... and since part of my job is rather borderline with data science/analytics, having Pandas available has been a very good.

* Cassandra basics
* Jenkins base pipeline CI
* HTTP requests, including asynchronous ones
* Using decorators
* Do better logging
* Type and function annotations in Python
* Build a custom factory for Cassandra that returns a pandas `DataFrame`
* Some extensive use of `pytest` including parametrization, fixtures, mocking
* Selenium basics as a proof of concept to do end-to-end testing of our dashboard
* Using Docker
* Play with binary file formats (`arrow`, `parquet`) sending them over a network
* Handling config files using `ConfigParser`
* Use click to create a CLI
* Built a `Flask` app
* Appreciate Pycharm's debugger

Most likely I've forgotten some minor things, but this is the bulk of it. In the future, I'll try to write about some noteworthy elements of this list. Particularly the Flask based access to the cassandra database that returns a pandas dataframe as a parquet file, arrow stream, or pretty rendered HTML.

Going forwards, I'm highly interested in exploring how to improve testing with the `hypothesis` library, but still need to find a good case use for it. Also, want to explore the field of statistical programming using `pymc3`. Beyond that, hopefully I'll start doing some stuff in Go soon.

