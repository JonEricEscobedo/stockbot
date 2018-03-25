<template>
  <div>
    <img class="rounded" v-bind:src="stockData.logo" />
    <h1 class="display-1">{{ stockData.ticker }}</h1>
  </div>
</template>

<script>
export default {
  props: ['stock-data']
}
</script>

<style>
</style>
