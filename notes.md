# Dataclasses in Python

## Example 1

It's a complex system. We use Celery to manage our background tasks.

## Example 2

- How do we know that this parameter is a dictionary?
- How do we know that this dictionary has a key "currency"? Are we sure that this key is always present?
- How do we know that the value of this key is a string?
- We have to find where this function is called and check what parameters are passed to it.
- What if we want to change the name of the parameter? It's a string so "refactor" feature of IDE will not help us.

Of course we can expand `filters` and create separate parameters for each filter, but there could be a lot of them and
it's not good for readability. And as I said before, this function is called in different part of the system, so we have
to pass our filters through 10 other functions to reach this place. And if we will change the signature of this
function, we will have to change the signature of all these functions above.

## Example 3

Dataclass is my way to go when you have to gather some data into a single object.

Sometimes we call this type of objects "data transfer objects" or DTOs, because they are used to transfer data between
different parts of the system, and they don't have any logic.

## Example 8 

Dacite works with

- collections
- optional fields
- unions

It also checks types.

# Open source

We use dacite a lot in our projects, so we decided to contribute to this project as a company. We found a time between
our sprints and we fixed a few bugs and we also improved the performance of this library. It was a win-win
situation, because we improved performance of our own system a lot and we gave something back to the community.
What's more, we described our experience in a blog post and I hope it was nice marketing for FLYR. I think it's 
very good to show that you are not only using open source, but you are also contributing to it.
