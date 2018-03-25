<template>
  <div>
    <div v-if="stockData">
      <StockDetails :stock-data="stockData" />
      <StockQuote :stock-data="stockData" :prediction-data="predictionData" />
    </div>
  </div>
</template>

<script>
import StockDetails from './StockDetails.vue'
import StockQuote from './StockQuote.vue'

export default {
  components: { StockDetails, StockQuote },
  props: ['stock-data', 'prediction-data']
}
</script>

<style>

</style>
