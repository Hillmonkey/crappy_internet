const CHART = document.getElementById("myChart");
console.log(CHART);
let lineChart = new Chart(CHART, {
  type: 'line',
  data: {
    labels: ["59", "58", "57", "56", "55", "54", "53", "52", "51", "50",
	     "49", "48", "47", "46", "45", "44", "43", "42", "41", "40",
             "39", "38", "37", "36", "35", "34", "33", "32", "31", "30",
             "29", "28", "27", "26", "25", "24", "23", "22", "21", "20",
             "19", "18", "17", "16", "15", "14", "13", "12", "11", "10",
             "09", "08", "07", "06", "05", "04", "03", "02", "01", "00"],

    // labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    datasets: [{
      label: "Internet Connectivity, 60 Second Resolution",
      fill: false,
      lineTension: 0.1,
      backgroundColor: "rgba(75, 192, 192, 0.4)",
      borderColor:  "rgba(75, 192, 192, 1)",
      borderCapStype: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(75, 192, 192, 1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75, 192, 192, 1)",
      pointHoverBorderWidth: 2,
      pointHitRadius: 10,
      data: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks:  {
          beginAtZero: true
        }
      }]
    }
  }
});
