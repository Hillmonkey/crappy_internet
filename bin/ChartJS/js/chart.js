const CHART = document.getElementById("myChart");
console.log(CHART);
let lineChart = new Chart(CHART, {
  type: 'line',
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    datasets: [{
      label: "My First dataset",
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
      data: [65, 59, 80, 81, 56, 55, 40]
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
