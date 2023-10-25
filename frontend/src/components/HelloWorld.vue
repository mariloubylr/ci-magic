<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    {{ data }}
  </div>
</template>

<script setup lang="ts">
import data from '../../data_dir/ComplexData.json'
defineProps({
  msg: String
})
</script>
