<template>
  <main>
<button @click="start"> 시작 </button>
<GChart

    type="LineChart"
    :data="chartData"
    :options="chartOptions"
  />
  </main>
</template>

<script setup>

import {GChart} from 'vue-google-charts' 
import {ref, onMounted} from 'vue'

const myData = [
          ['2014', 100],
          ['2015', 117],
          ['2016', 660],
          ['2017', 103],
          ['2017', 103],
          ['2017', 103],
          ['2017', 103],
          ['2017', 103],
]

  const chartData = ref([
  ['Year', 'cost'],
  ])

const chartOptions = ref({
  chart: {
    title: '코인 차트',
  }
  })

let intervalId; 

const start = function () {

   clearInterval(intervalId);

   intervalId = setInterval(() => {
     }, interval);
    for (let i = 0; i < myData.length; i++) {
      chartData.value.push(myData[i]);
    }
  const gChart = new GChart();
  gChart.draw('chart_div', chartData.value, chartOptions.value);
}

</script>

