<script setup lang="ts">
const nuxtApp = useNuxtApp();

const { data: translations, refresh } = await useFetch(setApiUrl("/translations/about"), {
  key: "aboutStrings",
  headers: { "X-User-Locale": useState("userLocale") },
});

onMounted(async () => {
  // await refresh();
});
</script>

<template lang="html">
  <div>
    <NuxtPage />
  </div>
</template>

<style lang="css" scoped></style>
