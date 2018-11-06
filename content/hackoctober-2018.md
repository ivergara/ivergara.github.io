Title: My "Hacktober" 2018 experience
Date: 2018-11-06 10:20
Category: Open Source, Python
Tags: open source 
Slug: hackoctober-2018
Summary: My first experience contributing during Hacktoberfest.
Status: published

Last year I learned rather late about the hack october activity in the open source world. This year, wasn't that different, and I didn't manage to plan ahead on how to participate. But this story would be extremely boring if it ended like this.

By chance, I stumbled upon a little project called [deon](https://github.com/drivendataorg/deon/) that generates a checklist of good practices for data based workflows. I'll not go into depth about it since [they](http://deon.drivendata.org/) do a great job at explaining at large what their objectives are.

`deon` is little CLI project in `python`. And although it is rather simple, in my opinion it is smartly done. Luckily, one of their open [issues](https://github.com/drivendataorg/deon/issues/66) was to extract all the logic they had placed into the main CLI entrypoint command to its own "core" function leaving the CLI as a wrapper around it. Since this project uses `click` as a CLI framework and I've been using it to learn how to create and organice nice CLI applications I thought "hey, this looks like something that can be done quickly!". And indeed it was quick, and the [contribution](https://github.com/drivendataorg/deon/pull/73) was merged promptly. 

Since the changes left the test suite a bit badly organized (in my opinion), I did set to change and clean up the test suite. Repurposing the old tests that were dealing with the CLI directly for the new core, and then creating lightweight CLI testing function. Fortunately they were using `pytest` which I realy like and use it exclusively by now in my own work, thus I managed to use some parametrization to reduce lines of code and verbosity.
The [PR](https://github.com/drivendataorg/deon/pull/74) was recently merged to the master branch and I'm satisfied with the looks of the test suite, even when there is still room for improvement.

After this success, I kept looking into the open issues. The second one I found that was more on the technical side is related to offer the creation of checklists via a [web application](https://github.com/drivendataorg/deon/issues/33). Someone already had commented showing interest in implementing it, but that was more than a month earlier and there was no movement in his forked repository. Thus, I decided to start tackling it. Once again, using what I've been experimenting with, chose `flask` to implement a web application with a single endpoint. For now the basic skeleton of [my suggested solution](https://github.com/ivergara/deon/pull/1) is more or less complete and further development would need feedback from the project owners/maintainers.

So, in the end, and without forcing it, I ended contributing a tiny bit into an open source project during October. It does even mark my first contribution in code as previously I've [contributed](https://github.com/pandas-dev/pandas/pull/21496) with some cleaning and docummenting of the test suite in `pandas` (which I hope to continue at some point). Moreover, I did contribute by using directly what what I've been learning since transitioning to being a full time software developer.
