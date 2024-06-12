<script setup lang="ts">
const { data: play } = useNuxtData("playData");
</script>

<template lang="html">
  <div v-if="play.trivia" class="container">
    <div class="d-flex flex-row justify-content-center">
      <div class="col-12 col-md-6">
        <blockquote class="fs-5">
          <p class="quote-text">{{ play.trivia }}</p>
        </blockquote>
      </div>
    </div>
    <hr />
  </div>
</template>

<style lang="css" scoped></style>
