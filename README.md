# Magna.css

*Magna* is the latin word for *great*. Because using *Magna.css* is a great idea. Because it reduces the amount of coding you have to do. Because it's so great.

## Introduction

As a front end developer, you probably use colors for text all the time. This is a very tedious process, as you have to add all these hex codes to the CSS.

```
.element {
    color: #b00b13; /* ugh, so tedious */
}
```

But imagine a world where none of this is necessary. Imagine a world, where, to change the color of an element, you only have to add a single class to your HTML.

```
<h1 class="color-b00bi3">So refreshing!</h1>
```

With *Magna.css*, you no longer have to imagine this world. You can live with it *right now*.

Simply download the `generator.py`, generate your `magna.css` file, and start saving time and money.

## Usage

Before you're able to use `Magna.css`, you first have to generate your own CSS-file with the `generator.py`-Script.

There are some arguments to change the output:

This will generate a plain css file:
```
$ python generate.py > magna.css
```

This will generate a minifed css file:
```
$ python generate.py -m > magna.min.css
```

This will generate a Sass file:
```
$ python generate.py -sass > magna.sass
```

Now just upload it to your server, and link to it from your HTML.

## Inspiration

*Magna.css* is heavily inspired by the great work the Tachyon-Team does with their CSS-Framework. Just look at this marvelous piece of code: https://www.npmjs.com/package/tachyons-position
