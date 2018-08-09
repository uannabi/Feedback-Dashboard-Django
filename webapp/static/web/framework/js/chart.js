var chartData = [
    {
        "date": "2012",
        "Growth": 5,
        "townName": "New York",
        // "townName2": "Welcome",
        "townSize": 20,
        // "Steps": 400.71,
        "duration": 5
    },
    {
        "date": "2013",
        "Growth": 7,
        "townName": "Washington",
        "townSize": 14,
        // "Steps": 46.71,
        "duration": 7
        
    },
    {
        "date": "2014",
        "Growth": 6,
        "townName": "Wilmington",
        "townSize": 14,
        // "Steps": 59.22,
        "duration": 6
    },
    {
        "date": "2015",
        "Growth": 8,
        "townName": "Jacksonville",
        "townSize": 7,
        // "Steps": 65.35,
        "duration": 8
    },
    {
        "date": "2016",
        "Growth": 7.5,
        "townName": "Miami",
        "townName2": "Going",
        "townSize": 10,
        // "Steps": 61.83,
        "duration": 7.5
    },
    {
        "date": "2017",
        "Growth": 9,
        "townName": "Tallahassee",
        "townSize": 7,
        // "Steps": 35.46,
        "duration": 9
    },
    {
        "date": "2018",
        "Growth": 10,
        "townName": "New Orleans",
        "townSize": 10,
        //  "Steps": 10.94,
        // "duration": 482
        "duration": 10
    }
    // {
    //     "date": "2019",
    //     // "Growth": 238,
    //     // "townName": "Houston",
    //     // "townName2": "Houston",
    //     // "townSize": 16,
    //     //  "Steps": 35.76,
    //     // "duration": 484
    //     // "duration": 11
    // },
    // {
    //     "date": "2020",
    //     // "Growth": 218,
    //     // "townName": "Dalas",
    //     // "townSize": 17,
    //     // "Steps": 40.8,
    //     // "duration": 287
    // },
    // {
    //     "date": "2023",
    //     // "Growth": 349,
    //     // "townName": "Oklahoma City",
    //     // "townSize": 11,
    //     //  "Steps": 35.49,
    //     // "duration": 485
    // },
    // {
    //     "date": "2024",
    //     // "Growth": 603,
    //     // "townName": "Kansas City",
    //     // "townSize": 10,
    //     //  "Steps": 39.1,
    //     // "duration": 890
    // },
    // {
    //     "date": "2025",
    //     // "Growth": 534,
    //     // "townName": "Denver",
    //     // "townName2": "Denver",
    //     // "townSize": 18,
    //     //  "Steps": 35.74,
    //     // "duration": 810
    // }
    // {
    //     "date": "2026",
    //     // "townName": "Salt Lake City",
    //     // "townSize": 12,
    //     // "Growth": 425,
    //     // "duration": 670,
    //     //  "Steps": 40.75,
    //     // "alpha":0.4
    // },
    // {
    //     "date": "2027",
    //     //  "Steps": 46.1,
    //     // "duration": 470,
    //     // "townName": "Las Vegas",
       
    // },
    // {
    //     "date": "2028",
    //     // "Steps": 40.1
    // },
    // {
    //     "date": "2029",
    //     // "Steps": 35.1
    // },
    // {
    //     "date": "2030",
    //     // "Steps": 76.19,
    //     "townSize": 22
    //     // "townName2": "Adiva Graphics",
    //     // "bulletClass": "lastBullet"
    // }
    
];
var chart = AmCharts.makeChart("chartdiv", {
  type: "serial",
  theme: "dark",
  dataDateFormat: "YYYY-MM-DD",
  dataProvider: chartData,

  addClassNames: true,
  startDuration:1,
  color: "#02d565",
  marginLeft: 0,

  categoryField: "date",
  categoryAxis: {
    parseDates: true,
    minPeriod: "YYYY",
    autoGridCount: false,
    gridCount: 50,
    gridAlpha: 0.1,
    gridColor: "#02d565",
    axisColor: "#555555",
    dateFormats: [{
        period: 'DD',
        format: 'DD'
    }, {
        period: 'WW',
        format: 'MMM DD'
    }, {
        period: 'MM',
        format: 'MMM'
    }, {
        period: 'YYYY',
        format: 'YYYY'
    }]
  },

  valueAxes: [{
    id: "a1",
    title: "Growth",
    gridAlpha: 0,
    axisAlpha: 0
  },{
    id: "a2",
    position: "right",
    gridAlpha: 0,
    axisAlpha: 0,
    labelsEnabled: false
  },{
    id: "a3",
    title: "Sucess",
     position: "right",
    // gridAlpha: 0,
    // axisAlpha: 0,
    // inside: true,
    // duration: "mm",
    // durationUnits: {
    //     DD: "d. ",
    //     hh: "h ",
    //     mm: "min",
    //     ss: ""
    // }
  }],
  graphs: [{
    id: "g1",
    valueField:  "Growth",
    title:  "growth",
    type:  "column",
    fillAlphas:  0.5,
    valueAxis:  "a1",
    balloonText:  "[[value]] Growth",
    // legendValueText:  "[[value]] Days",
    legendPeriodValueText:  "total: [['']] Growth",
    lineColor:  "#263138",
    alphaField:  "alpha",
  },{
    id: "g2",
    valueField: "Steps",
    classNameField: "bulletClass",
    title: "flow",
    type: "line",
    valueAxis: "a2",
    lineColor: "#02d565",
    lineThickness: 1,
    legendValueText: "[[description]]/[[value]]",
    descriptionField: "townName",
    bullet: "round",
    bulletSizeField: "townSize",
    bulletBorderColor: "#fff",
    bulletBorderAlpha: 1,
    bulletBorderThickness: 2,
    bulletColor: "#e7373f",
    labelText: "[[townName2]]",
    labelPosition: "right",
    balloonText: "Steps:[[]]",
    showBalloon: true,
    animationPlayed: true,
  },{
    id: "g3",
    title: "Progress",
    valueField: "duration",
    type: "line",
    valueAxis: "a3",
    lineColor: "#e51b24",
    balloonText: "[[value]]",
    lineThickness: 1,
    legendValueText: "[[value]]",
    bullet: "round",
    bulletBorderColor: "#fff",
    bulletBorderThickness: 1,
    bulletBorderAlpha: 1,
    dashLengthField: "dashLength",
    animationPlayed: true
  }],

  chartCursor: {
    zoomable: true,
    categoryBalloonDateFormat: "DD",
    cursorAlpha: 0,
    valueBalloonsEnabled: false
  },
  legend: {
    bulletType: "round",
    equalWidths: false,
    valueWidth: 120,
    useGraphSettings: true,
    color: "#02d565"
  }
});