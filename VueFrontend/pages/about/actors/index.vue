<script setup lang="ts">
const { data: actors, refresh } = await useFetch(setApiUrl("/actors/"), {
  key: "actorsData",
  headers: { "X-User-Locale": useState("userLocale") },

});

onMounted(async () => {
  // await refresh();
});
</script>

<template lang="html">
  <div>
    <div class="container mt-3">
      <ActorsActorCards />
    </div>
  </div>
</template>

<style lang="css" scoped></style>
