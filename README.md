# Week 5: Replication Project

## Task 1: Add a histogram

The example that we're replicating has a histogram that rises from the X and Y axes, showing the number of points in the scatterplot that appear between each axis tick (picture below).

We've seen bar charts in last week's reading and this week's class demo. Recall that we'll use the SVG [rect](http://www.w3schools.com/svg/svg_rect.asp) element for the bars. In order to take care of transforming our data into bins, we can use D3's [histogram layout](https://github.com/d3/d3-3.x-api-reference/blob/master/Histogram-Layout.md). We'll need to create a new linear scale for the height of the bars (corresponding to the number of points in the bin), but perhaps we can recycle the existing X and Y axes to position the bars?

Be sure to read the documentation on `histogram.value()`.

One additional note: we'll want the number of bins to equal the number of gaps between ticks on our axis. We briefly discussed in class how the `axis.ticks()` method passes through to the `scale.ticks()` method of its scale (set with `axis.scale()`) to figure out where to place its tick marks (and how many will fit nicely). We too can take advantage of `scale.ticks()`. Try running `x.ticks()` in the browser console and see if you can use that output when you create your histogram layout.

## Task 2: Final project proposal (first draft)

We're looking for a short proposal on what you want to explore with your final portfolio. One page of writing should be enough to get across these three things:

1. What's the data? You want a specific dataset that has ideally 200 to 1,000 rows with a variety of different columns to explore. Having different types of data in the columns (dates, geographies, continuous variables and categorical ones, a hierarchy if possible) will give you a lot of flexibility in what you can explore. Once you choose your dataset, describe it for us. Number of rows, what is one row, number of columns, column types, data source, any anything else that might be important.

2. Prior Art - what else has been done with this data? Specifically, having a sense for what prior visualizations of this data you  take inspiration from, what they did well, and their limits. What have former attempts to examine this data missed? What story did they fail to tell? If you don't know of, or can't find, graphs about this exact data, find some that are analogous. Make sure to link to (or include) any specific graphs so we can take a look at them.

3. Novel Questions - have a sense of what you want to get out of the data. A lack of clarity is ok - even good - but you should have some initial sparks of curiosity. What are the ways we can potentially interrogate this data that are only possible through an interactive visualization? What's difficult to understand or comprehend about it? What potential stories could you discover?

## Reading

* [Scott Murray on Layouts](http://chimera.labs.oreilly.com/books/1230000000345/ch11.html)
* [Histogram layout documentation](https://github.com/d3/d3-3.x-api-reference/blob/master/Histogram-Layout.md)
* [Bostock block using histogram layout](http://bl.ocks.org/mbostock/3048450) (Note that this example is using the v4 API; `histogram.domain()` and `histogram.thresholds()` replace `histogram.bins()` in the v3 API that we're using.)
* [See, Think, Design, Produce by Jonathan Corum](http://style.org/stdp3/)
