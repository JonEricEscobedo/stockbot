<template>
  <div>
    <Navbar />
    <Splash :stock-data="stockData"></Splash>
    <About />
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from './Navbar.vue'
import Splash from './Splash.vue'
import About from './About.vue'

export default {
  components: { Navbar, Splash, About },
  data () {
    return {
      stockData: null
    }
  },
  methods: {
    getStockData () {
      this.stockData = this.getStockDataFromBackend()
    },
    getStockDataFromBackend () {
      const path = `${process.env.API_URL}/api/data/stock`
      const ticker = 'nvda'
      axios.get(path, {
        params: {
          ticker: ticker
        }
      })
        .then(response => {
          this.stockData = response.data.stock
        })
        .catch(error => {
          console.log('Error fetching', error)
        })
    }
  },
  created () {
    this.getStockData()
  }
}
</script>

<style>

</style>
