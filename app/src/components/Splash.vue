<template>
  <section>
    <div class="container flex-center">
      <div class="row flex-center pt-5 mt-5">
        <div class="col align-self-center text-center">
          <Stock :stock-data="stockData" :prediction-data="predictionData"></Stock>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Stock from './Stock.vue'

export default {
  components: { Stock },
  props: ['stock-data', 'prediction-data']
}
</script>

<style>
  section {
    min-height: 100vh;
  }
</style>
