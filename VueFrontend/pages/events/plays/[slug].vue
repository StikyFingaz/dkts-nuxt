<script setup lang="ts">
const route = useRoute();

const { data: play } = await useFetch(setApiUrl(`/plays/${route.params.slug}`), {
  key: "playData",
  headers: {
    "X-User-Locale": useState("userLocale"),
    "X-User-Timezone": useState("userTimezone"),
  },
});

onMounted(() => {
  // if (error.value) {
  //   console.error("Failed to fetch play data:", error.value);
  // }
});
</script>

<template lang="html">
  <div id="playContainer">
    <div class="test"></div>
    <PlayPosterRow>
      <template #images>
        <!-- <img class="img-fluid poster-image" :src="`/media/plays/${play.slug}/poster.jpg`" alt="" /> -->
        <NuxtImg
          format="webp"
          :src="`/media/plays/${play.slug}/poster.jpg`"
          :alt="`Poster - ${play.name}`"
          class="img-fluid poster-image col-12 col-lg-11"
          width="1000"
          height="1400"
          sizes="70vw lg:30vw"
          :placeholder="[10, 14]"
        />
      </template>
    </PlayPosterRow>
    <PlayDetailsRow />
    <!-- <PlayActors /> -->
    <PlayTrailerRow v-if="play.has_trailer" :slug="play.slug" />
    <PlayImageGallery :slug="play.slug" />
  </div>
</template>

<style lang="css" scoped>
@media (min-width: 1024px) {
  .poster-image {
    max-height: 90vh;
  }
}
</style>
