# cookiecutter-ruby

This project defines a [Cookiecutter](https://cookiecutter.readthedocs.io/) template for creating Ruby projects
with some optioned defaults.

## How to use

First, install [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html) and then run this
command:

`cookiecutter gh:douglas/cookiecutter-ruby`

It will allow you to select between `minitest` and `rspec`, configure Gemfile accordingly and also add some test
templates.

After you run the previous command, you will end up with the project directory in our current folder, so enter
on it and run:

`bundle install`

To install the gems according to your selections and you're good to go =)

## How to run tests on the new project

You can use this command:

`rake test`

## How to run rubocop on the new project

`rake rubocop`

## Gems installed by default

- rake                 # For running tasks
- awesome_print        # For awesome printin' on terminal
- rubocop              # Linting
- rubocop-shopify"     # Follow same patterns I used at Shopify
- rubocop-performance  # For performance improvement suggestions
- rubocop-rake         # Use Rubocop within Rake

### minitest

- minitest
- minitest-reporters
- mocha

### Rspec

- rspec
