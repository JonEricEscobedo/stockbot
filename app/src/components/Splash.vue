<template>
  <div>
    <section>
      <div class="container flex-center">
        <div class="row flex-center pt-5 mt-5">
          <div class="offset-md-1 col-md-4 text-center text-md-left align-self-center">
            <!-- <img class="rounded" src="{{logo.url}}" /> -->
            <!-- <h1 class="display-1">{{raw_data.quote.symbol}}</h1> -->
            <!-- <p class="lead">{{raw_data.quote.companyName}}</p> -->
            <!-- <p class="lead">Today's average: ${{stock_quote_avg}}</p> -->
            <!-- <p class="lead">Tomorrow's average: <span><small class="text-muted">Coming soon</small></span></p> -->
            <h1 class="display-1">Ticker</h1>
            <p class="lead">Company name, Inc.</p>
            <p class="lead">Today's average: $300.00</p>
            <p class="lead">Tomorrow's average: <span><small class="text-muted">Coming soon</small></span></p>
          </div>
          <div class="col-md-6">
            <img src="../assets/phone-transparent-mockup.png" alt="iphone 7" class="img-fluid">
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style>
  section {
    min-height: 100vh;
  }
</style>
