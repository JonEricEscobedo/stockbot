<template>
  <div>
    <p class="lead">{{ stockData.company }}</p>
    <p class="lead">Today's average: ${{ stockData.quote }}</p>
    <p class="lead">Tomorrow's predicted average: ${{ predictionData.tomorrow_avg }}</p>
  </div>
</template>

<script>
export default {
  props: ['stock-data', 'prediction-data']
}
</script>

<style>
</style>
