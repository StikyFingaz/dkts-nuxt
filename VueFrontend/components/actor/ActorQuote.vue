<script setup lang="ts">
defineProps<{
  quote?: string;
}>();
</script>

<template lang="html">
  <div>
    <blockquote class="blockquote">
      <p class="quote-text">{{ quote }}</p>
    </blockquote>
  </div>
</template>

<style lang="css" scoped></style>
