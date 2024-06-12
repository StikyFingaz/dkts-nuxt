<script setup lang="ts">
defineProps<{
  nickname?: string;
}>();
</script>

<template lang="html">
  <div class="card actor-card">
    <NuxtLinkLocale :to="`/about/actors/${nickname}`">
      <slot name="images"> </slot>
    </NuxtLinkLocale>
    <div class="card-body text-bg-dark d-flex justify-content-center p-0">
      <span class="card-title text-truncate m-1 ms-2 fs-5">
        <slot name="name"> </slot>
      </span>
    </div>
  </div>
</template>

<style lang="css" scoped></style>
