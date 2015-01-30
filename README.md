# Magna.css

*Magna* is the latin word for *great*. Because using *Magna.css* is a great idea. Because it reduces the amount of coding you have to do. Because it's so great.

## Introduction

As a front end developer, you probably use colors for text all the time. This is a very tedious process, as you have to add all these pesky hex codes to your CSS.

```
.element {
    color: #b00b13; /* ugh, so tedious */
}
```

But imagine a world where none of this is necessary. Imagine a world, where, to change the color of an element, you only have to add a single class to your HTML.

```
<h1 class="color-b00bi3">So refreshing!</h1>
```

With *Magna.css*, you no longer have to imagine this world. You can live in it *right now*.

Simply download `generator.py`, generate your very own `magna.css`, and start saving time and money.

## Usage

Before you're able to use *Magna.css*, you first have to generate your own CSS file with the `generator.py` script.

Want a vanilla CSS file? Use this:
```
$ python generate.py > magna.css
```

Want a syntactically awesome style sheet? Use this:
```
$ python generate.py -sass > magna.sass
```

Want 100% of the colors with only 76.3138625% of the file size? Then this is for you:
```
$ python generate.py -m > magna.min.css
```

Now just upload it to your server, and link to it from your HTML.

## Inspiration

*Magna.css* is heavily inspired by the great work the TACHYONS team does with their CSS framework. Just look at this marvelous piece of code: https://www.npmjs.com/package/tachyons-position
