<!-- # Don't skip out on documentation -->

More often than not I've worked on projects that, to my dismay, had limited to no documentation. Some projects didn't even include README files (fun experience when you're trying to get a custom project running). You can't always control the code that you inherit, whether it's legacy code in your own organization or an open source project. You can however make everyone else's lives easier by including some form of documentation.

A non-exhaustive list of documentation your application should include:

## Official Documentation

### README
A `README` is one of the simplest, quickest forms of documentation, albeit very useful in helping a developer get started on a project. Every project should include a `README` with some installation instructions and code examples. Alternatively you can break out parts of your `README` into several other files like an `INSTALL` for installation instructions or `CONTRIBUTING` for specific instructions on the accepted development practices for contributing to the project.

### API and Developer documentation
API and Developer documentation is important for understanding application logic and helps to explain the functionality of components within an application. API and Developer docs tend to be much more verbose than a simple README document. On larger projects, lack of api documentation is dangerous. This can lead to a lot of technical debt, especially when the logic of how to interact with an API or application is only present in the minds of a few people, or worse a single person. If that person leaves an organization or [gets hit by a bus](https://en.wikipedia.org/wiki/Bus_factor), you'll end up in quite a bit of trouble. The logic of an application should be well documented and available for anyone that is part of the project.

### UML, ER Diagrams, Use Case Diagrams, etc.
Diagrams and other visual representations of an application help present the application at a high level. Some diagrams are helpful for both developers and non technical staff of an organization. There are applications that help generate some diagrams automatically from existing application classes or models.

#### Some example tools
If you're developing a Django application you can generate a diagram for your models using [`django-extensions`](http://django-extensions.readthedocs.org/en/latest/graph_models.html) which uses `PyGraphviz`. If you're using MySQL, [MySQL Workbench](https://www.mysql.com/products/workbench/) has an option to generate an ER Diagram from your database schema.

If by some off chance no one has developed a tool to generate models for the language or framework you're using, you could always become a pioneer in that endeavor.


## Commenting your code

### Doc strings
If your development language supports the use of doc strings, make use of them. Doc strings are helpful in giving a brief explanation of the functionality of a class, method, function, etc. Doc strings may include parameters that a function or class constructor accepts. Follow the common conventions of your language, framework, and/or organization when writing doc strings. In some cases if doc strings don't exist or if it's not commonly used in your development language, investigate suitable alternatives for documenting the general functionality of your code.

### Block and Inline comments
Block and Inline comments should be used intelligently and sparingly. Overuse of comments can be overwhelming when reading code, and are considered a code smell.

A poor example of a `block comment` in Python:
```python
def add_two_numbers(a, b):
    # Adds a and b
    return a + b
```


If the code is very clear and obvious, you shouldn't include a comment:

Example of a poor `inline comment` in JavaScript:
```javascript
function addOne(x){
  x = x + 1;  // Increment x by 1
  return x;
}
```

Personally I prefer to stay away from inline comments and use block comments wherever an explanation of the code is needed.


## Implicit Documentation

### Changelog and Release notes
Changelog and release notes are arguably slightly less important than many of the other forms of documentation especially since it can be a bit time consuming to sift through them for valuable information. They can be useful though, and on some projects in companies and in the open source community they are mandatory. If you're a single author of a small sample app or you're building an [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product) you may be able to skip out on this one for the present time, especially if you have a very tight deadline. You can always reconstruct a changelog or release notes file based off of well written version control commit history. If you're working with a team of developers where knowledge of what is complete is crucial (without looking at open tickets/issues), including a changelog and release notes should probably be part of your repertoire.

### Version Control Logs
If you're using `git` for version control, don't be tempted to do this: `git commit -a -m "Fixed some stuff"`. Vague commit messages don't help anyone, especially when you're trying to reference when a specific change was made in the code.

There are plenty of opinionated styles out there for git commit messages, whichever you choose, be mindful of other developers including the most likely to look at the code in the future, **future you**. You don't want to anger **future you**.

### Unit and Acceptance Tests
Tests can be considered a form of implicit documentation. Including unit tests will ensure that your code maintains it's expected functionality across changes and doesn't regress to a error ridden state. Well written tests can help define the expected logic and functionality of a component in an application.


## Fallacies
You might still be tempted to think:

**"I don't have time to write documentation, I need to get this project done now!".**

* No, you should have enough time to at least write a `README` file so that the next developer taking over your code can at least set up the project or understand what the project does.

* You can take an incremental approach to documenting your code. It doesn't take much more time to include a few comments or doc strings.


**"I'll remember what this piece of code does".**

* If it's a complex piece of code, chances are, you probably won't remember what it does.


**"No one else is ever going to look at this code"**

* That might be true especially if it's a small unpublished personal project, but if there's a high probability of your code being used by someone else or taken over by another author, you better write some documentation.


**"I don't need to write documentation, good code is self documenting"**

* The next author of the codebase will be cursing you to hell if your code is difficult to understand for them. You're better off including some documentation.


## Final thoughts
Unfortunately writing documentation takes time. You might have a very close deadline or management breathing down your neck on the status of a project. Don't let those situations negatively affect your code. Documentation should be part of your development process.

The gains of having some form of documentation are enormous.
