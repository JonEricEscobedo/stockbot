<template>
  <div>
    <Navbar />
    <Splash />
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
  props: {
    stockData: Object
  }
  // data () {
  //   return {
  //     stockQuote: 0
  //   }
  // },
  // methods: {
  //   getRandom () {
  //     this.stockQuote = this.getRandomFromBackend()
  //   },
  //   getRandomFromBackend () {
  //     const path = `http://localhost:8080/api/data/stock`
  //     axios.get(path)
  //       .then(response => {
  //         this.stockQuote = response.data.stockQuote
  //       })
  //       .catch(error => {
  //         console.log('Error fetching', error)
  //       })
  //   }
  // },
  // created () {
  //   this.getRandom()
  // }
}
</script>

<style>

</style>
