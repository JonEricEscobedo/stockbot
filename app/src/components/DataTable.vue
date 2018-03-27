<template>
  <div class="table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th>Today's Avg <br><small>{{ stockData.date }}</small></th>
          <th>Tomorrow <br><small>70% chance of</small></th>
          <th>Tomorrow <br><small>85% chance of</small></th>
          <th>Tomorrow <br><small>65% chance of</small></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th></th>
          <td>Placeholder</td>
          <td>Placeholder</td>
          <td>Placeholder</td>
        </tr>
        <tr>
          <th>${{ stockData.quote }}</th>
          <td>${{ predictionData.tomorrow_avg }}</td>
          <td>Placeholder</td>
          <td>Placeholder</td>
        </tr>
        <tr>
          <th></th>
          <td>Placeholder</td>
          <td>Placeholder</td>
          <td>Placeholder</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  props: ['stock-data', 'prediction-data'],
  created () {
    console.log(this.stockData.date, moment(this.stockData.date).valueOf())
  }
}
</script>
