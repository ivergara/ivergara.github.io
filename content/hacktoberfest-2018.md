Title: My "Hacktober" 2018 experience
Date: 2018-11-06 10:20
Category: Open Source, Python
Tags: open source 
Slug: hackoctober-2018
Summary: My first experience contributing during Hacktoberfest.
Status: published

My Hacktoberfest 2018 Experience
Last year I learned rather late about the Hackoctoberfest. This year, wasn’t that much different, and I didn’t manage to plan ahead on how to participate. But this story would be extremely boring if it ended like this.

By the end of the month of October, and by chance, I ended up stumbling upon a little project called deon that generates a good practices checklist for data based experiments. I’ll not go into depth about it since they do a great job at explaining what are their objectives.

More importantly, deon is small in scope and rather simple, but smartly done. One of their issues was to extract all the logic they had placed into the main CLI entrypoint to it own “core” function leaving the CLI as a wrapper around it.

Since this project uses click as a CLI framework and I’ve been using it to learn how to create and organize nice CLI applications I thought “hey, this looks like something that can be done quickly!”. And indeed it was quick, and my contribution was merged promptly.

Since in my opinion the changes left the test suite a bit badly organized, I did set to change and clean up the test. Repurposing the old tests that were dealing with the CLI directly for the new core, and then creating lightweight CLI testing suite, focusing on the CLI and not on the newly extracted core. Fortunately they were using pytest which I realy like and use it exclusively by now, thus I managed to use some parametrization to reduce lines of code.
The PR was merged after some minor details. Personally, I’m satisfied with the looks of the test suite, even when there is still room for improvement.

After this success, I kept looking into the open issues. The second one I found that was more on the technical side is related to offer the creation of the checklist via a web application. Someone already had commented showing interest in implementing it, but that was more than a month earlier and there was no movement in his forked repository. Thus, I decided to start tackling it. Once again, using what I’ve been experimenting with, chose flask to implement a web application with a single endpoint. For now the basic skeleton of my suggested solution is more or less complete and further development would need feedback from the project owners/maintainers. Unfortunatelly the comment on the issue has not been considered, perhaps I should go ahead and try out a pull request directly.

So, in the end, and without forcing it, I ended contributing a tiny bit into an open source project during October-November. It does even mark my first contribution in code as previously I’ve contributed with some cleaning and docummenting of the test suite in pandas (which I hope to continue at some point). Moreover, I did contribute by using directly what what I’ve been learning since transitioning to being a full time software developer and what I’ve explored personally.