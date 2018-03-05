<template>
  <div>
    <section>
      <div class="container flex-center">
        <div class="row flex-center pt-5 mt-5">
          <div class="offset-md-1 col-md-4 text-center text-md-left align-self-center">
            <div v-if="stockData">
              <img class="rounded" v-bind:src="stockData.logo" />
              <h1 class="display-1">{{ stockData.ticker }}</h1>
              <p class="lead">{{ stockData.company }}</p>
              <p class="lead">Today's average: ${{ stockData.quote }}</p>
              <p class="lead">Tomorrow's average: <span><small class="text-muted">Coming soon</small></span></p>
            </div>
          </div>
          <div class="col-md-6">
            <img src="../assets/phone-transparent-mockup.png" alt="iphone 7" class="img-fluid">
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  props: ['stock-data']
}
</script>

<style>
  section {
    min-height: 100vh;
  }
</style>
