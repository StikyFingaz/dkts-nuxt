<script setup lang="ts">
defineProps<{
  slug?: string;
}>();
</script>

<template lang="html">
  <div id="trailerContainer" class="container-fluid">
    <div class="container text-center mt-2 mt-md-2 mb-3">
      <!-- TODO: Use webP/avif for the video poster -->
      <video :poster="`/media/plays/${slug}/cover.jpg`" class="col-12 col-md-9 mt-3 mb-2" controls preload="metadata">
        <source :src="`/media/plays/${slug}/trailer.webm`" type="video/mp4" />
        <source :src="`/media/plays/${slug}/trailer.mp4`" type="video/mp4" />
      </video>
    </div>
  </div>
</template>

<style lang="css" scoped></style>
