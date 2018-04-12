<template>
  <div class="table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th>Today's Avg <br><small>{{ stockData.date }}</small></th>
          <th>Tomorrow (Algo 1)<br><small>{{ predictionData.probability }}% chance {{ predictionData.verbal_analysis }}</small></th>
          <th>Tomorrow (Algo 2)<br><small>xx% chance of</small></th>
          <th>Tomorrow (Algo 3)<br><small>xx% chance of</small></th>
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
          <td>${{ predictionData.lower_range }} - {{ predictionData.upper_range }}</td>
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

export default {
  props: ['stock-data', 'prediction-data'],
  created () {
    console.log('==>', this.predictionData)
  }
}
</script>
