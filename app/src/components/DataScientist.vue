<template>
  <div>
    <Navbar @update-stock-ticker="updateStockTicker" :on-quote-click="getStockDataFromBackend" />
    <div class="container flex-center"  v-if="stockData">
      <div class="row flex-center pt-5 mt-5">
        <div class="col-12 text-center">
          <StockDetails :stock-data="stockData" />
        </div>
      </div>
      <div class="row">
        <DataTable :stock-data="stockData" :prediction-data="predictionData" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from './Navbar.vue'
import StockDetails from './StockDetails.vue'
import DataTable from './DataTable.vue'

export default {
  components: { Navbar, StockDetails, DataTable },
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
          this.predictionData = response.data.prediction
        })
        .catch(error => {
          console.log('Error fetching', error)
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
.shade {
  background: rgba(0,0,0,0.5);
}
</style>
