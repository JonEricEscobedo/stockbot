<template>
  <div>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark ">
      <div class="container">
        <a class="navbar-brand" id="brand" href="/"><strong>Intellivest</strong></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-7" aria-controls="navbarSupportedContent-7" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent-7">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#disclaimer">Disclaimer</a>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0" v-on:submit.prevent>
            <input class="form-control mr-sm-2" type="search" placeholder="Stock ticker" aria-label="Search" @change="onChange" onclick="this.select()">
            <button class="btn btn-outline-danger my-2 my-sm-0" @click="onQuoteClick">Quote</button>
          </form>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  props: ['onQuoteClick'],
  methods: {
    onChange (input) {
      this.$emit('update-stock-ticker', input.target.value)
    }
  }
}
</script>

<style>
  #brand {
    color: #C50000
  }
</style>
