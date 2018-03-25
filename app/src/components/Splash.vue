<template>
  <section>
    <div class="container flex-center">
      <div class="row flex-center pt-5 mt-5">
        <div class="offset-md-1 col-md-4 text-center text-md-left align-self-center">
          <Stock :stock-data="stockData" :prediction-data="predictionData"></Stock>
        </div>
        <div class="col-md-6">
          <SplashImage />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Stock from './Stock.vue'
import SplashImage from './SplashImage.vue'

export default {
  components: { Stock, SplashImage },
  props: ['stock-data', 'prediction-data']
}
</script>

<style>
  section {
    min-height: 100vh;
  }
</style>
