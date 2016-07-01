# Week 4: Replication Project

## Task 1: Bring your own data
We need a dataset with somewhere between 200 and 1,000 observations (ideally) and two quantitative variables that have a potentially interesting relationship. We'll also need to identify at least one way in which we can filter that data.

Working from where we ended class (the current state of this repository), replace the unemployment/inflation data in data.json with your own. As before, you can use [Mr. Data Converter](https://shancarter.github.io/mr-data-converter/) to transform a CSV into JSON.

Update the references to the data variables `unemployment` and `inflation` as appropriate, and adjust the scales as needed. (Recall that the domain `[0, d3.max(...)]` gives us a scale ranging from 0 to the highest value of the data, while `d3.extent(...)` lets us look for both the min and the max value of the data simultaneously; there's also a `d3.min()` that works as you would expect.)

Finally, update the filter control to work with your data. There's no requirement to use a dropdown menu as is currently the case; you could also use buttons as we did in weeks 2 and 3, or some other control that we haven't discussed yet.

## Task 2: Add axes
The last thing we did in class was make space for the axes by adding margins to our chart. Now, following the examples shown in the reading (below), let's add an X and a Y axis. Three requirements here:

1. If an axis uses percentages or dollar figures, the tick labels should be formatted accordingly (note that the Scott Murray tutorial describes how to do this with percentages, for other kinds of formatting, see the [d3.format() documentation](https://github.com/d3/d3/wiki/Formatting)).
2. We should add titles to each of the axes (see part 3 of the Bostock reading where he shows how to do this for the Y axis; we also need to label our X axis, of course).
3. The finished project example that I showed had the axis lines make a grid pattern (similar to the [FiveThirtyEight house style](http://i2.wp.com/espnfivethirtyeight.files.wordpress.com/2015/01/roeder-worstgames-1.png)), as opposed to the standard tick mark configuration. D3's [SVG Axes documentation](https://github.com/d3/d3/wiki/SVG-Axes) links to [this block](http://bl.ocks.org/mbostock/3371592) as an example. Can you figure out how to extend that example to create a grid?

## Reading

* [Scott Murray, Intro to Axes](http://alignedleft.com/tutorials/d3/axes)
* [Dashing D3.js, D3.js Axes](https://www.dashingd3js.com/d3js-axes)
* [Mike Bostock, Let's Make a Bar Chart](https://bost.ocks.org/mike/bar/) ([part 2](https://bost.ocks.org/mike/bar/2/), [part 3](https://bost.ocks.org/mike/bar/3/))

## Additional Resources

* [Mike Bostock, General Update Pattern block](http://bl.ocks.org/mbostock/3808218) ([part 2](http://bl.ocks.org/mbostock/3808221), [part 3](http://bl.ocks.org/mbostock/3808234))
* [Chris Given, Interactive Update Pattern block](https://bl.ocks.org/cmgiven/9d37c9478f325ce9370d)
* [SVG Axes documentation](https://github.com/d3/d3/wiki/SVG-Axes)
* [Formatting documentation](https://github.com/d3/d3/wiki/Formatting)
* [MDN SVG documentation](https://developer.mozilla.org/en-US/docs/Web/SVG)
* [MDN Basic Shapes tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Basic_Shapes)
