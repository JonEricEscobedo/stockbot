<template>
  <div>
    <Navbar @update-stock-ticker="updateStockTicker" :on-quote-click="getStockDataFromBackend" />
    <Splash :stock-data="stockData" :prediction-data="predictionData" />
    <Disclaimer />
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from './Navbar.vue'
import Splash from './Splash.vue'
import Disclaimer from './Disclaimer.vue'
/* eslint-env jquery */
export default {
  components: { Navbar, Splash, Disclaimer },
  data () {
    return {
      stockData: null,
      predictionData: null,
      ticker: ''
    }
  },
  methods: {
    getStockDataFromBackend () {
      const path = `${process.env.API_URL}/api/data/stock`
      axios.get(path, {
        params: {
          ticker: this.ticker
        }
      })
        .then(response => {
          this.stockData = response.data.stock
          this.predictionData = response.data.predictions
          $('.navbar-collapse').collapse('hide')
        })
        .catch(error => {
          console.log('Error fetching stock data', error)
        })
    },
    updateStockTicker (newData) {
      // Update this.ticker to reflect user inputted stock ticker
      this.ticker = newData
    }
  },
  created () {
    this.ticker = 'tsla' // Load TSLA stock data on component creation
    this.getStockDataFromBackend()
  }
}
</script>

<style>
</style>
