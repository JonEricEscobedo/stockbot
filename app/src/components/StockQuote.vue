<template>
  <div>
    <p class="lead">{{ stockData.company }}</p>
    <p class="lead">Today's average: ${{ stockData.quote }}</p>
    <p class="lead">Tomorrow's predicted average: <a class="disclaimer-link" href="#disclaimer">${{ predictionData.prediction1.tomorrow_avg }}*</a></p>
  </div>
</template>

<script>
export default {
  props: ['stock-data', 'prediction-data']
}
</script>

<style>
  a {
    text-decoration: none;
    color: #2c3e50;
  }

  a:hover {
    text-decoration: none;
    color: #C50000;
  }
</style>
