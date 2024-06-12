<script setup lang="ts">
const nuxtApp = useNuxtApp();

const { data: translations, refresh: refreshEventStrings } = await useFetch(setApiUrl("/translations/events"), {
  key: "eventStrings",
  headers: { "X-User-Locale": useState("userLocale") },
  // getCachedData(key) {
  //   return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  // },
});

const { data: plays, refresh: refreshPlays } = await useFetch(setApiUrl("/plays/"), {
  key: "playsData",
  headers: { "X-User-Locale": useState("userLocale") },
  // getCachedData(key) {
  //   return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  // },
});

onMounted(async () => {
  // try {
  //   await Promise.all([refreshEventStrings(), refreshPlays()]);
  // } catch (error) {
  //   console.error("Error fetching data:", error);
  // }
});
</script>

<template lang="html">
  <div>
    <NuxtPage />
  </div>
</template>

<style lang="css" scoped></style>
