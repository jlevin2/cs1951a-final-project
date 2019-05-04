// Config {{{
/*jshint esversion: 6 */ 
// }}}
// Consts {{{
const margin = {top: 10, right: 30, bottom: 30, left: 40};
const width = 950 - margin.left - margin.right;
const height = 700 - margin.top - margin.bottom;
const years = ["1997_98", "1998_99", "1999_00", "2000_01", "2001_02","2002_03","2003_04", "2004_05", "2005_06", "2006_07", "2007_08", "2008_09", "2009_10", "2010_11", "2011_12", "2012_13", "2013_14", "2014_15", "2015_16", "2016_17"];
const num_years = years.length;
const svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

const background_color = "#7584c2";
const bars_colors = ["#5680e9", "#84ceeb", "5ab9ea", "8860d0"];
const line_color = "#FFF8DC"; //"#393f4d";
const text_color = "black";
const labels = ["Median Debt", "Low Income Median Debt", "Medium Income Median Debt", "High Income Median Debt"];
//}}}
// helpers {{{
// text_from_bkt(bracket) {{{
// gets nicer text for labels
function text_from_bkt(bracket){
    if (bracket == "DEBT_MDN"){
        return labels[0];
    }
    if (bracket == "LO_INC_DEBT_MDN"){
        return labels[1];
    }
    if (bracket == "MD_INC_DEBT_MDN"){
        return labels[2];
    }
    if (bracket == "HI_INC_DEBT_MDN"){
        return labels[3];
    }
}
//}}}
// prettify_year(year) / prettify_year_tick(year) {{{
function prettify_year(year){
    return year.replace("_", " - ");
}

function prettify_year_tick(year){
    return year.replace("_", "/");
}
//}}}
// edit_title(year) {{{
function edit_title(year){
    d3.select('p#value-step')
        .text("Median College Debt by Income Bracket: " + prettify_year(year))
        .style("font-weight", "bold")
        .style("color", "black");
}
//}}}
//}}}
// Plotting {{{
// clear_plot() {{{
// clears the plot
function clear_plot() {
    svg.selectAll("rect").remove();
    svg.selectAll("line").remove();
    svg.selectAll("circle").remove();
}
//}}}
// plot_one_bracket(data, bracket, x, y, color) {{{
// plots one income bracket
function plot_one_bracket(data, bracket, x, y, color) {
    var data_sorted = data.sort(function(x, y){
       return d3.ascending(x[bracket], y[bracket]);
    });
    var q1 = d3.quantile(data_sorted, 0.25, d => d[bracket]);
    var median = d3.quantile(data_sorted, 0.5, d => d[bracket]);
    var q3 = d3.quantile(data_sorted, 0.75, d => d[bracket]);
    var interQuantileRange = q3 - q1;
    var min = d3.quantile(data_sorted, 0, d => d[bracket]);
    var max = q3 + 1.5*interQuantileRange;
    // a few features for the box
    var bwidth = 100;
    
    center = x(text_from_bkt(bracket)) + 61;
    
    // Show the main vertical line
    svg
    .append("line")
      .attr("x1", center+bwidth/2)
      .attr("x2", center+bwidth/2)
      .attr("y1", y(min) )
      .attr("y2", y(max) )
      .attr("stroke-width", 2)
      .attr("stroke", line_color);
    

    // Show the box
    svg
    .append("rect")
      .attr("x", center)
      .attr("y", y(q3) )
      .attr("height", (y(q1)-y(q3)) )
      .attr("width", bwidth )
      .attr("stroke", line_color)
      .attr("stroke-width", 2)
      .style("fill", color);

    // show median, min and max horizontal lines
    svg
    .selectAll("toto")
    .data([min, median, max])
    .enter()
    .append("line")
      .attr("x1", center)
      .attr("x2", center+bwidth)
      .attr("y1", function(d){ return(y(d));} )
      .attr("y2", function(d){ return(y(d));} )
      .attr("stroke", line_color) 
      .attr("stroke-width", 2);
    
    // outliers
    svg.append("g")
        .attr("class", "dot")
        .selectAll('circle')
        .data(data_sorted)
        .enter()
        .filter(function(d) { return d[bracket] > max; })
        .append("circle")
        .attr("cx", d => { return center + bwidth/2; })
        .attr("cy", d => { return y(d[bracket]); })
        .attr("r", d => { return 5; })
        .style("stroke", d => {return line_color; })
        .style("stroke-width", d => {return 2; })
        .style("fill", d => {return color; })
        .append("title")
        .text(d => {return d.INSTNM; });
}
//}}}
// plot_one_year(data, year, width, height) {{{
// plots all brackets for a year
function plot_one_year(data, year, width, height) {

    // actual data plotting
    tmp_data_slice = data.slice(); 

    first_years = tmp_data_slice.filter(function(d, i) {
        if (d.YEAR == year){
            return d;
        } 
    });
    console.log(first_years.length);
   
    // Show the Y scale
    var y = d3.scaleLinear()
      .domain([0, 45000])
      .range([height, 0]);
    svg.call(d3.axisLeft(y));

    var x = d3.scaleBand()
      .range([0, width])
      .domain(labels)
      .padding(0.05);
    
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    plot_one_bracket(first_years, "DEBT_MDN", x, y, bars_colors[0]);
    plot_one_bracket(first_years, "LO_INC_DEBT_MDN", x, y, bars_colors[1]);
    plot_one_bracket(first_years, "MD_INC_DEBT_MDN", x, y, bars_colors[2]);
    plot_one_bracket(first_years, "HI_INC_DEBT_MDN", x, y, bars_colors[3]);
    // plot the dots
    // Compute summary statistics used for the box:
}
// }}}
// }}}
// D3 Graph Creation {{{
d3.csv("only_relevant_data.csv")
    .then(data => { // data[0][i] = i'th row of file 0 == 1996_97
        data.forEach(function(d){ 
            d.DEBT_MDN = +d.DEBT_MDN; 
            d.LO_INC_DEBT_MDN = +d.LO_INC_DEBT_MDN; 
            d.MD_INC_DEBT_MDN = +d.MD_INC_DEBT_MDN; 
            d.HI_INC_DEBT_MDN = +d.HI_INC_DEBT_MDN; 
        });

        // year slider
        //add_gradient();

        d3.selectAll("body")
            .style("background-color", background_color)
            .style("color", text_color);

        var sliderStep = d3
            .sliderBottom()
            .min(0)
            .max(years.length - 1)
            .width(width-50)
            .tickFormat(function (d) {
                out = prettify_year_tick(years[d]);
                return out;
            })
            .ticks(years.length - 1)
            .step(1)
            .default(0)
            .fill(line_color)
            .on('onchange', val => {
                year = years[val];
                edit_title(year);
                clear_plot();
                plot_one_year(data, year, width, height);
            });

        var gStep = d3
            .select('div#slider-step')
            .append('svg')
            .attr('width', width)
            .attr('height', 100)
            .append('g')
            .attr('transform', 'translate(30,30)');

        gStep.call(sliderStep);
        var year = years[0];
        edit_title(year);
        // plot the data
        plot_one_year(data, year, width, height);
       
});
// }}}
