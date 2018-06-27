<template>
  <div class="table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th>Today's Avg <br><small>{{ stockData.date }}</small></th>
          <th>Tomorrow (Algo 1)<br><small>{{ predictionData.prediction1.probability }}% chance {{ predictionData.prediction1.verbal_analysis }}</small></th>
          <th>Tomorrow (Algo 2)<br><small>{{ predictionData.prediction2.probability }}% chance {{ predictionData.prediction2.verbal_analysis }}</small></th>
          <th>Tomorrow (Algo 3)<br><small>{{ predictionData.prediction3.probability }}% chance {{ predictionData.prediction3.verbal_analysis }}</small></th>
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
          <td>${{ predictionData.prediction1.lower_range }} - {{ predictionData.prediction1.upper_range }}</td>
          <td>${{ predictionData.prediction2.lower_range }} - {{ predictionData.prediction2.upper_range }}</td>
          <td>${{ predictionData.prediction3.lower_range }} - {{ predictionData.prediction3.upper_range }}</td>
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
    // console.log('==>', this.predictionData)
  }
}
</script>
