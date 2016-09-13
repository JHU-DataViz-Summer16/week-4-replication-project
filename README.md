# Week 6: Replication Project

## Task 1: Complete your histogram

If you didn't reach a functional histogram last week, let's get to that point this week. You might refer to both the [notes to last week's assignment](blob/master/WEEK_5.md), as well as [this week's class demo](https://github.com/JHU-DataViz-Summer16/week-6-class-demo) (and note that you can follow it step-by-step by looking at the [commit history](https://github.com/JHU-DataViz-Summer16/week-6-class-demo/commits/master)).

Note that "functional" has two parts: 1. it accurately bins the data using the same ticks as the axis, and 2. it updates along with the scatterplot as changes are made to the options.

## Task 2: Refactor your chart using the constructor pattern

Following the example of [this week's class demo](https://github.com/JHU-DataViz-Summer16/week-6-class-demo), replace your global `setup()` and `update()` functions with a `Chart` constructor function and a `Chart.prototype.update()` method. The contents of these functions can remain mostly unchanged, except that we can now take the global variables `svg`, `x`, and `y` and make them properties of the chart, defined and accessed by calling `this.svg` (or, as shown in the demo, `chart.svg`, after setting `var chart = this` at the top of each function).

## Choose Your Own Task 3

Choose one of the following:

### Add a line to your chart

As shown in the example (image below), we can add an SVG [line element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line). Note that a line has four attributes we can set: `x1`, `x2`, `y1`, and `y2`.

What should our line show? Your choice. Note that I have already included the [Simple Statistics](http://simplestatistics.org) library, which could help to dynamically process your data. You could, for example, run a simple [linear regression](http://simplestatistics.org/docs/#linearRegression), or mark the [mean](http://simplestatistics.org/docs/#mean) of your x and y variables.

As we briefly showed in class, you'll probably need to use [Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) to transform your data from an array of objects into an array of numbers, as expected by Simple Statistics.

### Add a tooltip to your chart

As we did [in class](https://github.com/JHU-DataViz-Summer16/week-6-class-demo), use [D3.tip](http://bl.ocks.org/Caged/6476579) to add tooltips to your data. Note that the D3.tip script is not currently included in your project, so you'll need to add the following code under the other `<script>` tags that import D3 and Simple Statistics (but above your own Javascript code):

```js
<script type="text/javascript" src="https://unpkg.com/d3-tip@0.6.7/index.js"></script>
```

## Task 4: Revised final project proposal

We'll share notes on your proposal drafts this weekend. Based on our feedback and your continued thinking, please email a revised proposal prior to class.

![Finished Project](https://raw.githubusercontent.com/JHU-DataViz-Summer16/week-4-replication-project/master/finished.png)
